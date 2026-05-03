# API REST con Flask – Autenticación y SQLite
Este proyecto consiste en el desarrollo de una API REST utilizando Flask.

La aplicación permite:

- Registro de usuarios  
- Inicio de sesión con autenticación  
- Protección de rutas mediante sesión  
- Persistencia de datos utilizando SQLite  
- Cliente en consola para interactuar con la API  

Las contraseñas se almacenan hasheadas utilizando `flask-bcrypt` para mayor seguridad.

---

## Instalación y Ejecución

1. Instalar dependencias: `pip install flask flask-bcrypt requests`
2. Ejecutar el servidor en consola `py servidor.py`. Se iniciará en `http://127.0.0.1:5000`
3. En otra terminal ejecutar el cliente (opcional) `py cliente.py`

### Base de Datos

Se utiliza SQLite.

El archivo `usuarios.db` se genera automáticamente al iniciar el servidor.

La tabla contiene:
```
id
usuario
clave (hasheada)
```

## Endpoints disponibles
🔹 Registro de usuario

POST /registro

```
{
  "usuario": "nombre",
  "clave": "1234"
}
```

🔹 Inicio de sesión

POST /login

```
{
  "usuario": "nombre",
  "clave": "1234"
}
```

Si las credenciales son correctas, se crea una sesión.

🔹 Tareas (Ruta protegida)

GET /tareas

Si el usuario está autenticado → muestra la página de tareas.
Si no está autenticado → redirige a /no-autorizado.
🔹 Ruta de no autorizado

GET /no-autorizado

Muestra un mensaje indicando que el usuario debe iniciar sesión.

