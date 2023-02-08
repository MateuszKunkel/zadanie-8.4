from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/mypage/contact', methods=['GET', 'POST'])
def func():
    if request.method == 'GET':
        return render_template("greeting.html")
    elif request.method == 'POST':
        print(request.form)
        return redirect("/mypage/contact")

@app.route('/mypage/me', methods=['GET'])
def message():
    return render_template("form.html")

if __name__ == "__main__": 
    app.run(debug = True)