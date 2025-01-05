import os
from flask import Flask, render_template, request
from groq import Groq

app = Flask(__name__)
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    result = ""
    if request.method == 'POST':
        user_input = request.form['user_prompt']
        completion = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=False
        )
        result = completion.choices[0].message.content
    return render_template("home.html", result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)