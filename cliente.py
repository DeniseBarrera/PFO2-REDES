import requests

URL_BASE = "http://localhost:5000"

def registrar():
    print("\nREGISTRO")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    datos = {
        "usuario": usuario,
        "contraseña": contraseña
    }

    respuesta = requests.post(f"{URL_BASE}/registro", json=datos)

    if respuesta.status_code == 201:
        print("Registro exitoso.")
    elif respuesta.status_code == 409:
        print("El usuario ya existe.")
    else:
        print("Error:", respuesta.json())

def login():
    print("\nLOGIN")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    datos = {
        "usuario": usuario,
        "contraseña": contraseña
    }

    respuesta = requests.post(f"{URL_BASE}/login", json=datos)

    if respuesta.status_code == 200:
        print("Login exitoso.")
        print("Cargando página de bienvenida...")
        tareas_response = requests.get(f"{URL_BASE}/tareas")

        if tareas_response.status_code == 200:
            print("\nPágina HTML recibida:")
            print("="*40)
            print(tareas_response.text[:1000])  # solo muestra primeros 1000 caracteres
            print("="*40)
            print("\nPágina cargada correctamente. Abrila en tu navegador: http://localhost:5000/tareas")
        else:
            print("Error al cargar tareas.")
    
    else:
        print("Credenciales incorrectas.")

def menu():
    print("=== Cliente de consola ===")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    eleccion = input("Elija una opción (1 o 2): ")

    if eleccion == "1":
        registrar()
    elif eleccion == "2":
        login()
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    menu()
