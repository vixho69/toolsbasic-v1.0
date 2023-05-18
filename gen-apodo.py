import random
import os
os.system("cls" if os.name == "nt" else "clear")
while True:
    print("idea realizada por ale")
    dd = int(input("¿cuantas veces quieres mesclar el apodo?: "))
    gg = int(input("¿cuantas veces quieres repetir?: "))
    os.system("cls" if os.name == "nt" else "clear")
    for gg in range(gg):
        ss = ["pablito","tutoxica","uwu","123","owo","lul","ola","pato",":O","noc","yokse","XD","X","D","paz","eso","tilin","gato","ye","a","O","o"]
        print("")
        ks = "".join(random.sample(ss, dd))
        print(f"{ks}\n")
    print("¿quieres volver a generar?")
    jh = input("ingresa (s/n): ").lower()
    os.system("cls" if os.name == "nt" else "clear")
    if jh != "s":
        print("adios!")
        break
