from pandasai import SmartDataframe
from pandasai.llm import OpenAI
import streamlit as st
import string
import random
import pandas as pd
openai_api_key= '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'

data_chat_bot = pd.read_csv("/Users/rahulkushwaha/gENAI/demand_forecasting_interpreter/Data/Diageo_gen.csv")

def chat_bot(open_ai_key,df,user_question):
    llm = OpenAI(api_token=open_ai_key)
    df = SmartDataframe(df, config={"llm": llm})
    return df.chat(user_question)
with st.container(height=300):
    def randon_string() -> str:
        return "".join(random.choices(string.ascii_uppercase + string.digits, k=10))

    def chat_actions():
        st.session_state["chat_history"].append(
            {"role": "user", "content": st.session_state["chat_input"]},
        )

        st.session_state["chat_history"].append(
            {
                "role": "assistant",
                #"content": randon_string(),
                "content": chat_bot(openai_api_key,data_chat_bot,st.session_state["chat_input"]),
            },  # This can be replaced with your chat response logic
        )


    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []


    


    for i in st.session_state["chat_history"]:
        with st.chat_message(name=i["role"]):
            st.write(i["content"])

st.chat_input("Ask Me?", on_submit=chat_actions, key="chat_input")
def reset_conversation():
    st.session_state.conversation = None
    st.session_state.chat_history = []
st.button('Reset Chat', on_click=reset_conversation)
