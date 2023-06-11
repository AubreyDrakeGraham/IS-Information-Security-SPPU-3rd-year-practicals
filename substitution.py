substitution_dict = {
    'a': 'q',
    'b': 'w',
    'c': 'e',
    'd': 'r',
    'e': 't',
    'f': 'y',
    'g': 'u',
    'h': 'i',
    'i': 'o',
    'j': 'p',
    'k': 'a',
    'l': 's',
    'm': 'd',
    'n': 'f',
    'o': 'g',
    'p': 'h',
    'q': 'j',
    'r': 'k',
    's': 'l',
    't': 'z',
    'u': 'x',
    'v': 'c',
    'w': 'v',
    'x': 'b',
    'y': 'n',
    'z': 'm',
    ' ': ' '
}


def encrypt(plaintext):
    ciphertext = ""
    for char in plaintext:
        
        if char.lower() in substitution_dict:
            
            ciphertext += substitution_dict[char.lower()]
        else:
            
            ciphertext += char
    return ciphertext


def decrypt(ciphertext):
    plaintext = ""
    for char in ciphertext:
       
        if char.lower() in [v.lower() for v in substitution_dict.values()]:
            
            for k, v in substitution_dict.items():
                if v.lower() == char.lower():
                    plaintext += k
                    break
        else:
            
            plaintext += char
    return plaintext


plaintext = "Hello, world!"
ciphertext = encrypt(plaintext)
decrypted_plaintext = decrypt(ciphertext)

print("Original text:", plaintext)
print("Encrypted text:", ciphertext)
print("Decrypted text:", decrypted_plaintext)
