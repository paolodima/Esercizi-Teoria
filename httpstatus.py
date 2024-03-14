import http.client

host = input("Inserire host/ip del sistema target: ")
port = input("Inserire la porta del sistema target: ")

if (port == ""):
	port = 80
	
else: port = int(port)

try:
	connection = http.client.HTTPConnection(host,port)
	connection.request("OPTIONS", "/")
	response = connection.getresponse()
	print("Lo status è: " , response.status)
	connection.close()
except ConnectionRefusedError:
	print("Connessione Fallita")
