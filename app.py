from langchain import OpenAI
from langchain.agents import create_csv_agent
import openai
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
import os


def make_prediction(prompt):
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=10
    )
    return response.choices[0].text.strip()


def main():

    load_dotenv()

    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")
    
    st.title("Excel Prediction Chatbot")
    
   
    csv_file = st.file_uploader("Upload Excel file", type=["csv"])
    
    if csv_file is not None:
    # Save the uploaded file to a temporary location
        temp_file_path = "temp.csv"
        with open(temp_file_path, "wb") as file:
            file.write(csv_file.getvalue())

        agent = create_csv_agent(
            OpenAI(temperature=0), temp_file_path, verbose=True)

        user_question = st.text_input("Enter your column name for prediction: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))
    
if __name__ == '__main__':
    main()
