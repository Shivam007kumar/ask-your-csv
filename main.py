import streamlit as st
from langchain_experimental.agents import create_csv_agent
from langchain_openai import OpenAI
from dotenv import load_dotenv
import tempfile
import os

def main():
    load_dotenv()

    st.set_page_config(page_title="Ask your CSV 📈")
    st.header("Ask your CSV 📈")

    user_csv = st.file_uploader("Upload your CSV file", type="csv")

    if user_csv is not None:
        user_question = st.text_input("Ask a question about your CSV")

  
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
            temp_file.write(user_csv.read())
            temp_file_path = temp_file.name


        llm = OpenAI(temperature=0.01)

      
        agent = create_csv_agent(llm, temp_file_path, verbose=True, allow_dangerous_code=True)

        if user_question:
            response = agent.run(user_question)
            st.write(f"Your question: {user_question}")
            st.write(f"Answer: {response}")

  
        os.remove(temp_file_path)

if __name__ == "__main__":
    main()