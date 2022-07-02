from flask import Flask, render_template

app = Flask(__name__)


@app.route("/inicio")
def inicio():  # put application's code here
    return render_template("inicio.html")

@app.route("/contatos")
def contatos():  # put application's code here
    return render_template("contatos.html")

@app.route("/produtos")
def produtos():  # put application's code here
    return render_template("produtos.html")


if __name__ == "__main__":
    app.run(debug=True)
