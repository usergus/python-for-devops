# app.py
from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Health Calculator API!"})

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    try:
        height = data['height']
        weight = data['weight']
        result = calculate_bmi(height, weight)
        return jsonify({"operation": "BMI Calculation", "bmi": result})
    except KeyError:
        return jsonify({"error": "Missing required parameters 'height' and 'weight'"}), 400

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.get_json()
    try:
        height_cm = data['height']  # La hauteur doit être fournie en cm directement
        weight = data['weight']
        age = data['age']
        gender = data['gender']
        result = calculate_bmr(height_cm, weight, age, gender)
        return jsonify({"operation": "BMR Calculation", "bmr": result})
    except KeyError:
        return jsonify({"error": "Missing required parameters 'height', 'weight', 'age', and 'gender'"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)