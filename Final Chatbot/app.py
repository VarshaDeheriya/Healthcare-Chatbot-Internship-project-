from flask import Flask ,render_template,request
from datetime import datetime


app = Flask(__name__)

##################################################

you = []
bot = ["Hello I am a bot Happy to see you , tell me your problem ."]
time = []


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chatbot',methods=["GET","POST"])
def chatbot():
    if request.method == "POST":
        time_now = datetime.now().strftime("%H:%M")
        str1 = request.form.get('names')
        if len(str1)!=0:
            you.append(str1)
            bot.append(str1)
            time.append(time_now)
        return render_template('chatbot.html',results = zip(you,bot,time))
    else:
        you.clear()
        bot.clear()
        return render_template('chatbot.html')





##################################################


if __name__ == '__main__':
    app.run(debug=True)