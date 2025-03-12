import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np

# Sample product data
data = {
    "Product": ["Laptop", "Smartphone", "Headphones", "Smartwatch", "Tablet", "Camera", "Shoes", "Backpack", "Gaming Console", "Smart TV", "Bluetooth Speaker", "Wireless Earbuds", "Mechanical Keyboard", "Monitor", "Printer", "Fitness Band", "Jacket", "Sunglasses", "Handbag", "Jeans", "T-shirt", "Sneakers", "Watch", "Hat"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics", "Electronics", "Fashion", "Fashion", "Electronics", "Electronics", "Accessories", "Accessories", "Accessories", "Electronics", "Electronics", "Fitness", "Fashion", "Fashion", "Fashion", "Fashion", "Fashion", "Fashion", "Fashion", "Fashion"],
    "Price": [70000, 30000, 2000, 15000, 25000, 40000, 3000, 2000, 50000, 45000, 5000, 6000, 7000, 20000, 15000, 8000, 5000, 3500, 7000, 2500, 1500, 4000, 6000, 1000],
    "Ratings": [4.5, 4.7, 4.2, 4.3, 4.6, 4.4, 4.1, 4.0, 4.8, 4.6, 4.3, 4.5, 4.7, 4.4, 4.2, 4.5, 4.3, 4.2, 4.6, 4.0, 3.9, 4.5, 4.3, 4.1],
    "Stock": [10, 25, 50, 15, 20, 5, 30, 40, 12, 18, 35, 40, 22, 10, 8, 25, 20, 15, 18, 30, 40, 25, 12, 50],
    "Discount": [10, 15, 5, 8, 12, 20, 25, 18, 10, 15, 8, 10, 12, 5, 10, 18, 20, 15, 18, 10, 12, 15, 10, 5],
    "Buy From": ["Amazon", "Flipkart", "Croma", "Amazon", "Reliance Digital", "Amazon", "Nike", "Amazon", "Flipkart", "Amazon", "Flipkart", "Amazon", "Croma", "Flipkart", "Amazon", "Nike", "Myntra", "LensKart", "Amazon", "Levi's", "Myntra", "Adidas", "Titan", "Amazon"]
}
df = pd.DataFrame(data)

# Function to recommend products based on category
def recommend_products(categories):
    return df[df["Category"].isin(categories)]

# Function to filter products by budget
def filter_by_budget(budget):
    return df[df["Price"] <= budget]

# Function to get best discounts
def best_discounts():
    return df.sort_values(by="Discount", ascending=False).head(5)

# Streamlit UI
st.title("🛍️ Personalized Shopping Assistant")
st.write("Find the best products tailored to your needs!")

# Multi-category selection
categories = st.multiselect("Choose categories", df["Category"].unique())
if categories:
    recommended = recommend_products(categories)
    st.write("### Recommended Products:")
    st.table(recommended)

# Budget filtering
budget = st.slider("Select your budget", min_value=1000, max_value=80000, step=1000)
filtered_products = filter_by_budget(budget)
st.write("### Products within your budget:")
st.table(filtered_products)

# Filter fashion-related products under budget
if "Fashion" in categories:
    fashion_products = df[(df["Category"] == "Fashion") & (df["Price"] <= budget)]
    st.write("### Fashion Products Within Your Budget:")
    st.table(fashion_products)

# Display best discounts
st.write("### Top 5 Best Discounts:")
st.table(best_discounts())

# Wishlist feature
wishlist = st.multiselect("Add products to your wishlist", df["Product"].tolist())
st.write("### Your Wishlist:", wishlist)

# Product comparison
to_compare = st.multiselect("Select products to compare", df["Product"].tolist())
if to_compare:
    comparison_data = df[df["Product"].isin(to_compare)]
    st.write("### Price Comparison:")
    st.table(comparison_data)

    # Price Comparison Bar Chart
    st.write("### Price Comparison Chart")
    plt.figure(figsize=(8,5))
    plt.bar(comparison_data["Product"], comparison_data["Price"], color='skyblue')
    plt.xlabel("Products")
    plt.ylabel("Price")
    plt.title("Price Comparison")
    st.pyplot(plt)

# AI-powered product suggestion
if st.button("Get AI-Powered Suggestions"):
    suggestion = random.choice(df["Product"].tolist())
    st.success(f"Based on your preferences, we suggest: **{suggestion}**! Buy from {df[df['Product'] == suggestion]['Buy From'].values[0]}.")

# Display vendor links
st.write("### Where to Buy:")
for _, row in df.iterrows():
    st.write(f"**{row['Product']}** - Buy from [{row['Buy From']}](#)")

# Visualizations
st.write("### Data Visualizations")

# Pie chart for category distribution
st.write("#### Category Distribution")
fig, ax = plt.subplots()
category_counts = df["Category"].value_counts()
ax.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
ax.axis('equal')
st.pyplot(fig)

# Histogram of Prices
st.write("#### Price Distribution")
fig, ax = plt.subplots()
ax.hist(df["Price"], bins=10, color='blue', edgecolor='black')
ax.set_xlabel("Price")
ax.set_ylabel("Count")
ax.set_title("Price Distribution of Products")
st.pyplot(fig)

# Line graph of stock availability
st.write("#### Stock Availability Trend")
fig, ax = plt.subplots()
ax.plot(df["Product"], df["Stock"], marker='o', linestyle='-', color='green')
ax.set_xlabel("Product")
ax.set_ylabel("Stock Availability")
ax.set_title("Stock Trend Across Products")
plt.xticks(rotation=90)
st.pyplot(fig)

# Footer
st.write("---")
st.write("Developed with ❤️ using Streamlit")
