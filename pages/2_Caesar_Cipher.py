import streamlit as st
from nav import navi

st.set_page_config(
    page_title="Caesar Cipher",
    page_icon="🔒",
    layout="wide"
)
navi()

def encrypt_decrypt(text, shift_keys, ifdecrypt):
    """
    Encrypts a text using Caesar Cipher with a list of shift keys.
    Args:
        text: The text to encrypt.
        shift_keys: A list of integers representing the shift values for each character.
        ifdecrypt: flag if decrypt or encrypt
    Returns:
        A string containing the encrypted text if encrypt and plain text if decrypt
    """
    result = ""
    cipher_output = ""
    
    for n, char in enumerate(text):
        shift_key = shift_keys[n % len(shift_keys)] 
        if 32 <= ord(char) <= 126:
            if ifdecrypt:
                new_char = chr((ord(char) - shift_key - 32 ) % 94 + 32)
            else:
                new_char = chr((ord(char) + shift_key - 32 ) % 94 + 32 )
            result += new_char
            cipher_output += f"\n{n} {char} {shift_key} {new_char}\n"
        else:
            result += char
            cipher_output += f"{n} {char} {shift_key} {char}"
    return result, cipher_output
    
                

if __name__ == "__main__":
    # Example usage
    st.write("# Welcome To Caesar Cipher🔒🔒🔒")
    text = st.text_area("Plaintext:")
    shift_keys = list(map(int, st.text_area("Shift Keys:").split()))

    if st.button("Encrypt"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("## ENCRYPTED PROCESS")
            encrypt, cipher_output = encrypt_decrypt(text, shift_keys, ifdecrypt=False)
            st.write(cipher_output)
           
        with col2:
            st.write("## DECRYPTED PROCESS")
            decrypt, decrypt_output = encrypt_decrypt(encrypt, shift_keys, ifdecrypt=True)
            st.write(decrypt_output)
           
        with col3:
            st.write("## RESULTS")
            st.write("Text:",text)
            st.write("Shift keys:", ' '.join(map(str, shift_keys)))
            st.write("Cipher:", encrypt)
            st.write("Decrypted text:", decrypt)