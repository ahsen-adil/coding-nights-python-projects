import streamlit as st
import random
import string


# Function to generate a random password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    return "".join(random.choice(characters) for _ in range(length))


# Streamlit UI setup
st.title("Simple Password Generator")

length = st.slider("Select password length:", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include numbers")
use_special = st.checkbox("Include special characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)

    # Display generated password with a read-only text input for easy copy-paste
    st.text_input("Generated Password:", value=password, key="generated_password", type="default", disabled=False)

    # Optional Tip
    st.caption("💡 You can select and copy the password directly from the text box above.")

