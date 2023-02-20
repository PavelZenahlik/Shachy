import pygame
pygame.init()


class Stav_hry():
    def __init__(self):
        """
        Pole sachu je znaceno 2D listem
        30 znaci prazdne policko
        1x znaci cernou barvu
        2x znaci bilou barvu
        x1 znaci krale (king)
        x2 znaci dámu (queen)
        x3 znaci vez (rook)
        x4 znaci strelce (bishop)
        x5 znaci jezdce (knight)
        x6 znaci pesce (pawn)
        """
        self.pole = [
            ["13", "15", "14", "12", "11", "14", "15", "13"],
            ["16", "16", "16", "16", "16", '16', "16", "16"],
            ["30", "30", "30", "30", "30", "30", "30", "30"],
            ["30", "30", "30", "30", "30", "30", "30", "30"],
            ["30", "30", "30", "30", "30", "30", "30", "30"],
            ["30", "30", "30", "30", "30", "30", "30", "30"],
            ["26", "26", "26", "26", "26", "26", "26", "26"],
            ["23", "25", "24", "22", "21", "24", "25", "23"]
        ]


VYSKA_OKNA = 512  # obrazek figurky je 64x64, 64*8 = 512
SIRKA_OKNA = 512
POCET_CTVERCU_RADEK = 8
VELIKOST_CTVERCE = VYSKA_OKNA // POCET_CTVERCU_RADEK

FIGURKY = {}


def nacist_obrazky():
    list_obrazku = ["11", "12", "13", "14", "15",
                    "16", "21", "22", "23", "24", "25", "26"]  # jmena figurek, soubory se take tak jmenuji
    for obrazek in list_obrazku:
        FIGURKY[obrazek] = pygame.transform.scale(pygame.image.load(
            f"img/{obrazek}.png"), (VELIKOST_CTVERCE - 4, VELIKOST_CTVERCE - 4))  # nacteni jednotlivych obrazku


FPS = 30


def main():
    obrazovka = pygame.display.set_mode((VYSKA_OKNA, SIRKA_OKNA))
    clock = pygame.time.Clock()
    obrazovka.fill(pygame.Color(255, 255, 255))
    pole_sachy = Stav_hry()
    nacist_obrazky()  # nacist obrazky jen jednou
    spusteno = True
    while spusteno:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spusteno = False
        vypsat_stav_hry(obrazovka, pole_sachy)
        clock.tick(FPS)
        pygame.display.flip()


# vypisuje aktualni stav hry

def vypsat_stav_hry(obrazovka, pole_sachy):
    vypsat_ctverce(obrazovka)
    vypsat_figurky(obrazovka, pole_sachy.pole)


# vypisuje vsechny ctverce sachovnice

def vypsat_ctverce(obrazovka):
    barvy = [pygame.Color(255, 255, 255), pygame.Color(175, 175, 175)]
    for radek in range(POCET_CTVERCU_RADEK):
        for sloupec in range(POCET_CTVERCU_RADEK):
            barva = barvy[(radek + sloupec) % 2]
            pygame.draw.rect(obrazovka, barva, pygame.Rect(
                sloupec * VELIKOST_CTVERCE, radek * VELIKOST_CTVERCE, VELIKOST_CTVERCE, VELIKOST_CTVERCE))


# vypisuje figurky pomoci aktualniho stavu pole

def vypsat_figurky(obrazovka, pole_sachy):
    for radek in range(POCET_CTVERCU_RADEK):
        for sloupec in range(POCET_CTVERCU_RADEK):
            figurka = pole_sachy[radek][sloupec]
            if figurka != "30":  # policko neni prazdny
                obrazovka.blit(FIGURKY[figurka], pygame.Rect(
                    sloupec * VELIKOST_CTVERCE, radek * VELIKOST_CTVERCE + 2, VELIKOST_CTVERCE, VELIKOST_CTVERCE))


if __name__ == "__main__":
    main()

pygame.quit()
