Activity = "\033[95mAssignment No. 2"
print(Activity)

#Vigenere cipher activity
#use def function to encrypt plaintext
def vigenere_cipher(plaintext, keyword):
    plaintext = plaintext.replace("","").upper()
    keyword = keyword.upper()
    ciphertext = ""
    for i in range(len(plaintext)):
        character = plaintext[i]
        key_character = keyword[i % len(keyword)]
        character_value = ord(character) - ord('A')
        key_character_value = ord(key_character) - ord('A')
        cipher_value = (character_value + key_character_value) % 26
        cipher_character = chr(cipher_value + ord('A'))
        ciphertext += cipher_character
    return ciphertext
#ask user to input for plaintext and keyword
plaintext = input("Enter plaintext (all uppercase letters, no spaces): ")
keyword = input("Enter keyword (all uppercase letters): ")
#encrypt the plaintext using vigenere cipher
ciphertext = vigenere_cipher(plaintext, keyword)
#print the output
print("Ciphertext: " + ciphertext)