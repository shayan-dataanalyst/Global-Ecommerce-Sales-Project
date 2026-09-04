# Importing Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Loading Dataset
df = pd.read_csv(
    r"C:\Users\PCC\Desktop\VS Code\Python\Muhammad Shayan\Global_Ecommerce_Sales_Project\01_Raw_Dataset\Raw_Dataset_Global_Ecommerce_Sales.csv"
)


# print(df["Customer_Name"].unique())

# print(df["Customer_Name"].value_counts())

# # Showing First 5 Rows
# print(df.head())

# # Finding Dataset Shape
# print("\nDataset Shape:")
# print(df.shape)

# # 2. Clean column names
# df.columns = (
#     df.columns
#     .str.strip()
#     .str.replace(r"\s+", "_", regex=True)
#     .str.replace(r"[-]+", "_", regex=True)
# )

# # Finding Column Names
# print("\nCleaned columns:")
# print(df.columns.tolist())

# # Replace common missing-value symbols
# missing_values = [
#     "", " ", "NA", "N/A", "n/a",
#     "null", "NULL", "None", "-"
# ]

# df = df.replace(missing_values, np.nan)

# # Remove duplicate rows
# before_duplicates = len(df)

# df = df.drop_duplicates()

# after_duplicates = len(df)

# print("\nDuplicate rows removed:",
#       before_duplicates - after_duplicates)

# # Finding Data Types
# print("\nData Types:")
# print(df.dtypes)

# # Finding Missing Values
# print("\nMissing Values:")
# print(df.isnull().sum())

# # Finding Duplicate Rows
# print("\nDuplicate Rows:")
# print(df.duplicated().sum())

# # Finding Basic Statistics
# print("\nDescriptive Statistics:")
# print(df.describe())

# # Converting Order Date into Date Format
# df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# # Checking Date Conversion
# print("\nOrder Date Data Type:")
# print(df["Order_Date"].dtype)

# # Checking Unique Customer Segments
# print("\nCustomer Segments:")
# print(df["Customer_Segment"].unique())

# # Checking Unique Product Categories
# print("\nProduct Categories:")
# print(df["Product_Category"].unique())

# # Checking Unique Regions
# print("\nRegions:")
# print(df["Region"].unique())

# # Checking Unique Payment Methods
# print("\nPayment Methods:")
# print(df["Payment_Method"].unique())

# # Checking Numerical Columns
# print("\nNumerical Columns:")
# print(df.select_dtypes(include=np.number).columns.tolist())

# # Checking Negative Values in Quantity
# print("\nNegative Quantity:")
# print(df[df["Quantity"] < 0])

# # Checking Negative Sales
# print("\nNegative Sales:")
# print(df[df["Total_Sales"] < 0])

# # Checking Negative Profit
# print("\nNegative Profit:")
# print(df[df["Profit"] < 0])

# # Checking Discount Range
# print("\nDiscount Range:")
# print(df["Discount_Percent"].min())
# print(df["Discount_Percent"].max())


# ###########################################################
# # Finding Total Sales
# total_sales = df["Total_Sales"].sum()
# print("\nTotal Sales:")
# print(total_sales)

# # Finding Total Profit
# total_profit = df["Profit"].sum()
# print("\nTotal Profit:")
# print(total_profit)

# # Finding Total Orders
# total_orders = df["Order_ID"].nunique()
# print("\nTotal Orders:")
# print(total_orders)

# # Finding Total Customers
# total_customers = df["Customer_Name"].nunique()
# print("\nTotal Customers:")
# print(total_customers)

# # Finding Total Quantity Sold
# total_quantity = df["Quantity"].sum()
# print("\nTotal Quantity Sold:")
# print(total_quantity)

# # Finding Average Order Value
# average_order_value = total_sales / total_orders
# print("\nAverage Order Value:")
# print(round(average_order_value, 2))

# # Finding Profit Margin
# profit_margin = (total_profit / total_sales) * 100
# print("\nProfit Margin:")
# print(round(profit_margin, 2), "%")

# # Finding Sales by Region
# region_sales = df.groupby("Region")["Total_Sales"].sum()
# print("\nSales by Region:")
# print(region_sales.sort_values(ascending=False))

