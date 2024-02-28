import streamlit as st

st.header('This is my first web app!')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

code = '''def cat():
    print("Hello, Cat")'''
st.code(code, language='python')

cat = st.checkbox('Do you think your instructor is awesome')

if cat:
    st.write('He is!')