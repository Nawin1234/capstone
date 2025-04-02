import streamlit as st
import google.generativeai as genai

# Configure API key (Avoid hardcoding API keys in production)
API_KEY = "AIzaSyDAn69hpc4jYH4z3QsflRB_aazoBvPQw4g"
genai.configure(api_key=API_KEY)

# Fetch available models
try:
    available_models = [model.name for model in genai.list_models()]
    MODEL_NAME = "models/gemini-1.5-pro-latest" if "models/gemini-1.5-pro-latest" in available_models else "models/gemini-1.5-pro"
    
    if MODEL_NAME not in available_models:
        st.error(f"No supported Gemini models found. Available models: {available_models}")
        st.stop()
except Exception as e:
    st.error(f"Error fetching models: {e}")
    st.stop()

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
            prompt = f"I have these ingredients: {ingredients}. Can you suggest a detailed recipe?"
            if cuisine_type != "Any":
                prompt += f" Make it a {cuisine_type} dish."
            
            try:
                model = genai.GenerativeModel(model_name=MODEL_NAME)
                response = model.generate_content(prompt)
                
                st.subheader("🍽️ Here's Your Recipe:")
                st.write(response.text if hasattr(response, 'text') else "No response received. Try again.")
            except Exception as e:
                st.error(f"Error generating recipe: {e}")
    else:
        st.warning("Please enter some ingredients.")

# Footer
st.markdown("---")
st.markdown("🔹 Built with ❤️ using Streamlit & Google Gemini AI")


