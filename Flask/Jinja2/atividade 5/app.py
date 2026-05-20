from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    nome = "Erick"
    dados = {"nome": "Erick", "idade": 17}
    usuario = {"nome": "Erick", "email": "12401188@email.com"}
    alunos = ["Enzo", "Rafael", "Jeffrey", "Erick", "João"]
    nota = 6

    return render_template(
        "base.html", nome=nome, dados=dados, usuario=usuario, alunos=alunos, nota=nota
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        USUARIO_VALIDO = "Erick"
        SENHA_VALIDA = "12401188"

        if usuario == USUARIO_VALIDO and senha == SENHA_VALIDA:
            return f"<h1>Bem-vindo, {usuario}!</h1>"
        else:
            return "<h1>Login inválido</h1>"
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
