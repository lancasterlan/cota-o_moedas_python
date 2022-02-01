#coding: utf-8

#Dhyego Lancaster
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
import pandas as pd

#wa.me/5562982382773
contatos_df = pd.read_excel('enviar.xlsx')
print(contatos_df)
navegador = webdriver.Edge()
navegador = get('http://web.whatsapp.com')

while len(navegador.find_elements_by_id('isde')) < 1:
    time.sleep(1)

for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, 'Pessoa']
    numero = contatos_df.loc[i, 'Numero']
    texto = urllib.parse.quote(f'Oi {pessoa}! {mensagem}')
    link = f'http://web.whatsapp.com/send?phone+{numero}%text+{texto}'
    navegador.get(link)
    while len(navegador.find_elements_by_id('isde')) < 1:
        time.sleep(1)
    navegador.find_elements_by_xpath('colocar o xpath//*[@id="main"]/footer/div[1]/div[2]/div').send_keys(Keys.ENTER)
    time.sleep(10)