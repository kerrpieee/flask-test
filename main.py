from flask import Flask
from datetime import datetime

# print(__name__)

app = Flask(__name__)

books = {1: "Python book", 2: "Java book", 3: "Flask book"}


@app.route("/bmi/name=<name>&height=<h>&weight=<w>")
def my_bmi(name, h, w):
    try:
        BMI = round(eval(w) / ((eval(h) / 100) ** 2), 2)
        return f"<h1><span style='color:blue'>{name}</span> BMI:{BMI}</h1>"
    except Exception as e:
        print(e)
    return "<h2>參數不正確!</h2>"


@app.route("/sum/x=<x>&y=<y>")
def my_sum(x, y):
    try:
        total = eval(x) + eval(y)
        return f"<h1>{x}+{y}={total}</h1>"
    except Exception as e:
        print(e)
    return "<h2>參數不正確!</h2>"


@app.route("/book/<int:id>")
def show_book(id):
    if id not in books:
        return f"<h2 style='color:red'>無此編號:{id}</h2>"
    return f"<h1>第{id}本書:{books[id]}</h1>"


@app.route("/books")
def show_books():
    return books


@app.route("/")
def index():
    today = datetime.now()
    print(today)
    return f"<h1>Hello Flask!<br>{today}</h1>"


app.run()
