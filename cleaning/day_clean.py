import pandas as pd

# Load original day.csv
df_day = pd.read_csv("Data/bike sharing/day.csv")

# Parse datetime
df_day["datetime"] = pd.to_datetime(df_day["dteday"])

# Tạo các khóa
df_day["date_key"] = df_day["datetime"].dt.strftime("%Y%m%d").astype(int)

# Chọn các cột giống với hour
columns_day = [
    "date_key", "season", "weathersit", "holiday", "workingday",
    "temp", "atemp", "hum", "windspeed", "casual", "registered", "cnt"
]

df_clean_day = df_day[columns_day]

df_clean_day = df_clean_day.rename(columns={
    'season': 'season_key',
    'weathersit': 'weather_key',
    'holiday': 'holiday_flag',
    'workingday': 'workingday_flag',
    'temp': 'temperature',
    'atemp': 'feeling_temp',
    'hum': 'humidity',
    'cnt': 'total_count',
    'casual': 'casual_count',
    'registered': 'registered_count'
})

# Export
df_clean_day.to_csv("day_clean.csv", index=False)
