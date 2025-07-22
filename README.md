# Ejemplo de Conexión MQTT con Python (Publicador y Suscriptor)

Este proyecto muestra cómo conectar un cliente **MQTT** en Python utilizando el broker gratuito de `test.mosquitto.org`, mediante el uso de los scripts `publisher.py` y `subscriber.py`.

---

## 📦 Requisitos

- Python 3.7 o superior
- Visual Studio Code (opcional pero recomendado)
- pip
- Biblioteca `paho-mqtt`

---

## 🧪 Crear entorno virtual (Windows y macOS)

### 🪟 En **Windows**:

```bash
python -m venv env
env\Scripts\activate
```

### 🍎 En **Mac (macOS)** o Linux:

```bash
python3 -m venv env
source env/bin/activate
```

---

## 🧠 Activar entorno virtual en **Visual Studio Code**

1. Abre la carpeta del proyecto en VS Code.
2. Presiona `Ctrl + Shift + P` (Windows) o `Cmd + Shift + P` (Mac).
3. Escribe `Python: Select Interpreter` y selecciona el que diga `./env/bin/python` o similar.
4. Si no aparece, reinicia VS Code o asegúrate de haber activado el entorno antes de abrirlo.

---

## 📥 Instalar dependencias

Con el entorno virtual activado, ejecuta:

```bash
pip install paho-mqtt
```

---

## 🚀 Ejecutar los scripts

### ✅ 1. Inicia el suscriptor:

```bash
python subscriber.py
```

Deberías ver un mensaje como:

```
📡 Conectado al broker MQTT
```

### ✅ 2. En otra terminal, ejecuta el publicador:

```bash
python publisher.py
```

Y deberías ver:

```
📤 Mensaje publicado: 'Mensaje desde el publicador MQTT en el tópico iot-class'
```

El suscriptor mostrará el mensaje recibido automáticamente.

---

## 🧪 Tópico utilizado

Ambos scripts utilizan el tópico: `iot-class`.

---

## 📚 Créditos

Creado como ejemplo educativo para clases de Arquitectura IoT con Python y MQTT.