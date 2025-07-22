import paho.mqtt.client as mqtt

broker = "test.mosquitto.org"
puerto = 8080
topico = "iot-class"

# Callback para conexión
def on_connect(client, userdata, flags, reasonCode, properties):
    print("📡 Conectado al broker MQTT por WebSocket")
    client.subscribe(topico)

# Callback para mensaje recibido
def on_message(client, userdata, msg):
    print(f"📥 Mensaje recibido en {msg.topic}: {msg.payload.decode()}")

# Callback para desconexión (API v2 requiere 5 argumentos)
def on_disconnect(client, userdata, disconnect_flags, reasonCode, properties):
    print(f"🔌 Desconectado del broker. Código: {reasonCode}")

# Crear cliente con API moderna y WebSocket
cliente = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, transport="websockets")
cliente.on_connect = on_connect
cliente.on_message = on_message
cliente.on_disconnect = on_disconnect

# Conectar y escuchar
cliente.connect(broker, puerto, keepalive=60)
cliente.loop_forever()
