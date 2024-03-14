import socket 
import sys 

target = input("inserisci l'indirizzo ip da scansire: ")
portrange = input("Inserisci il range di porte da scansire: ")

lowport = int(portrange.split('-')[0])
highport = int(portrange.split('-')[1])

print("Scansisco l'host: ", target ,"dalla porta: ", lowport ,"alla porta: ", highport)
status_precedente = 0
for port in range(lowport, highport +1):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(1)
	if (status_precedente != 0):
		sys.stdout.write("\033[A")
		sys.stdout.write("\033[K")
		status_precedente = 0
	
	status = s.connect_ex((target,port))
	if (status == 0):
		print('*** Porta', port, "-APERTA ***")
	else:
		print("Porta", port, "-CHIUSA", status)
		status_precedente = status
	s.close()


