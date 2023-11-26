from flask import Flask

app=Flask(__name__)

@app.route("/Welcome")
def print_msg():
    return "Welcome to ABC Corporation"

@app.route("/")
def details():
    details="""
    Company Name: ABC Corporation
    Location: India
    Contact Detail: 999-999-9999"""
    return details
if __name__=="__main__":
    app.run(host="0.0.0.0",port=3000)