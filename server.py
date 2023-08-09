from flask import Flask, render_template, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=[],
    storage_uri="memory://",
)

correct_answers = {
    "box1": "homogeneous",
    "box2": "heterogeneous",
    "box3": "homogeneous",
    "box4": "homogeneous",
    "box5": "heterogeneous",
    "box6": "heterogeneous",
    "box7": "homogeneous",
    "box8": "heterogeneous",
    "box9": "homogeneous",
    "box10": "homogeneous",
    "box11": "homogeneous",
    "box12": "homogeneous",
}
total_questions = len(correct_answers)
correct_count = 0 


@app.route('/')

def index():
    return render_template('game.html')

@app.route('/check_answer', methods=['POST'])
def check_answer():
    global correct_count  # Access the global correct count
    input_value = request.json['answer'].strip().lower()
    input_type = request.json['type']

    if input_type in correct_answers:
        correct_answer = correct_answers[input_type].strip().lower()
        is_correct = input_value == correct_answer
        if is_correct:
            correct_count += 1  # Increment correct count
    else:
        is_correct = False

    
    return jsonify({'is_correct': is_correct})

if __name__ == '__main__':
    app.run(debug=True)