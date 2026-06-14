def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            elif char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        else:
            encrypted_text += char

    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

            elif char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

        else:
            decrypted_text += char

    return decrypted_text


while True:
    print("\n===== Caesar Cipher =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        message = input("Enter the message: ")
        shift = int(input("Enter shift value: "))

        encrypted = encrypt(message, shift)

        print("Encrypted Message:", encrypted)

    elif choice == '2':
        message = input("Enter the encrypted message: ")
        shift = int(input("Enter shift value: "))

        decrypted = decrypt(message, shift)

        print("Decrypted Message:", decrypted)

    elif choice == '3':
        print("Program Ended.")
        break

    else:
        print("Invalid Choice! Try Again.")