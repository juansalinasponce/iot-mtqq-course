import time
import json
import random
from datetime import datetime
import paho.mqtt.client as paho
from paho import mqtt

# Configuración del broker
broker = "d877452fee134f5880b6c842de7aa98f.s1.eu.hivemq.cloud"
puerto = 8883
topico = "sensores"
usuario = "jsalinas"
contrasena = "$Atokongo2025"

# Callbacks
def on_connect(client, userdata, flags, reasonCode, properties=None):
    print("✅ Conectado al broker HiveMQ Cloud")

def on_publish(client, userdata, mid, properties=None):
    print(f"📤 Mensaje enviado correctamente. mid={mid}")

def on_disconnect(client, userdata, disconnect_flags, reasonCode, properties=None):
    print(f"🔌 Desconectado del broker. Código: {reasonCode}")

# Cliente MQTT
cliente = paho.Client(client_id="", protocol=paho.MQTTv5)
cliente.username_pw_set(usuario, contrasena)
cliente.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

cliente.on_connect = on_connect
cliente.on_publish = on_publish
cliente.on_disconnect = on_disconnect

cliente.connect(broker, puerto)
cliente.loop_start()

# Bucle de publicación simulada
try:
    while True:
        # Generar datos simulados
        payload = {
            "device_id": "sensor-001",
            "usuario": "juan.salinas",
            "timestamp": datetime.utcnow().isoformat(),
            "location": {
                "latitude": round(random.uniform(-12.05, -12.00), 6),
                "longitude": round(random.uniform(-77.05, -77.00), 6),
                "altitude": round(random.uniform(150, 200), 1)
            },
            "type": "temperature_humidity",
            "readings": {
                "temperature_c": round(random.uniform(20, 30), 2),
                "humidity_percent": round(random.uniform(40, 80), 2)
            },
            "battery_level": random.randint(20, 100),
            "status": random.choice(["active", "idle", "offline"])
        }

        # Publicar el mensaje como JSON
        mensaje = json.dumps(payload)
        cliente.publish(topico, payload=mensaje, qos=1)
        print(f"📤 Enviado a '{topico}': {mensaje}")

        time.sleep(5)  # Espera 5 segundos entre mensajes

except KeyboardInterrupt:
    print("🛑 Publicador detenido por el usuario.")

finally:
    cliente.loop_stop()
    cliente.disconnect()
