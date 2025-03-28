import streamlit as st
import google.generativeai as genai
import os

# Configure API key securely
API_KEY = os.getenv("GEMINI_API_KEY")  # Set this in your environment variables
if not API_KEY:
    st.error("API key not found. Please set GEMINI_API_KEY as an environment variable.")
    st.stop()

genai.configure(api_key=API_KEY)

# Streamlit UI
st.set_page_config(page_title="AI Recipe Generator", page_icon="🍽️")
st.title("🍲 AI-Powered Recipe Generator")

# Sidebar
st.sidebar.header("Settings")
cuisine_type = st.sidebar.selectbox("Choose Cuisine Type:", ["Any", "Indian", "Italian", "Chinese", "Mexican", "French"])

# User input
ingredients = st.text_area("🥕 Enter ingredients (comma-separated):")

if st.button("Generate Recipe"):
    if ingredients:
        with st.spinner("Cooking up your recipe..."):
            # Generate recipe prompt
            prompt = f"I have these ingredients: {ingredients}. Can you suggest a detailed recipe?"
            if cuisine_type != "Any":
                prompt += f" Make it a {cuisine_type} dish."
            
            try:
                # Call Gemini AI
                model = genai.GenerativeModel("gemini-pro")
                response = model.generate_content(prompt)
                
                # Display the result
                st.subheader("🍽️ Here's Your Recipe:")
                st.write(response.text if response else "No response received. Try again.")
            except Exception as e:
                st.error(f"Error generating recipe: {e}")
    else:
        st.warning("Please enter some ingredients.")

# Footer
st.markdown("---")
st.markdown("🔹 Built with ❤️ using Streamlit & Google Gemini AI")

