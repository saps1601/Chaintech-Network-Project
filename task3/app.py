from flask import Flask, render_template
app=Flask(__name__)
import datetime
import random


quotes=["Life isn’t about getting and having, it’s about giving and being.",
"Whatever the mind of man can conceive and believe, it can achieve.",
"Strive not to be a success, but rather to be of value.",
"Two roads diverged in a wood, and I—I took the one less traveled by, And that has made all the difference.",
"I attribute my success to this: I never gave or took any excuse.",
"You miss 100% of the shots you don’t take."]

@app.route('/')
def index():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_quote = random.choice(quotes)
    return render_template('index.html', time=current_time, quote=random_quote)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
