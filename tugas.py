import streamlit as st

st.title("Contoh Program Streamlit")
with st.form(key="my_form"):
    nama = st.text_input("nama lengkap")
    jenis_kelamin = st.radio("Jelis Kelamin", ("Laki-Laki", "Perempuan"))
    submit = st.form_submit_button(label="Kirim")