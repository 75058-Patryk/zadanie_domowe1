import random
droga = random.randint(1,1000)
sr_spalanie = input("podaj sr_spalanie auta (l/100km)")
cena_paliwa = float(input("podaj cene paliwa na stacji cpn"))
zuzycie_paliwa =int(droga)//int(sr_spalanie)
print("przewidywanie zuzycie paliwa wynosi:",zuzycie_paliwa,"L oraz przewidywane koszty podrozy wynosza",cena_paliwa*zuzycie_paliwa)