from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<h2>Simple Flask Calculator</h2>

<form method="post">
    Number 1: <input type="number" name="num1" required><br><br>
    Number 2: <input type="number" name="num2" required><br><br>

    Operation:
    <select name="operation">
        <option value="add">Add</option>
        <option value="sub">Subtract</option>
        <option value="mul">Multiply</option>
        <option value="div">Divide</option>
    </select><br><br>

    <input type="submit" value="Calculate">
</form>

<h3>Result: {{result}}</h3>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        op = request.form["operation"]

        if op == "add":
            result = num1 + num2
        elif op == "sub":
            result = num1 - num2
        elif op == "mul":
            result = num1 * num2
        elif op == "div":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero"

    return render_template_string(html, result=result)

if __name__ == "__main__":
    app.run(debug=True)
