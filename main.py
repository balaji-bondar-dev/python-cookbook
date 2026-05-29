# pandas is a powerful data manipulation library in Python. It provides data structures and functions needed to manipulate structured data seamlessly. In this example, we create a DataFrame with some sample data, including names, ages, cities, and today's date as a datetime object. We then convert the 'todays_datetime' column to a datetime format and print the DataFrame to see the results.
import pandas as pd

df = pd.DataFrame(
    {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "Los Angeles", "Chicago"],
        "todays_datetime": pd.to_datetime("2024-06-01"),
    }
)

df["todays_datetime"] = pd.to_datetime(df["todays_datetime"])
print(df)
