from random import randint, choice
import time

name = input("Podaj imie swojego wojownika: ")
life = 100
mana = 100
zbroja = 5
doswiadczenie = 1000
zloto = 1000

def atak_mieczem():
    return randint(5, 10)

def zaklecie():
    global mana
    if mana < 5:
        print("Nie masz wystarczajacej ilosci many! ")
        return 0
    mana -= 10
    return randint(10, 15)

sila_ataku = atak_mieczem()
sila_zaklecia = zaklecie()

def opoznienie(czas):
    time.sleep(czas)

def menu_glowne():
    print(f"\nWitaj {name}! Jestes gotowy na nowe wyzwania?")
    print("1 - Walcz!")
    print("2 - Misje")
    print("3 - Zobacz swoj ekwipunek")
    print("4 - Ulepsz swojego wojownika")
    print("5 - Sklep")
    print("6 - Opusc gre")

def pokaz_misje():
    print("\nMisje do wykonania: ")
    print("1 - Pokonac zlowrogiego czarnoksieznika (Nagroda: 50xp, 50 zlota)")
    print("2 - Zabic smoka (Nagroda: 70 xp, 100 zlota)")
    print("3 - Zatrzymac trolla przed zniszczeniem wioski (Nagroda: 20xp, 20 zlota)")
    print("4 - Zabic zombie, aby zapobiec apokalipsie (Nagroda: 40xp, 80 zlota)")
    print("5 - Powstrzymac demona przed opetaniem mieszkancow wioski (Nagroda: 100xp , 200 zlota)")
    print("6 - Zabic weza (Nagroda: 10xp, 10 zlota)")
    print("7 - Powrot do menu")

def wybierz_rodzaj_ataku():
    print('a/A - Wykonaj atak mieczen')
    print('b/B - Rzuc potezne zaklecie!')
    x = input().upper()
    if x == 'A':
        return atak_mieczem()
    elif x == 'B':
         return zaklecie()
    else:
        print("Nie wybrano akcji!")
        return 0

def random_opponent():
    przeciwnicy = [
        ["Czarnoksieznik", 30, 7, 10, 10],
        ["Smok", 45, 10, 15, 20],
        ["Troll", 20, 5, 10, 15],
        ["Zombie", 15, 5, 10, 5],
        ["Ork", 25, 15, 15, 10],
        ["Demon", 50, 15, 30, 50],
        ["Wąż", 10, 5, 10, 10],
    ]
    return choice(przeciwnicy)

def twoj_ekwipunek():
    print(f"\nTutaj mozesz zobaczyc swoj ekwipunek!")
    print(f"Zycie: masz {life} zycia")
    print(f"Mana: masz {mana} many")
    print(f"Odpornosc zbroi: {zbroja}")
    print(f"Doswiadczenie, ktore zdobyles: {doswiadczenie}")
    print(f"Zloto: {zloto}")

def misja_1():
    przeciwnik = ["Czarnoksieznik", 30, 7, 50, 50]
    return walka(przeciwnik)

def misja_2():
    przeciwnik = ["Smok", 45, 10, 70, 100]
    return walka(przeciwnik)

def misja_3():
    przeciwnik = ["Troll", 20, 5, 20, 20]
    return walka(przeciwnik)

def misja_4():
    przeciwnik = ["Zombie", 15, 5, 40, 80   ]
    return walka(przeciwnik)

def misja_5():
    przeciwnik = ["Demon,", 50, 15, 100, 200]
    return walka(przeciwnik)


def misja_6():
    przeciwnik = ["Wąż", 10, 5, 10, 10]
    return walka(przeciwnik)

def ulepsz_wojownika():
    global life, mana, doswiadczenie, sila_ataku, sila_zaklecia, zbroja
    if doswiadczenie >= 10:
        print("Masz sporo doswiadczenia, wykorzystaj je!")
        x = input("Co chcesz ulepszyc? (1 - Atak mieczem, 2 - Zaklecie, 3 - Zbroje, 4 - Zycie, 5 - Mane ): ")
        if x == '1':
            sila_ataku += 5
            print("Twoj atak mieczem zostal zwiekszony o 5!")
        elif x == '2':
            sila_zaklecia += 10 
            print("Moc twojego zaklecia wzrosla o 10!")
        elif x == '3': 
            zbroja += 5
            print("Odpornosc twojej zbroi jest teraz wieksza o 5!")
        elif x == '4':
            life += 10
            print("Masz teraz o 10 wiecej zycia!")
        elif x == '5':
            mana += 10
            print('Ilosc twojej many wzrosla o 10!')
        doswiadczenie -= 10
    else:
        print("Nie masz wystarczajaco doswiadczenia, sproboj je zdobyc!")


