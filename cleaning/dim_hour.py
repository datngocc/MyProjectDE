import pandas as pd

hours = list(range(24))  # 0 → 23

# Gán buổi trong ngày
periods = ['Night' if h < 6 else
           'Morning' if h < 12 else
           'Afternoon' if h < 18 else
           'Evening' for h in hours]

# Gán giờ cao điểm (giả định: 7–9h sáng và 17–19h chiều)
is_peak = [1 if h in [7, 8, 17, 18] else 0 for h in hours]

# Tạo dataframe
df_hour = pd.DataFrame({
    "HOUR_KEY": hours,
    "HOUR": hours,
    "PERIOD_OF_DAY": periods,
    "IS_PEAK_HOUR": is_peak
})

# Xuất ra file
df_hour.to_csv("MyProjectDE/data_output/dim_hour.csv", index=False)
