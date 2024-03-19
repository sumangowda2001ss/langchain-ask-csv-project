import streamlit as st
import csv  # Import the csv module
from langchain_experimental.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv

def main():

    load_dotenv()

    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your csv")

    user_csv = st.file_uploader("Upload your csv file", type="csv")
    
    if user_csv is not None:
        user_question = st.text_input("Ask a question about your csv:")

        llm = OpenAI(temperature=0)
        agent = create_csv_agent(llm=llm, path=user_csv, verbose=True)

        if user_question is not None and user_question !="":
            response = agent.run(user_question)
            st.write(response)
            

if __name__== "__main__":
    main()
