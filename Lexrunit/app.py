from flask import Flask, render_template, send_from_directory, request
import os
import forms

app = Flask(__name__)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"),
    "favicon.ico", mimetype="image/vnd.microsoft.icon")

@app.route("/", methods = ["POST", "GET"])
@app.route("/home", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        forms.form_action()
        return render_template("Lex.html")
    else:
        return render_template("Lex.html")

@app.errorhandler(500)
def internal_server(error):
    return render_template("servererror.html"), 500

@app.errorhandler(404)
def not_found(error):
    return render_template("notfound.html"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3030)
