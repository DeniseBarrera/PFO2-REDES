from flask import Flask, request, jsonify, render_template, url_for
import sqlite3
import bcrypt

app = Flask(__name__)

def init_db():
    with sqlite3.connect("base.db") as con:
        cur = con.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    USUARIO text unique not null,
                    contraseña TEXT NOT NULL
                    )
                """)
        con.commit()
init_db()

@app.route("/registro", methods=["POST"])
def registrar_usuario():
    datos = request.get_json()
    usuario = datos.get("usuario")
    contraseña = datos.get("contraseña")

    if not usuario or not contraseña:
        return jsonify({"error": "Datos incompletos"}), 400
    
    contraseña_hashed = bcrypt.hashpw(contraseña.encode("utf-8"), bcrypt.gensalt())

    try:
        with sqlite3.connect("base.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)", (usuario, contraseña_hashed))
            con.commit()
            return jsonify({"mensaje": "Usuario registrado con éxito"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "El usuario ya existe"}), 409

@app.route("/login", methods=["POST"])
def login():
    datos = request.get_json()
    usuario = datos.get("usuario")
    contraseña = datos.get("contraseña")

    with sqlite3.connect("base.db") as con:
        cur = con.cursor()
        cur.execute("SELECT contraseña FROM usuarios WHERE usuario = ?", (usuario,))
        fila = cur.fetchone()

        if fila and bcrypt.checkpw(contraseña.encode("utf-8"), fila[0]):
            return jsonify({"mensaje": "Login exitoso"}), 200
        else:
            return jsonify({"error": "Credenciales incorrectas"}), 401

@app.route("/tareas", methods=["GET"])
def tareas():
    return render_template("bienvenida.html")

if __name__ == "__main__":
    app.run(debug=True)