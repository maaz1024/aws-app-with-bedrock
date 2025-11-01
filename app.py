import streamlit as st
import requests
import json

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Blog Generator",
    page_icon="🤖",
    layout="centered"
)

# --- AWS API Gateway URL ---
API_URL = "https://ye9eic9y78.execute-api.us-east-1.amazonaws.com/dev/blog-generation"

# --- Main App Interface ---
st.title("🤖 AI Blog Generator")
st.markdown(
    "Enter a topic below and the AI (powered by AWS Bedrock & Llama 3) "
    "will write a blog post and save it to an S3 bucket."
)

# --- Form for User Input ---
with st.form(key="blog_form"):
    blog_topic = st.text_input(
        "Enter a blog topic:", 
        placeholder="e.g., 'The future of Generative AI in education'"
    )
    submit_button = st.form_submit_button(label="Generate Blog Post")

# --- Handle Form Submission ---
if submit_button and blog_topic:
    with st.spinner("Generating your blog post... This might take a moment."):
        try:
            # 1. Define the payload to send to your Lambda
            payload = {
                "blog_topic": blog_topic
            }
            
            # 2. Make the POST request to your API Gateway
            response = requests.post(API_URL, json=payload, timeout=60)
            
            # 3. Check the response
            if response.status_code == 200:
                response_data = response.json()
                # Get the success message from the JSON
                st.success(f"✅ {response_data['message']}") 
                st.balloons()
                
                # Get the blog post from the JSON and display it
                st.subheader("Generated Blog Post:")
                st.markdown(response_data['generated_blog'])
                
            else:
                # Error if the API call failed
                st.error(
                    f"Failed to generate blog. API returned status: {response.status_code}"
                )
                st.text(f"Error details: {response.text}")

        except requests.exceptions.RequestException as e:
            # Handle network or connection errors
            st.error(f"An error occurred: {e}")
            
elif submit_button and not blog_topic:
    st.warning("Please enter a blog topic.")