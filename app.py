from flask import Flask, jsonify, render_template
import wolastoqeynumbers, random
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/getnum")
def getnum():
    num = random.randint(1,100)
    num_as_str = wolastoqeynumbers.to_words(num)
    return jsonify(num=num,num_as_str=num_as_str)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/wolasuweltomuwakon/')
def wolasuweltomuwakon():
    return render_template('wolasuweltomuwakon.html')

if __name__ == '__main__':
    app.run()
