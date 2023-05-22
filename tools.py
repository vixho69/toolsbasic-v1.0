import time
import random
import string
import os
os.system("cls" if os.name == "nt" else "clear")
while True:
    print("Tools v1.0")
    print("")
    print("Ingresa (s/n) para volver en cada opcion!")
    print("[1] Generador de contraseñas")
    print("[2] Generador de codigos fakes")
    print("[3] Generador de numeros random")
    print("[4] Pronto.")
    print("[5] Salir.")
    ss = int(input("Ingresa: "))
    if ss == 1:
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            ss = string.ascii_letters + string.punctuation + string.digits
            dd = int(input("Ingresa una cantidad (maxim 94): "))
            kk = "".join(random.sample(ss,dd))
            print(kk)
            jj = input("¿Volver a generar?: ").lower()
            os.system("cls" if os.name == "nt" else "clear")
            if jj != "s":
                break
    elif ss == 2:
        os.system("cls" if os.name == "nt" else "clear")
        print("[1] Codigos de roblox fakes")
        print("[2] Codigos de activador de codigos de win10")
        ps = int(input("Ingresa una opcion: "))
        if ps == 1:
            os.system("cls" if os.name == "nt" else "clear")
            while True:
                kk = int(input("¿Cuantos quieres generar?: "))
                for gg in range(kk):
                    ss = string.digits
                    os1 = 3
                    os2 = 2
                    os3 = 1
                    os4 = 3
                    os5 = 1
                    sp = "-"
                    op1 = "".join(random.sample(ss,os1))
                    op2 = "".join(random.sample(ss,os2))
                    op3 = "".join(random.sample(ss,os3))
                    op4 = "".join(random.sample(ss,os4))
                    op5 = "".join(random.sample(ss,os5))
                    print(f"{op1}{sp}{op2}{sp}{op3}{sp}{op4}{sp}{op5}")
                hh = input("¿Quieres volver a generar?: ").lower()
                os.system("cls" if os.name == "nt" else "clear")
                if hh != "s":
                    break
        elif ss == 2:
            os.system("cls" if os.name == "nt" else "clear")
            while True:
                hd = int(input("¿Cuantos codigos quieres generar?: "))
                for t in range(hd):
                    rt = "23456789" + "QWRTYPDFGHJKXCVBNM"
                    pp = 5
                    kl = "-"
                    kd = "".join(random.sample(rt,pp))
                    k1 = "".join(random.sample(rt,pp))
                    k2 = "".join(random.sample(rt,pp))
                    k3 = "".join(random.sample(rt,pp))
                    k4 = "".join(random.sample(rt,pp))
                    print(f"{kd}{kl}{k1}{kl}{k2}{kl}{k3}{kl}{k4}")
                jt = input("Quieres volver a generar?: ").lower()
                os.system("cls" if os.name == "nt" else "clear")
                if jt != "s":
                    break  
    elif ss == 3:
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("Generador de numeros fakes")
            print("")
            print("[1] Numeros chilenos.")
            print("[2] pronto.")
            print("")
            fd = int(input("ingresa una opcion: "))
            if fd == 1:
                po = int(input("Cuantos numeros deseas generar?: "))
                for h in range(po):
                    y = string.digits
                    j = 4
                    ks = "+56 9 "
                    kp = " "
                    k = "".join(random.sample(y,j))
                    k1 = "".join(random.sample(y,j))
                    print(f"{ks}{k}{kp}{k1}")
                jq = input("Quieres volver a generar?: ").lower()
                os.system("cls" if os.name == "nt" else "clear")
                if jq != "s":
                    break
            elif fd == 2:
                os.system("cls" if os.name == "nt" else "clear")
                print("pronto.")
                time.sleep(2)
                os.system("cls" if os.name == "nt" else "clear")
                break
    elif ss == 4:
        os.system("cls" if os.name == "nt" else "clear")
        print("pronto.")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        print("esperando.")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
    elif ss == 5:
        os.system("cls" if os.name == "nt" else "clear")
        print("Adios!")
        break
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("opcion invalida.")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        print("esperando.")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
