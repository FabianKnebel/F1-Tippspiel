########################################################################################################################
# F1 Tippspiel - HTML-Seite erstellen
# 18.03.2020
# Fabian Knebel
########################################################################################################################


def html_seite_erstellen(alles_dict, rennen_dict):
    tippliste = ["Pole Position", "Schnellste Runde", "Platz 1", "Platz 2", "Platz 3", "Platz 4", "Platz 5"]  # welche Tipps gibt es

    gesamtpunkte_dic = {}  # Dictionary mit den Gesamtpunkten für jeden Spieler anlegen
    for spieler in alles_dict:  # für jeden Spieler
        gesamtpunkte_dic[spieler] = alles_dict[spieler]["Gesamtpunkte"]  # Gesamptunkte des Spielers in das Dictionary geben
    # das Dictionary nach Gesamtpunktestand absteigend sortieren
    gesamtpunkte_dic_ordered = {k: v for k, v in sorted(gesamtpunkte_dic.items(), key=lambda item: item[1], reverse=True)}

    html_head = """<!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <title>F1 Tippspiel</title>
        <style>
            body.light-mode {
                padding: 20px;
                background-color: white;
                color: black;
                font-size: 25px;
            }
    
            table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
                text-align: center;
            }
            table.tabelle_gesamt th {
                background-color: black;
                color: white;
            }
    
            .buttonwrapper {
                text-align: center;
            }
    
            .column33 {
              float: left;
              width: 33%;
            }
            .column50 {
              float: left;
              width: 50%;
            }
            .column66 {
              float: left;
              width: 66%;
            }
            .row:after {
              content: "";
              display: table;
              clear: both;
            }
    
            th:empty{
                visibility: hidden;
            }
            td:empty{
                visibility: hidden;
            }
            table.tabelle_einzelnd tr:nth-child(even) {
                background-color: #eee;
            }
            table.tabelle_einzelnd tr:nth-child(odd) {
                background-color: #fff;
            }
        </style>
    </head>
    <body id="body" class="light-mode">"""  # HTML-Kopf inkl. style/css-Angaben

    gesamtpunktetabelle_head = """<div>
        <table style="width:20%" align="center" class="tabelle_gesamt">
            <caption style="padding-bottom:2%;"><b>Gesamtpunktestand</b></caption>
            <tr>
                <th>Platz</th>
                <th>Name</th>
                <th>Punkte</th>
            </tr>"""  # Anfang der Gesamtpunktetabelle

    gesamtpunktetabelle_inhalt = ""  # Inhalt der Gesamtpunktetabelle initialisieren
    platzierung_counter = 1  # durchgehender Platzierungscounter
    for spieler in gesamtpunkte_dic_ordered:  # für jeden Spieler
        spieler_mit_gleichen_punkten = gesamtpunktetabelle_inhalt.count(f"<td>{gesamtpunkte_dic_ordered[spieler]}</td>")  # gucken, wie viele Spieler schon die gleichen Punkte haben
        if spieler_mit_gleichen_punkten > 0:  # falls es mindestens 1 Spieler mit gleichen Punkten gibt
            gesamtpunktetabelle_inhalt += """        <tr>
                        <td>{platz}.</td>
                        <td>{name}</td>
                        <td>{punkte}</td>
                    </tr>""".format(platz=platzierung_counter-spieler_mit_gleichen_punkten, name=spieler, punkte=gesamtpunkte_dic_ordered[spieler])  # Punkte in Tabelle einfügen, Platzierung wie der letzte Spieler mit gleicher Punktzahl
        else:  # einmaliger Punktestand
            gesamtpunktetabelle_inhalt += """        <tr>
                <td>{platz}.</td>
                <td>{name}</td>
                <td>{punkte}</td>
            </tr>""".format(platz=platzierung_counter, name=spieler, punkte=gesamtpunkte_dic_ordered[spieler])  # Punkte in Tabelle hinzufügen
        platzierung_counter += 1  # Platzierungscounter hochzählen

    gesamtpunktetabelle_end = """    </table>
    </div>
    <hr>"""  # Ende der Gesamtpunktetabelle

    gesamtpunktetabelle = gesamtpunktetabelle_head + gesamtpunktetabelle_inhalt + gesamtpunktetabelle_end  # Gesamtpunktetabelle erstellen

    hiertippabgeben = """
    <div align="center">
        <a href="https://docs.google.com/spreadsheets/d/17ll6U13lleRD-XJ0pDEskA96i_knYogba_O-B4B6rMk/edit?usp=sharing">HIER Tipps abgeben</a>
    </div>
    <hr>"""  # "Tipp hier abgeben"-Abschnitt

    regeln = """
    <div class="buttonwrapper">
        <button onclick="showhideRegeln()">Regeln ein-/ausklappen</button>
    </div>
    <script>
    function showhideRegeln() {
      var x = document.getElementById("regeln");
      if (x.style.display === "none") {
        x.style.display = "block";
      } else {
        x.style.display = "none";
      }
    }
    </script>
    
    <div id="regeln">
        <h2>Regeln:</h2>
        <p>Es werden <b><strong>pro Rennwochenende 7 Tipps abgegeben</strong></b> - einer für die <b>Pole Position</b>, einer für die <b>schnellste Rennrunde</b> und die restlichen für die <b>Top 5</b>. (Dabei zählt das offizielle Endergebnis inkl. Strafen usw.) Tipps müssen bis spätestens zum Start der jweiligen Session abgegeben werden.</p>
    
        <div class="row">
            <div class="column33">
                <p>Falls <b>richtig getippt</b> wurde, gibt es folgende Punkte:</p>
                <table class="punkte_zuweisung">
                    <tr>
                        <td>Pole Position</td>
                        <td>50 Punkte</td>
                    </tr>
                    <tr>
                        <td>Schnellste Runde</td>
                        <td>50 Punkte</td>
                    </tr>
                    <tr>
                        <td>Platz 1</td>
                        <td>100 Punkte</td>
                    </tr>
                    <tr>
                        <td>Platz 2</td>
                        <td>90 Punkte</td>
                    </tr>
                    <tr>
                        <td>Platz 3</td>
                        <td>80 Punkte</td>
                    </tr>
                    <tr>
                        <td>Platz 4</td>
                        <td>70 Punkte</td>
                    </tr>
                    <tr>
                        <td>Platz 5</td>
                        <td>60 Punkte</td>
                    </tr>
                </table>
            </div>
            <div class="column33">
                <p>Falls <b>nicht richtig getippt</b> wurde, gibt es für die Platzdifferenz (Tipp-Ergebnis) Punkte:</p>
                <table class="punkte_zuweisung">
                    <tr>
                        <td>1 Platz Unterschied</td>
                        <td>50 Punkte</td>
                    </tr>
                    <tr>
                        <td>2 Plätze Unterschied</td>
                        <td>45 Punkte</td>
                    </tr>
                    <tr>
                        <td>3 Plätze Unterschied</td>
                        <td>40 Punkte</td>
                    </tr>
                    <tr>
                        <td>4 Plätze Unterschied</td>
                        <td>40 Punkte</td>
                    </tr>
                    <tr>
                        <td>5 Plätze Unterschied</td>
                        <td>35 Punkte</td>
                    </tr>
                    <tr>
                        <td>6 Plätze Unterschied</td>
                        <td>30 Punkte</td>
                    </tr>
                    <tr>
                        <td>7 Plätze Unterschied</td>
                        <td>25 Punkte</td>
                    </tr>
                    <tr>
                        <td>8 Plätze Unterschied</td>
                        <td>20 Punkte</td>
                    </tr>
                    <tr>
                        <td>9 Plätze Unterschied</td>
                        <td>15 Punkte</td>
                    </tr>
                    <tr>
                        <td>10 Plätze Unterschied</td>
                        <td>5 Punkte</td>
                    </tr>
                    <tr>
                        <td>>=11 Plätze Unterschied</td>
                        <td>0 Punkte</td>
                    </tr>
                </table>
            </div>
            <div class="column33"></div>
        </div>"""  # Regelabschnitt

    beispiel = """
        <div class="buttonwrapper" style="padding-top:1%;">
            <button onclick="showhideBeispiel()">Beispiel ein-/ausklappen</button>
        </div>
        <script>
        function showhideBeispiel() {
          var x = document.getElementById("beispiel");
          if (x.style.display === "none") {
            x.style.display = "block";
          } else {
            x.style.display = "none";
          }
        }
        </script>
    
        <div id="beispiel" class="row" style="padding-top:2%;">
            <div class="column66">
                <p><i>Ein Beispiel:</i> Ein fiktiver<b>(!)</b> Peter Maffay tippt: PP:HAM, SR:HAM, P1:HAM, P2:BOT, P3:VET, P4:LEC, P5:ALB</p>
                <p>Und das Rennergebnis lautet: PP:BOT, SR:HAM, P1:HAM, P2:LEC, P3:VET, P4:ALB, P5:BOT</p>
                <p>Dann würde diese fivtive Person insgesamt 370 Punkte bekommen. (PP:falsch → 0 Pkt. + SR:richtig → 50 Pkt. + P1:richtig → 100 Pkt. + P2:falsch → BOT ist auf P5 statt auf P3 → 5-3=2 Plätze Differenz → 45 Pkt. + P3:richtig → 80 Pkt., P4:falsch → LEC ist auf P2 statt auf P4 → 4-2=2 Plätze Differenz → 45 Pkt. + P5:falsch → ALB ist auf P4 statt auf P5 → 5-4=1 Platz Differenz → 50 Pkt. ⇒ 370 Punkte)</p>
            </div>
            <div class="column33">
                <table class="tabelle_beispiel" style="float:left;">
                    <tr>
                        <th></th>
                        <th>Tipp Peter</th>
                        <th>Rennergebnis</th>
                        <th>Punkte</th>
                    </tr>
                    <tr>
                        <td>PP</td>
                        <td>HAM</td>
                        <td>BOT</td>
                        <td>0</td>
                    </tr>
                    <tr>
                        <td>SR</td>
                        <td>HAM</td>
                        <td>HAM</td>
                        <td>50</td>
                    </tr>
                    <tr>
                        <td>P1</td>
                        <td>HAM</td>
                        <td>HAM</td>
                        <td>100</td>
                    </tr>
                    <tr>
                        <td>P2</td>
                        <td>BOT</td>
                        <td>LEC</td>
                        <td>45</td>
                    </tr>
                    <tr>
                        <td>P3</td>
                        <td>VET</td>
                        <td>VET</td>
                        <td>80</td>
                    </tr>
                    <tr>
                        <td>P4</td>
                        <td>LEC</td>
                        <td>ALB</td>
                        <td>45</td>
                    </tr>
                    <tr>
                        <td>P5</td>
                        <td>ALB</td>
                        <td>BOT</td>
                        <td>50</td>
                    </tr>
                        <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td><b>370</b></td>
                    </tr>
                </table>
            </div>
        </div>
    </div>
    <hr>"""  # Beispielsabschnitt

    def einzeltabelle_erstellen(_rennnummer=0):
        """
        Funktion, die die Tabellen für jedes einzelne Rennen erstellt (Tipps - Punkte für jeden Spieler)
        :param _rennnummer: Nummer des Rennens für das die Tabelle erstellt werden soll
        :return: _einzeltabelle: HMTL-Text für die Tabelle zurückgeben
        """
        einzeltabelle_head = f"""
        <div>
            <table style="width:20%; padding-top:2%" align="center" class="tabelle_einzelnd">
                <caption style="padding-bottom:2%;"><b>Tipps/Punkte: Rennen {_rennnummer}</b></caption>\n"""  # Start der Einzeltabelle

        einzeltabelle_zeile0_head = """         <tr>
                    <th></th>\n"""
        einzeltabelle_zeile0_inhalt = ""
        for _spieler in alles_dict:
            einzeltabelle_zeile0_inhalt += f"               <th colspan='2'>{_spieler}</th>\n"
        einzeltabelle_zeile0_inhalt += f"               <th rowspan='2'>Ergebnis</th>\n"  # Ergebnisspalte
        einzeltabelle_zeile0_foot = "           </tr>"

        einzeltabelle_zeile1_head = """
                <tr>
                    <td></td>"""
        einzeltabelle_zeile1_inhalt = ""
        for _i in range(0, len(alles_dict)):
            einzeltabelle_zeile1_inhalt += """                <td>Tipp</td>
                    <td>Punkte</td>\n"""
        einzeltabelle_zeile1_foot = """            </tr>\n"""

        einzeltabelle_zeile1 = einzeltabelle_zeile1_head + einzeltabelle_zeile1_inhalt + einzeltabelle_zeile1_foot

        einzeltabelle_inhalt = ""
        for tippname in tippliste:
            einzeltabelle_inhalt_row_start = """          <tr>\n"""
            einzeltabelle_inhalt_row = ""
            anfang_der_tabelle = True
            for _spieler in alles_dict:
                if anfang_der_tabelle:
                    einzeltabelle_inhalt_row += f"""            <td><b>{tippname}</b></td>\n"""
                    anfang_der_tabelle = False
                einzeltabelle_inhalt_row += f"""            <td>{alles_dict[_spieler]["Rennen {num} Tipp".format(num=_rennnummer)][tippliste.index(tippname)]}</td>
                <td>{alles_dict[_spieler]["Rennen {num} Punkte".format(num=_rennnummer)][tippliste.index(tippname)]}</td>\n"""
            einzeltabelle_inhalt_row += f"""            <td><b>{rennen_dict[_rennnummer]["Ergebnis"][tippliste.index(tippname)]}</b></td>\n"""

            einzeltabelle_inhalt_row_end = """          </tr>\n"""
            einzeltabelle_inhalt += einzeltabelle_inhalt_row_start + einzeltabelle_inhalt_row + einzeltabelle_inhalt_row_end

        einzeltabelle_zeile_last_head = """         <tr>
                    <td></td>\n"""
        einzeltabelle_zeile_last_inhalt = ""
        for _spieler in alles_dict:
            einzeltabelle_zeile_last_inhalt += f"               <td colspan='2'><b>{alles_dict[_spieler]['Rennen {num} Punkte'.format(num=_rennnummer)][-1]}</b></td>\n"
        # einzeltabelle_zeile_last_inhalt += f"               <td></td>\n"  # erstmal keine Ergebnisspalte
        einzeltabelle_zeile_last_foot = "           </tr>"

        einzeltabelle_foot = """
            </table>
        </div>
        <br>\n"""  # Ende der Einzeltabelle

        _einzeltabelle = einzeltabelle_head + einzeltabelle_zeile0_head + einzeltabelle_zeile0_inhalt\
            + einzeltabelle_zeile0_foot + einzeltabelle_zeile1 + einzeltabelle_inhalt\
            + einzeltabelle_zeile_last_head + einzeltabelle_zeile_last_inhalt + einzeltabelle_zeile_last_foot \
            + einzeltabelle_foot  # Einzeltabelle zusammenfügen
        return _einzeltabelle  # HTML-Text für die Tabelle zurückgeben

    html_einzeltabellen = ""
    for i in rennen_dict:
        einzeltabelle = einzeltabelle_erstellen(i)
        html_einzeltabellen += einzeltabelle

    # https://www.rssdog.com/index.php?url=https%3A%2F%2Fwww.formel1.de%2Frss%2Fformel-1%2Ffeed.xml&mode=html&showonly=&maxitems=0&showdescs=1&desctrim=0&descmax=0&tabwidth=100%25&linktarget=_blank&textsize=inherit&bordercol=%23d4d0c8&headbgcol=%23999999&headtxtcol=%23ffffff&titlebgcol=%23f1eded&titletxtcol=%23000000&itembgcol=%23ffffff&itemtxtcol=%23000000
    html_rss = """
<hr>
<iframe width="100%" height="750" frameborder="0" class="rssdog" src="https://www.rssdog.com/index.php?url=https%3A%2F%2Fwww.formel1.de%2Frss%2Fformel-1%2Ffeed.xml&mode=html&showonly=&maxitems=0&showdescs=1&desctrim=0&descmax=0&tabwidth=100%25&linktarget=_blank&textsize=inherit&bordercol=%23d4d0c8&headbgcol=%23999999&headtxtcol=%23ffffff&titlebgcol=%23f1eded&titletxtcol=%23000000&itembgcol=%23ffffff&itemtxtcol=%23000000&ctl=0"></iframe>"""

    html_foot = """<br>
    
</body>
</html>"""  # HTML-foot

    html = html_head + gesamtpunktetabelle + hiertippabgeben + regeln + beispiel + \
        html_einzeltabellen + \
        html_rss + html_foot  # gesamten HTML-Text zusammenfügen

    with open("testoutput.html", "w", encoding="UTF-8") as outputfile:  # in Datei schreiben
        outputfile.write(html)  # HTML-Text schreiben
    return html


