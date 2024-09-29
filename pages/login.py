import streamlit as st
from main import client
st.title("Login")
email = st.text_input("E-Mail")
password = st.text_input("Password")
db = client['host']
collection = db['ctakers']
    

if st.button("Submit"):

    result = collection.find_one({"email": email})
    
    if result:
        if result["password"] == password:
            st.write("Login Successful")
            if result["type"] == "patient":
                st.write("Redirecting to patient portal")
            elif result["type"] == "institution":
                st.write("Redirecting to institution portal")
        else:
            st.write("Passwords don't match")
    else:
        st.write("User does not exist")
        


    #create mongodb query to search for email in the database
        #if it doesn't exist, write "user does not exist"
    #if it does, check if passwords match
        #if they doesn't, write "passwords don't match"
    #if both above are true, then send them to the proper portal

    # depending on class type of user, send them to the proper portal
        #if user is a patient, send them to the patient portal
        #if user is an institution, send them to the institution portal
        
    #Delete this once you implement it