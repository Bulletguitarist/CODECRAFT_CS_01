## Caesar Cipher 

## Introduction

The *Caesar Cipher* is a very simple type of encryption where each letter in a message is shifted by a fixed number. This project is a basic Python program that can encrypt and decrypt any message using a shift value.

This README is kept *very simple* so you can use it easily in school/college projects or GitHub.

---

## What Is the Caesar Cipher?

It is a method where:

* You pick a number (shift value)
* Every letter is moved forward by that number
* Example (Shift = 3):

  * A → D
  * B → E
  * X → A (wrap-around)

That's it — very simple.

---

## Features

* Encrypts text
* Decrypts text
* Keeps spaces, numbers, and symbols unchanged
* Works for both uppercase and lowercase letters

---

## File Included

* *first.py* — The main Python script

---

## How the Program Works (Easy Explanation)

1. User enters a message.
2. User enters a shift value.
3. The program shifts each letter forward (encrypt).
4. For decryption, the program shifts letters back.

---

## Python Code


def encrypt(text, shift):
    result = ""
    shift = shift % 26
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)


---

## How to Run

1. Install Python
2. Save the code in a file named *first.py*
3. Open terminal/command prompt
4. Run:


python first.py


## Example

*Input:*


HELLO
Shift = 3


*Output:*


KHOOR
HELLO


---

## Author
Jyotirmoy Mahapatra
