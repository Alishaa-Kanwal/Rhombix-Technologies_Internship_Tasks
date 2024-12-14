from flask import Flask, render_template, request
app = Flask(__name__)

def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

@app.route("/", methods=["GET", "POST"])
def home():
    result = []
    if request.method == "POST":
        try:
            num = int(request.form.get("count"))
            if num <= 0:
                result = ["Please enter a positive number!"]
            else:
                result = fibonacci(num)
        except ValueError:
            result = ["Invalid input! Please enter a valid number."]
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
