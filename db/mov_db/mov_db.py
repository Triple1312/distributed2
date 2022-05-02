from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)
print("mov_db")
@app.route("/hello")
def hello():
    return "hello from mov_db on port 5002"

if __name__ == '__main__':
    app.run()