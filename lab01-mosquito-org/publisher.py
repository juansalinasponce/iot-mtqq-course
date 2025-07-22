import paho.mqtt.client as mqtt
import time
from datetime import datetime

broker = "test.mosquitto.org"
puerto = 1883
topico = "iot-class"

# Obtener fecha y hora actual
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
mensaje = f"Mensaje MQTT desde Juan por puerto 1883 | Enviado: {timestamp}"

# Crear cliente con API moderna
cliente = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Callback conexión exitosa
def on_connect(client, userdata, flags, reasonCode, properties):
    if reasonCode == 0:
        print("✅ Conectado exitosamente al broker.")
        client.publish(topico, mensaje)
        print(f"📤 Mensaje publicado: {mensaje}")
    else:
        print(f"⚠️ Error en conexión: código {reasonCode}")

# Callback desconexión
def on_disconnect(client, userdata, disconnect_flags, reasonCode, properties):
    print(f"🔌 Desconectado del broker. Código: {reasonCode}")

cliente.on_connect = on_connect
cliente.on_disconnect = on_disconnect

try:
    cliente.connect(broker, puerto, keepalive=60)
    cliente.loop_start()
    time.sleep(3)
    cliente.loop_stop()
    cliente.disconnect()
except Exception as e:
    print(f"❌ Error al conectar: {e}")
