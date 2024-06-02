import datetime
import time
import sys
import threading
from pythonosc import dispatcher, osc_server
import logging
import time 

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

# Función para verificar la hora
def verificar_hora():
    # Definir la hora objetivo
    hora_objetivo = datetime.time(12, 10, 50)
    hora_apagado = datetime.time(19, 50, 50)
    while True:
        # Obtén la hora actual
        ahora = datetime.datetime.now().time()

        # Imprime la hora actual
        #print("Hora actual:", ahora)

        # Comparar la hora actual con la hora objetivo
        if ahora.hour == hora_objetivo.hour and ahora.minute == hora_objetivo.minute and ahora.second == hora_objetivo.second:
            print("¡Es exactamente las 22:03:50 horas!")
            ws.call(requests.StartStream())
            #break
        elif ahora.hour == hora_apagado.hour and ahora.minute == hora_apagado.minute and ahora.second == hora_apagado.second:
        # Esperar un segundo antes de verificar nuevamente
            print("Se apaga el streaming")
            ws.call(requests.StopStream())
        time.sleep(1)

# Llamar a la función para iniciar la verificación
verificar_hora()
