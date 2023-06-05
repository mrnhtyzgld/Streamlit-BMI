import streamlit as st

st.title("BMI Calculator")

st.header("The tool for calculating your BMI")

poundRatio = 0.45359237 #kilogram
footRatio = 30.48 #cm
inchRatio = 2.54 #cm

firstName =     str(st.text_input('First name'))
lastName =      str(st.text_input('Last name'))
st.selectbox('Gender', ['Man', 'Women', 'Prefer not to say'])
unit =          str(st.selectbox('Unit system', ['metric', 'imperial']))
if unit == "metric":
    height = st.number_input('Height:', 0, 200, value=170)
    weight = st.number_input('Weight:', 0, 200, value=80)

elif unit == "imperial":
    height = st.number_input('Height (feet):', 0, 10, value=5) * footRatio +     st.number_input('Height (inch):', 0, 12, value=0) * inchRatio
    weight = st.number_input('Weight (pound):', 0, 400, value=160) * poundRatio


bmi = weight / ((height/100)**2)
if st.button('Find BMI'):
    st.write(firstName, " ", lastName, ", your BMI says you are:")
    if bmi < 18.5:
        st.write("          Under Weight")
    elif bmi < 25:
        st.write("          Normal Weight")
    elif bmi < 30:
        st.write("          Over Weight")
    elif bmi < 40:
        st.write("          Obese")
    else:
        st.write("          Extreme Obese")


