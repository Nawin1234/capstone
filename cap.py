import streamlit as st
import google.generativeai as genai

# Configure API key
API_KEY = "AIzaSyDue2-UbEd_-Pd4crt96ycAjiNfLn7MhQc"
genai.configure(api_key=API_KEY)
MODEL_NAME = "models/gemini-1.5-pro-latest"

# Streamlit UI
st.set_page_config(page_title="AI Recipe Assistant", page_icon="🍽️")
st.title("🍽️ AI-Powered Kitchen Assistant")

# Sidebar
st.sidebar.header("Settings")
cuisine_type = st.sidebar.selectbox("Choose Cuisine Type:", ["Any", "Indian", "Italian", "Chinese", "Mexican", "French"])

# Main tabs
tab1, tab2, tab3 = st.tabs(["📋 Recipe Generator", "♻️ Leftover Dish", "🍎 Nutrition Info"])

# === TAB 1: Recipe Generator ===
with tab1:
    st.header("🧑‍🍳 Recipe from Ingredients")
    ingredients = st.text_area("Enter ingredients (comma-separated):", key="ingredients")
    if st.button("Generate Recipe", key="btn1"):
        if ingredients:
            prompt = f"I have these ingredients: {ingredients}. Suggest a detailed recipe."
            if cuisine_type != "Any":
                prompt += f" Make it a {cuisine_type} dish."

            with st.spinner("Cooking up your recipe..."):
                try:
                    model = genai.GenerativeModel(MODEL_NAME)
                    response = model.generate_content(prompt)
                    st.success("Here’s your recipe!")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error generating recipe: {e}")
        else:
            st.warning("Please enter some ingredients.")

# === TAB 2: Leftover Dish Creator ===
with tab2:
    st.header("♻️ Create Dish from Leftovers")
    leftovers = st.text_area("Enter your leftover items:", key="leftovers")
    if st.button("Generate Dish from Leftovers", key="btn2"):
        if leftovers:
            prompt = f"I have the following leftover food items: {leftovers}. Suggest a creative new dish I can make."
            with st.spinner("Getting creative with your leftovers..."):
                try:
                    model = genai.GenerativeModel(MODEL_NAME)
                    response = model.generate_content(prompt)
                    st.success("Here's your leftover makeover!")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error generating leftover dish: {e}")
        else:
            st.warning("Please enter leftover items.")

# === TAB 3: Nutrition Analyzer ===
with tab3:
    st.header("🍎 Nutritional Estimator")
    nutrition_items = st.text_area("Enter food items or recipe ingredients to analyze:", key="nutrition")
    if st.button("Analyze Nutrition", key="btn3"):
        if nutrition_items:
            prompt = f"Based on these ingredients or a dish: {nutrition_items}, estimate the nutritional breakdown per serving. Include calories, protein, fat, and carbs."
            with st.spinner("Analyzing nutrition..."):
                try:
                    model = genai.GenerativeModel(MODEL_NAME)
                    response = model.generate_content(prompt)
                    st.success("Estimated Nutrition:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error generating nutrition data: {e}")
        else:
            st.warning("Please enter some ingredients or a dish name.")



