
import socket


# Configuración del servidor
HOST = "localhost"
PORT = 5000


def conectar_servidor():
# Crea el socket y se conecta al servidor.
    try:
        # Crear el socket TCP
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conectar al servidor
        cliente.connect((HOST, PORT))

        print(f"Conectado al servidor {HOST}:{PORT}")

        return cliente

    except ConnectionRefusedError:
        print("No se pudo conectar al servidor.")
        print("Verificá que el servidor esté ejecutándose.")
        return None


def enviar_mensajes(cliente):
# Permite enviar múltiples mensajes al servidor hasta que el usuario escriba 'exito'.
    while True:
        mensaje = input("Escribí un mensaje (o 'exito' para salir): ")

        try:
            # Enviar el mensaje al servidor
            cliente.sendall(mensaje.encode("utf-8"))

            # Finalizar si el usuario escribió 'exito'
            if mensaje.lower() == "exito":
                break

            # Recibir la respuesta del servidor
            respuesta = cliente.recv(1024).decode("utf-8")

            # Mostrar la respuesta
            print(f"Respuesta del servidor: {respuesta}")

        except ConnectionError as error:
            print(f"Error de conexión: {error}")
            break


# ****Función principal del cliente.****
def main():

    # Conectarse al servidor
    cliente = conectar_servidor()

    if cliente is None:
        return
 
    try:
        # Enviar mensajes al servidor
        enviar_mensajes(cliente)

    finally:
        # Cerrar la conexión
        cliente.close()
        print("Conexión cerrada.")


# Ejecutar el cliente
if __name__ == "__main__":
    main()