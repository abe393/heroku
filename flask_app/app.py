from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import the CORS extension

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

"""
@app.route('/')
def index():
    return render_template('index.html')
"""
@app.route('/api/submit', methods=['POST'])
def submit():
    data = request.get_json()
    user_input = data.get('userInput')
    # You can perform backend processing with the user input here if needed
    return jsonify({'result': f'Success! You entered: {user_input}'})
@app.route('/test')
def test(): 
    if(request.method == 'GET'): 
        data = {"data": "Hello World"} 
        return jsonify(data) 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))