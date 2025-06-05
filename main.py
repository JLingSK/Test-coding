import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize attendance records in session state
if 'records' not in st.session_state:
    st.session_state.records = []

st.title("Real-Time Attendance System")

name = st.text_input("Enter your name:")

if st.button("Mark Attendance"):
    if name:
        # Add name and current time
        st.session_state.records.append({
            "Name": name,
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        st.success(f"Attendance marked for {name}")
    else:
        st.warning("Please enter your name.")

if st.button("View Attendance"):
    st.write("Attendance Records:")
    if st.session_state.records:
        df = pd.DataFrame(st.session_state.records)
        st.write(df)
    else:
        st.write("No attendance records yet.")

# Add a download button for attendance data
if st.session_state.records:
    df = pd.DataFrame(st.session_state.records)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Attendance as CSV",
        data=csv,
        file_name='attendance.csv',
        mime='text/csv'
    )
