import streamlit as st 

def convert_unit(from_unit, to_unit, value):
    conversions = {
        "meters_kilometers": 0.001, # 1 meter = 0.001 kilometer
        "kilometers_meters": 1000,  # 1 kilometer = 1000 meter
        "grams_kilograms": 0.001,  # 1 gram = 0.001 kilogram
        "kilograms_grams": 1000,   # 1 kilogram = 1000 gram
    }

    key = f"{from_unit}_{to_unit}"
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Invalid unit"
    
st.title("Unit Converter")

value = st.number_input("Enter the value to convert",min_value=1.0,step=0.1)

unit_from = st.selectbox("convert from:", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("convert to:", ["meters", "kilometers", "grams", "kilograms"])

if st.button("Convert"):
    result = convert_unit(unit_from, unit_to, value)
    st.success(f"The result is {result}")







