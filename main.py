'''
Lab 6
Thurstan Ngo
'''


def encode(password):
    encoded = ""
    for i in range(len(password)):
        encoded += str((int(password[i]) + 3) % 10)
    return encoded

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
            print(encoded_password)

        if option == 3:
            break


if __name__ == '__main__':
    main()