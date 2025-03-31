from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def calculate_probability(hand, num_players):
    # Placeholder for actual probability calculation
    return round(random.uniform(0, 1), 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            hand = request.form.get('hand')
            num_players = int(request.form.get('num_players', 2))
            probability = calculate_probability(hand, num_players)
            return jsonify({'probability': probability})
        return render_template('index.html')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)