import streamlit as st

def navi():
    columns = st.columns((1,1,1,1))

    with columns[0]:
        st.page_link("pages/0_XOR_Cipher.py", label="XOR Cipher", icon="🔑", use_container_width=True)
    with columns[1]:
        st.page_link("pages/1_Primitive_Root.py", label="Primitive Root", icon="🔑", use_container_width=True)
    with columns[2]:
        st.page_link("pages/2_Caesar_Cipher.py", label="Caesar Cipher", icon="🔑", use_container_width=True)
    with columns[3]:
        st.page_link("pages/3_Block_Cipher.py", label="Block Cipher", icon="🔑", use_container_width=True)
        