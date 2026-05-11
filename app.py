import streamlit as st
import joblib

# Load files
model = joblib.load('lagos_house_model.pkl')
le = joblib.load('location_encoder.pkl')

st.title("Lagos House Rent Predictor")

# Get locations and remove the word 'Other' from the list
all_locations = sorted([loc for loc in le.classes_.tolist() if loc != 'Other'])

location = st.selectbox("Where is the house?", all_locations)
bedrooms = st.slider("How many bedrooms?", 1, 10, 3)
p_type = st.selectbox("Property Type", ["Flat", "Duplex", "Bungalow", "Terrace"])

if st.button("Predict Price"):
    # Find the numeric code from the original encoder
    loc_code = list(le.classes_).index(location)
    prediction = model.predict([[bedrooms, loc_code, 0]])[0]
    [st.success(f"Estimated Yearly Rent: ₦{float(prediction):,.2f}")
