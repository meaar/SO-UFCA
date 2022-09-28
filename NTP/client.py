import socket

DATA_PAYLOAD = 2048

def client(host='localhost', port=8082):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print ("Conectando %s porta %s" %server_address)
    sock.connect(server_address)
    try:
        started = True
        while started:
            print("Digite o número correspondente as opções abaixo")
            message = input("[1] Data\n[2] Hora\n[3] Data e Hora\n[4] Fechar\n")
            if message == '1':
                message = "date"
                started = False
            elif message == '2':
                message = "time"
                started = False
            elif message == '3':
                message = "date-time"
                started = False
            elif message == '4':
                started = False
                return sock.close()
            else:
                print("Opção inválida")
        print ("Enviando %s" %message)
        sock.sendall(message.encode('UTF-8'))
        data = sock.recv(DATA_PAYLOAD)
        print("Recebido %s" %str(data.decode()))
    except socket.error as e:
        print ("Socket error: %s" %str(e))
    except Exception as e:
        print ("Other exception: %s" %str(e))
    finally:
        print ("Closing connection to the server")
        sock.close()

client()