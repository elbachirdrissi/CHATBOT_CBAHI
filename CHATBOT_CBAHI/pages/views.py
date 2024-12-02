from django.shortcuts import render, redirect
from django.contrib.staticfiles import finders
import google.generativeai as genai

file_path = finders.find('data/data.txt')
if file_path:
    with open(file_path, 'r', encoding='utf-8') as file:
        text_content = file.read()
else:
    raise FileNotFoundError("File not found in static files.")

genai.configure(api_key="AIzaSyBy9czHsgzweMg3Q_Hy1N9w5EzoxYprytQ")

def query_gpt(prompt):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

def clear_chat(request):
    if request.method == 'POST':
        # Clear the session data for the conversation
        request.session['conversation'] = []
    return redirect('index') 

def index(request):
    conversation = request.session.get('conversation', []) 
       
    if request.method == 'GET' and 'user_message' in request.GET:
        user_query = request.GET.get('user_message') 
        if user_query:
            prompt = f"""
            {text_content}
            User: {user_query}
            BOT:
            """
            bot_response = query_gpt(prompt)
        else:
            bot_response = "لم تكتب شيئا، تفضل بالسؤال"
    
        conversation.append( {'sender': 'user', 'text': user_query} )
        conversation.append( {'sender': 'bot', 'text': bot_response} )
        request.session['conversation'] = conversation
            
    return render(request, 'chatBoot_CBAHI.html', {'conversation': conversation})
        