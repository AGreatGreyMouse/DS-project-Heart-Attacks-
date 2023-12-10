from flask import (Flask, request, render_template, url_for)

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/all')
def al():
    return render_template('all.html')


@app.route('/game', methods=["GET", "POST"])
def count():
    if request.method == 'POST':
        x = request.form['cnt']

        return render_template('game.html', result=x)
    else:
        return render_template('game.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)
