#coding: utf-8

#Dhyego Lancaster

import requests
from datetime import date
#aqui entra no site e captura os valores atualizados pela essa api
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,ETH-BRL")
requisicao_dic = requisicao.json()
#aqui seleciona a moeda e escolhe o campo bid da API
cotacao_dolar = requisicao_dic[f'USDBRL']['bid']
cotacao_euro = requisicao_dic[f'EURBRL']['bid']
cotacao_btc = requisicao_dic[f'BTCBRL']['bid']
cotacao_eth = requisicao_dic[f'ETHBRL']['bid']

#print(cotacao_euro,cotacao_euro,cotacao_btc,cotacao_eth)
#aqui voce manipula a data
data_atual = date.today()
data_atual = '{}/{}/{}'.format(data_atual.day, data_atual.month,data_atual.year)
#aqui vai imprimir na tela
print(f' Cotação de Moedas do dia {data_atual}:')
print(f' Dolar: {cotacao_dolar}')
print(f' Euro: {cotacao_euro}')
print(f' Bitcoin: {cotacao_btc}')
print(f' Etherium: {cotacao_eth}')
