import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import HumanMessage, SystemMessage

from src.config import instruction

from langchain_community.chat_models import ChatOpenAI

from src.config import instruction

load_dotenv()

OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def ask_bot(user_message,instruction):
    
    model = ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0,streaming=True)
    
    
    responses=model(
    [
        SystemMessage(content=instruction),
        HumanMessage(content=user_message),
    ]
)
    
    return responses.content

if __name__=="__main__":
    user_message = "give me a brief description of the menu?"
    responses=ask_bot(user_message,instruction=instruction)
    print(responses)