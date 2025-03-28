import streamlit as st
import google.generativeai as genai

# Configure API key securely
API_KEY = "AIzaSyDAn69hpc4jYH4z3QsflRB_aazoBvPQw4g"

genai.configure(api_key=API_KEY)

# Get available models dynamically
try:
    available_models = [model.name for model in genai.list_models()]
    if "gemini-pro" in available_models:
        MODEL_NAME = "gemini-pro"
    elif "gemini-pro-latest" in available_models:
        MODEL_NAME = "gemini-pro-latest"
    else:
        st.error("No supported Gemini models found. Please check your API access.")
        st.stop()
except Exception as e:
    st.error(f"Error fetching available models: {e}")
    st.stop()

# Streamlit UI
st.set_page_config(page_title="AI Recipe Generator", page_icon="\U0001F37D\uFE0F")
st.title("\U0001F372 AI-Powered Recipe Generator")

# Sidebar
st.sidebar.header("Settings")
cuisine_type = st.sidebar.selectbox("Choose Cuisine Type:", ["Any", "Indian", "Italian", "Chinese", "Mexican", "French"])

# User input
ingredients = st.text_area("\U0001F955 Enter ingredients (comma-separated):")

if st.button("Generate Recipe"):
    if ingredients:
        with st.spinner("Cooking up your recipe..."):
            # Generate recipe prompt
            prompt = f"I have these ingredients: {ingredients}. Can you suggest a detailed recipe?"
            if cuisine_type != "Any":
                prompt += f" Make it a {cuisine_type} dish."
            
            try:
                # Use the correct Gemini model
                model = genai.GenerativeModel(MODEL_NAME)
                response = model.generate_content(prompt)
                
                # Display the result
                st.subheader("\U0001F37D\uFE0F Here's Your Recipe:")
                st.write(response.text if hasattr(response, 'text') else "No response received. Try again.")
            except Exception as e:
                st.error(f"Error generating recipe: {e}")
    else:
        st.warning("Please enter some ingredients.")

# Footer
st.markdown("---")
st.markdown("\U0001F539 Built with \u2764\uFE0F using Streamlit & Google Gemini AI")
