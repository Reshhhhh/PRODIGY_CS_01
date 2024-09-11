def encrypt(plaintext,n):
    ans = ""
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch==" ":
            ans+=" "
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)    
    return ans

def decrypt():
    encrypted_message = input("Enter the message to be decrypted: ").strip()
    letters="abcdefghijklmnopqrstuvwxyz"
    k = int(input("Enter the Shift key to decrypt: "))
    decrypted_message = ""
    for ch in encrypted_message:
        if ch in letters:
            position = letters.find(ch)
            new_pos = (position - k) % 26
            new_char = letters[new_pos]
            decrypted_message += new_char
        else:
            decrypted_message += ch
    print("Your decrypted message is: " + decrypted_message)

def choices():
    choice = int(input('''CAESER CIPHER
        1. ENCRYPTION (1)
        2. DECRYPTION (2)

Enter user choice: '''))
    if choice == 1:
        plaintext = input("Enter the Message to be encrypted: ")
        n = int(input("Enter Shift key to encrypt: "))
        print("Your encrypted message is: " + encrypt(plaintext,n))
    elif choice == 2:
        decrypt()
    else:
        print("\nInvalid Option. Press 1 (or) 2 to continue.")
        choices()

choices()
while True:
    a = input("Enter yes/no to continue: ")
    if a=="yes":
        print("\n")
        choices()
        continue
    elif a=="no":
        break
    else:
        print("Enter either yes/no to proceed")








