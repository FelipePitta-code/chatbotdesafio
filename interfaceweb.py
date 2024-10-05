from flask import Flask, render_template, request, redirect, url_for
from desafio import resposta  

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  
def homepage():
    variavel = 'Chatbot: Bem vindo ao Chatbot da InfoBio Jr'
    
    if request.method == 'POST':
        user_input = request.form['user_input']
       
        return redirect(url_for('chat', user_input=user_input))
    
    return render_template('homepage.html')  

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    messages = [] 
    
    if request.method == 'POST':
        user_input = request.form['user_input']
        resposta_chat = resposta(user_input)  
        messages.append({'user': user_input, 'bot': resposta_chat}) 
    
    else:
      
        user_input = request.args.get('user_input')
        if user_input:
            resposta_chat = resposta(user_input)
            messages.append({'user': user_input, 'bot': resposta_chat})

    return render_template('chat.html', messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
