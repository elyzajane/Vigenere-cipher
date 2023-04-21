#Vigenere cipher activity
#use def function to encrypt plaintext
def vigenere_cipher(plaintext, keyword):
    plaintext = plaintext.replace("","").upper()
    keyword = keyword.upper()
    ciphertext = ""
#ask user to input for plaintext and keyword
#encrypt the plaintext using vigenere cipher
#print the output