def sklep():
    global zloto, life, mana, zbroja
    print("\nWitaj w sklepie! Znajdziesz tu wiele potrzebnych rzeczy")
    print("1 - eliksir zdrowia: koszt 20 zlota, odzyskujesz 35 zycia")
    print("2 - eliksir magii: koszt 10 zlota, odzyskujesz 20 many")
    print("3 - nowa zbroja: koszt 30 zlota, odpornosc twojej zbroi wzrasta o 15")
    print("4 - powrot do menu glownego")

    decyzja = input("\nNa co sie zdecydujesz? (1/2/3/4) ")
    if decyzja == '1':
        if zloto >= 20:
            zloto -= 20
            life += 35
            print("Kupujesz eliksir zdrowia! Twoje zycie wzrasta o 35")
        else: 
            print("Nie masz wystarczajaco zlota, sproboj zdobyc je w jakiejs misji")
    elif decyzja == '2':
        if zloto >= 10:
            zloto -= 10
            mana += 20
            print("Kupujesz eliksir magii! Twoja mana wzrosla o 20.")
        else:
            print("Nie masz wystarczajaco zlota, sproboj zdobyc je w jakiejs misji")
    elif decyzja == '3':
        if zloto >= 30:
            zloto -= 30
            zbroja += 15
            print("Kupujesz nowa zbroje! Odpornosc wzrosla o 15")
        else:
            print("Nie masz wystarczajaco zlota, sprobuj zdobyc je w jakiejs misji")
    elif decyzja == '4':
        print("Wracasz do menu glownego")
    else:
        print("Nieprawidlowy wybor")



def walka(przeciwnik):
    global life, mana, doswiadczenie, zloto
    print(f"\nSpotkales {przeciwnik[0]}! Przygotuj sie do walki!\n")
    while przeciwnik[1] > 0:
        atak = wybierz_rodzaj_ataku()
        przeciwnik[1] -= atak
        if przeciwnik[1] < 0:
            przeciwnik[1] = 0
        print(f"Zadajesz {atak} obrazen! {przeciwnik[0]} ma teraz {przeciwnik[1]} zycia")
        
        
        if przeciwnik[1] == 0:
            print(f"Udalo ci sie pokonac {przeciwnik[0]}!\n")
            doswiadczenie += przeciwnik[3]
            print(f"Zdobywasz {przeciwnik[3]} punktów doświadczenia! Twoje doświadczenie to teraz {doswiadczenie}.")
            zloto += przeciwnik[4]
            print(f"Znalazłeś {przeciwnik[4]} złota!")
            
            return True
        
        atak_przeciwnika = randint(przeciwnik[2] - 2, przeciwnik[2] + 2)
        life -= atak_przeciwnika
        print(f"{przeciwnik[0]} zadaje {atak_przeciwnika} obrażeń! Masz teraz {life} życia.\n")
        
        if life <= 0:
            print("Zostales pokonany... Koniec gry!")
            return False
    return True

while life > 0:
    menu_glowne()
    wybor = input("\nCo chcesz zrobic? (1/2/3/4/5/6): ")

    if wybor == '1':
        przeciwnik = random_opponent()  
        if not walka(przeciwnik):
            break
    elif wybor == '2':
        pokaz_misje()
        wybor_misji = input("\nWybierz misje (1/2/3/4/5/6) lub (7) by wrocic do menu: ")
        if wybor_misji == '1':
            if not misja_1():
                break
        elif wybor_misji == '2':
            if not misja_2():
                break
        elif wybor_misji == '3':
            if not misja_3():
                break
        elif wybor_misji == '4':
            if not misja_4():
                break
        elif wybor_misji == '5':
            if not misja_5():
                break
        elif wybor_misji == '6':
            if not misja_6():
                break
        elif wybor_misji == '7':
            print("Wracasz do menu glownego!")
            
        else:
            print("Nieprawidlowy wybor")
    elif wybor == '3':
        twoj_ekwipunek()
    elif wybor == '4':
       ulepsz_wojownika()
    elif wybor == '5':
        sklep()
    elif wybor == '6':
        print("Konczysz gre! Do zobaczenia pozniej")
    else:
        print("Nieprawidlowy wybor")
    
    opoznienie(1)
