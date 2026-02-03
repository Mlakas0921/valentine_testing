import streamlit as st
import random

# Set page title and icon
st.set_page_config(page_title="Valentine's Invite", page_icon="💖")

# Initialize "Yes" button size in session state so it stays big after clicking "No"
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 1.0

# Header
st.title("Rajani, Will you be my Valentine? 🥺")

# Create two columns for the buttons
col1, col2 = st.columns([1, 1])

with col1:
    # The "Yes" button grows every time "No" is clicked
    btn_text = "YES"
    if st.button(btn_text, use_container_width=True, type="primary"):
        st.balloons() # Native Streamlit celebration!
        st.success("YAAAAAAAY! 🎉😁😁😁")
        st.image("https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif")
        st.stop() # Stops the rest of the code from running

with col2:
    # In Streamlit, buttons can't "run away" easily, so we make "Yes" grow instead!
    if st.button("No", use_container_width=True):
        st.session_state.yes_size += 0.5
        st.write("“No” seems a bit shy 😈")

# Visual cue that the Yes button is getting bigger (Optional feedback)
if st.session_state.yes_size > 1.0:
    st.info(f"The 'Yes' button is now {int(st.session_state.yes_size * 100)}% more likely to be clicked!")
