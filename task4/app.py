from flask import Flask, render_template, request
import datetime
import random

app = Flask(__name__)

quotes = [
    "Life isn’t about getting and having, it’s about giving and being.",
    "Whatever the mind of man can conceive and believe, it can achieve.",
    "Strive not to be a success, but rather to be of value.",
    "Two roads diverged in a wood, and I—I took the one less traveled by, And that has made all the difference.",
    "I attribute my success to this: I never gave or took any excuse.",
    "You miss 100% of the shots you don’t take."
]

@app.route('/')
def index():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_quote = random.choice(quotes)
    return render_template('index.html', time=current_time, quote=random_quote)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        gender = request.form['gender']
        nationality = request.form['nationality']
        email = request.form['email']
        address = request.form['address']
        city = request.form['city']
        pincode = request.form['pincode']
        state = request.form['state']
        country = request.form['country']

        return f"""
        <h1>Form Submitted Successfully!</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Phone:</strong> {phone}</p>
        <p><strong>Gender:</strong> {gender}</p>
        <p><strong>Nationality:</strong> {nationality}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Address:</strong> {address}</p>
        <p><strong>City:</strong> {city}</p>
        <p><strong>Pincode:</strong> {pincode}</p>
        <p><strong>State:</strong> {state}</p>
        <p><strong>Country:</strong> {country}</p>
        """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
