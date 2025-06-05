import streamlit as st

# Initialize attendance records in session state
if 'records' not in st.session_state:
    st.session_state.records = []

st.title("Real-Time Attendance System")

name = st.text_input("Enter your name:")

if st.button("Mark Attendance"):
    if name:
        st.session_state.records.append(name)
        st.success(f"Attendance marked for {name}")
    else:
        st.warning("Please enter your name.")

if st.button("View Attendance"):
    st.write("Attendance Records:")
    st.write(st.session_state.records)