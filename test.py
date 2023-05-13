import streamlit as st

def process_string(input_string):
    # You can do anything with the input string here.
    # I'll just return the input string as it is.
    return input_string

st.title('String Processing App')

user_input = st.text_input('Enter a string')
output_string = process_string(user_input)

if st.button('Process String'):
    st.write('Processed String: ', output_string)