import pathlib
from sys import argv

import csv
import  os
dane = []
#sprawdzamy czy mamy conajmniej 2 argumenty
if argv.__len__() < 3:
	print("za mało argumentów")
	exit()
	# Sprawdzamy czy istnieje katalog/plik
if  os.path.exists(argv[1]):
	# sprawadzamy czy to jest plik
	if os.path.isfile(argv[1]):
		# otwieramy plik
		with open(argv[1], newline="") as f:
			reader = csv.reader(f,delimiter=';')
			for line in reader:
				dane.append(line)
		# analizujemy argumenty zmian
		for i in range(3, len(argv)):
			parametr = argv[i]
			p = parametr.split(',')
			x = int(p[0])
			y = int(p[1])
			if y >= dane.__len__() or x >= dane[y].__len__():
				print("wpolrzedne z poza rozmiaru tablicy")
				continue
			else:
				dane[y][x] = p[2]
		# Fw otwarty plik do zapisu
		with open(argv[2], "w", newline="") as fw:
			writer = csv.writer(fw)
			for i in dane:
				writer.writerow(i)

	else:
		# istnieje a to nie jest plik czyli katalog
		katalog = pathlib.Path(argv[1])
		for plik in katalog.glob('*.csv'):
			print(plik)
else:
	# wyciągamy nazwe katalogu (Folderu)
	sciezka = os.path.dirname(argv[1])
	# sprawdzamy czy istnieje i czy jest Katalogiem(nie jest plikien)
	if os.path.exists(sciezka) and os.path.isfile(sciezka) == False:
		katalog = pathlib.Path(sciezka)
		# wyswietlamy wszystkie pliki w Katalogu (Folderze)
		for plik in katalog.glob('*.csv'):
			print(plik)
	else:
		print("nie istnieje plik lub katolog pod podana sciezka")	#nie istnieje





