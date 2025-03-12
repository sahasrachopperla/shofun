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
def recommend_products(category):
    return df[df["Category"] == category][["Product", "Price", "Ratings", "Discount", "Buy From"]]

# Function to filter products by budget
def filter_by_budget(budget):
    return df[df["Price"] <= budget]

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

# Footer
st.write("---")
st.write("Developed with ❤️ using Streamlit")
