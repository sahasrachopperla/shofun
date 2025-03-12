import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Sample product data
data = {
    "Product": ["Laptop", "Smartphone", "Headphones", "Smartwatch", "Tablet", "Camera", "Shoes", "Backpack", "Gaming Console", "Smart TV", "Bluetooth Speaker", "Wireless Earbuds", "Mechanical Keyboard", "Monitor", "Printer", "Fitness Band", "Jacket", "Sunglasses", "Handbag", "Jeans", "T-shirt", "Sneakers", "Watch", "Hat"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics", "Electronics", "Fashion", "Fashion", "Electronics", "Electronics", "Accessories", "Accessories", "Accessories", "Electronics", "Electronics", "Fitness", "Fashion", "Fashion", "Fashion", "Fashion", "Fashion", "Fashion", "Fashion", "Fashion"],
    "Price": [70000, 30000, 2000, 15000, 25000, 40000, 3000, 2000, 50000, 45000, 5000, 6000, 7000, 20000, 15000, 8000, 5000, 3500, 7000, 2500, 1500, 4000, 6000, 1000],
    "Ratings": [4.5, 4.7, 4.2, 4.3, 4.6, 4.4, 4.1, 4.0, 4.8, 4.6, 4.3, 4.5, 4.7, 4.4, 4.2, 4.5, 4.3, 4.2, 4.6, 4.0, 3.9, 4.5, 4.3, 4.1],
    "Stock": [10, 25, 50, 15, 20, 5, 30, 40, 12, 18, 35, 40, 22, 10, 8, 25, 20, 15, 18, 30, 40, 25, 12, 50],
    "Buy From": ["Amazon", "Flipkart", "Amazon", "Croma", "Reliance Digital", "Amazon", "Nike", "Amazon", "Flipkart", "Reliance Digital", "Amazon", "Flipkart", "Amazon", "Croma", "Amazon", "Nike", "Myntra", "Ray-Ban", "Amazon", "Levi's", "H&M", "Adidas", "Titan", "Amazon"]
}
df = pd.DataFrame(data)

# Function to recommend products based on category
def recommend_products(categories):
    return df[df["Category"].isin(categories)]

# Function to filter products by budget
def filter_by_budget(budget, categories):
    return df[(df["Price"] <= budget) & (df["Category"].isin(categories))]

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
filtered_products = filter_by_budget(budget, categories)
st.write("### Products within your budget:")
st.table(filtered_products)

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
    fig, ax = plt.subplots()
    sns.barplot(x=comparison_data["Product"], y=comparison_data["Price"], palette="coolwarm", ax=ax)
    ax.set_xlabel("Products")
    ax.set_ylabel("Price")
    ax.set_title("Price Comparison")
    plt.xticks(rotation=90)
    st.pyplot(fig)

# AI-powered product suggestion
if st.button("Get AI-Powered Suggestions"):
    suggestion_row = df.sample(1).iloc[0]
    st.success(f"Based on your preferences, we suggest: **{suggestion_row['Product']}**! You can buy it from **{suggestion_row['Buy From']}**.")

# Visualizations
st.write("### Data Visualizations")

# Pie chart for category distribution
st.write("#### Category Distribution")
fig = px.pie(df, names="Category", title="Product Category Distribution")
st.plotly_chart(fig)

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
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["Product"], y=df["Stock"], mode='lines+markers', name='Stock'))
fig.update_layout(title="Stock Trend Across Products", xaxis_title="Product", yaxis_title="Stock Availability")
st.plotly_chart(fig)

# Footer
st.write("---")
st.write("Developed with ❤️ using Streamlit")
