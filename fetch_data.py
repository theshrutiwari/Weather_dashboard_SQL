import requests
import sqlite3
from datetime import datetime
from config import API_KEY, CITY, BASE_URL, DB_PATH

def fetch_weather():
    params = {"q": CITY, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    weather = (
        CITY,
        data["main"]["temp"],
        data["main"]["humidity"],
        data["wind"]["speed"],
        data["weather"][0]["description"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    return weather

def store_weather(weather):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO weather_data (city, temp, humidity, wind_speed, condition, datetime)
        VALUES (?, ?, ?, ?, ?, ?)
    """, weather)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    weather = fetch_weather()
    store_weather(weather)
    print(f"✅ Data stored: {weather}")
