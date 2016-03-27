from flask import Flask, render_template, request
import json

import run

app = Flask(__name__, template_folder="./templates",
        static_url_path="/static",
        static_folder="./static")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/set', methods=['POST'])
def set():
    run.led.fill(tuple(request.json))
    run.led.update()
    return json.dumps({'status':'OK'});

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
