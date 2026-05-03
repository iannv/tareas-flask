import requests

session = requests.Session()
BASE_URL = "http://127.0.0.1:5000"


def tareas():
    response = session.get(f"{BASE_URL}/tareas")
    print(response.text)


def registro():
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")

    response = session.post(
        f"{BASE_URL}/registro",
        json={"usuario": usuario, "clave": clave},
    )

    print(response.json())


def login():
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")

    response = session.post(
        f"{BASE_URL}/login",
        json={"usuario": usuario, "clave": clave},
    )

    print(response.json())

    if response.status_code == 200:
        print("\nAccediendo a tareas...\n")
        tareas()


while True:
    print("\n1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Elegir opción: ")

    if opcion == "1":
        registro()
    elif opcion == "2":
        login()
    elif opcion == "3":
        break