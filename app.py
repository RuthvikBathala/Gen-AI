import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
import streamlit as st
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.MCQ import generate_evaluate_chain
from src.mcqgenerator.logger import logging

with open('response.json','r') as file:
    RESPONSE_JSON=json.load(file)

st.title("MCQs Creator Application with Langchain")
df=None
with st.form("user_input"):
    uploaded_file=st.file_uploader("Upload pdf or txt file")  
    no_of_mcqs=st.number_input("No. of MCQs", min_value=3, max_value=50)
    subject=st.text_input("Insert Subject", max_chars=100)
    tone=st.text_input("Difficulty level of questions", max_chars=100)
    button=st.form_submit_button("Create MCQs")
    if button and uploaded_file is not None and no_of_mcqs and subject and tone:
        with st.spinner("Loading ..."):
            try:
                text= read_file(uploaded_file)
                with get_openai_callback() as cb:
                    response=generate_evaluate_chain(
                        {
                        "text": text,
                        "number": no_of_mcqs,
                        "subject":subject,
                        "tone": tone,
                        "response_json": json.dumps(RESPONSE_JSON)
                        }
                    )
            except Exception as e:
                traceback.print_exception(type(e), e,e.__traceback__)
                st.error("Error")
            else:
                print(f"Total Tokens:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Completion Tokens:{cb.completion_tokens}")
                print(f"Total Cost:{cb.total_cost}")
                if isinstance(response,dict):
                    quiz=response.get("quiz",None)
                    if quiz is not None:
                        table_data=get_table_data(quiz)
                        if table_data is not None:
                            df=pd.DataFrame(table_data)
                            df.index=df.index+1
                            st.table(df)
                            st.text_area(label="Review",value=response["review"])
                            
                        else:
                            st.error("Error in the table data")
                else:
                    st.write(response)

if df is not None:
    csv_data = df.to_csv(index=False)
    st.download_button(
        label="Download Quiz as CSV",
        data=csv_data,
        file_name="quiz.csv"
    )