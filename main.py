'''
Lab 6
Thurstan Ngo
'''


def encode(password):
    encoded = ""
    for i in range(len(password)):
        encoded += str((int(password[i]) + 3) % 10)
    return encoded

def decode(encodedPassword):
    decodedPassword = ""
    for num in encodedPassword:
        if int(num) >= 3 and int(num) <= 9:
            decodedPassword += str(int(num) - 3)
        elif int(num) == 0:
            decodedPassword += "7"
        elif int(num) == 1:
            decodedPassword += "8"
        elif int(num) == 2:
            decodedPassword += "9"

    return decodedPassword


def main():
    while True:
        # Print menu with encoder and decoder options
        print("Menu")
        print("-----------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("Choose an option: "))

        if option == 1:
            password = ""
            while len(password) != 8:
                password = input("Enter your password: ")
            encoded_password = encode(password)

        #smaple comment
        if option == 2:
            decodedPassword = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decodedPassword}")

        if option == 3:
            break


if __name__ == '__main__':
    main()