import pandas as pd
import os

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src" / "my-new-project"))
from utils.helper import calculate_total_value


df = pd.read_csv("data/raw/sales-data.csv")
print(df)

# Add total column (price × quantity)
"""
total = []
for index, row in df.iterrows():
    total_value = calculate_total_value(row["quantity"], row["price"])
    total.append(total_value)
df["total"] = total
print(df)
"""


# create output directory if it doesn't exist
output_dir = "data/processed"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save dataframe to json file
df.to_json(
    os.path.join(output_dir, "sales-data-processed.json"), orient="records", lines=True
)
