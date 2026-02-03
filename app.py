import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Valentine's Invite", page_icon="💖")

# 2. Initialize "Yes" button size in session state
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 1.0

# 3. Display your uploaded GIF
# Change "panda.gif" to your exact filename if it's different!
st.image("panda.gif", width=300)

# 4. Header
st.title("Rajani, Will you be my Valentine? 🥺")

# 5. Create two columns for the buttons
col1, col2 = st.columns([1, 1])

with col1:
    # The "Yes" button text/size
    if st.button("YES", use_container_width=True, type="primary"):
        st.balloons() 
        st.success("YAAAAAAAY! 🎉😁😁😁")
        # Optional: You can add another celebratory GIF here too!
        st.image("https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif")
        st.stop() 

with col2:
    # Logic for the "No" button
    if st.button("No", use_container_width=True):
        st.session_state.yes_size += 0.4
        st.write("“No” seems a bit shy 😈")

# 6. Make the "Yes" button grow visually (Optional Text Feedback)
if st.session_state.yes_size > 1.0:
    st.info("The 'Yes' button is getting bigger... you know what to do! 😉")
