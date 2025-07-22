import paho.mqtt.client as paho
from paho import mqtt

broker = "d877452fee134f5880b6c842de7aa98f.s1.eu.hivemq.cloud"
puerto = 8883
topico = "iot-class"
usuario = "jsalinas"
contrasena = "$Atokongo2025"

def on_connect(client, userdata, flags, reasonCode, properties=None):
    print("✅ Conectado al broker HiveMQ Cloud")
    client.subscribe(topico, qos=1)

def on_message(client, userdata, msg):
    print(f"📥 Mensaje recibido en {msg.topic}: {msg.payload.decode()}")

def on_disconnect(client, userdata, disconnect_flags, reasonCode, properties=None):
    print(f"🔌 Desconectado. Código: {reasonCode}")

cliente = paho.Client(client_id="", protocol=paho.MQTTv5)
cliente.username_pw_set(usuario, contrasena)
cliente.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

cliente.on_connect = on_connect
cliente.on_message = on_message
cliente.on_disconnect = on_disconnect

cliente.connect(broker, puerto)
cliente.loop_forever()