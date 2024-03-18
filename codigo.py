#PROJETO DE AUTOMAÇÃO
import pyautogui
import time

#pesquisar o e-mail automaticamente

pyautogui.PAUSE = 3
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
pyautogui.PAUSE = 6

pyautogui.write("conta gmail")
pyautogui.PAUSE = 5
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=1789, y=220)

pyautogui.write("lanacaroline.1150@gmail.com")
pyautogui.press("enter")
pyautogui.PAUSE = 3
pyautogui.write("roseane453677")
pyautogui.press("enter")
import pandas
tabela = pandas.read_csv("dadoscolaboradores.csv")
print(tabela)

