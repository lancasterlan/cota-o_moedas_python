#coding: utf-8

#Dhyego Lancaster

import pyautogui
import time

#no site do pyautogui tem todas as funçoes
#o computador nao pode mexer, deixar o codigo rodar
#abrir o windows
#pyautogui.alert('Lancaster, O codigo vai rodar, NÃO MEXE NO COMPUTADOR!')
#tempo para cada operação
pyautogui.PAUSE = 0.5
pyautogui.press('winleft')
pyautogui.write('edge')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')
pyautogui.hotkey('winleft', 'e')
#comando que buscar posição do mouse, use notebook jupyter
#pyautogui.position()
pyautogui.moveTo(909, 290)
pyautogui.mouseDown()
pyautogui.press('enter')
pyautogui.moveTo(844, 201)
pyautogui.mouseDown()
pyautogui.moveTo(407, 629)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.mouseUp()
pyautogui.alert('COMPUTADOR, liberado!')
#tempo para cada operação