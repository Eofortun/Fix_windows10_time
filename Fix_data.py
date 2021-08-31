import requests
import os
import json
from time import sleep

#Leia o README.md para alterar seu fuso/localização
url = f"http://worldtimeapi.org/api/timezone/America/Maceio"

#Faz a requisição no Worldtimeapi.org
dados_json = requests.get(url)


#Mostra o json completo
#print(dados_json.text)

#carrega o arquivo como json para que possa ser manuseado
All = json.loads(dados_json.text)

'''

Exmplo de string: datetime = "datetime":"2021-08-28T14:06:03.641040-03:00"

'''

#Inverte a string do intervalo [0:10] com [::-1]
data = ((All['datetime'][0:10])[::-1])

#Manuseia a string obtida com json para obter os valores do intervalo [11:19]
hora = All['datetime'][11:19]

#Formata a data: yyyy/mm/dd, para dd/mm/yyyy.
form_data = (data[0:2])[::-1] + '/' +(data[3:5])[::-1] + '/' + (data[6:10])[::-1]
print(f"Data:{form_data}\nHora:{hora}")


sleep(2)
#Altera data do sistema.
os.system("date " + form_data)

sleep(2)
#Altera a hora.
os.system("time " + hora)


#BASEADO EM https://lecram.tumblr.com/post/2952089335/relogio-windows
