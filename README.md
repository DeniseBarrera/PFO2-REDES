#  Sistema de Gestión de Tareas - API Flask + SQLite

Este proyecto es un sistema básico de gestión de usuarios y tareas utilizando **Python**, **Flask** y **SQLite**. 
Forma parte de mi entrega de practica formativa de Sistema de Redes (PFO 2).

##  Funcionalidades

- Registro de usuarios con contraseñas protegidas.
- Inicio de sesión con verificación segura.
- Visualización de un HTML de bienvenida.
- Base de datos persistente usando SQLite.
- API REST desarrollada con Flask.

---
##  Instalación y ejecución

1. **Clonar el repositorio** o descargar los archivos.
2. **Crear un entorno virtual** (opcional):

   python -m venv venv

3. **Activar el entorno virtual**
Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate

4. **Instalar dependencias**
 pip install -r requirements.txt

5. **Ejecutar la API**
 python servidor.py

 ###Endpoints
 POST/registro
 Registra un nuevo usuario
 Body: {
  "usuario": "nombre",
  "contraseña": "1234"
}

POST/login
Body: {
  "usuario": "nombre",
  "contraseña": "1234"
}

GET/tareas
Devuelve HTML con mensaje de bienvenida!!

Capturas podran ser vistas en la carpeta capturas/

¿Por qué hashear contraseñas?
Hashear contraseñas es importantisimo para proteger los datos sensibles de los usuarios. De esta forma, incluso si alguien accede a la base de datos, no podrá leer las contraseñas reales.

Ventajas de usar SQLite en este proyecto
Es una base de datos liviana y rápida.

No requiere servidor, ideal para proyectos pequeños.

Guarda todo en un archivo .db que podés mover fácilmente.

Se integra de forma nativa con Python.
--------------------------------------------------------------

Denise Barrera