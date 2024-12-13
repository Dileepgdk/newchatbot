import openai
import streamlit as st

OPENAI_API_KEY = "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"

st.title("ChatGPT-Model")

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("what is up?"):
    st.session_state.message.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat.message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_stste.messages
            ],
            stream=True,
        ):
            full_response += response.choice[0].delta.get("content", "")
            message_placeholder.markdown(full_response + " ")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
