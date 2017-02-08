orig_Team_key = "OrigTeam"
player_Name_key = "playerName"
year_key = "year"
price_Status_key = "priceStatus" # this key will be remove
dest_Team_key = "DestTeam"
price_key = "price"
type_key = "type"
dest_country_key = "DestCountry"
orig_country_key = "OrigCountry"

start_year = 2007
number_of_seasons = 10

# array of tuples each tuple is : (int: year , string: json file path contains all transferd for this year)
all_years_files_path = []
[all_years_files_path.append((start_year+i, "Transfers_"+str(start_year+i)+"_"+str(start_year+i+1)+".json")) for i in range(number_of_seasons)]


data_dir_path = "crawlerData"


teams_dic = {}

teams_dic["KANSAS CITY"] = ("KANSAS CITY", "USA")
teams_dic["KAPFENBERGER SV"] = ("KAPFENBERGER SV", "Austria")
teams_dic["KARLSRUHER"] = ("KARLSRUHER", "Germany")
teams_dic["KARLSRUHE"] = ("KARLSRUHER", "Germany")
teams_dic["KARPATY LVIV"] = ("KARPATY LVIV" "Ukraine")
teams_dic["KASHIMA ANTLERS"] = ("KASHIMA ANTLERS", "Japan")
teams_dic["KASHIWA REYSOL"] = ("KASHIWA REYSOL", "Japan")
teams_dic["KASIMPASA"] = ("KASIMPASA", "Turkey")
teams_dic["KAWASAKI FRONTALE"] = ("KAWASAKI FRONTALE", "Japan")
teams_dic["KAYSERISPOR"] = ("KAYSERISPOR", "Turkey")
teams_dic["KILMARNOCK"] = ("KILMARNOCK", "Scotland")
teams_dic["KLN"] = ("KOLN", "Germany")
teams_dic["KOLN"] = ("KOLN", "Germany")
teams_dic["KOBENHAVN"] = ("KOBENHAVN", "Denemark")
teams_dic["KOPER"] = ("KOPER", "Slovenia")
teams_dic["KORTRIJK"] = ("KORTRIJK", "Belgium")
teams_dic["KRYLYA S SAMARA"] = ("KRYLYA S SAMARA", "Russia")
teams_dic["KUBAN"] = ("KUBAN", "Russia")
teams_dic["KUBAN KRASNODAR"] = ("KUBAN", "Russia")

teams_dic["LA EQUIDAD"] = ("LA EQUIDAD", "Colombia")
teams_dic["LA GALAXY"] = ("LA GALAXY", "USA")
teams_dic["LANUS"] = ("LANUS", "Argentina")
teams_dic["LAS PALMAS"] = ("LAS PALMAS", "Spain")
teams_dic["LATINA"] = ("LATINA", "Italy")
teams_dic["LAVAL"] = ("LAVAL", "Canada")
teams_dic["LAZIO"] = ("LAZIO", "Italy")
teams_dic["LDU QUITO"] = ("LDU QUITO", "Ecuador")
teams_dic["LE HAVRE"] = ("LE HAVRE", "France")

teams_dic["LE MANS"] = ("LE MANS", "France")
teams_dic["LECCE"] = ("LECCE", "Italy")
teams_dic["LECH POZNAN"] = ("LECH POZNAN", "Poland")
teams_dic["LECHIA GDANSK"] = ("LECHIA GDANSK", "Poland")
teams_dic["LEEDS"] = ("LEEDS", "England")
teams_dic["LEEDS UNITED"] = ("LEEDS", "England")
teams_dic["LEGIA WARSAW"] = ("LEGIA WARSAW", "Poland")
teams_dic["LEGIA WARSZAWA"] = ("LEGIA WARSAW", "Poland")
teams_dic["LEICESTER"] = ("LEICESTER", "England")
teams_dic["LEIXES SC"] = ("LEIXES SC", "Portogal")

