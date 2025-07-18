import pandas as pd

# Đọc dữ liệu gốc
df = pd.read_csv("Data/bike sharing/hour.csv")

# Tạo datetime thực tế
df['datetime'] = pd.to_datetime(df['dteday']) + pd.to_timedelta(df['hr'], unit='h')

# Tạo khóa
df['datetime_key'] = df['datetime'].dt.strftime('%Y%m%d%H').astype(int)
df['date_key'] = df['datetime'].dt.strftime('%Y%m%d').astype(int)
df['hour_key'] = df['hr']

# Chọn các cột cần thiết
columns_needed = [
    'datetime_key', 'date_key', 'hour_key',
    'season', 'weathersit', 'holiday', 'workingday',
    'temp', 'atemp', 'hum', 'windspeed',
    'casual', 'registered', 'cnt'
]
df_clean = df[columns_needed]

# Đổi tên cho rõ ràng
df_clean = df_clean.rename(columns={
    'weathersit': 'weather_key',
    'season': 'season_key',
    'holiday': 'holiday_flag',
    'workingday': 'workingday_flag',
    'cnt': 'total_count',
    'temp': 'temperature',
    'atemp': 'feeling_temp',
    'hum': 'humidity'
})

# Xuất ra file mới
df_clean.to_csv("hour_clean.csv", index=False)
