import json
import paho.mqtt.client as paho
from paho import mqtt
import mysql.connector
from datetime import datetime

# Configuración MQTT
broker = "d877452fee134f5880b6c842de7aa98f.s1.eu.hivemq.cloud"
puerto = 8883
topico = "sensores"
usuario_mqtt = "jsalinas"
contrasena_mqtt = "$Atokongo2025"

# Configuración base de datos MySQL
db_config = {
    "host": "195.179.239.0",
    "user": "u349685578_admin",
    "password": "@Atokongo2025",
    "database": "u349685578_clases"
}

# Conectar a la base de datos
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Callback de conexión
def on_connect(client, userdata, flags, reasonCode, properties=None):
    print("✅ Conectado al broker HiveMQ Cloud")
    client.subscribe(topico, qos=1)

# Callback de mensaje
def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())

        sql = (
            "INSERT INTO lecturas_sensores ("
            "device_id, usuario, timestamp_utc, latitude, longitude, altitude, "
            "tipo_sensor, temperature_c, humidity_percent, battery_level, status"
            ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )

        values = (
            payload.get("device_id"),
            payload.get("usuario"),
            payload.get("timestamp"),
            payload["location"].get("latitude"),
            payload["location"].get("longitude"),
            payload["location"].get("altitude"),
            payload.get("type"),
            payload["readings"].get("temperature_c"),
            payload["readings"].get("humidity_percent"),
            payload.get("battery_level"),
            payload.get("status")
        )

        cursor.execute(sql, values)
        conn.commit()
        print("✅ Datos insertados en la base de datos")

    except Exception as e:
        print(f"❌ Error al procesar/insertar mensaje: {e}")

# Callback de desconexión
def on_disconnect(client, userdata, disconnect_flags, reasonCode, properties=None):
    print(f"🔌 Desconectado del broker. Código: {reasonCode}")

# Cliente MQTT
cliente = paho.Client(client_id="", protocol=paho.MQTTv5)
cliente.username_pw_set(usuario_mqtt, contrasena_mqtt)
cliente.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

cliente.on_connect = on_connect
cliente.on_message = on_message
cliente.on_disconnect = on_disconnect

# Iniciar conexión
cliente.connect(broker, puerto)
cliente.loop_forever()