teams_dic["LENS"] = ("LENS", "France")
teams_dic["LEVANTE"] = ("LEVANTE", "Spain")
teams_dic["LEVERKUSEN"] = ("LEVERKUSEN", "Germany")
teams_dic["LEVSKI SOFIA"] = ("LEVSKI SOFIA", "Bulgria")
teams_dic["LIBERTY PROFESSIONALS"] = ("LIBERTY PROFESSIONALS", "Ghana")
teams_dic["LIERSE"] = ("LIERSE", "Belgium")
teams_dic["LILLE"] = ("LILLE", "France")
teams_dic["LILLESTROM"] = ("LILLESTROM", "Norway")
teams_dic["LITEX"] = ("LITEX", "Bulgria")
teams_dic["LIV MONTEVIDEO"] = ("LIVERPOOL MONTEVIDEO", "Uruguay")

teams_dic["LIVERPOOL"] = ("LIVERPOOL", "England")
teams_dic["LIVERPOOL DE MONTEVIDEO"] = ("LIVERPOOL MONTEVIDEO", "Uruguay")
teams_dic["LIVORNO"] = ("LIVORNO", "Italy")
teams_dic["LLANEROS"] = ("LLANEROS", "Colombia")
teams_dic["LOKOMOTIV MOSCOW"] = ("LOKOMOTIV MOSCOW", "Russia")
teams_dic["LOKOMOTIV"] = ("LOKOMOTIV MOSCOW", "Russia")
teams_dic["LOK MOSCOW"] = ("LOKOMOTIV MOSCOW", "Russia")

teams_dic["LORIENT"] = ("LORIENT", "France")
teams_dic["LUDOGORETS"] = ("LUDOGORETS", "Bulgria")
teams_dic["LUZERN"] = ("LUZERN", "Switzerland")
teams_dic["LYNGBY"] = ("LYNGBY", "Denemark")
teams_dic["LYON"] = ("LYON", "France")
teams_dic["MACCABI HAIFA"] = ("MACCABI HAIFA", "Israel")
teams_dic["MACCABI TEL AVIV"] = ("MACCABI TEL AVIV", "Israel")

teams_dic["MAINZ"] = ("MAINZ", "Germany")
teams_dic["MALAGA"] = ("MALAGA", "Spain")
teams_dic["MALLORCA"] = ("MALLORCA", "Spain")
teams_dic["MALMO"] = ("MALMO", "Sweden")
teams_dic["MALMO FF"] = ("MALMO", "Sweden")
teams_dic["MALMOE FF"] = ("MALMO", "Sweden")


teams_dic["MANCESTER CITY"] = ("MANCHESTER CITY", "England")
teams_dic["MANCHESTER C"] = ("MANCHESTER CITY", "England")
teams_dic["MANCHESTER CITY"] = ("MANCHESTER CITY", "England")
teams_dic["MANCHESTERY CITY"] = ("MANCHESTER CITY", "England")
teams_dic["MANCHESTER UNITED"] = ("MANCHESTER UNITED", "England")
teams_dic["MANCHESTER UTD"] = ("MANCHESTER UNITED", "England")

teams_dic["MANFREDONIA"] = ("MANFREDONIA", "Italy")
teams_dic["MARIBOR"] = ("MARIBOR", "Slovenia")
teams_dic["MARITIMO"] = ("MARITIMO", "Portugal")
teams_dic["MARSEILLE"] = ("MARSEILLE", "France")
teams_dic["MELBOURNE HEART"] = ("MELBOURNE", "Australia")
teams_dic["MELBOURNE VICTORY"] = ("MELBOURNE", "Australia")

teams_dic["MELFI"] = ("MELFI", "Italy")
teams_dic["MELGAR AREQUIPA"] = ("MELGAR AREQUIPA", "Peru")
teams_dic["MESSINA"] = ("MESSINA", "Italy")

