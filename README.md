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

- Instalar dependencias: `pip install flask flask-bcrypt requests`
- Ejecutar el servidor en consola `py servidor.py`. Se iniciará en `http://127.0.0.1:5000`

- Ejecutar el cliente desde consola
  - En otra terminal ejecutar el cliente `py cliente.py`

- Ejecutar el cliente desde el navegador
  - Abrir el navegador en `http://127.0.0.1:5000/login-web`

### Base de Datos

Se utiliza SQLite. El archivo `usuarios.db` se genera automáticamente al iniciar el servidor.

La tabla contiene:
```
id
usuario
clave (hasheada)
```

## Endpoints disponibles
🔹 Registro de usuario `POST /registro`

```
{
  "usuario": "nombre",
  "clave": "1234"
}
```

🔹 Inicio de sesión `POST /login`

Si las credenciales son correctas, se crea una sesión.

```
{
  "usuario": "nombre",
  "clave": "1234"
}
```

🔹 Tareas (Ruta protegida) `GET /tareas`

Si el usuario está autenticado, muestra la página de tareas.

Si no está autenticado, muestra mensaje que se debe iniciar sesión.





