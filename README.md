# CazaVectores - Sistema de Gestión de Inventario

Aplicación web para gestión de inventario con control de vencimientos, movimientos y chat interno.

## 🧹 Limpieza de Base de Datos

Antes de desplegar, ejecuta el script de limpieza para eliminar datos sensibles:

```bash
python limpiar_db.py
```

Este script:
- ✅ Elimina todos los productos, movimientos y mensajes
- ✅ Mantiene la estructura de la base de datos
- ✅ Conserva solo el usuario admin (admin/admin123)
- ✅ Resetea los auto-increment

## Despliegue en Hosting Gratuito

### Opción Recomendada: PythonAnywhere

1. **Crear cuenta** en [PythonAnywhere](https://www.pythonanywhere.com) (plan gratuito)

2. **Crear Web App:**
   - Ir a "Web" → "Add a new web app"
   - Seleccionar "Flask"
   - Elegir Python 3.8 o superior

3. **Configurar Base de Datos:**
   - Ir a "Databases" → Crear MySQL database
   - Anotar las credenciales (host, user, password, database name)

4. **Subir Código:**
   - Usar el editor web de PythonAnywhere o Git
   - Subir todos los archivos del proyecto

5. **Configurar Variables de Entorno:**
   - Crear archivo `.env` en tu directorio home
   - Configurar las variables según `.env.example`

6. **Instalar Dependencias:**
   - En la consola de PythonAnywhere: `pip install -r requirements.txt`

7. **Configurar WSGI:**
   - Editar el archivo WSGI generado
   - Asegurar que apunte a tu `app.py`

8. **Recargar la App:**
   - En "Web" → Reload

### Variables de Entorno Requeridas

Crear un archivo `.env` con:

```
SECRET_KEY=tu_clave_secreta_segura
DB_HOST=tu_usuario.mysql.pythonanywhere-services.com
DB_USER=tu_usuario
DB_PASSWORD=tu_password_mysql
DB_NAME=tu_usuario$cazavectores
```

### Notas Importantes

- El plan gratuito tiene límites de CPU y almacenamiento
- La base de datos MySQL gratuita es de 50MB
- Para producción, considera cambiar a PostgreSQL o SQLite

## Funcionalidades

- Gestión de inventario con FEFO (First Expired, First Out)
- Control de vencimientos
- Registro de movimientos
- Chat interno
- Exportación a Excel
- Filtros por usuario, tipo, fechas

## Tecnologías

- Flask
- MySQL
- OpenPyXL para Excel
- HTML/CSS/JavaScript básico