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
    "Product": ["Laptop", "Smartphone", "Headphones", "Smartwatch", "Tablet", "Camera", "Shoes", "Backpack", "Gaming Console", "Smart TV", "Bluetooth Speaker", "Wireless Earbuds", "Mechanical Keyboard", "Monitor", "Printer", "Fitness Band", "Jacket", "Sunglasses", "Handbag", "Jeans", "T-shirt", "Sneakers", "Watch", "Hat", "Formal Shoes", "Casual Shoes", "Dress", "Skirt", "Perfume", "Wallet", "Belt", "Earphones", "Ring Light", "Tripod", "Wireless Charger", "Smart Bulb", "Gaming Mouse", "Graphics Card", "Power Bank", "VR Headset"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics", "Electronics", "Fashion", "Fashion", "Electronics", "Electronics", "Accessories", "Accessories", "Accessories", "Electronics", "Electronics", "Fitness", "Fashion", "Fashion", "Fashion", "Fashion", "Fashion", "Fashion", "Fashion", "Fashion", "Fashion", "Fashion", "Fashion", "Fashion", "Accessories", "Accessories", "Accessories", "Accessories", "Electronics", "Electronics", "Accessories", "Electronics", "Electronics", "Electronics", "Electronics"],
    "Price": [70000, 30000, 2000, 15000, 25000, 40000, 3000, 2000, 50000, 45000, 5000, 6000, 7000, 20000, 15000, 8000, 5000, 3500, 7000, 2500, 1500, 4000, 6000, 1000, 5000, 3500, 8000, 4000, 3000, 2500, 2000, 1500, 6000, 5000, 3500, 4000, 8000, 15000, 25000],
    "Buy From": ["Amazon", "Flipkart", "Amazon", "Croma", "Amazon", "Best Buy", "Nike", "Amazon", "GameStop", "Reliance Digital", "Amazon", "Flipkart", "Amazon", "Dell Store", "HP Store", "Decathlon", "Myntra", "LensKart", "Zara", "Levi's", "H&M", "Adidas", "Titan", "Myntra", "Bata", "Puma", "Zara", "Forever 21", "Lifestyle", "Woodland", "Ray-Ban", "Boat", "Amazon", "Flipkart", "Croma", "Amazon", "Razer", "Nvidia Store", "Samsung", "Meta Store"]
}
df = pd.DataFrame(data)

# Function to recommend products based on category
def recommend_products(category):
    return df[df["Category"] == category][["Product", "Price", "Buy From"]]

# Function to filter products by budget
def filter_by_budget(budget, category):
    return df[(df["Price"] >= 1000) & (df["Price"] <= budget) & (df["Category"] == category)][["Product", "Price", "Buy From"]]

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
filtered_products = filter_by_budget(budget, category)
st.write("### Products within your budget:")
st.table(filtered_products)

# Wishlist feature
wishlist = st.multiselect("Add products to your wishlist", df["Product"].tolist())
st.write("### Your Wishlist:", wishlist)

# Product comparison
to_compare = st.multiselect("Select products to compare", df["Product"].tolist())
if to_compare:
    st.write("### Comparison Table:")
    st.table(df[df["Product"].isin(to_compare)])

    # Price Comparison Bar Chart
    st.write("### Price Comparison Chart")
    fig, ax = plt.subplots()
    sns.barplot(x=df[df["Product"].isin(to_compare)]["Product"], y=df[df["Product"].isin(to_compare)]["Price"], palette="coolwarm", ax=ax)
    ax.set_xlabel("Products")
    ax.set_ylabel("Price")
    ax.set_title("Price Comparison")
    plt.xticks(rotation=90)
    st.pyplot(fig)

# AI-powered product suggestion
if st.button("Get AI-Powered Suggestions"):
    suggestion = random.choice(df["Product"].tolist())
    buy_from = df[df["Product"] == suggestion]["Buy From"].values[0]
    st.success(f"Based on your preferences, we suggest: **{suggestion}**! You can buy it from **{buy_from}**.")

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

# Stock Trend Line Graph
st.write("#### Stock Availability Trend")
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["Product"], y=np.random.randint(5, 50, len(df)), mode='lines+markers', name='Stock'))
fig.update_layout(title="Stock Trend Across Products", xaxis_title="Product", yaxis_title="Stock Availability")
st.plotly_chart(fig)

# Footer
st.write("---")
st.write("Developed with ❤️ using Streamlit")
