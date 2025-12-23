"""
Project Name : E-Commerce Sales Dashboard
Description  : Sales analysis using NumPy, Pandas, and Matplotlib
Author       : Bacher of science,information and computer science
Purpose     : Understand business sales data and visualize insights
"""


# 1. IMPORT REQUIRED LIBRARIES

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 2. CREATE E-COMMERCE DATA

data = {
    "Order_ID": [1001, 1002, 1003, 1004, 1005, 1006],
    "Product": ["Mobile", "Laptop", "Shoes", "Mobile", "Laptop", "Shoes"],
    "Category": ["Electronics", "Electronics", "Fashion",
                 "Electronics", "Electronics", "Fashion"],
    "Price": [15000, 55000, 3000, 16000, 52000, 3500],
    "Quantity": [2, 1, 3, 1, 1, 2],
    "Month": ["Jan", "Jan", "Feb", "Feb", "Mar", "Mar"]
}

df = pd.DataFrame(data)

print("\n--- Original Sales Data ---")
print(df)



# 3. FEATURE ENGINEERING

# Business logic: Total Sales = Price × Quantity

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("\n--- Data After Calculating Total Sales ---")
print(df)



# 4. NUMPY ANALYSIS

# Fast numerical insights

total_revenue = np.sum(df["Total_Sales"])
average_order_value = np.mean(df["Total_Sales"])
highest_order = np.max(df["Total_Sales"])

print("\n--- Sales Summary (NumPy) ---")
print("Total Revenue       :", total_revenue)
print("Average Order Value :", average_order_value)
print("Highest Order Value :", highest_order)


# 5. PANDAS BUSINESS ANALYSIS

# Category-wise and Month-wise analysis

category_sales = df.groupby("Category")["Total_Sales"].sum()
monthly_sales = df.groupby("Month")["Total_Sales"].sum()

print("\n--- Category-wise Sales ---")
print(category_sales)

print("\n--- Monthly Sales ---")
print(monthly_sales)


# 6. DATA VISUALIZATION

# Category-wise Sales (Bar Chart)

plt.figure()
category_sales.plot(kind="bar")
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

# Monthly Sales Trend (Line Chart)
plt.figure()
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

# Sales Distribution (Pie Chart)
plt.figure()
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Distribution by Category")
plt.ylabel("")
plt.show()



# 7. PROJECT COMPLETION MESSAGE

print("\nE-Commerce Sales Dashboard executed successfully.")
