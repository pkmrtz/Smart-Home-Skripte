import time
import board
import adafruit_dht
import socket
import ssl

HOST = 'dddrey.info'
PORT = 1337
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

def connect():
	print("Connecting...")
	global sock, wrappedSocket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	wrappedSocket = ssl.create_default_context().wrap_socket(sock,server_hostname=HOST)
	wrappedSocket.connect((HOST, PORT))

while True:
	try:
		connect()
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
		wrappedSocket.close()
		time.sleep(5)
		continue
	time.sleep(10)
