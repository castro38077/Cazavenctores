import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return pymysql.connect(
        host=os.environ.get('MYSQLHOST'),
        user=os.environ.get('MYSQLUSER'),
        password=os.environ.get('MYSQLPASSWORD'),
        database=os.environ.get('MYSQLDATABASE'),
        port=int(os.environ.get('MYSQLPORT')),
        cursorclass=pymysql.cursors.DictCursor
    )

def limpiar_base_datos():
    """Limpia todos los datos pero mantiene la estructura de la base de datos"""

    connection = get_connection()
    cursor = connection.cursor()

    try:
        print("🧹 Iniciando limpieza de base de datos...")

        # Limpiar movimientos primero (foreign keys)
        cursor.execute("DELETE FROM movimientos")
        print("✅ Movimientos eliminados")

        # Limpiar productos
        cursor.execute("DELETE FROM productos")
        print("✅ Productos eliminados")

        # Limpiar mensajes
        cursor.execute("DELETE FROM mensajes")
        print("✅ Mensajes eliminados")

        # Mantener solo usuario admin (cambiar 'admin' por el username que uses)
        cursor.execute("DELETE FROM usuarios WHERE username != 'admin'")
        print("✅ Usuarios eliminados (excepto admin)")

        # Resetear auto_increment si es necesario
        cursor.execute("ALTER TABLE productos AUTO_INCREMENT = 1")
        cursor.execute("ALTER TABLE movimientos AUTO_INCREMENT = 1")
        cursor.execute("ALTER TABLE mensajes AUTO_INCREMENT = 1")
        cursor.execute("ALTER TABLE usuarios AUTO_INCREMENT = 1")
        print("✅ Auto-increment reseteado")

        connection.commit()
        print("🎉 Base de datos limpiada exitosamente!")

    except Exception as e:
        print(f"❌ Error durante la limpieza: {e}")
        connection.rollback()

    finally:
        connection.close()

def crear_usuario_admin():
    """Crea usuario admin si no existe"""

    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Verificar si existe admin
        cursor.execute("SELECT * FROM usuarios WHERE username = 'admin'")
        admin = cursor.fetchone()

        if not admin:
            # Crear usuario admin
            cursor.execute(
                "INSERT INTO usuarios (username, password) VALUES (%s, %s)",
                ('admin', 'admin123')  # Cambia la contraseña por una segura
            )
            connection.commit()
            print("👤 Usuario admin creado: admin / admin123")
        else:
            print("👤 Usuario admin ya existe")

    except Exception as e:
        print(f"❌ Error creando usuario admin: {e}")

    finally:
        connection.close()

if __name__ == "__main__":
    print("🔧 Script de limpieza de base de datos para CazaVectores")
    print("=" * 50)

    limpiar_base_datos()
    crear_usuario_admin()

    print("\n✅ Proceso completado. La base de datos está lista para el despliegue.")