from DES import des_encrypt, des_decrypt  
import os

def text_to_bin(text):
    return ''.join(f'{ord(c):08b}' for c in text)

def bin_to_text(bin_str):
    chars = [bin_str[i:i+8] for i in range(0, len(bin_str), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)

def pad(text):
    pad_len = 8 - (len(text) % 8)
    return text + chr(pad_len) * pad_len

def unpad(text):
    pad_len = ord(text[-1])
    return text[:-pad_len]

def encrypt_file(input_file, output_file, key64):
    with open(input_file, 'r', encoding='utf-8') as f:
        plaintext = f.read()

    plaintext = pad(plaintext)
    plaintext_bin = text_to_bin(plaintext)

    encrypted_bin = ''
    for i in range(0, len(plaintext_bin), 64):
        block = plaintext_bin[i:i+64]
        encrypted_bin += des_encrypt(block, key64)

    with open(output_file, 'w') as f:
        f.write(encrypted_bin)

def decrypt_file(input_file, output_file, key64):
    with open(input_file, 'r') as f:
        encrypted_bin = f.read()

    decrypted_bin = ''
    for i in range(0, len(encrypted_bin), 64):
        block = encrypted_bin[i:i+64]
        decrypted_bin += des_decrypt(block, key64)

    decrypted_text = unpad(bin_to_text(decrypted_bin))

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decrypted_text)

# Exemplo de uso
if __name__ == '__main__':
    key64 = '0001001100110100010101110111100110011011101111001101111111110001'

    encrypt_file('entrada.txt', 'saida_cifrada.txt', key64)
    print("Criptografado: saida_cifrada.txt")

    decrypt_file('saida_cifrada.txt', 'saida_decifrada.txt', key64)
    print("Decifrado: saida_decifrada.txt")
