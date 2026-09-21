
import socket
import threading
import sqlite3
from datetime import datetime


# Configuración del servidor
HOST = "localhost"
PORT = 5000
DATABASE = "chat.db"


def inicializar_db():
    # Crea la base de datos y la tabla de mensajes si todavía no existen.
    try:
        conexion = sqlite3.connect(DATABASE)
        cursor = conexion.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT NOT NULL,
                fecha_envio TEXT NOT NULL,
                ip_cliente TEXT NOT NULL
            )
        """)

        conexion.commit()
        conexion.close()

        print("Base de datos inicializada correctamente.")

    except sqlite3.Error as error:
        print(f"Error al acceder a la base de datos: {error}")


def guardar_mensaje(contenido, fecha_envio, ip_cliente):
    #  Guarda un mensaje recibido en la base de datos.   
    try:
        conexion = sqlite3.connect(DATABASE)
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO mensajes (contenido, fecha_envio, ip_cliente)
            VALUES (?, ?, ?)
        """, (contenido, fecha_envio, ip_cliente))

        conexion.commit()
        conexion.close()

        return True

    except sqlite3.Error as error:
        print(f"Error al guardar el mensaje: {error}")
        return False


def inicializar_socket():    
    # Crea y configura el socket TCP del servidor.    
    try:
        # Configuración del socket TCP/IP
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Vincular el socket a localhost y al puerto 5000
        servidor.bind((HOST, PORT))

        # Escuchar conexiones entrantes
        servidor.listen(5)

        print(f"Servidor escuchando en {HOST}:{PORT}...")

        return servidor

    except OSError as error:
        print(f"Error al iniciar el servidor: {error}")
        print("Es posible que el puerto esté ocupado.")
        return None


def atender_cliente(conn, addr):  
    # Atiende a un cliente, recibe sus mensajes, los guarda en la base de datos y envía respuestas.  
    print(f"Cliente conectado: {addr[0]}")

    try:
        while True:
            # Recibir el mensaje del cliente
            datos = conn.recv(1024)

            # Si no hay datos, el cliente cerró la conexión
            if not datos:
                break

            mensaje = datos.decode("utf-8")

            # 'exito' indica que el cliente quiere finalizar
            if mensaje.lower() == "exito":
                print(f"Cliente {addr[0]} finalizó la conexión.")
                break

            print(f"Mensaje recibido de {addr[0]}: {mensaje}")

            # Obtener la fecha y hora del mensaje
            fecha_envio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Guardar el mensaje en la base de datos
            guardado = guardar_mensaje(
                mensaje,
                fecha_envio,
                addr[0]
            )

            if guardado:
                # Respuesta solicitada por la consigna
                respuesta = f"Mensaje recibido: {fecha_envio}"
            else:
                respuesta = "Error al guardar el mensaje en la base de datos."

            # Enviar la respuesta al cliente
            conn.sendall(respuesta.encode("utf-8"))

    except ConnectionError as error:
        print(f"Error de conexión con {addr[0]}: {error}")

    finally:
        conn.close()
        print(f"Conexión cerrada con {addr[0]}.")


def aceptar_conexiones(servidor):    
    # Acepta conexiones y crea un hilo para cada cliente.    
    while True:
        try:
            # Aceptar una conexión entrante
            conn, addr = servidor.accept()

            # Crear un hilo para atender al cliente
            hilo = threading.Thread(
                target=atender_cliente,
                args=(conn, addr)
            )

            # Iniciar el hilo
            hilo.start()

        except OSError as error:
            print(f"Error al aceptar la conexión: {error}")
            break


#  ****Función principal del servidor.****
def main(): 
    
    # Inicializar la base de datos
    inicializar_db()

    # Inicializar el socket
    servidor = inicializar_socket()

    if servidor is None:
        return

    try:
        # Esperar conexiones de los clientes
        aceptar_conexiones(servidor)

    except KeyboardInterrupt:
        print("\nServidor detenido por el usuario.")

    finally:
        # Cerrar el socket del servidor
        servidor.close()
        print("Servidor cerrado.")



# Ejecutar el servidor
if __name__ == "__main__":
    main()
