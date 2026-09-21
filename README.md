# TP: Implementación de un Chat Básico Cliente-Servidor con Sockets y Base de Datos

## 📌 Propuesta Formativa Obligatoria

### 🎯 Objetivo

Aprender a configurar un servidor de sockets en Python que reciba mensajes de clientes, los almacene en una base de datos y envíe confirmaciones, aplicando buenas prácticas de modularización y manejo de errores.

Utilizar los comentarios para explicar las configuraciones en el servidor.

---

## 🖥️ Servidor

* ✅ Crear un socket que escuche en `localhost:5000`.

* ✅ Usar funciones separadas para:

  * Inicializar el socket.
  * Aceptar conexiones y recibir mensajes.
  * Guardar cada mensaje en una DB SQLite con los campos:

    * `id`
    * `contenido`
    * `fecha_envio`
    * `ip_cliente`
  * Manejar errores:

    * Puerto ocupado.
    * DB no accesible.

* ✅ Responder al cliente con:

```text
Mensaje recibido: <timestamp>
```

---

## 💻 Cliente

* ✅ Tener la capacidad de conectarse al servidor y enviar múltiples mensajes hasta que el usuario escriba `exito`.

* ✅ Mostrar la respuesta del servidor para cada mensaje.

---

## 🗄️ Base de datos

Se utiliza el módulo `sqlite3` para la base de datos.

La tabla utilizada para almacenar los mensajes contiene los siguientes campos:

| Campo         | Descripción                       |
| ------------- | --------------------------------- |
| `id`          | Identificador del mensaje         |
| `contenido`   | Contenido del mensaje enviado     |
| `fecha_envio` | Fecha y hora de envío del mensaje |
| `ip_cliente`  | Dirección IP del cliente          |

---

## 🧪 Pruebas locales

* ✅ Ejecutar primero el servidor.
* ✅ Ejecutar el cliente en otra terminal.
* ✅ Enviar múltiples mensajes desde el cliente.
* ✅ Verificar la respuesta del servidor para cada mensaje.
* ✅ Verificar que los mensajes sean almacenados correctamente en la base de datos.

### Ejecución

**1. Iniciar el servidor:**

```bash
python server.py
```

**2. En otra terminal, iniciar el cliente:**

```bash
python cliente.py
```

**3. Enviar los mensajes que se quieran probar.**

Para finalizar la conexión:

```text
exito
```

---

## 💡 Mejoras y conceptos aplicados

Además de cumplir con los requisitos de la propuesta, se incorporaron algunos conceptos vistos durante la cursada:

* 🧵 **Multithreading:** se utilizó para que cada cliente pueda ser atendido de manera independiente mediante un hilo.
* 🔌 **Manejo de múltiples clientes:** el servidor puede aceptar conexiones de diferentes clientes sin tener que finalizar la conexión anterior.
* 🧩 **Modularización:** se separaron las diferentes tareas del servidor y del cliente en funciones independientes para organizar mejor el código.
* 🛡️ **Manejo de errores:** se incorporaron controles para detectar problemas de conexión, puerto ocupado y acceso a la base de datos.
* 🗄️ **Persistencia de datos:** los mensajes recibidos quedan almacenados en SQLite para poder consultarlos posteriormente.


