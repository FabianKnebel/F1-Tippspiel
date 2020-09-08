########################################################################################################################
# F1 Tippspiel - Tipps vom gsheet lesen
# 18.03.2020
# Fabian Knebel
########################################################################################################################
import pandas
from tippspiel import rechnen


def spielertipps_lesen():
    """
    Funktion liest die Tipps der Spieler vom gsheet aus
    :return: alles_dict: gibt Dict mit Spielernamen aus - jedem ist ein Dict mit "Gesamtpunkte", "Rennen x Tipp" und "Rennen x Punkte" für jedes Rennen zugeordnet
    """
    googleSheetID = "17ll6U13lleRD-XJ0pDEskA96i_knYogba_O-B4B6rMk"  # gsheet ID
    worksheetName1 = "Tippen"  # Name der Tabelle mit den Spielertipps
    url1 = f"https://docs.google.com/spreadsheets/d/{googleSheetID}/gviz/tq?tqx=out:csv&sheet={worksheetName1}"  # Link
    data = pandas.read_csv(url1)  # Daten als csv vom Link lesen

    spieler_liste = []  # Liste aller Spieler mit ihren Namen
    alles_dict = {}  # Dict mit Spielernamen - jedem ist ein Dict mit "Gesamtpunkte", "Rennen x Tipp" und "Rennen x Punkte" für jedes Rennen zugeordnet

    for column in data.columns:  # Spalten auslesen
        if column == "Tipp" or "Unnamed" in column:  # erste Spalte ("Tipp") und unbeschriebene Spalten
            pass  # überspringen
        else:  # alle Spielerspalten auslesen
            spieler_liste += [column]  # Name des Spielers zur Spielerliste hinzufügen
            alles_dict[column] = {}  # Spieler im alles umfassenden Dictionary anlegen

    for spieler in spieler_liste:  # für jeden Spieler
        zeilen = len(data[spieler])  # wie viele Zeilen umfassen die Daten?
        alles_dict[spieler]["Gesamtpunkte"] = 0  # Gesamtpunkte auf 0 initialisieren
        for z in range(zeilen):  # jede Datenzeile auslesen
            if data[spieler][z] == spieler:  # falls der Name des Spielers in der geprüften Zeile auftaucht
                rennname = data['Tipp'][z]  # Name des Rennens aus der "Tipp"-Spalte lesen
                alles_dict[spieler][f"{rennname} Tipp"] = []  # Tippliste für das Rennen initialisieren
                alles_dict[spieler][f"{rennname} Punkte"] = None  # Punkteliste für das Rennen initialisieren
                tipp = [data[spieler][z+1], data[spieler][z+2], data[spieler][z+3], data[spieler][z+4], data[spieler][z+5],
                        data[spieler][z+6], data[spieler][z+7]]  # die Tipps für das Rennen in eine Liste schreiben
                alles_dict[spieler][f"{rennname} Tipp"] = tipp  # Tippliste für das Rennen speichern
    return alles_dict  # allumfassendes Dict zurückgeben


def ergebnisse_lesen():
    """
    Funktion liest die Ergebnisse und Informationen zu einem Rennen vom gsheet aus
    :return: rennen_liste: gibt Liste mit den Namen aller Rennen zurück ("Rennen x" x = Rennummer)
    rennen_dict: gibt alle Informationen des gsheets in einem Dict zurück ({Rennummer}: {"Land": "{land}", "Ort": {ort}, ..., "Ergebnis": [{pp}, {sr}, {1.}, {2.}, ...]})
    """
    googleSheetID = "17ll6U13lleRD-XJ0pDEskA96i_knYogba_O-B4B6rMk"  # gsheet ID
    worksheetName2 = "Ergebnisse"  # Name der Tabelle mit den Rennergebnissen
    url2 = f"https://docs.google.com/spreadsheets/d/{googleSheetID}/gviz/tq?tqx=out:csv&sheet={worksheetName2}"  # Link
    data = pandas.read_csv(url2)  # aus Ergebnistabelle lesen

    rennen_liste = []  # Liste aller Rennnamen ("Rennen x" x = Rennummer)
    rennen_dict = {}  # alle Informationen und das Ergebnis zu jedem Rennen

    for column in data.columns:  # für jede Spalte mit Daten
        if column == "1" or "Unnamed" in column:  # 1. Spalte und leere Spalten (am Ende der Datei)
            pass  # überspringen
        else:  # für alle anderen Rennspalten
            rennen_liste += [column]  # Rennnamen zur Rennliste hinzufügen
            rennen_dict[int(column.replace("Rennen ", ""))] = {}  # Rennnummer(!) zur Kennung zum Dict hinzufügen

    for rennen in rennen_liste:  # für jedes Rennen
        # zeilen = len(data[rennen])
        for z in range(0, 7):  # die ersten 7 Zeilen beinhalten Daten zum Rennen
            spaltenname = data["1"][z]  # die Informationskategorie aus der 1. Zeile auslesen
            rennen_dict[int(rennen.replace("Rennen ", ""))][spaltenname] = data[rennen][z]  # Daten zum Dict hinzufügen

        # Ergebnis des Rennens abspeichern
        rennen_dict[int(rennen.replace("Rennen ", ""))]["Ergebnis"] = [data[rennen][7]] + [data[rennen][8]]\
            + [data[rennen][9]] + [data[rennen][10]] + [data[rennen][11]] + [data[rennen][12]] + [data[rennen][13]]\
            + [data[rennen][14]] + [data[rennen][15]] + [data[rennen][16]] + [data[rennen][17]] + [data[rennen][18]]\
            + [data[rennen][19]] + [data[rennen][20]] + [data[rennen][21]] + [data[rennen][22]] + [data[rennen][23]]\
            + [data[rennen][24]] + [data[rennen][25]] + [data[rennen][26]] + [data[rennen][27]] + [data[rennen][28]]
    return rennen_liste, rennen_dict  # Liste mit Rennamen und Dict mit allen Renninfos ausgeben


if __name__ == "__main__":
    alles_dict_ausgelesen = spielertipps_lesen()  # Tipps auslesen
    # Ausgabe
    print(alles_dict_ausgelesen)
    print(alles_dict_ausgelesen["Fabian"][f"Rennen {0} Tipp"])
    print()

    rennen_liste_ausgelesen, rennen_dict_ausgelesen = ergebnisse_lesen()  # Ergebnisse auslesen
    # Ausgabe
    print(rennen_liste_ausgelesen)
    print(rennen_dict_ausgelesen)

    # Test-/Beispielausgabe
    print()
    print(rechnen(alles_dict_ausgelesen["Fabian"][f"Rennen {0} Tipp"], rennen_dict_ausgelesen[0]["Ergebnis"]))
