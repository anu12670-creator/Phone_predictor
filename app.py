import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

st.set_page_config(page_title="Phone Addiction Predictor", layout="centered")

st.title("📱 Phone Addiction Level Predictor")

st.write("Fill all details below:")

# ---- INPUTS ----
age = st.number_input("Age", 10, 80)
gender = st.selectbox("Gender", ["Male", "Female"])

daily_usage = st.number_input("Daily Usage Hours", 0.0, 24.0)
sleep_hours = st.number_input("Sleep Hours", 0.0, 12.0)

# ⚠️ KEEP SAME WRONG NAME AS TRAINING
interllectual = st.number_input("Interllectual Performance", 0.0, 10.0)

social = st.number_input("Social Interactions", 0.0, 10.0)
exercise = st.number_input("Exercise Hours", 0.0, 10.0)

anxiety = st.number_input("Anxiety Level", 0.0, 10.0)
depression = st.number_input("Depression Level", 0.0, 10.0)
self_esteem = st.number_input("Self Esteem", 0.0, 10.0)

screen_bed = st.number_input("Screen Time Before Bed", 0.0, 10.0)
phone_checks = st.number_input("Phone Checks Per Day", 0, 500)
apps_used = st.number_input("Apps Used Daily", 0, 50)

social_media = st.number_input("Time on Social Media", 0.0, 12.0)
gaming = st.number_input("Time on Gaming", 0.0, 12.0)
education = st.number_input("Time on Education", 0.0, 12.0)

purpose = st.selectbox("Phone Usage Purpose", [
    "Social", "Gaming", "Education", "Work", "Other"
])

family = st.number_input("Family Communication", 0.0, 10.0)
weekend = st.number_input("Weekend Usage Hours", 0.0, 24.0)

# ---- ENCODING ----
gender = 1 if gender == "Male" else 0

purpose_map = {
    "Social": 0,
    "Gaming": 1,
    "Education": 2,
    "Work": 3,
    "Other": 4
}
purpose = purpose_map[purpose]

# ---- CREATE INPUT DATA ----
input_data = pd.DataFrame([{
    "Age": age,
    "Gender": gender,
    "Daily_Usage_Hours": daily_usage,
    "Sleep_Hours": sleep_hours,
    "Interllectual_Performance": interllectual,  # ⚠️ MATCH MODEL
    "Social_Interactions": social,
    "Exercise_Hours": exercise,
    "Anxiety_Level": anxiety,
    "Depression_Level": depression,
    "Self_Esteem": self_esteem,
    "Screen_Time_Before_Bed": screen_bed,
    "Phone_Checks_Per_Day": phone_checks,
    "Apps_Used_Daily": apps_used,
    "Time_on_Social_Media": social_media,
    "Time_on_Gaming": gaming,
    "Time_on_Education": education,
    "Phone_Usage_Purpose": purpose,
    "Family_Communication": family,
    "Weekend_Usage_Hours": weekend
}])

# ---- PREDICTION ----
if st.button("Predict Addiction Level"):
    try:
        prediction = model.predict(input_data)[0]

        st.success(f"Predicted Addiction Level: {prediction}")

        if prediction <= 2:
            st.info("🟢 Low Addiction")
        elif prediction <= 4:
            st.warning("🟡 Moderate Addiction")
        else:
            st.error("🔴 High Addiction")

    except Exception as e:
        st.error(f"Error: {e}")