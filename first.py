# first.py

def encrypt(text, shift):
    result = ""
    # sanitize shift to 0-25 range
    shift = shift % 26
    for char in text:
        if char.isalpha():
            # choose base depending on case
            base = ord('A') if char.isupper() else ord('a')
            # convert to 0-25, add shift, wrap with %26, convert back
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char
    return result

def decrypt(text, shift):
    # decryption is encryption with negative shift
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher ===")
    message = input("Enter your message: ")
    # input validation for shift
    while True:
        try:
            shift = int(input("Enter shift value (integer): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer for shift.")
    enc = encrypt(message, shift)
    dec = decrypt(enc, shift)
    print("\nEncrypted message:", enc)
    print("Decrypted message:", dec)

if __name__ == "__main__":
    main()

