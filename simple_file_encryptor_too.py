print("Simple File Encyptor with  Caesar Cipher")

filename=input("Enter the file name to encrypt: ")
try:
    with open(filename, 'r') as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
def ceaser_cypher(text,shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base= ord ('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text
encrypted_content = ceaser_cypher(content, 3)
print(encrypted_content)