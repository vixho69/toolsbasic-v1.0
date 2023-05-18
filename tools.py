import time
import random
import string
import os
os.system("cls" if os.name == "nt" else "clear")
while True:
    print("tools v2")
    print("")
    print("ingresa (s/n) para volver en cada opcion!")
    print("[1] generador de contraseñas")
    print("[2] generador de codigos fakes")
    print("[3] pronto.")
    print("[4] pronto.")
    print("[5] salir.
    ss = int(input("ingresa: "))
    if ss == 1:
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            ss = string.ascii_letters + string.punctuation + string.digits
            dd = int(input("ingresa una cantidad (maxim 94): "))
            kk = "".join(random.sample(ss,dd))
            print(kk)
            jj = input("¿volver a generar?: ").lower()
            os.system("cls" if os.name == "nt" else "clear")
            if jj != "s":
                break
    elif ss == 2:
        os.system("cls" if os.name == "nt" else "clear")
        print("[1] codigos de roblox fakes")
        print("[2] codigos de activador de codigos de win10")
        ps = int(input("ingresa una opcion: "))
        if ps == 1:
            os.system("cls" if os.name == "nt" else "clear")
            while True:
                kk = int(input("¿cuantos quieres generar?: "))
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
                hh = input("¿quieres volver a generar?: ").lower()
                os.system("cls" if os.name == "nt" else "clear")
                if hh != "s":
                    break
        elif ss == 2:
            os.system("cls" if os.name == "nt" else "clear")
            while True:
                hd = int(input("¿cuantos codigos quieres generar?: "))
                for t in range(hd):
                    rt = string.digits + string.ascii_uppercase
                    pp = 5
                    kl = "-"
                    kd = "".join(random.sample(rt,pp))
                    k1 = "".join(random.sample(rt,pp))
                    k2 = "".join(random.sample(rt,pp))
                    k3 = "".join(random.sample(rt,pp))
                    k4 = "".join(random.sample(rt,pp))
                    print(f"{kd}{kl}{k1}{kl}{k2}{kl}{k3}{kl}{k4}")
                jt = input("quieres volver a generar?: ").lower()
                os.system("cls" if os.name == "nt" else "clear")
                if jt != "s":
                    break
    elif ss == 3:
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            print("pronto.")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            print("esperando.")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
            break

    elif ss == 4:
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            print("pronto.")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            print("esperando.")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
            break
     elif ss == 5:
          print()
          os.system("cls" if os.name == "nt" else "clear")
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("opcion invalida.")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        print("esperando.")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