# # Finding Sales by Category
# category_sales = df.groupby("Product_Category")["Total_Sales"].sum()
# print("\nSales by Category:")
# print(category_sales.sort_values(ascending=False))

# # Finding Profit by Category
# category_profit = df.groupby("Product_Category")["Profit"].sum()
# print("\nProfit by Category:")
# print(category_profit.sort_values(ascending=False))

# # Finding Sales by Customer Segment
# segment_sales = df.groupby("Customer_Segment")["Total_Sales"].sum()
# print("\nSales by Customer Segment:")
# print(segment_sales.sort_values(ascending=False))

# # Finding Sales by Payment Method
# payment_sales = df.groupby("Payment_Method")["Total_Sales"].sum()
# print("\nSales by Payment Method:")
# print(payment_sales.sort_values(ascending=False))

# # Finding Sales by Country
# country_sales = df.groupby("Country")["Total_Sales"].sum()
# print("\nTop Countries by Sales:")
# print(country_sales.sort_values(ascending=False).head(10))

# # Finding Top 10 Products by Sales
# top_products_sales = (
#     df.groupby("Product_Name")["Total_Sales"]
#     .sum()
#     .sort_values(ascending=False)
#     .head(10)
# )
# print("\nTop 10 Products by Sales:")
# print(top_products_sales)

# # Finding Top 10 Products by Profit
# top_products_profit = (
#     df.groupby("Product_Name")["Profit"]
#     .sum()
#     .sort_values(ascending=False)
#     .head(10)
# )
# print("\nTop 10 Products by Profit:")
# print(top_products_profit)

# # Finding Top 10 Products by Quantity
# top_products_quantity = (
#     df.groupby("Product_Name")["Quantity"]
#     .sum()
#     .sort_values(ascending=False)
#     .head(10)
# )
# print("\nTop 10 Products by Quantity:")
# print(top_products_quantity)

# # Finding Top 10 Customers by Sales
# top_customers = (
#     df.groupby("Customer_Name")["Total_Sales"]
#     .sum()
#     .sort_values(ascending=False)
#     .head(10)
# )
# print("\nTop 10 Customers:")
# print(top_customers)

# # Finding Top Customers by Orders
# customer_orders = (
#     df.groupby("Customer_Name")["Order_ID"]
#     .nunique()
#     .sort_values(ascending=False)
#     .head(10)
# )
# print("\nTop Customers by Number of Orders:")
# print(customer_orders)

# # Creating Year-Month Column
# df["Year_Month"] = df["Order_Date"].dt.to_period("M")

# # Finding Monthly Sales
# monthly_sales = df.groupby("Year_Month")["Total_Sales"].sum()
# print("\nMonthly Sales:")
# print(monthly_sales)

# # Finding Monthly Profit
# monthly_profit = df.groupby("Year_Month")["Profit"].sum()
# print("\nMonthly Profit:")
# print(monthly_profit)

# # Finding Average Discount
# average_discount = df["Discount_Percent"].mean()
# print("\nAverage Discount:")
# print(round(average_discount, 2), "%")

# # Finding Average Profit by Discount
# discount_profit = df.groupby("Discount_Percent")["Profit"].mean()
# print("\nAverage Profit by Discount:")
# print(discount_profit)

# # Finding Best Region
# print("\nBest Region:")
# print(region_sales.idxmax())

# # Finding Best Category
# print("\nBest Category:")
# print(category_sales.idxmax())

# # Finding Most Profitable Category
# print("\nMost Profitable Category:")
# print(category_profit.idxmax())

# # Finding Best Customer Segment
# print("\nBest Customer Segment:")
# print(segment_sales.idxmax())

# # Finding Best Payment Method
# print("\nBest Payment Method:")
# print(payment_sales.idxmax())

# ######## Charts ########
# # Creating Monthly Sales Chart
# plt.figure(figsize=(12, 6))
# monthly_sales.plot(kind="line", marker="o")
# plt.title("Monthly Sales Trend")
# plt.xlabel("Month")
# plt.ylabel("Total Sales")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # Creating Monthly Profit Chart
# plt.figure(figsize=(12, 6))
# monthly_profit.plot(kind="line", marker="o")
# plt.title("Monthly Profit Trend")
# plt.xlabel("Month")
# plt.ylabel("Total Profit")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # Creating Category Sales Chart
# plt.figure(figsize=(10, 6))
# category_sales.sort_values().plot(kind="barh")
# plt.title("Sales by Product Category")
# plt.xlabel("Total Sales")
# plt.ylabel("Product Category")
# plt.tight_layout()
# plt.show()

