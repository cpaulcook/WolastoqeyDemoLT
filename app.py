from flask import Flask, render_template
import wolastoqeynumbers, random
app = Flask(__name__)


@app.route('/')
def home():
    num = random.randint(1,100)
    num_as_str = wolastoqeynumbers.to_words(num)
    return render_template("home.html", num=num, num_as_str=num_as_str)

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
