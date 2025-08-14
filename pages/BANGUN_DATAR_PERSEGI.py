import streamlit as st

st.title("PERSEGI")
st.markdown("""
### RUMUS :
- K = Keliling
- L = Luas
- V = Volume
- p = Panjang
- l = Lebar
- t = Tinggi
### RUMUS MENCARI KELILING :
- K = 4 x (p + l + t)
### RUMUS MENCARI LUAS :
- L = 2 x (p x l) + (p x t) + (l x t)
### RUMUS MENCARI VOLUME :
- V = p x l x t
""")
st.subheader("👇Masukan Angka👇")
sisi = st.number_input("Masukan Panjang Sisi:")
st.header("KELILING")
keliling = sisi**2
st.subheader(keliling)

st.header("LUAS")
luas = 4 * sisi
st.subheader(luas)

