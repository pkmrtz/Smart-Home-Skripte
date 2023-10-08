import time
import board
import adafruit_dht
import socket

HOST = '82.165.66.189'
PORT = 5555
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
connected = False

def connect():
	global sock
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST, PORT))

while True:
	try:
		if connected == False:
			print("Connecting...")
			connect()
			connected = True
		temperature = dhtDevice.temperature
		humidity = dhtDevice.humidity
		print("temp:",temperature,"humid:",humidity)
		sock.sendall(str.encode(",".join([str(temperature), str(humidity)])))

	except RuntimeError as error:
		print(error.args[0])
		time.sleep(2)
		continue
	except Exception as error:
		print("Connection Error")
		connected = False
		sock.close()
		time.sleep(5)
		continue
	time.sleep(10)
