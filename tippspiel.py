########################################################################################################################
# F1 Tippspiel - Punkte ausrechnen
# 16.03.2020
# Fabian Knebel
########################################################################################################################
import random


# Punkte eines Spielers für ein Rennen ausrechnen
def rechnen(tippliste_alles, ergebnis_liste):
    """
    Punkte eines Spielers anhand seines Tipps für ein Rennen ausrechnen
    :param tippliste_alles: Liste der Tipps (PP, SR, Platzierungen) des Spielers
    :param ergebnis_liste: Liste der Ergebnisse (PP, SR, Platzierungen) des Rennens
    :return: punkte_liste: Liste, die die Punkte der einzelnen Tipps hat (letzte Zahl ist die Gesamtpunktzahl für das R)
    """

    punkte_richtig_dict = {
        1: 100,
        2: 90,
        3: 80,
        4: 70,
        5: 60,
    }  # Dictionary für welchen Platz es wie viele Punkte gibt
    punkte_differenz_dict = {
        1: 50,
        2: 45,
        3: 40,
        4: 35,
        5: 30,
        6: 25,
        7: 20,
        8: 15,
        9: 10,
        10: 5,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: 0,
        16: 0,
        17: 0,
        18: 0,
        19: 0,
        20: 0,
    }  # Dictionary für welche Platzdifferenz es wie viele Punkte gibt
    punkte_sonst_dict = {
        "PP": 50,
        "SR": 50,
    }  # Dictionary wie viele Punkte es für PP- und SR-Tipps gibt

    punkte_liste = []
    punkte = 0  # Initialisierung der Punkte
    if tippliste_alles[0] == ergebnis_liste[0]:  # falls Pole Position-Tipp stimmt
        punkte_liste += [punkte_sonst_dict["PP"]]  # Punkte für richtigen PP-Tipp zur Liste hinzufügen
        punkte += punkte_sonst_dict["PP"]  # Punkte für richtigen PP-Tipp zu den Gesamtpunkten hinzufügen
    else:  # Pole-Position falsch gestippt
        punkte_liste += [0]  # Punkte für falschen PP-Tipp zur Liste hinzufügen
    if tippliste_alles[1] == ergebnis_liste[1]:  # falls Schnellste Runde-Tipp stimmt
        punkte_liste += [punkte_sonst_dict["SR"]]  # Punkte für richtigen SR-Tipp zur Liste hinzufügen
        punkte += punkte_sonst_dict["SR"]  # Punkte für richtigen SR-Tipp zu den Gesamtpunkten hinzufügen
    else:  # Schnellste Runde falsch gestippt
        punkte_liste += [0]  # Punkte für falschen SR-Tipp zur Liste hinzufügen

    rennergebnis = ergebnis_liste[2:]  # Rennergebnisliste ohne PP und SR
    tippliste = tippliste_alles[2:]  # Tippliste ohne PP- und SR-Tipp

    for i in range(1, 6):  # Durchlauf für die Plätze 1-5
        if tippliste[i-1] == "-":  # falls kein Tipp angegeben wurde
            punkte_liste += [0]  # kein Tipp = 0 Punkte (zur Liste hinzufügen)
            punkte += 0  # Tipp nicht abgegeben = 0 Punkte
        elif tippliste[i-1] == rennergebnis[i-1]:  # wenn Tipp und Ergebnis an gleicher Stelle stehen
            punkte_liste += [punkte_richtig_dict[i]]  # richtige Punkte für den richtigen Platz zu Liste hinzufügen
            punkte += punkte_richtig_dict[i]  # richtige Punkte für den richtigen Platz zu den Gesamtpkten hinzurechnen
            # print(f"Platz {i}: Richtig! Punkte: {punkte_richtig_dict[i]}")  # Ausgabe
        else:
            platzierung_tipp = tippliste.index(tippliste[i-1]) + 1  # Platzierung im Tipp
            platzierung_rennen = rennergebnis.index(tippliste[i-1]) + 1  # Platzierung im Ergebnis
            if platzierung_rennen - platzierung_tipp > 0:  # negatives Ergebnis verhindern
                platzdifferenz = platzierung_rennen - platzierung_tipp
            else:
                platzdifferenz = platzierung_tipp - platzierung_rennen  # Differernz zwischen Tipp und Ergebnis
            punkte_liste += [punkte_differenz_dict[platzdifferenz]]  # Punkte für Platzdifferenz zur Liste hinzufügen
            punkte += punkte_differenz_dict[platzdifferenz]  # Punkte für Platzdifferenz zu den Gesamtpkten hinzurechnen
            # print(f"Platz {i}: Differenz: {platzdifferenz} Punkte: {punkte_differenz_dict[platzdifferenz]}")  # Ausgab
    punkte_liste += [punkte]  # Gesamtpunkte für das Rennen an die Liste anhängen
    return punkte_liste  # Rückgabe Punkteliste (letzte Zahl ist Gesamtpunktzahl für das Rennen)


