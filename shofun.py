import streamlit as st
import pandas as pd
import random

# Sample product data
data = {
    "Product": ["Laptop", "Smartphone", "Headphones", "Smartwatch", "Tablet", "Camera", "Shoes", "Backpack"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics", "Electronics", "Fashion", "Fashion"],
    "Price": [70000, 30000, 2000, 15000, 25000, 40000, 3000, 2000]
}
df = pd.DataFrame(data)

# Function to recommend products based on category
def recommend_products(category):
    return df[df["Category"] == category]["Product"].tolist()

# Function to filter products by budget
def filter_by_budget(budget):
    return df[df["Price"] <= budget]

# Streamlit UI
st.title("🛍️ Personalized Shopping Assistant")
st.write("Find the best products tailored to your needs!")

# User preferences
category = st.selectbox("Choose a category", df["Category"].unique())
recommended = recommend_products(category)
st.write("### Recommended Products:", recommended)

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

# AI-powered product suggestion (Basic Random Suggestion for Demo)
if st.button("Get AI-Powered Suggestions"):
    suggestion = random.choice(df["Product"].tolist())
    st.success(f"Based on your preferences, we suggest: **{suggestion}**!")

# Footer
st.write("---")
st.write("Developed with ❤️ using Streamlit")
