import streamlit as st

def xor_encrypt(plaintext, key):
    """Encrypts plaintext using XOR cipher with the given key, printing bits involved."""

    ciphertext = bytearray()
    for i in range(len(plaintext)):
        plaintext_byte = plaintext[i]
        key_byte = key[i % len(key)]
        cipher_byte = plaintext_byte ^ key_byte

        st.write("Plaintext byte:", format(plaintext_byte, '08b'), "=", chr(plaintext_byte))
        st.write("Key byte:      ", format(key_byte, '08b'), "=", chr(key_byte))
        st.write("XOR result:    ", format(cipher_byte, '08b'), "=", chr(cipher_byte))
        st.write("--------------------")
        ciphertext.append(cipher_byte)

    return ciphertext

def xor_decrypt(ciphertext, key):
    """Decrypts ciphertext using XOR cipher with the given key."""
    return xor_encrypt(ciphertext, key)  # XOR decryption is the same as encryption


# Example usage:
st.write("# Welcome To XOR Cipher🔒🔒🔒")
plaintext = bytes(st.text_area("Plaintext:").encode())
key = bytes(st.text_area("Key:").encode())

if st.button("Encrypt!"):
    if plaintext == key:
        st.write("Plaintext should not be equal to the key")
    elif len(plaintext.decode()) < len(key.decode()):
        st.write("Plaintext length should be equal or greater than the length of key")
    else:
        encrypt = xor_encrypt(plaintext, key)
        st.write("Ciphertext:", encrypt.decode())
        
        decrypt = xor_decrypt(encrypt, key)
        st.write("Decrypted:", decrypt.decode())


