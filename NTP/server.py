from asyncio import threads
import socket
import threading
import datetime

DATA_PAYLOAD = 2048

def server(host='localhost', port=8082):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    print ("Iniciando servidor na porta %s %s" %server_address)
    sock.bind(server_address)
    sock.listen(5)
    while True:
        print ("Esperando mensagem do cliente")
        client, address = sock.accept()
        thread = threading.Thread(target=serverThread, args=(client,))
        thread.start()
        
def serverThread(client):
    data = client.recv(DATA_PAYLOAD)
    if data:
        data = data.decode()
        if data == "date":
            data = getDate()
        elif data == "time":
            data = getTime()
        elif data == "date-time":
            data = getDate()+','+getTime()
        client.send(data.encode('UTF-8'))
        client.close()

def getTime():
    now = datetime.datetime.now()
    hour = str(now.hour)
    minute = str(now.minute)
    second = str(now.second)
    if len(hour) < 2:   
        hour = '0'+hour
    elif len(minute) < 2:
        minute = '0'+minute
    elif len(second) < 2:
        second = '0'+second
    return hour+':'+minute+':'+second

def getDate():
    now = datetime.datetime.now()
    day = str(now.day)
    month = str(now.month)
    year = str(now.year)
    if len(day) < 2:   
        day = '0'+day
    elif len(month) < 2:
        month = '0'+month
    elif len(year) < 2:
        year = '0'+year
    return day+'-'+month+'-'+year

server()