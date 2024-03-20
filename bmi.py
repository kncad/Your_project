from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(height, weight):
    bmi = weight / ((height/100) ** 2)
    return bmi

def get_health_suggestion(bmi):
    if bmi < 18.5:
        return "You are underweight. Try to eat a balanced diet with sufficient calories."
    elif 18.5 <= bmi < 24.9:
        return "You are at a healthy weight. Keep up the good work!"
    elif 25 <= bmi < 29.9:
        return "You are overweight. Consider increasing physical activity and reducing calorie intake."
    else:
        return "You are obese. Consult a healthcare professional for personalized advice."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        age = int(request.form['age'])
        sex = request.form['sex']
        
        bmi = calculate_bmi(height, weight)
        suggestion = get_health_suggestion(bmi)
        
        return render_template('result.html', bmi=bmi, suggestion=suggestion)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
