import streamlit as st
import pandas as pd
import pytz
from datetime import datetime

# Set your daily code here (change this value each day)
DAILY_CODE = "cohort trece"  # <-- Change this code daily
  

# Initialize attendance records in session state
if 'records' not in st.session_state:
    st.session_state.records = []

st.title("Real-Time Cohort Trece Attendance")

name = st.text_input("Enter your name:")
user_birthday = st.text_input("Enter your Birthday (YYYYMMDD):")
attendance_code = st.text_input("Enter today's attendance code: (Hint: my FB name, like '/manchester united'/)")  # <-- Add this line
suggestion = st.text_input("Suggest the next app to write:")  # <-- New input

if st.button("Mark Attendance"):
    if not name or not user_birthday or not attendance_code:
        st.warning("Please enter your name, birthday, and today's attendance code.")
    elif not user_birthday.isdigit():
        st.warning("Birthday must be numbers only, without symbols or letters.")
    elif attendance_code != DAILY_CODE:
        st.error("Invalid attendance code. Please get the correct code from the organizer.")
    else:
        st.session_state.records.append({
            "Birthday": user_birthday,
            "Name": name,
            "Suggestion": suggestion,  
            "Time": datetime.now(pytz.timezone("Asia/Kuala_Lumpur")).strftime("%Y-%m-%d %H:%M:%S")
        })
        st.success(f"Attendance marked for {name} (ID: {user_birthday})")

# New section for viewing own attendance
st.subheader("View Your Attendance")
view_birthday = st.text_input("Enter your birthday (YYYYMMDD) to view your attendance:")

if st.button("View My Attendance"):
    if not view_birthday:
        st.warning("Please enter your birthday (YYYYMMDD) to view attendance.")
    elif not view_birthday.isdigit():
        st.warning("Birthday must be numbers only, without symbols or letters.")
    else:
        # Filter records for this ID
        user_records = [rec for rec in st.session_state.records if rec["Birthday"] == view_birthday]
        if user_records:
            df = pd.DataFrame(user_records)
            st.write(df)
        else:
            st.info("No attendance records found for this date.")

# Passcode input for download (admin only)
passcode = st.text_input("For Min only, enter passcode to download attendance:", type="password")

if st.session_state.records:
    if passcode == "123456":
        df = pd.DataFrame(st.session_state.records)
        csv = df.to_csv(index=False).encode('utf+8')
        st.download_button(
            label="Download Attendance as CSV",
            data=csv,
            file_name='attendance.csv',
            mime='text/csv'
        )
    elif passcode:
        st.error("Incorrect passcode.")
