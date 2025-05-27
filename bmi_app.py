import streamlit as st

st.title("BMI Calculator")

name = st.text_input("Enter your name:")
height = st.number_input("Enter your height in meters:", min_value=0.5, max_value=2.5, step=0.01)
weight = st.number_input("Enter your weight in kg:", min_value=10.0, max_value=300.0, step=0.1)

if st.button("Calculate BMI"):
    if name and height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.write(f"Hello {name}, your BMI is: **{bmi:.2f}**")
        if bmi < 18.5:
            st.info("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        elif 30 <= bmi < 34.9:
            st.error("You are obese (Class 1).")
        elif 35 <= bmi < 39.9:
            st.error("You are obese (Class 2).")
        elif bmi >= 40:
            st.error("You are obese (Class 3).")
        st.write("Thank you for using the BMI calculator!")
    else:
        st.warning("Please enter all fields.")