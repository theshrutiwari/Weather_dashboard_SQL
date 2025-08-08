CREATE TABLE IF NOT EXISTS weather_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    temp REAL,
    humidity INTEGER,
    wind_speed REAL,
    condition TEXT,
    datetime TEXT
);
