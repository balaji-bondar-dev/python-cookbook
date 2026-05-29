# pandas is a powerful data manipulation library in Python. It provides data structures and functions needed to manipulate structured data seamlessly. In this example, we create a DataFrame with some sample data, including names, ages, cities, and today's date as a datetime object. We then convert the 'todays_datetime' column to a datetime format and print the DataFrame to see the results.
import pandas as pd
import os

df = pd.read_csv("data/raw/sales-data.csv")
print(df)

# create output directory if it doesn't exist
output_dir = "data/processed"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save dataframe to json file
df.to_json(
    os.path.join(output_dir, "sales-data-processed.json"), orient="records", lines=True
)

# Save dataframe to csv file
df.to_csv(os.path.join(output_dir, "sales-data-processed.csv"), index=False)

# Save dataframe to excel file
df.to_excel(os.path.join(output_dir, "sales-data-processed.xlsx"), index=False)
