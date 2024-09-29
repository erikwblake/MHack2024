import streamlit as st

st.title("Create New User")
name = st.text_input("Enter New Username")
password = st.text_input("Enter New Password")
password2 = st.text_input("Reenter New Password")

failed = False

col1, col2 = st.columns(2)
with col1:
    if st.button("Patient"):
        patient = True
        #populate rest of info
        with st.form("patient_form"):
        #populate rest of info
            dob = st.text_input("Enter Your Date of Birth (MM/DD/YYYY):")
            needs = st.text_input("Enter Your Needs:")
            meds = st.text_input("Enter The Medications You Use:")
            submitted = st.form_submit_button("Submit")
            if submitted and (password == password2):
                st.write("Account made!")
                 #PUSH NEW PATIENT INFO INTO DATABSE
            elif submitted and (password != password2):
                failed = True
if(failed):
    st.write("There was an error with your submission. Please try again.")
with col2:
    if st.button("Institution"):
        patient = False
        with st.form("Institution_form"):
            services = st.text_input("Enter The Services Your Home/Institution Provides:")
        #location = 
        #We'll figure this out eventually^^
            capacity = st.number_input( "Enter Your Resident Capacity", min_value=0, step=1)
            current_num = st.number_input("How Many Residents Are Currently Staying At Your Home/Institution:", min_value=0, step=1)
            rate = st.number_input("Enter Your Home/Institution's Monthly Charges:")
            submitted = st.form_submit_button("Submit")
            if submitted and (password == password2):
                st.write("Account made!")
                #PUSH NEW INSTITUTION INFO INTO DATABSE
            elif submitted and (password != password2):
                failed = True
if(failed):
    st.write("There was an error with your submission. Please try again.")