import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np

# Sample product data
data = {
    "Product": ["Laptop", "Smartphone", "Headphones", "Smartwatch", "Tablet", "Camera", "Shoes", "Backpack"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics", "Electronics", "Fashion", "Fashion"],
    "Price": [70000, 30000, 2000, 15000, 25000, 40000, 3000, 2000],
    "Ratings": [4.5, 4.7, 4.2, 4.3, 4.6, 4.4, 4.1, 4.0],
    "Stock": [10, 25, 50, 15, 20, 5, 30, 40],
    "Discount": [10, 15, 5, 8, 12, 20, 25, 18]
}
df = pd.DataFrame(data)

# Function to recommend products based on category
def recommend_products(category):
    return df[df["Category"] == category][["Product", "Price", "Ratings", "Discount"]]

# Function to filter products by budget
def filter_by_budget(budget):
    return df[df["Price"] <= budget]

# Function to plot price distribution
def plot_price_distribution():
    fig, ax = plt.subplots()
    ax.bar(df["Product"], df["Price"], color='skyblue')
    plt.xticks(rotation=45)
    plt.xlabel("Product")
    plt.ylabel("Price")
    plt.title("Product Price Distribution")
    st.pyplot(fig)

# Function to plot ratings
def plot_ratings():
    fig, ax = plt.subplots()
    ax.bar(df["Product"], df["Ratings"], color='orange')
    plt.xticks(rotation=45)
    plt.xlabel("Product")
    plt.ylabel("Ratings")
    plt.title("Product Ratings")
    st.pyplot(fig)

# Function to show best discounts
def best_discounts():
    top_discounts = df.sort_values(by="Discount", ascending=False).head(5)
    st.write("### Best Discounted Products")
    st.table(top_discounts)

# Function to plot product comparison
def plot_comparison(products):
    if products:
        selected_df = df[df["Product"].isin(products)]
        fig, ax = plt.subplots()
        ax.bar(selected_df["Product"], selected_df["Price"], color='purple', label="Price")
        ax.set_xlabel("Product")
        ax.set_ylabel("Price")
        ax.set_title("Product Price Comparison")
        plt.xticks(rotation=45)
        plt.legend()
        st.pyplot(fig)

# Streamlit UI
st.title("🛍️ Personalized Shopping Assistant")
st.write("Find the best products tailored to your needs!")

# User preferences
category = st.selectbox("Choose a category", df["Category"].unique())
recommended = recommend_products(category)
st.write("### Recommended Products:")
st.table(recommended)

# Budget filtering
budget = st.slider("Select your budget", min_value=1000, max_value=80000, step=1000)
filtered_products = filter_by_budget(budget)
st.write("### Products within your budget:")
st.table(filtered_products)

# Wishlist feature
wishlist = st.multiselect("Add products to your wishlist", df["Product"].tolist())
st.write("### Your Wishlist:", wishlist)

# Product comparison
to_compare = st.multiselect("Select products to compare", df["Product"].tolist())
st.write("### Comparison Table:")
st.table(df[df["Product"].isin(to_compare)])
plot_comparison(to_compare)

# AI-powered product suggestion (Basic Random Suggestion for Demo)
if st.button("Get AI-Powered Suggestions"):
    suggestion = random.choice(df["Product"].tolist())
    st.success(f"Based on your preferences, we suggest: **{suggestion}**!")

# Display Graphs
st.write("### Price Distribution of Products")
plot_price_distribution()

st.write("### Product Ratings Overview")
plot_ratings()

# Show best discounted products
best_discounts()

# Stock availability alert
low_stock = df[df["Stock"] < 10]
if not low_stock.empty:
    st.warning("⚠️ The following products are low in stock:")
    st.table(low_stock)

# Footer
st.write("---")
st.write("Developed with ❤️ using Streamlit")
