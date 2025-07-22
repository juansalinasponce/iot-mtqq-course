import time
import paho.mqtt.client as paho
from paho import mqtt
from datetime import datetime

broker = "d877452fee134f5880b6c842de7aa98f.s1.eu.hivemq.cloud"
puerto = 8883
topico = "iot-class"
usuario = "jsalinas"
contrasena = "$Atokongo2025"

mensaje = f"Mensaje MQTT enviado por publisher | Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def on_connect(client, userdata, flags, reasonCode, properties=None):
    print("✅ Conectado al broker HiveMQ Cloud")
    client.publish(topico, payload=mensaje, qos=1)

def on_publish(client, userdata, mid, properties=None):
    print(f"📤 Mensaje publicado: {mensaje}")

def on_disconnect(client, userdata, disconnect_flags, reasonCode, properties=None):
    print(f"🔌 Desconectado. Código: {reasonCode}")

cliente = paho.Client(client_id="", protocol=paho.MQTTv5)
cliente.username_pw_set(usuario, contrasena)
cliente.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

cliente.on_connect = on_connect
cliente.on_publish = on_publish
cliente.on_disconnect = on_disconnect

cliente.connect(broker, puerto)
cliente.loop_start()
time.sleep(3)
cliente.loop_stop()
cliente.disconnect()