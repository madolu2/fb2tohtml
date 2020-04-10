import xmlparser


xmlp = xmlparser.XMLParser('books\Dorofeev_Dzhedayskie-tehniki-Kak-vospitat-svoyu-obezyanu-opustoshit-inboks-i-sberech-mysletoplivo.SVhkuA.481115.fb2')
print(xmlp.get_text())