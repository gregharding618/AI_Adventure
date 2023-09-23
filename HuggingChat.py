from hugchat import hugchat
from hugchat.login import Login
import os
from dotenv import load_dotenv
from huggingface_hub import HfApi

load_dotenv()


def call_huggingchat_api():
    email = os.environ.get("EMAIL")
    password = os.environ.get("PASSWORD")
    sign = Login(email, password)
    cookies = sign.login()

    cookie_path_dir = "./cookies_snapshot"
    sign.saveCookiesToDir(cookie_path_dir)
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    while True:
        user_input = input("Your message: ")
        response = chatbot.chat(
            text=f"You are an AI that generates C# code for Unity. You will only respond with code "
                 f"that solves the prompt the user presents you. Do not add any dialogue, suggestions"
                 f", explanations or comments that are not C# code. Respond with code and nothing but"
                 f" code. User's prompt: {user_input}",
            temperature=0.00001,
            top_p=0.05,
            return_full_text=False
        )
        print(response)

    # # Create a new conversation
    # id = chatbot.new_conversation()
    # chatbot.change_conversation(id)
    #
    # # Get conversation list
    # conversation_list = chatbot.get_conversation_list()
    #
    # # Switch model (default: meta-llama/Llama-2-70b-chat-hf. )
    # chatbot.switch_llm(0) # Switch to `OpenAssistant/oasst-sft-6-llama-30b-xor`
    # chatbot.switch_llm(1) # Switch to `meta-llama/Llama-2-70b-chat-hf`


if __name__ == "__main__":
    try:
        call_huggingchat_api()
    except Exception as e:
        print(e)