teams_dic["METALIST"] = ("METALIST", "Ukraine")
teams_dic["METALIST KHARKIV"] = ("METALIST", "Ukraine")
teams_dic["METALLURG DONETSK"] = ("METALLURG DONETSK", "Ukraine")
teams_dic["METZ"] = ("METZ", "France")

teams_dic["MFK KOSICE"] = ("MFK KOSICE", "Slovakia")
teams_dic["MIDDLESBROUGH"] = ("MIDDLESBROUGH", "England")
teams_dic["MIDTJYLLAND"] = ("MIDTJYLLAND", "Denemark")
teams_dic["MILAN"] = ("FC MILAN", "Italy")
teams_dic["MJALLBY"] = ("MJALLBY", "Sweden")
teams_dic["MK DONS"] = ("MK DONS", "England")
teams_dic["MODENA"] = ("MODENA", "Italy")
teams_dic["MOGREN"] = ("MOGREN", "Montenegro")
teams_dic["MOLDE"] = ("MOLDE", "Norway")
teams_dic["MOLDE FK"] = ("MOLDE", "Norway")

teams_dic["MONACO"] = ("MONACO", "France")
teams_dic["MONTERREY"] = ("MONTERREY", "Mexico")
teams_dic["MONTPELLIER"] = ("MONTPELLIER", "Mexico")
teams_dic["MOREIRENSE"] = ("MOREIRENSE", "Portugal")

teams_dic["MORELIA"] = ("MORELIA", "Mexico")
teams_dic["MOTAGUA"] = ("MOTAGUA", "Honduras")
teams_dic["MOTAGUA"] = ("MOREIRENSE", "Portugal")
teams_dic["MOTHERWELL"] = ("MOTHERWELL", "Scotland")
teams_dic["MSI RIGHTS"] = ("MSI RIGHTS", "Russia")
teams_dic["MSK ZILINA"] = ("MSK ZILINA", "Slovakia")
teams_dic["MTK BUDAPEST"] = ("MTK BUDAPEST", "Hungary")
teams_dic["MUNICH 1860"] = ("MUNICH 1860", "Germany")
teams_dic["MVV MAASTRICHT"] = ("MVV MAASTRICHT", "Holland")
teams_dic["N CHICAGO"] = ("CHICAGO", "USA")

teams_dic["NAC BREDA"] = ("NAC BREDA", "Holland")
teams_dic["N NACIONAL"] = ("NACIONAL MONTEVIDEO", "Uruguay")
teams_dic["NACIONAL MADEIRA"] = ("NACIONAL MADEIRA", "Portugal")
teams_dic["NACIONAL MONTEVIDEO"] = ("NACIONAL MONTEVIDEO", "Uruguay")
teams_dic["NAFTA"] = ("NAFTA", "Slovenia")
teams_dic["NAGOYA"] = ("NAGOYA", "Japan")
teams_dic["NANTES"] = ("NANTES", "France")
teams_dic["NANCY"] = ("NANTES", "France")
teams_dic["NAPOLI"] = ("NAPOLI", "Italy")

teams_dic["NAUTICO"] = ("NAUTICO", "Brazil")
teams_dic["NEC NIJMEGEN"] = ("NIJMEGEN", "Holland")
teams_dic["NESET FK"] = ("NESET FK", "Norway")
teams_dic["NEUCHATEL XAMAX"] = ("NEUCHATEL XAMAX", "Switzerland")
teams_dic["NEW YORK RED BULLS"] = ("NEW YORK RED BULLS", "USA")
teams_dic["NEWCASTLE"] = ("NEWCASTLE", "England")
teams_dic["NEWCASTLE FC"] = ("NEWCASTLE", "England")
teams_dic["NEWCASTLE JETS"] = ("NEWCASTLE", "England")

teams_dic["NEWELLS"] = ("NEWELLS", "Argentina")
teams_dic["NEWELLS OLD BOYS"] = ("NEWELLS", "Argentina")
teams_dic["NEWPORT COUNTY"] = ("NEWPORT COUNTY", "England")
teams_dic["NICE"] = ("NICE", "France")
teams_dic["NIORT"] = ("NIORT", "France")

