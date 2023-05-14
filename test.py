# import streamlit as st

# def process_string(input_string):
#     # You can do anything with the input string here.
#     # I'll just return the input string as it is.
#     return input_string

# st.title('String Processing App')

# user_input = st.text_input('Enter a string')
# output_string = process_string(user_input)

# if st.button('Process String'):
#     st.write('Processed String: ', output_string)
import streamlit as st
from streamlit_chat import message

st.set_page_config(
    page_title="String Processing Chat",
    page_icon=":speech_balloon:"
)

st.header("String Processing Chat - Demo")
st.markdown("[Github](https://github.com/your-github-link)")

if 'past_user_inputs' not in st.session_state:
    st.session_state['past_user_inputs'] = []
if 'past_outputs' not in st.session_state:
    st.session_state['past_outputs'] = []

def process_string(input_string):
    # You can do anything with the input string here.
    # I'll just return the input string as it is.
    return input_string

def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text 

user_input = get_text()

if user_input:
    output_string = process_string(user_input)

    st.session_state.past_user_inputs.append(user_input)
    st.session_state.past_outputs.append(output_string)
    print(st.session_state.past_outputs.append(output_string))

if st.session_state['past_user_inputs']:

    # for i in range(len(st.session_state['past_user_inputs'])-1, -1, -1):
        # message(st.session_state['past_outputs'][i], key=str(i))
        # message(st.session_state['past_user_inputs'][i], is_user=True, key=str(i) + '_user')
    message(st.session_state['past_outputs'][-1], key=len(st.session_state.past_user_inputs))
    message(st.session_state['past_user_inputs'][-1], is_user=True, key=len(st.session_state.past_user_inputs) + '_user')
