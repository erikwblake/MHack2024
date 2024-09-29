import streamlit as st

st.title("Foster Matchmaker")

st.write("Find the best foster home for your needs.")

col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/profiles.py", label="My Profile", icon="👤")
with col2:
    st.page_link("pages/matching.py", label="Matching", icon="🫂")

col3, col4 = st.columns(2)
with col3:
    st.page_link("pages/login.py", label="Login", icon="🔑")
with col4:
    st.page_link("pages/create_user.py", label="Sign Up", icon="➕")