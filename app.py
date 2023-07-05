import openai
import pandas as pd
import streamlit as st

openai.api_key = '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 '


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


def generate_predictions(file_path):
    
    try:
        df = pd.read_csv(file_path, engine='openpyxl')
        st.success("File successfully loaded!")
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return
    
    
    for index, row in df.iterrows():
        
        input_data = row['input_column_name']
        
       
        prediction = make_prediction(input_data)
        
        
        st.write(f"Prediction for input {index + 1}: {prediction}")



file_path = 'user_input.csv'


def main():
    st.title("Excel Prediction Chatbot")
    
   
    file = st.file_uploader("Upload Excel file", type=["csv"])
    
    if file is not None:
        
        generate_predictions(file.name)  
    
if __name__ == '__main__':
    main()
