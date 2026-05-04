from flask import Flask, request, jsonify, session, redirect, url_for
import sqlite3
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "super_clave_secreta"
bcrypt = Bcrypt(app)

DATABASE = "usuarios.db"


# =========================
# CREAR BASE DE DATOS
# =========================
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            clave TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


init_db()


# =========================
# REGISTRO
# =========================
@app.route("/registro", methods=["POST"])
def registro():
    data = request.json
    usuario = data.get("usuario")
    clave = data.get("clave")

    if not usuario or not clave:
        return jsonify({"error": "Faltan datos"}), 400

    hashed = bcrypt.generate_password_hash(clave).decode("utf-8")

    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (usuario, clave) VALUES (?, ?)", (usuario, hashed)
        )
        conn.commit()
        conn.close()
        return jsonify({"mensaje": "Usuario registrado correctamente"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "El usuario ya existe"}), 400


# =========================
# LOGIN DESDE CONSOLA
# =========================
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    usuario = data.get("usuario")
    clave = data.get("clave")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT clave FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado and bcrypt.check_password_hash(resultado[0], clave):
        session["usuario"] = usuario
        return jsonify({"mensaje": "Login exitoso"}), 200
    else:
        return jsonify({"error": "Credenciales incorrectas"}), 401


# Login desde la web
@app.route("/login-web")
def login_web():
    return """
    <h2>Iniciar Sesión</h2>
    <form method="post" action="/login-web">
        Usuario: <input name="usuario"><br><br>
        Clave: <input type="password" name="clave"><br><br>
        <button type="submit">Iniciar sesión</button>
    </form>
    """


@app.route("/login-web", methods=["POST"])
def procesar_login_web():
    usuario = request.form.get("usuario")
    clave = request.form.get("clave")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT clave FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado and bcrypt.check_password_hash(resultado[0], clave):
        session["usuario"] = usuario
        return redirect("/tareas")
    else:
        return "Credenciales incorrectas"


# =========================
# TAREAS
# =========================
@app.route("/tareas", methods=["GET"])
def tareas():
    if "usuario" not in session:
        return f""" <p>Debes iniciar sesión para acceder a las tareas.</p> """

    return f"""
    <h1>Bienvenido/a {session['usuario']} al sistema de tareas</h1>
    """

if __name__ == "__main__":
    app.run(debug=True)
