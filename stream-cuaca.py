import pickle
import streamlit as st

st.markdown("""
    <style>
        body .stApp {
            background-color: #87CEEB !important;
            color: #ffffff !important;
        }
        /* Mengubah warna teks di kotak teks (textbox) */
        .stTextInput > div > div > input {
            color: #000000 !important;
        }
        /* Mengubah warna kotak teks */
        .stTextInput > div > div > input {
            background-color: #ffffff !important;
        }
         /* Mengubah warna teks judul */
        .stApp h1 {
            color: #000000 !important;
        }
        /* Mengubah warna teks masukan */
        .stTextInput label {
            color: #000000 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Baca model
cuaca_model = pickle.load(open('trained_model2.sav', 'rb'))

# Judul web
st.title('Weather Prediction in Singapore')

col1, col2, col3 = st.columns(3)

# Input
with col1:
    dt = st.text_input('Enter the value for time difference (dt)')
with col2:
    sunrise = st.text_input('Enter the value for sunrise time', key="sunrise")
with col3:
    sunset = st.text_input('Enter the value for sunset time')
with col1:
    moonrise = st.text_input('Enter the value for moonrise time')
with col2:
    moonset = st.text_input('Enter the value for moonset time')
with col3:
    moon_phase = st.text_input('Enter the value for moon phase')
with col1:
    pressure = st.text_input('Enter the value for atmospheric pressure')
with col2:
    wind_speed = st.text_input('Enter the value for wind speed')
with col3:
    wind_gust = st.text_input('Enter the value for wind gust')
with col1:
    rain = st.text_input('Enter the value for rainfall')
with col2:
    uvi = st.text_input('Enter the value for UV index')
with col3:
    temp_day = st.text_input('Enter the value for daytime temperature')
with col1:
    temp_max = st.text_input('Enter the value for maximum temperature')
with col2:
    temp_night = st.text_input('Enter the value for nighttime temperature')
with col3:
    temp_eve = st.text_input('Enter the value for evening temperature')
with col1:
    feels_like_day = st.text_input('Enter the value for perceived temperature during the day')
with col2:
    feels_like_eve = st.text_input('Enter the value for perceived temperature during the evening')
with col3:
    current = st.text_input('Enter the current weather condition')

weather_descriptions = {
    501: "moderate rain",
    500: "light rain",
    803: "broken clouds",
    804: "overcast clouds",
    502: "heavy intensity rain",
    801: "few clouds",
    802: "scattered clouds",
    503: "very heavy rain",
    800: "clear sky"
}

# Create a button for prediction
if st.button('Weather Prediction Test'):
    try:
        # Convert input to float type
        input_data = [float(dt), float(sunrise), float(sunset), float(moonrise), float(moonset),
                      float(moon_phase), float(pressure), float(wind_speed), float(wind_gust),
                      float(rain), float(uvi), float(temp_day), float(temp_max), float(temp_night),
                      float(temp_eve), float(feels_like_day), float(feels_like_eve), float(current)]

        # Make prediction
        cuaca_pred = cuaca_model.predict([input_data])

        # Extract the predicted value
        predicted_value = int(cuaca_pred[0])  # Ensure it's an integer
        st.write(f"<span style='color:black'>{predicted_value}</span>", unsafe_allow_html=True)  # Log the predicted value
        
        # Determine weather description
        cuaca_diagnosis = weather_descriptions.get(predicted_value, "The weather forecast is unknown.")
        st.write(f"<span style='color:black'>The weather forecast predicts: {cuaca_diagnosis}</span>", unsafe_allow_html=True)
    except ValueError:
        st.write(f"<span style='color:black'>Make sure all inputs are numbers.</span>", unsafe_allow_html=True)

    st.success(cuaca_diagnosis)