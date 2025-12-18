import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("="*70)
print("   SALES ANALYSIS & FORECASTING SYSTEM")
print("   Professional Data Analytics Project")
print("="*70)


# Step 1: Create a realistic sales dataset

np.random.seed(42)

start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=x) for x in range(365)]

data = {
    'Date': dates,
    'Product': np.random.choice(
        ['Laptop', 'Phone', 'Tablet', 'Watch'], 365
    ),
    'City': np.random.choice(
        ['Mumbai', 'Delhi', 'Bangalore', 'Chennai'], 365
    ),
    'Sales': np.random.randint(10000, 100000, 365),
    'Units': np.random.randint(1, 20, 365)
}

df = pd.DataFrame(data)

# Extract useful time-based fields for analysis
df['Month'] = pd.to_datetime(df['Date']).dt.month
df['Quarter'] = pd.to_datetime(df['Date']).dt.quarter

# Step 2: Basic dataset understanding

print("\n[1] DATASET OVERVIEW")
print("="*70)

print(f"Total Records: {len(df)}")
print(f"Date Range: {df['Date'].min()} to {df['Date'].max()}")

print(f"\nFirst 10 records:\n{df.head(10)}")


# Step 3: Business-level insights

print("\n[2] BUSINESS INSIGHTS")
print("="*70)


total_revenue = df['Sales'].sum()
avg_daily_sales = df['Sales'].mean()

print(f"Total Revenue: Rs. {total_revenue:,.2f}")
print(f"Average Daily Sales: Rs. {avg_daily_sales:,.2f}")

# Product-wise sales analysis
print("\nProduct-wise Performance:")
product_sales = df.groupby('Product').agg({
    'Sales': ['sum', 'mean', 'count']
}).round(2)
print(product_sales)

# City-wise sales comparison
print("\nCity-wise Performance:")
city_sales = df.groupby('City')['Sales'].agg(
    ['sum', 'mean']
).round(2)
city_sales = city_sales.sort_values('sum', ascending=False)
print(city_sales)

# Monthly sales trend
print("\nMonthly Sales Trend:")
monthly = df.groupby('Month')['Sales'].sum()
print(monthly)


# Step 4: Identifying top performers

print("\n[3] TOP PERFORMERS")
print("="*70)

top_days = df.nlargest(
    5, 'Sales'
)[['Date', 'Product', 'City', 'Sales']]

print("Top 5 Sales Days:")
print(top_days)

# Quarterly performance summary
print("\nQuarterly Performance:")
quarterly = df.groupby('Quarter')['Sales'].sum()
print(quarterly)


# Step 5: Save outputs for reporting

df.to_csv('sales_data_complete.csv', index=False)
product_sales.to_csv('product_performance.csv')
city_sales.to_csv('city_performance.csv')

print("\n[4] FILES GENERATED")
print("="*70)
print("✓ sales_data_complete.csv")
print("✓ product_performance.csv")
print("✓ city_performance.csv")

print("\n[SUCCESS] ANALYSIS COMPLETE!")
print("="*70)
