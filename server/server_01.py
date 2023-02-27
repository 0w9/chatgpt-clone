from flask import Flask
from flask import request
from transformers import pipeline, set_seed

app = Flask(__name__)

def runPrompt(prompt): 
    generator = pipeline('text-generation', model='openai-gpt')
    response = generator(f'{prompt}', max_length=100, num_return_sequences=1)[0]["generated_text"]
    
    print(f'Prompt: {prompt} | Response: {response}\n')
    return str(response)

@app.route('/prompt')
def prompt():
    prompt = request.args.get('prompt')

    # fix the cors headers
    response = app.make_response(runPrompt(prompt))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/run')
def run():
    return "e"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)