# Girasol

# Despliegue de una Aplicación Flask en Heroku

## Pasos para Desplegar en Heroku

1. **Crea una cuenta en Heroku**:
   - Regístrate en [Heroku](https://www.heroku.com/) si no tienes una cuenta.

2. **Instala la CLI de Heroku**:
   - Descarga e instala la [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

3. **Prepara tu aplicación Flask**:
   - Asegúrate de que tu aplicación Flask esté funcionando correctamente en tu máquina local.
   - Crea un archivo `requirements.txt` que contenga todas las dependencias de tu proyecto. Puedes generarlo con el siguiente comando:
     ```bash
     pip freeze > requirements.txt
     ```

4. **Crea un archivo `Procfile`**:
   - En el directorio raíz de tu proyecto, crea un archivo llamado `Procfile` (sin extensión) y añade lo siguiente:
     ```
     web: python app.py
     ```
   - Asegúrate de reemplazar `app.py` con el nombre de tu archivo principal si es diferente.

5. **Configura el archivo `runtime.txt` (opcional)**:
   - Si deseas especificar una versión de Python, crea un archivo llamado `runtime.txt` y escribe la versión deseada, por ejemplo:
     ```
     python-3.10.0
     ```

6. **Inicia sesión en Heroku**:
   - Abre tu terminal y ejecuta:
     ```bash
     heroku login
     ```

7. **Crea una nueva aplicación en Heroku**:
   - Crea una nueva aplicación con:
     ```bash
     heroku create nombre-de-tu-aplicacion
     ```
   - Reemplaza `nombre-de-tu-aplicacion` con un nombre único.

8. **Sube tu aplicación a Heroku**:
   - Asegúrate de estar en el directorio de tu proyecto y ejecuta:
     ```bash
     git init  # Solo si no has inicializado un repositorio Git
     git add .
     git commit -m "Preparando para Heroku"
     git push heroku master
     ```

9. **Accede a tu aplicación**:
   - Una vez que el despliegue sea exitoso, puedes abrir tu aplicación en el navegador con:
     ```bash
     heroku open
     ```

## Consideraciones Finales

- **Configuraciones de entorno**: Si necesitas variables de entorno (como claves de API), puedes configurarlas en Heroku usando:
  ```bash
  heroku config:set NOMBRE_VARIABLE=valor
