from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        name = request.form["name"]
        age = int(request.form["age"])
        nationality = request.form["nationality"].strip().lower()

        if age >= 18 and nationality == "indian":
            result = f"✅ Hello {name}, You are Eligible to Vote."
        else:
            result = f"❌ Hello {name}, You are Not Eligible to Vote."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)