def hauptprogramm():
    # unnütze + ungenutzte Fakten
    info_dict = {
        "saison2020": {
            "HAM": {
                "Name": "Lewis Hamilton",
                "Abkürzung": "HAM",
                "Team": "Mercedes",
                "Nummer": 44,
                "Land": "Großbritannien",
            },
            "BOT": {
                "Name": "Valteri Bottas",
                "Abkürzung": "BOT",
                "Team": "Mercedes",
                "Nummer": 77,
                "Land": "Finnland",
            },
            "VET": {
                "Name": "Sebastian Vettel",
                "Abkürzung": "VET",
                "Team": "Ferrari",
                "Nummer": 5,
                "Land": "Deutschland",
            },
            "LEC": {
                "Name": "Charles Leclerc",
                "Abkürzung": "LEC",
                "Team": "Ferrari",
                "Nummer": 16,
                "Land": "Monaco",
            },
            "ALB": {
                "Name": "Alexander Albon",
                "Abkürzung": "ALB",
                "Team": "Red Bull",
                "Nummer": 23,
                "Land": "Thailand",
            },
            "VER": {
                "Name": "Max Verstappen",
                "Abkürzung": "VER",
                "Team": "Red Bull",
                "Nummer": 33,
                "Land": "Niederlande",
            },
            "NOR": {
                "Name": "Lando Norris",
                "Abkürzung": "NOR",
                "Team": "McLaren",
                "Nummer": 4,
                "Land": "Großbritannien",
            },
            "SAI": {
                "Name": "Carlos Sainz",
                "Abkürzung": "SAI",
                "Team": "McLaren",
                "Nummer": 55,
                "Land": "Spanien",
            },
            "RIC": {
                "Name": "Daniel Ricciardo",
                "Abkürzung": "RIC",
                "Team": "Renault",
                "Nummer": 3,
                "Land": "Australien",
            },
            "OCO": {
                "Name": "Esteban Ocon",
                "Abkürzung": "OCO",
                "Team": "Renault",
                "Nummer": 31,
                "Land": "Frankreich",
            },
            "GAS": {
                "Name": "Pierre Gasly",
                "Abkürzung": "GAS",
                "Team": "AlphaTauri",
                "Nummer": 10,
                "Land": "Frankreich",
            },
            "KWJ": {
                "Name": "Daniil Kwjat",
                "Abkürzung": "KWJ",
                "Team": "AlphaTauri",
                "Nummer": 26,
                "Land": "Russland",
            },
            "PER": {
                "Name": "Sergio Perez",
                "Abkürzung": "PER",
                "Team": "Racing Point",
                "Nummer": 11,
                "Land": "Mexiko",
            },
            "STR": {
                "Name": "Lance Stroll",
                "Abkürzung": "STR",
                "Team": "Racing Point",
                "Nummer": 18,
                "Land": "Kanada",
            },
            "RAI": {
                "Name": "Kimi Raikkönen",
                "Abkürzung": "RAI",
                "Team": "Alfa Romeo",
                "Nummer": 7,
                "Land": "Finnland",
            },
            "GIO": {
                "Name": "Antonio Giovinazzi",
                "Abkürzung": "GIO",
                "Team": "Alfa Romeo",
                "Nummer": 99,
                "Land": "Italien",
            },
            "GRO": {
                "Name": "Romain Grosjean",
                "Abkürzung": "GRO",
                "Team": "Haas",
                "Nummer": 8,
                "Land": "Frankreich",
            },
            "MAG": {
                "Name": "Kevin Magnussen",
                "Abkürzung": "MAG",
                "Team": "Haas",
                "Nummer": 20,
                "Land": "Dänemark",
            },
            "LAT": {
                "Name": "Nicholas Latifi",
                "Abkürzung": "LAT",
                "Team": "Williams",
                "Nummer": 6,
                "Land": "Kanada",
            },
            "RUS": {
                "Name": "George Russel",
                "Abkürzung": "RUS",
                "Team": "Williams",
                "Nummer": 63,
                "Land": "Großbritannien",
            },
        }
    }
    print("Unnütze Fakten:\n", info_dict)

    # Besipielergebnis für Rennen1
    rennen1 = ["HAM", "HAM",
               "HAM", "BOT", "VET", "LEC", "ALB", "VER", "NOR", "SAI", "RIC", "OCO",
               "GAS", "KWJ", "PER", "STR", "RAI", "GIO", "GRO", "MAG", "LAT", "RUS"]

    spieler1 = [random.choice(rennen1)]  # Pole Position Tipp
    # spieler1 += [random.choice(rennen1)]  # Schnellste Runde Tipp
    spieler1 += ["-"]  # Schnellste Runde Tipp (vergessen abzugeben)
    spieler1 += [random.choice(rennen1)]  # Erster Tipp
    while len(spieler1) < 7:  # insgesamt müssen 7 Tipps abgegeben werden
        tipp = random.choice(rennen1)  # zufällig tippen
        while tipp in spieler1:  # falls der Name schon im Tipp existiert, einen anderen wählen
            tipp = random.choice(rennen1)  # anderen zufälligen Tipp abgeben
        spieler1 += [tipp]  # tipp zur Tippliste hinzufügen

    punkte_spieler1 = rechnen(spieler1, rennen1)  # Punkte des Spielers1 für Rennen1 ausrechnen

    # Ausgabe
    print("Rennergebnis:", rennen1)
    print("Spieler1 Tipp:", spieler1)
    print(f"Punkteliste: {punkte_spieler1}")
    print(f"Gesamtpunkte: {punkte_spieler1[-1]}")
    return


if __name__ == "__main__":
    hauptprogramm()
