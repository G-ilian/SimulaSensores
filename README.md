<h1 align ="center">Exercício Avaliativo de S202 - Simula sensores</h1>

<p align="center">
<img src="https://github.com/G-ilian/SimulaSensores/blob/main/python%2Bmongo_logo.jpg" height="300" width="500" >
</p>

<p>Aplicação de caráter simples desenvolvida para a disciplina de S202, para implementar os conceitos de bancos orientados a documentos</p>

- Projeto

<p>Totalmente desenvolvida em Python.Com persistência de dados feita através do MongoDB Atlas, que é um banco orientado a documentos.</p>
<p>A aplicação utilizasse dos conceitos de threads, de forma que estas servirão para simular sensores de temperuta, que estão a cada 2 segundos gerando dados sobre a temperatura do ambiente e armazenando tais dados dentro de um banco de dados, caso essa temperatura exceda os 38ºC a leitura do sensor que teve tal leitura é parada e o sistema prossegue leitura nos outros sensores.</p>

### 📋 Pré-requisitos para execução
- Visual Studio Code ou PyCharm
- MongoDB


### 🚀 Começando
Para obter uma cópia do projeto a fim de operá-lo/testá-lo em sua máquina,clone o repositório em uma pasta na sua máquina:

```
git clone git@github.com:G-ilian/SimulaSensores.git
```

### 🔧 Instalação e Configuração do BD
<p>Após ter clonado o projeto em seu computador, acesse uma IDE de sua opção, desde que esta tenha suporte para a linguagem Python, e abra a pasta onde você clonou o repositório, dentro dessa IDE abra o terminal e execute os seguintes passos: </p>

- Para executar o projeto é de suma importância estar na pasta de raiz do mesmo, caso você tenha aberto o projeto na pasta de raiz "Ex Avaliativo - Simula Sensores", desconsidere este passo. Agora se você não estiver na pasta de raiz execute o seguinte comando no terminal: 
    
```
cd "Ex Avaliativo - Simula Sensores"
``` 

- Estando na pasta raiz do projeto e com o terminal aberto, instale as bibliotecas que são pré requisitos para executar o código, isto pode ser feito através do seguinte comando :

```
pip install -r requirements.txt
```

Obs: Sugiro a criação de uma venv e sua ativação para que você isole seu sistema operacional do projeto, após estar com a venv ativada execute o comando anteriormente mostrada.

- :floppy_disk: Configuração do banco de dados
<p>A estrutura de pastas do projeto, ficou da seguinte maneira: </p>


    📂 Ex Avaliativo - Simula Sensores/
        📂db/
            📄bancodedados.py
        📄main.py

Para configurar seu banco de dados, acesse a pasta db, e entre no arquivo bancodedados.py, neste momento terá a presença de uma classe e uma função mais abaixo que faz a inicialiazação desta, e um escrito "url_do_seu_banco", substitua aqui a url de seu MongoDB Atlas, lembrando que este tem que ser gerado e compativel com suas configurações de python.

# ▶️ Execução
<p>Passado estes passos iniciais, você já pode executar o projeto para ver seu funcionamento, estando na pasta de raiz e no terminal dê o seguinte comando</p>

```
python main.py
```

## ✒️ Autor

***Gabriel Ilian Fonseca Barboza*** - [Gabriel](https://github.com/G-ilian)