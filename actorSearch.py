from flask import Flask, redirect, url_for , render_template, request
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("home.html")

@app.route("/<usr>")
def user(usr):
    

    return "User is %s " %(usr)

if __name__ == "__main__":
    app.run(debug=True)