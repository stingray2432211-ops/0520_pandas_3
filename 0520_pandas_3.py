import pandas as pd

df = pd.read_csv("SuperMarket Analysis.csv")

df.columns = df.columns.str.strip()

print(df.columns.tolist())

if "Total" in df.columns:
    sales_col = "Total"
elif "total" in df.columns:
    sales_col = "total"
elif "Sales" in df.columns:
    sales_col = "Sales"
else:
    print("找不到銷售額欄位")
    exit()

product_summary = df.groupby("Product line").agg(
    Total_Sales=(sales_col, "sum"),
    Avg_Rating=("Rating", "mean")
).round(2)

print(product_summary)