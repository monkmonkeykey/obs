import sys
import threading
from pythonosc import dispatcher, osc_server
import logging
import time 
# Configuración del logging
logging.basicConfig(level=logging.DEBUG)

# Importar obswebsocket
sys.path.append('../')
from obswebsocket import obsws, requests  # noqa: E402

# Configuración de la conexión con OBS
host = "192.168.1.33"
port = 4455
password = "mafufi"

ws = obsws(host, port, password)
ws.connect()
time.sleep(5)
ws.call(requests.StartStream())
time.sleep(5)
ws.disconnect()
