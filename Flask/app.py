from flask import Flask, render_template, request, jsonify
from flask import request

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def home_page() :
    return render_template('index.html') 

@app.route("/math", methods = ['POST'])
def math_operation() :
    if(request.method == "POST") :
        op = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = ''

        if(op == 'add') :
            sum = num1 + num2
            result = f"The sum of {num1} and {num2} yeilds {sum}!"
        elif(op == 'subtract') :
            subtract = num1 - num2
            result = f"The difference of {num1} and {num2} yeilds {subtract}!"
        elif(op == 'multiply') :
            multiply = num1 * num2
            result = f"The product of {num1} and {num2} yeilds {multiply}!"
        elif(op == 'divide') :
            divide = num1 / num2
            result = f"The division of {num1} and {num2} yeilds {divide}!"
        
        return render_template('results.html', result = result)

@app.route("/postman_data", methods = ['POST'])
def math_operation1() :
    if(request.method == "POST") :
        op = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        result = ''

        if(op == 'add') :
            sum = num1 + num2
            result = f"The sum of {num1} and {num2} yeilds {sum}!"
        elif(op == 'subtract') :
            subtract = num1 - num2
            result = f"The difference of {num1} and {num2} yeilds {subtract}!"
        elif(op == 'multiply') :
            multiply = num1 * num2
            result = f"The product of {num1} and {num2} yeilds {multiply}!"
        elif(op == 'divide') :
            divide = num1 / num2
            result = f"The division of {num1} and {num2} yeilds {divide}!"
        
        return jsonify(result)
# @app.route("/hello_world1")
# def hello_world1() :
#     return "<h1>Hello, World!1</h1>"

# @app.route("/hello_world2")
# def hello_world2() :
#     return "<h1>Hello, World!2</h1>"

# @app.route("/test")
# def test() :
#     a = 5 + 6
#     return "<h1>This is my function to run app {}</h1>".format(a)

# @app.route("/test1")
# def test1() :
#     data = request.args.get('x')
#     return "<h1>The data entered is {}</h1>".format(data)

if __name__ == "__main__" :
    app.run(host="0.0.0.0")