teams_dic["NK DOMZALE"] = ("NK DOMZALE", "Slovania")
teams_dic["NK MARIBOR"] = ("NK MARIBOR", "Slovenia")
teams_dic["NK ZAGREB"] = ("NK ZAGREB", "Croatia")
teams_dic["NORDSJAELLAND"] = ("NORDSJAELLAND", "Denemark")
teams_dic["NORTHAMPTON"] = ("NORTHAMPTON", "England")
teams_dic["NORWICH"] = ("NORWICH", "England")
teams_dic["NORWICH CITY"] = ("NORWICH", "England")


teams_dic["NOTTINGHAM FOREST"] = ("NOTTINGHAM FOREST", "England")
teams_dic["NOTT FOREST"] = ("NOTTINGHAM FOREST", "England")
teams_dic["NOTTS COUNTY"] = ("NOTTS COUNTY", "England")
teams_dic["NOVARA"] = ("NOVARA", "Italy")
teams_dic["NUMANCIA"] = ("NUMANCIA", "Spain")
teams_dic["NURNBERG"] = ("NURNBERG", "Germany")
teams_dic["NUREMBERG"] = ("NURNBERG", "Germany")

teams_dic["NY RED BULLS"] = ("NY RED BULLS", "USA")
teams_dic["NY RED BULLS"] = ("NY RED BULLS", "USA")
teams_dic["O HIGGINS"] = ("O HIGGINS", "Chile")
teams_dic["ODENSE"] = ("ODENSE", "Denemark")
teams_dic["OFI CRETE"] = ("OFI CRETE", "Greece")
teams_dic["OFI FC"] = ("OFI CRETE", "Greece")
teams_dic["OFK BELGRADE"] = ("OFK BELGRAD", "Serbia")
teams_dic["OFK BEOGRAD"] = ("OFK BELGRAD", "Serbia")
teams_dic["OFK BEOGRAD"] = ("NURNBERG", "Germany")
teams_dic["OH LEUVEN"] = ("OH LEUVEN", "Belgium")
teams_dic["OLDHAM"] = ("OLDHAM", "England")
teams_dic["OLHANENSE"] = ("OLHANENSE", "Portugal")

teams_dic["OLYMP MARSEILLE"] = ("MARSEILLE", "France")
teams_dic["OLYMPIQUE MARSEILLE"] = ("MARSEILLE", "France")
teams_dic["OLYMPIACOS"] = ("OLYMPIAKOS", "Greece")
teams_dic["OLYMPIAKOS"] = ("OLYMPIAKOS", "Greece")
teams_dic["ONCE CALDAS"] = ("ONCE CALDAS", "Colombia")
teams_dic["ORDUSPOR"] = ("ORDUSPOR", "Turkey")
teams_dic["OREBRO"] = ("OREBRO", "Sweden")
teams_dic["OSASUNA"] = ("OSASUNA", "Spain")
teams_dic["OSTERSUNDS"] = ("OSTERSUNDS", "Sweden")
teams_dic["P EJIDO"] = ("EJIDO", "Spain")
teams_dic["PACHUCA"] = ("PACHUCA", "Mexico")
teams_dic["PACOS FERREIRA"] = ("PACOS FERREIRA", "Portugal")
teams_dic["PACOS FERREITA"] = ("PACOS FERREIRA", "Portugal")
teams_dic["PADERBORN"] = ("PADERBORN", "Germany")
teams_dic["PADROENSE"] = ("PADROENSE", "Portugal")
teams_dic["PALERMO"] = ("PALERMO", "Italy")
teams_dic["PALERMA"] = ("PALERMO", "Italy")
teams_dic["PALMEIRAS"] = ("PALMEIRAS", "Brazil")
teams_dic["PANATHINAIKOS"] = ("PANATHINAIKOS", "Greece")
teams_dic["PANDURII"] = ("PANDURII", "Romania")
teams_dic["PAOK"] = ("PAOK SALONIKA", "Greece")
teams_dic["PAOK SALONIKA"] = ("PAOK SALONIKA", "Greece")
teams_dic["PARAGUAY"] = ("PARAGUAY FC", "Paraguay")
teams_dic["PARIS SG"] = ("PARIS SG", "France")
teams_dic["PARIS SAINTGERMAIN"] = ("PARIS SG", "France")
teams_dic["PARIS SAINT GERMAIN"] = ("PARIS SG", "France")
teams_dic["PARMA"] = ("PARMA", "Italy")

