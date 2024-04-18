import streamlit as st
from openai import OpenAI

# Read the API key from a file
file = open(r"C:\Users\pulki\OneDrive\Desktop\genAI_APP\key.txt")
key = file.read().strip()  # Strip whitespace and newlines
OPENAI_API_KEY = key
file.close()

# Initialize OpenAI client with the API key read from the file
client = OpenAI(api_key=OPENAI_API_KEY)

def main():
    # Configure Streamlit page
    st.set_page_config(page_title="GenAI App - AI Code Reviewer", layout="wide", initial_sidebar_state="collapsed")
    st.title("GenAI App - AI Code Reviewer")

    # Input area for Python code
    prompt = st.text_area("Enter your Python code here", height=400)
    
    # Button to trigger code review
    if st.button("Review Code"):
        if prompt:
            # Call OpenAI API to perform code review
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-0613",
                messages=[
                    {"role": "system", "content": """You are a helpful AI Assistant and Code reviewer.
                    Find the Bugs and errors in the program and give me the corrected code."""},
                    {"role": "user", "content": prompt}
                ]
            )
            # Display code review feedback
            st.subheader("Code Review Feedback")
            st.snow()
            st.write(response.choices[0].message.content)
        else:
            st.warning("Please enter Python code for review.")

if __name__ == "__main__":
    main()
