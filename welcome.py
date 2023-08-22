"""
Currency Convertor App
By: Abhishek Kumar 
"""
#imports
import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

def main():
    #main method
    if "name"not in st.session_state:
        st.session_state.name="" 
    with st.sidebar:
        user=st.text_input("Enter your name: ",value=st.session_state.name)
        if st.session_state.name != user:
            st.session_state["name"] = f"{user}"


    colored_header(
        label="WELCOME 👋",
        description=f"Hello {user}!😀 welcome to the world of cool apps.",
        color_name="violet-70"
    )

if __name__ == "__main__":
    main()