from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model = "mistral-small-2506",temperature=0.9,max_tokens=30)

response = model.invoke("write a happy poem on rain")

print(response.content)