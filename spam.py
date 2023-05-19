import pyautogui as gui
import time
import os
os.system("cls" if os.name == "nt" else "clear")
print("este script es para spamear pero debes estar en una app ya que se encarga de escribir lo que quieres")
time.sleep(5)
os.system("cls" if os.name == "nt" else "clear")
print("[1] continuar")
print("[2] terminar")
ss = int(input("ingresa una opcion: "))
os.system("cls" if os.name == "nt" else "clear")
if ss == 1:
    dd = input("ingresa lo que quieres spamear: ")
    jj = int(input("¿cuantas veces quieres repetir?: "))
    hh = int(input("y cuantas veces quieres que se demore en enviar (recomendado 1)"))
    os.system("cls" if os.name == "nt" else "clear")
    print("comenzamos en 10...")
    time.sleep(10)
    os.system("cls" if os.name == "nt" else "clear")
    for gg in range(jj):
        gui.write("dd")
        time.sleep(hh)
        gui.press("enter")
elif ss == 2:
    print()
