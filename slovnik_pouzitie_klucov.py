# ----------------------------------------
# Úloha: Zaradenie filmov podľa žánru
# Cieľ: pochopiť správne používanie pevných kľúčov vs. premenných v slovníkoch
# ----------------------------------------

# Máme zoznam filmov, kde každý film je slovník so záznamom o názve a žánri
filmy = [
    {"nazov": "Inception", "zaner": "sci-fi"},
    {"nazov": "Titanic", "zaner": "romantika"},
    {"nazov": "Matrix", "zaner": "sci-fi"},
    {"nazov": "La La Land", "zaner": "muzikal"},
    {"nazov": "Notebook", "zaner": "romantika"}
]

# Vytvoríme prázdny slovník, kde budeme filmy ukladať podľa ich žánru
filmy_podla_zanru = {}

# Prechádzame každý film v zozname "filmy"
for film in filmy:
    # Vytiahneme hodnotu pre kľúč "zaner" - teda aký žáner má tento film
    # Používame pevný kľúč "zaner" v úvodzovkách, pretože presne vieme, že také pole existuje
    zaner = film["zaner"]        # napr. "sci-fi"
    
    # Vytiahneme aj názov filmu z pevného kľúča "nazov"
    nazov = film["nazov"]         # napr. "Inception"

    # Teraz chceme uložiť názov filmu do správnej kategórie (žánru)
    # POZOR: teraz už nepíšeme "zaner" (pevný text), ale používame hodnotu premennej zaner
    # lebo "zaner" bude meniť svoju hodnotu ("sci-fi", "romantika", "muzikal" atď.)

    # Skontrolujeme, či už tento žáner existuje v slovníku
    if zaner in filmy_podla_zanru:
        # Ak žáner existuje, pridáme názov filmu do existujúceho zoznamu pre tento žáner
        filmy_podla_zanru[zaner].append(nazov)
    else:
        # Ak žáner ešte neexistuje, vytvoríme nový záznam:
        # nastavíme kľúč (hodnota v premennej zaner) na nový zoznam obsahujúci tento názov filmu
        filmy_podla_zanru[zaner] = [nazov]

# Po ukončení cyklu vypíšeme výsledný slovník
# kde:
# - kľúčom je žáner ("sci-fi", "romantika", "muzikal")
# - hodnotou je zoznam názvov filmov v tomto žánri
print(filmy_podla_zanru)