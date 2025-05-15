#!pip install streamlit 
import pandas as pd
import os

# Check if queries.csv exists, if not create it
if not os.path.exists("queries.csv"):
    pd.DataFrame(columns=["Email", "Query"]).to_csv("queries.csv", index=False)
import streamlit as st
import pandas as pd
import os

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Set page configuration
st.set_page_config(page_title="Ask Ky’ra – Your Internship Assistant", layout="centered")

# Styling for background and layout
st.markdown(
    """
    <style>
    .main {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
    }
    .stTextInput > div > input {
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    .stTextArea > div > textarea {
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header and welcome message
st.markdown("<h1 style='text-align: center; color: #2e7d32;'>👋 Ask Ky’ra – Your Internship Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Welcome to the Ky’ra Assistant! Enter your query below, and Ky’ra will assist you with your internship questions.</p>", unsafe_allow_html=True)

# Input fields
st.subheader("Your Details")
email_input = st.text_input("Student Email", placeholder="student123@college.edu", help="Enter your college email address.")
query_text = st.text_area("What would you like to ask Ky’ra?", height=150, placeholder="E.g., How can I prepare for my internship interview?")

# Function to save queries to CSV
def save_query(email, query):
    filename = "queries.csv"
    new_row = pd.DataFrame([[email, query]], columns=["Email", "Query"])
    if os.path.exists(filename):
        df = pd.read_csv(filename)
        df = pd.concat([df, new_row], ignore_index=True)
    else:
        df = new_row
    df.to_csv(filename, index=False)

# Submit button logic
if st.button("Submit", type="primary"):
    if not email_input or not query_text:
        st.error("Please enter both a valid email and a query.")
    else:
        try:
            # Simulate Ky’ra’s response (replace with actual API logic later)
            response = "Thank you for your question. Ky’ra will get back to you shortly with detailed assistance."
            
            # Save query to CSV
            save_query(email_input, query_text)
            
            # Append to chat history
            st.session_state.chat_history.append({"email": email_input, "query": query_text, "response": response})
            
            # Success message
            st.success("Your query has been submitted successfully!")
            
            # Display Ky’ra’s response
            st.markdown("**🧠 Ky’ra’s Response:**")
            st.info(response)
        except Exception as e:
            st.error(f"Failed to process query: {str(e)}")

# Display chat history
if st.session_state.chat_history:
    st.markdown("**🧾 Chat History:**")
    for i, entry in enumerate(st.session_state.chat_history):
        st.markdown(f"**{i+1}.** *{entry['email']}*: {entry['query']}")
        st.markdown(f"   *Ky’ra*: {entry['response']}")

# Note about CSV storage
st.markdown("*Note: Queries are saved in 'queries.csv' in the root folder of the Streamlit app environment.*")