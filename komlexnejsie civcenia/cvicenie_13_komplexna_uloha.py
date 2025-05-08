
def vypocitaj_obrat(objednavky):
    celkovy_obrat = 0
    for objednavka in objednavky:
        obrat = objednavka["cena"] * objednavka["mnozstvo"]
        celkovy_obrat += obrat
    return celkovy_obrat

def ziskaj_predaje_podla_produkta(objednavky):
    objednane_mnozstvo = {}
    for objednavka in objednavky:
        produkt = objednavka["produkt"]
        mnozstvo = objednavka["mnozstvo"]
        if produkt in objednane_mnozstvo:
            objednane_mnozstvo[produkt] += mnozstvo
        else:
            objednane_mnozstvo[produkt] = mnozstvo
    return objednane_mnozstvo

def najpredavanejsi_produkt(predaje_dict):
    max_predanych_kusov = 0
    produkt_max = None
    for produkt in predaje_dict:
        if predaje_dict[produkt] > max_predanych_kusov:
            max_predanych_kusov = predaje_dict[produkt]
            produkt_max = produkt
    return max_predanych_kusov, produkt_max

def print_vysledky(obrat, predaje, naj_kusy, naj_produkt):
    print(f"Celkový obrat je: {obrat}€")
    print("Predané množstvá podľa produktov:")
    for produkt, kusy in predaje.items():
        print(f" - {produkt}: {kusy} ks")
    print(f"Najpredávanejší produkt je {naj_produkt} s počtom {naj_kusy} ks")

def main():
    objednavky = [
        {"produkt": "Tricko", "cena": 20, "mnozstvo": 2},
        {"produkt": "Mikina", "cena": 40, "mnozstvo": 1},
        {"produkt": "Tricko", "cena": 20, "mnozstvo": 1},
        {"produkt": "Nohavice", "cena": 50, "mnozstvo": 1},
        {"produkt": "Tricko", "cena": 20, "mnozstvo": 3},
        {"produkt": "Mikina", "cena": 40, "mnozstvo": 2},
    ]

    obrat = vypocitaj_obrat(objednavky)
    predaje = ziskaj_predaje_podla_produkta(objednavky)
    naj_kusy, naj_produkt = najpredavanejsi_produkt(predaje)

    print_vysledky(obrat, predaje, naj_kusy, naj_produkt)

if __name__ == "__main__":
    main()
