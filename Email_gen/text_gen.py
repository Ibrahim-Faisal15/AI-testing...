from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

Groq_key = os.getenv('GROQ_API_KEY')
# print(Groq_key)



def text_generation(topic):

  chat = ChatGroq(
      temperature=0.5,
      model="llama3-70b-8192",
      api_key=Groq_key 
  )

  template = 'You will be an AI assistant who will explain physics concept in detail with proper derivation.'
  human_template = 'Please explain {text}.'

  prompt = ChatPromptTemplate.from_messages([
    ('system', template),
    ('human', human_template)
  ])

  chain = prompt | chat
  response = chain.invoke({'text': topic})


  AI_response = response.content
  return AI_response



