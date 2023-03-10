from flask import Flask, request, jsonify, render_template
import os
import openai

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_bio', methods=['POST'])
def generate_bio():
    data = request.form.to_dict()
    name = data['name']
    title = data['title']
    industry = data['industry']
    years_of_experience = data['years_of_experience']
    location = data['location']
    
    prompt = (f"Write a high quality and Professional LinkedIn bio for me {name}, I work as a {title} in the {industry} industry and have {years_of_experience} years of experience, based in {location}.")
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text
    return render_template('index.html', bio=message)