def hauptprogramm():
    # Beispielsdictionary jedem Spieler wird ein Dict mit Gesamtpunkten, Tipps und Punkten für jedes Rennen zugeordnet
    alles_dict_besipiel = {
        "Fabian": {
            "Gesamtpunkte": 5,
            "Rennen 0 Tipp": ['RUS', 'GRO', 'OCO', 'KWJ', 'ALB', 'LAT', 'LEC'],
            "Rennen 0 Punkte": [0, 0, 0, 0, 0, 0, 0, 5],
            "Rennen 1 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 1 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 2 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 2 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 3 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 3 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 4 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 4 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 5 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 5 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 6 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 6 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 7 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 7 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 8 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 8 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 9 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 9 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 10 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 10 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 11 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 11 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 12 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 12 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 13 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 13 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 14 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 14 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 15 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 15 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
        },
        "Jan-Philip": {
            "Gesamtpunkte": 15,
            "Rennen 0 Tipp": ['RAI', 'HAM', 'LEC', 'VER', 'KWJ', 'GIO', 'RIC'],
            "Rennen 0 Punkte": [0, 0, 0, 0, 0, 0, 0, 10],
            "Rennen 1 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 1 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 2 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 2 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 3 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 3 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 4 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 4 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 5 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 5 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 6 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 6 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 7 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 7 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 8 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 8 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 9 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 9 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 10 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 10 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 11 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 11 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 12 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 12 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 13 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 13 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 14 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 14 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 15 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 15 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
        },
        "Lea": {
            "Gesamtpunkte": 20,
            "Rennen 0 Tipp": ['RAI', 'GIO', 'RIC', 'SAI', 'HAM', 'BOT', 'KWJ'],
            "Rennen 0 Punkte": [0, 0, 0, 0, 0, 0, 0, 20],
            "Rennen 1 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 1 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 2 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 2 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 3 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 3 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 4 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 4 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 5 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 5 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 6 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 6 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 7 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 7 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 8 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 8 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 9 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 9 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 10 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 10 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 11 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 11 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 12 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 12 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 13 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 13 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 14 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 14 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 15 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 15 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
        },
        "Philipp": {
            "Gesamtpunkte": 15,
            "Rennen 0 Tipp": ['HAM', 'RIC', 'SAI', 'PER', 'LAT', 'ALB', 'LEC'],
            "Rennen 0 Punkte": [0, 0, 0, 0, 0, 0, 0, 15],
            "Rennen 1 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 1 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 2 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 2 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 3 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 3 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 4 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 4 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 5 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 5 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 6 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 6 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 7 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 7 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 8 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 8 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 9 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 9 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 10 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 10 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 11 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 11 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 12 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 12 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 13 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 13 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 14 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 14 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 15 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 15 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
        },
        "Peter": {
            "Gesamtpunkte": 15,
            "Rennen 0 Tipp": ['HAM', 'RIC', 'SAI', 'PER', 'LAT', 'ALB', 'LEC'],
            "Rennen 0 Punkte": [0, 0, 0, 0, 0, 0, 0, 15],
            "Rennen 1 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 1 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 2 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 2 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 3 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 3 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 4 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 4 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 5 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 5 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 6 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 6 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 7 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 7 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 8 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 8 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 9 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 9 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 10 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 10 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 11 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 11 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 12 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 12 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 13 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 13 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 14 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 14 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
            "Rennen 15 Tipp": ["-", "-", "-", "-", "-", "-", "-"],
            "Rennen 15 Punkte": [0, 0, 0, 0, 0, 0, 0, 0],
        },
    }
    # Beispielsdictionary mit allen Renninfos
    rennen_dict_beispiel = {
        0: {
            "Land": "Testland",
            "Ort": "Testort",
            "Streckenname": "Teststrecke",
            "Streckenlänge": "6,9 km",
            "Kurvenanzahl": "4",
            "Datum": "03/17/20",
            "Rennstart": "14:10",
            "Ergebnis": ['BOT', 'VER', 'HAM', 'BOT', 'VET', 'LEC', 'ALB', 'VER', 'NOR', 'SAI', 'RIC', 'OCO', 'GAS',
                         'KWJ', 'PER', 'STR', 'RAI', 'GIO', 'GRO', 'MAG', 'LAT', 'RUS'],
        },
        1: {
            "Land": "",
            "Ort": "",
            "Streckenname": "",
            "Streckenlänge": "",
            "Kurvenanzahl": "",
            "Datum": "",
            "Rennstart": "",
            "Ergebnis": ["#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        },
        2: {
            "Land": "",
            "Ort": "",
            "Streckenname": "",
            "Streckenlänge": "",
            "Kurvenanzahl": "",
            "Datum": "",
            "Rennstart": "",
            "Ergebnis": ["#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        },
        3: {
            "Land": "",
            "Ort": "",
            "Streckenname": "",
            "Streckenlänge": "",
            "Kurvenanzahl": "",
            "Datum": "",
            "Rennstart": "",
            "Ergebnis": ["#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        },
        4: {
            "Land": "",
            "Ort": "",
            "Streckenname": "",
            "Streckenlänge": "",
            "Kurvenanzahl": "",
            "Datum": "",
            "Rennstart": "",
            "Ergebnis": ["#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        },
        5: {
            "Land": "",
            "Ort": "",
            "Streckenname": "",
            "Streckenlänge": "",
            "Kurvenanzahl": "",
            "Datum": "",
            "Rennstart": "",
            "Ergebnis": ["#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        },
        6: {
            "Land": "",
            "Ort": "",
            "Streckenname": "",
            "Streckenlänge": "",
            "Kurvenanzahl": "",
            "Datum": "",
            "Rennstart": "",
            "Ergebnis": ["#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        },
        7: {
            "Land": "",
            "Ort": "",
            "Streckenname": "",
            "Streckenlänge": "",
            "Kurvenanzahl": "",
            "Datum": "",
            "Rennstart": "",
            "Ergebnis": ["#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        },
        8: {
            "Land": "",
            "Ort": "",
            "Streckenname": "",
            "Streckenlänge": "",
            "Kurvenanzahl": "",
            "Datum": "",
            "Rennstart": "",
            "Ergebnis": ["#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        },
        9: {
            "Land": "",
            "Ort": "",
            "Streckenname": "",
            "Streckenlänge": "",
            "Kurvenanzahl": "",
            "Datum": "",
            "Rennstart": "",
            "Ergebnis": ["#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        },
        10: {
            "Land": "",
            "Ort": "",
            "Streckenname": "",
            "Streckenlänge": "",
            "Kurvenanzahl": "",
            "Datum": "",
            "Rennstart": "",
            "Ergebnis": ["#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        },
        11: {
            "Land": "",
            "Ort": "",
            "Streckenname": "",
            "Streckenlänge": "",
            "Kurvenanzahl": "",
            "Datum": "",
            "Rennstart": "",
            "Ergebnis": ["#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        },
        12: {
            "Land": "",
            "Ort": "",
            "Streckenname": "",
            "Streckenlänge": "",
            "Kurvenanzahl": "",
            "Datum": "",
            "Rennstart": "",
            "Ergebnis": ["#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        },
        13: {
            "Land": "",
            "Ort": "",
            "Streckenname": "",
            "Streckenlänge": "",
            "Kurvenanzahl": "",
            "Datum": "",
            "Rennstart": "",
            "Ergebnis": ["#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        },
        14: {
            "Land": "",
            "Ort": "",
            "Streckenname": "",
            "Streckenlänge": "",
            "Kurvenanzahl": "",
            "Datum": "",
            "Rennstart": "",
            "Ergebnis": ["#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        },
        15: {
            "Land": "",
            "Ort": "",
            "Streckenname": "",
            "Streckenlänge": "",
            "Kurvenanzahl": "",
            "Datum": "",
            "Rennstart": "",
            "Ergebnis": ["#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
                         "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        },
    }
    seite = html_seite_erstellen(alles_dict_besipiel, rennen_dict_beispiel)
    print(seite)  # Ausgabe


if __name__ == "__main__":
    hauptprogramm()