# # Creating Region Sales Chart
# plt.figure(figsize=(10, 6))
# region_sales.sort_values().plot(kind="bar")
# plt.title("Sales by Region")
# plt.xlabel("Region")
# plt.ylabel("Total Sales")
# plt.xticks(rotation=30)
# plt.tight_layout()
# plt.show()

# # Creating Top Products Chart
# plt.figure(figsize=(12, 6))
# top_products_sales.sort_values().plot(kind="barh")
# plt.title("Top 10 Products by Sales")
# plt.xlabel("Total Sales")
# plt.ylabel("Product")
# plt.tight_layout()
# plt.show()

# # Creating Profit by Category Chart
# plt.figure(figsize=(10, 6))
# category_profit.sort_values().plot(kind="bar")
# plt.title("Profit by Product Category")
# plt.xlabel("Product Category")
# plt.ylabel("Total Profit")
# plt.xticks(rotation=30)
# plt.tight_layout()
# plt.show()

# # Creating Customer Segment Chart
# plt.figure(figsize=(10, 6))
# segment_sales.plot(kind="bar")
# plt.title("Sales by Customer Segment")
# plt.xlabel("Customer Segment")
# plt.ylabel("Total Sales")
# plt.xticks(rotation=30)
# plt.tight_layout()
# plt.show()

# # Creating Payment Method Chart
# plt.figure(figsize=(10, 6))
# payment_sales.plot(kind="bar")
# plt.title("Sales by Payment Method")
# plt.xlabel("Payment Method")
# plt.ylabel("Total Sales")
# plt.xticks(rotation=30)
# plt.tight_layout()
# plt.show()

# # Creating Top Customers Chart
# plt.figure(figsize=(12, 6))
# top_customers.sort_values().plot(kind="barh")
# plt.title("Top 10 Customers by Sales")
# plt.xlabel("Total Sales")
# plt.ylabel("Customer")
# plt.tight_layout()
# plt.show()

# # Creating Discount vs Profit Chart
# plt.figure(figsize=(10, 6))
# plt.scatter(
#     df["Discount_Percent"],
#     df["Profit"],
#     alpha=0.6
# )
# plt.title("Discount vs Profit")
# plt.xlabel("Discount %")
# plt.ylabel("Profit")
# plt.tight_layout()
# plt.show()

# # Finding Numerical Correlations
# numeric_data = df.select_dtypes(include=np.number)
# correlation = numeric_data.corr()

# print("\nCorrelation Matrix:")
# print(correlation)

# # Creating Correlation Heatmap
# plt.figure(figsize=(10, 7))
# sns.heatmap(
#     correlation,
#     annot=True,
#     cmap="coolwarm",
#     fmt=".2f"
# )
# plt.title("Correlation Heatmap")
# plt.tight_layout()
# plt.show()

# # Perform linear regression to analyze the relationship between discount and profit
# X = df[["Discount_Percent"]]
# y = df["Profit"]

# model = LinearRegression()
# model.fit(X, y)

# # Prediction
# y_pred = model.predict(X)

# print("Coefficient:", model.coef_[0])
# print("Intercept:", model.intercept_)
# print("R² Score:", model.score(X, y))

# # Plot
# plt.figure(figsize=(10, 6))
# plt.scatter(X, y)
# plt.plot(X, y_pred)
# plt.xlabel("Discount Percent")
# plt.ylabel("Profit")
# plt.title("Regression: Discount vs Profit")
# plt.show()

# # import pandas as pd

# # df = pd.read_excel("Projects/Global_Ecommerce_Sales.xlsx", sheet_name="Global Ecommerce Sales")

# # # Data check karna
# # print("Rows:", df.shape[0])
# # print("Columns:", df.shape[1])
# # print(df.head())

# # # CSV file banana
# # df.to_csv(
# #     r"C:\Users\PCC\Desktop\global_ecommerce_sales.csv",
# #     index=False
# # )

# # print("CSV successfully created!")
