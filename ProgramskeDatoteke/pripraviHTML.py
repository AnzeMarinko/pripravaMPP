import requests


def pripravi_html(datum, naslov, razmisljanje, avtor):
    # uvoz strani z Bozjo besedo
    url = 'https://hozana.si/index.php?datum={}'.format(datum)
    r = requests.get(url)
    hozana_html = r.text.split("\n")

    # ven izlusci berilo, psalm, evangelij in citat
    citat = ""
    berilo = ["", "", ""]   # naslov, vrstica, berilo
    psalm = ["", "", ""]   # vrstica, psalm, odpev
    evangelij = ["", "", ""]   # naslov, vrstica, evangelij

    iscem = 0   # iskane komponente stejemo od 0 do 9
    nasel = False
    for vrstica in hozana_html:
        if iscem == 0:
            if nasel:
                citat += vrstica[4:-11]
                iscem = 1
                nasel = False
            if "<h2 id=" in vrstica:
                nasel = True
        elif iscem == 1:
            if '<div class="naslov_berila">' in vrstica:
                berilo[0] += vrstica[27:-6]
                iscem = 2
        elif iscem == 2:
            berilo[1] += vrstica[59:-4]
            iscem = 3
        elif iscem == 3:
            if "<h2>" in vrstica:
                berilo[2] += vrstica[0:vrstica.index("<h2>")-4]
                berilo[2] = berilo[2][3:]
                iscem = 4
            else:
                berilo[2] += vrstica
        elif iscem == 4:
            if '<span style="font-style: italic;">&raquo;' in vrstica:
                psalm[2] += vrstica[vrstica.index("&raquo;")+7:vrstica.index("&laquo;")]
                iscem = 5
        elif iscem == 5:
            if '<p style="font-style: italic; padding: 10px 0px 10px 0px;">' in vrstica:
                psalm[0] += vrstica[vrstica.index('">')+2:vrstica.index("</p>")]
                iscem = 6
        elif iscem == 6:
            if '<div style="margin: 0px,' in vrstica:
                if nasel:
                    psalm[1] += "<br>"
                else:
                    nasel = True
                    psalm[1] += "</p><p>"
                psalm[1] += vrstica[vrstica.index('">')+2:vrstica.index("</div>")]
            elif '<div style="margin: 10px;' in vrstica:
                nasel = False
            elif "</div><h2>" in vrstica:
                psalm[1] = psalm[1][7:]
                iscem = 7
        elif iscem == 7:
            if '<div class="naslov_berila">' in vrstica:
                evangelij[0] += vrstica[vrstica.index('">')+2:vrstica.index("</div>")]
            elif '<p style="font-style: italic; padding: 10px 0px 10px 0px;">' in vrstica:
                evangelij[1] += vrstica[vrstica.index('">')+2:vrstica.index("</p>")]
                iscem = 8
        elif iscem == 8:
            if "<div style=" in vrstica:
                evangelij[2] += vrstica[0:vrstica.index("<div style=")-6]
                evangelij[2] = evangelij[2][3:]
                break
            elif "<hr" in vrstica:
                break
            else:
                evangelij[2] += vrstica

    file1 = open("ProgramskeDatoteke/sablonaHTML.html", "r", encoding='utf-8')
    html = ""
    for line in file1:
        html += line
    file1.close()
    html = html.format(datum[0:2], datum[3:5], datum[6:10],
                       datum[0:2], datum[3:5], datum[6:10],
                       berilo[0], berilo[1], berilo[2],
                       naslov, razmisljanje, avtor,
                       evangelij[0], evangelij[1], evangelij[2],
                       citat,
                       psalm[0], psalm[1], psalm[2])

    # zapisi v datoteko
    ime_datoteke = "izdelanePriprave/{}-{}-{}.html".format(datum[8:10], datum[3:5], datum[0:2])
    file = open(ime_datoteke, "w", encoding='utf-8')
    file.write(html)
    file.close() 
    return ime_datoteke
