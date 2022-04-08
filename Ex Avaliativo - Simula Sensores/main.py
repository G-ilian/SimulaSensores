## Exercício avaliativo de S202 - Banco de Dados 2 - Simula Sensores 
import threading
import time 
import random
from db.bancodedados import Database

# Conectando com o BD
db=Database('bancoiot','sensores')
db.resetDatabase()

# Gerar valores
def generate_values(nome,intervalo):
    while True:
        valores=random.uniform(30,40)
        print(nome,valores)
        db.create(nome,valores,'false')
        time.sleep(intervalo)

#Função usada para criar threads        
def thread(target,nome,t):
    return threading.Thread(target=target,args=(nome,t))
# Verificar de tirar a repetição de códigos
sensor1=thread(generate_values,'Sensor 1',2)
sensor2=thread(generate_values,'Sensor 2',2)
sensor3=thread(generate_values,'Sensor 3',2)

# Inicializando as threads
sensor1.start()
sensor2.start()
sensor3.start()
