import streamlit as st
import pandas as pd
import datetime
import csv
import os

# CSV file name
MOOD_FILE = "mood_log.csv"

# Ensure the CSV file has headers
def initialize_csv():
    if not os.path.exists(MOOD_FILE) or os.stat(MOOD_FILE).st_size == 0:
        with open(MOOD_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Mood"])  # Ensure correct headers

# Load mood data safely
def load_mood_data():
    initialize_csv()  # Ensure file is initialized
    try:
        data = pd.read_csv(MOOD_FILE, encoding="utf-8", on_bad_lines="skip")

        # Ensure "Date" and "Mood" columns exist
        if "Date" not in data.columns or "Mood" not in data.columns:
            data = pd.DataFrame(columns=["Date", "Mood"])

        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame(columns=["Date", "Mood"])  # Return empty DataFrame if error

# Save mood data
def save_mood_data(date, mood):
    with open(MOOD_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])

# Streamlit UI
st.set_page_config(page_title="Mood Tracker", page_icon="😊", layout="centered")

# App Title
st.markdown("<h1 style='text-align: center; color: #FF5733;'>Mood Tracker</h1>", unsafe_allow_html=True)

# Get today's date
today = datetime.date.today()

# Mood selection
st.subheader("🌟 How are you feeling today?")
mood = st.selectbox("Select your mood", ["Happy 😊", "Sad 😢", "Angry 😡", "Neutral 😐"])

# Log Mood Button
if st.button("💾 Log Mood"):
    save_mood_data(today, mood)
    st.success(f"✅ Mood Logged Successfully for {today}!")

# Load and process data
data = load_mood_data()

# Ensure "Mood" column exists before using value_counts()
if "Mood" in data.columns and not data.empty:
    st.subheader("📊 Mood Trends Over Time")

    # Convert date to datetime
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data = data.dropna()  # Remove invalid rows

    # Display mood frequency
    mood_counts = data["Mood"].value_counts()
    st.bar_chart(mood_counts)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("Built with ❤️ by [Ahsen Adil](https://github.com/ahsen-adil)", unsafe_allow_html=True)
