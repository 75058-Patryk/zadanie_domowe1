droga = input("podaj drogę przejechaną autem")
sr_spalanie = input("podaj sr_spalanie auta (l/100km)")
zuzycie_paliwa =int(droga)//int(sr_spalanie)
print("przewidywanie zuzycie paliwa wynosi:",zuzycie_paliwa,"L oraz przewidywane koszty podrozy wynosza",6.5*zuzycie_paliwa)