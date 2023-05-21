print("""Podaj rozmiar planszy np.
10
10""")
ROZMIAR_PLANSZY_X = int(input())
ROZMIAR_PLANSZY_Y = int(input())
print("podaj liczbe min")
ILOSC_MIN = int(input())
plansza = [[0 for i in range(ROZMIAR_PLANSZY_X)] for j in range(ROZMIAR_PLANSZY_Y)]
import random


def main():
    wypelnieniePlanszy(ROZMIAR_PLANSZY_X, ROZMIAR_PLANSZY_Y)
    if ILOSC_MIN <= ROZMIAR_PLANSZY_X * ROZMIAR_PLANSZY_Y:
        for m in range(ILOSC_MIN):
            losowanieMin()
        wypelnienieLiczbami()
        wypisaniePlanszy(ROZMIAR_PLANSZY_X, ROZMIAR_PLANSZY_Y)

def wypelnieniePlanszy(rozmiarX, rozmiarY):
    for i in range(rozmiarY):
        for j in range(rozmiarX):
            plansza[i][j] = 0

def wypisaniePlanszy(rozmiarX, rozmiarY):
    for i in range(rozmiarY):
        wiersz = ""
        for j in range(rozmiarX):
            wiersz += str(plansza[i][j])
            wiersz += " "
        print(wiersz)

def losowanieMin():
    losY = random.randint(0, (ROZMIAR_PLANSZY_Y-1))
    losX = random.randint(0, (ROZMIAR_PLANSZY_X-1))
    if plansza[losY][losX] == "X":
        losowanieMin()
    else:
        plansza[losY][losX] = "X"

def wypelnienieLiczbami():
    for i in range(ROZMIAR_PLANSZY_Y):
        for j in range(ROZMIAR_PLANSZY_X):
            if plansza[i][j] != "X":
                liczbaMin = liczMinyWSasiedztwie(j, i)
                plansza[i][j] = liczbaMin

def liczMinyWSasiedztwie(pozX, pozY):
    iloscMin = 0
    for g in range(-1, 2):
        for f in range(-1, 2):
             if not (g == 0 and f == 0):
                if 0 <= pozY + g < ROZMIAR_PLANSZY_Y and 0 <= pozX + f < ROZMIAR_PLANSZY_X:
                    if plansza[g+pozY][f+pozX] == "X":
                        iloscMin += 1
    return iloscMin

main()