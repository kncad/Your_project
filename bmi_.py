[15:14, 22/03/2024] Likith: from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(height, weight):
    bmi = weight / ((height/100) ** 2)
    B_bmi = round(bmi,2)
    return B_bmi

def get_health_suggestion(b,w):
    if b<20 :
        return "You are severly underweight. Try to eat a balanced diet with sufficient calories."
    elif ( b>=20 and b<25):
        return "You are at a healthy weight. Keep up the good work!"
    elif (b>=25 and b<30):
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
        suggestion = get_health_suggestion(bmi,weight)

        return render_template('result.html', bmi=bmi, suggestion=suggestion)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
