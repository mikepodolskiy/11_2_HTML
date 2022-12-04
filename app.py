import random
from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def hello():
#   return render_template('hello.html')

# @app.route('/')
# def hello2():
#   name = "Ivan"
#   phone = "+7 123 456 78 90"
#   return render_template('hello.html', name=name, phone=phone)


# @app.route('/')
# def hello2():
#     user_data = {
#         "name": "Ivan",
#         "phone": "+7 123 456 78 90",
#         "email": "ivan_dev@gmail.com",
#         "telegram": "ivan_dev",
#     }
#     return render_template('hello2.html', user=user_data)

# @app.route('/')
# def hello():
#   items = ["Python", "Java", "Kotlin", "Go"]
#   return render_template('hello.html', items=items)

@app.route('/')
def hello():
    is_blocked = random.choice([True, False])
    return render_template('hello3.html', is_blocked=is_blocked)


app.run()
