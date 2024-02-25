from pandasai import SmartDataframe
from pandasai.llm import OpenAI
import streamlit as st
import string
import random
import pandas as pd


def chat_bot(open_ai_key,df,user_question):
    llm = OpenAI(api_token=open_ai_key)
    df = SmartDataframe(df, config={"llm": llm})
    return df.chat(user_question)

