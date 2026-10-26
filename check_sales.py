import sys
import pandas as pd

df = pd.read_csv("sales.txt")
errors = []

expected = ["item", "quantity", "price"]
if list(df.columns) != expected:
    errors.append(f"Columns should be {expected}, found {list(df.columns)}")
else:
    if df.isnull().any().any():
        errors.append("There are missing values")
    if df["item"].duplicated().any():
        errors.append("Duplicate items found")
    if (df["quantity"] <= 0).any():
        errors.append("Quantity must be positive")
    if (df["price"] <= 0).any():
        errors.append("Price must be positive")

if errors:
    for e in errors:
        print("FAIL:", e)
    sys.exit(1)

print(f"OK: {len(df)} rows passed all checks")