teams_dic["PARTIZAN BELGRADE"] = ("PARTIZAN BELGRADE", "Serbia")
teams_dic["PARTIZAN"] = ("PARTIZAN BELGRADE", "Serbia")
teams_dic["PAS GIANNINA"] = ("PAS GIANNINA", "Greece")
teams_dic["PENAROL"] = ("PENAROL", "Uruguay")
teams_dic["PESCARA"] = ("PESCARA", "Italy")
teams_dic["PESCARA CALCIO"] = ("PESCARA", "Italy")
teams_dic["PETERBOROUGH"] = ("PETERBOROUGH", "England")
teams_dic["PIACENZA"] = ("PIACENZA", "Italy")
teams_dic["PISA CALCIO"] = ("PISA CALCIO", "Italy")
teams_dic["POLI TIMISOARA"] = ("POLI TIMISOARA", "Romonia")
teams_dic["POLONIA"] = ("POLONIA", "Poland")
teams_dic["PONFERRADINA"] = ("PONFERRADINA", "Spain")
teams_dic["PONTE PRETA"] = ("PONTE PRETA", "Brazil")
teams_dic["PORTO"] = ("PORTO", "Portugal")
teams_dic["PORTSMOUTH"] = ("PORTSMOUTH", "England")
teams_dic["POTENZA"] = ("POTENZA", "Italy")
teams_dic["PRESOV"] = ("PRESOV", "Slovakia")
teams_dic["PRESTON"] = ("PRESTON", "England")
teams_dic["PROGRESO"] = ("PROGRESO", "Mexico")
teams_dic["PSG"] = ("PARIS SG", "France")
teams_dic["PSV"] = ("PSV EINDHOVEN", "Holland")
teams_dic["PSV EINDHOVEN"] = ("PSV EINDHOVEN", "Holland")
teams_dic["PUERTOLLANO"] = ("PUERTOLLANO", "Spain")
teams_dic["QPR"] = ("QPR", "England")
teams_dic["QRP"] = ("QPR", "England")
teams_dic["QUINDIO"] = ("QUINDIO", "Colombia")
teams_dic["R C AVELLANEDA"] = ("R C AVELLANEDA", "Argentina")
teams_dic["R SALT LAKE"] = ("R SOLT LAKE", "USA")
teams_dic["RACING SANTANDER"] = ("RACING SANTANDER", "Spain")
teams_dic["RACING CLUB"] = ("RACING SANTANDER", "Spain")
teams_dic["R SANTANDER"] = ("RACING SANTANDER", "Spain")
teams_dic["R SOCIEDAD"] = ("REAL SOCIEDAD", "Spain")
teams_dic["RAD"] = ("RAD", "Serbia")
teams_dic["RAKOSPALOTAI"] = ("RAKOSPALOTAI", "Hungary")
teams_dic["RANGERS"] = ("RANGERS", "Scotland")
teams_dic["RAPID VIENNA"] = ("RAPID VIENNA", "Austria")
teams_dic["RAPID WIEN"] = ("RAPID VIENNA", "Austria")
teams_dic["RAYO VALLECANO"] = ("RAYO VALLECANO", "Spain")
teams_dic["READING"] = ("READING", "England")
teams_dic["REAL BETIS"] = ("REAL BETIS", "Spain")