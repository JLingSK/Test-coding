import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize attendance records in session state
if 'records' not in st.session_state:
    st.session_state.records = []

st.title("Real-Time Attendance System")

name = st.text_input("Enter your name:")
user_id = st.text_input("Enter your ID:")

if st.button("Mark Attendance"):
    if not name or not user_id:
        st.warning("Please enter both your name and ID.")
    elif not user_id.isdigit():
        st.warning("ID must be numbers only, without symbols or letters.")
    else:
        st.session_state.records.append({
            "ID": user_id,
            "Name": name,
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        st.success(f"Attendance marked for {name} (ID: {user_id})")

# New section for viewing own attendance
st.subheader("View Your Attendance")
view_id = st.text_input("Enter your ID to view your attendance:")

if st.button("View My Attendance"):
    if not view_id:
        st.warning("Please enter your ID to view attendance.")
    elif not view_id.isdigit():
        st.warning("ID must be numbers only, without symbols or letters.")
    else:
        # Filter records for this ID
        user_records = [rec for rec in st.session_state.records if rec["ID"] == view_id]
        if user_records:
            df = pd.DataFrame(user_records)
            st.write(df)
        else:
            st.info("No attendance records found for this ID.")

# Passcode input for download (admin only)
passcode = st.text_input("Enter passcode to download attendance:", type="password")

if st.session_state.records:
    if passcode == "123456":
        df = pd.DataFrame(st.session_state.records)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Attendance as CSV",
            data=csv,
            file_name='attendance.csv',
            mime='text/csv'
        )
    elif passcode:
        st.error("Incorrect passcode.")
