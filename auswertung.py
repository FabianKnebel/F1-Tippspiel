########################################################################################################################
# F1 Tippspiel - Auswertung
# 18.03.2020
# Fabian Knebel
########################################################################################################################
from read_sheet import ergebnisse_lesen
from read_sheet import spielertipps_lesen
from tippspiel import rechnen
from write_to_html import html_seite_erstellen


def auswertung(rennen_liste, rennen_dict, spieler_dict):
    for i in range(0, len(rennen_liste)):
        for spieler in spieler_dict:
            spieler_dict[spieler][f"Rennen {i} Punkte"] = rechnen(spieler_dict[spieler][f"Rennen {i} Tipp"], rennen_dict[i]["Ergebnis"])
    for spieler in spieler_dict:
        gesamtpunkte = 0
        for i in range(0, len(rennen_liste)):
            gesamtpunkte += spieler_dict[spieler][f"Rennen {i} Punkte"][-1]
        spieler_dict[spieler]["Gesamtpunkte"] = gesamtpunkte
    return spieler_dict


def hauptprogramm():
    rennen_liste_ausgelesen, rennen_ifo_dict_ausgelesen = ergebnisse_lesen()
    spieler_dict_ausgelesen = spielertipps_lesen()
    spieler_dict_ausgewertet = auswertung(rennen_liste_ausgelesen, rennen_ifo_dict_ausgelesen, spieler_dict_ausgelesen)
    html_seite_erstellen(spieler_dict_ausgewertet, rennen_ifo_dict_ausgelesen)
    return


if __name__ == "__main__":
    hauptprogramm()
