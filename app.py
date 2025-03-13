
import streamlit as st

st.title('BMI Calculator')

weight = st.number_input('Enter your weight in kilograms:')
height = st.number_input('Enter your height in meters:')

if st.button('Calculate BMI'):
    bmi = weight / (height ** 2)
    st.write('Your BMI is:', bmi)

    if bmi < 18.5:
        st.write('You are underweight.')
    elif bmi >= 18.5 and bmi < 25:
        st.write('You are within the healthy weight range.')
    elif bmi >= 25 and bmi < 30:
        st.write('You are overweight.')
    else:
        st.write('You are obese.')