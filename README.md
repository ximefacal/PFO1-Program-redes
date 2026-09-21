# TP: Implementación de un Chat Básico Cliente-Servidor

## 📌 Propuesta Formativa Obligatoria

Implementación de un sistema de comunicación **cliente-servidor** utilizando **sockets en Python** y una **base de datos SQLite**.

### 🎯 Objetivo

Configurar un servidor de sockets en Python que:

* Reciba mensajes de los clientes.
* Almacene los mensajes en una base de datos.
* Envíe confirmaciones al cliente.
* Utilice funciones separadas para organizar el código.
* Incluya manejo de errores.
* Utilice comentarios para explicar las configuraciones principales del servidor.

---

## 🖥️ Servidor

El servidor debe escuchar conexiones en `localhost:5000`.

### Requisitos

* ✅ Crear y configurar un socket TCP/IP.
* ✅ Escuchar conexiones en `localhost:5000`.
* ✅ Inicializar el socket mediante una función independiente.
* ✅ Aceptar conexiones de los clientes.
* ✅ Recibir mensajes enviados por los clientes.
* ✅ Guardar cada mensaje en una base de datos SQLite.
* ✅ Utilizar una tabla con los siguientes campos:

  * `id`
  * `contenido`
  * `fecha_envio`
  * `ip_cliente`
* ✅ Manejar errores relacionados con el puerto.
* ✅ Manejar errores relacionados con el acceso a la base de datos.
* ✅ Responder al cliente con el formato:

```text
Mensaje recibido: <timestamp>
```

* ✅ Utilizar comentarios para explicar las secciones principales del código.
* ✅ Utilizar hilos para permitir la atención de múltiples clientes.

---

## 💻 Cliente

El cliente permite establecer una conexión con el servidor y enviar múltiples mensajes.

### Requisitos

* ✅ Conectarse al servidor mediante un socket TCP/IP.
* ✅ Enviar múltiples mensajes durante una misma conexión.
* ✅ Mostrar la respuesta recibida del servidor.
* ✅ Finalizar la conexión cuando el usuario escribe `exito`.

---

## 🗄️ Base de datos

Se utiliza **SQLite** mediante el módulo `sqlite3` de Python.

La base de datos almacena los mensajes recibidos por el servidor junto con:

| Campo         | Descripción                               |
| ------------- | ----------------------------------------- |
| `id`          | Identificador único del mensaje           |
| `contenido`   | Texto enviado por el cliente              |
| `fecha_envio` | Fecha y hora en que se recibió el mensaje |
| `ip_cliente`  | Dirección IP del cliente                  |

---

## 🧪 Pruebas locales

Para realizar las pruebas:

* ✅ Ejecutar primero el servidor.
* ✅ Ejecutar el cliente en otra terminal.
* ✅ Enviar varios mensajes desde el cliente.
* ✅ Verificar las respuestas enviadas por el servidor.
* ✅ Verificar que los mensajes se almacenen correctamente en SQLite.
* ✅ Probar la conexión de varios clientes simultáneamente mediante hilos.
* ✅ Finalizar la conexión escribiendo `exito`.

### Ejecución

**1. Iniciar el servidor:**

```bash
python server.py
```

**2. En otra terminal, iniciar el cliente:**

```bash
python client.py
```

**3. Escribir los mensajes que se quieran enviar.**

Para finalizar:

```text
exito
```

---

## 🛠️ Tecnologías utilizadas

* 🐍 Python
* 🔌 Sockets TCP/IP
* 🗄️ SQLite
* 🧵 Threading
* 💻 Cliente-servidor
* 📝 GitHub
