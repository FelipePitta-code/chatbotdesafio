import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

def resposta(user_input):

    response = model.generate_content(user_input)
    return response.text




