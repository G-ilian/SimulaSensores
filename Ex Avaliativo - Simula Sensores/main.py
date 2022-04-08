## Exercício avaliativo de S202 - Banco de Dados 2 - Simula Sensores 
import threading
import time 
import random
from db.bancodedados import Database

# Conectando com o BD
db=Database('bancoiot','sensores')

db.resetDatabase() # Usei para facilitar a visualização, caso necessário pode ser comentado

# Gerar valores de acordo com o pedido

def generate_values(nome,intervalo):
    while True:
        # Valores entre 30 e 40 (ºC) gerados de forma aleatória 
        valores=random.uniform(30,40)
        # Mostrando os dados do sensor e sua temperatura
        print(nome,valores)

        #Condição de parada do armazenamento de dados
        if(valores<38):
            db.create(nome,valores,'ºC',False) # Valores menores que 38 ºC não alarmam o sensor
        else:
            db.create(nome,valores,'ºC',True)
            print(f'Atenção! Temperatura muito alta! Verificar {nome}!') # Informando o sensor que está com alta temperatura
            break

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
