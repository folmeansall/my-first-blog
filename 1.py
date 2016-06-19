uzytkownicy = {}
logged = None
def rejestracja():
	print('Imię?')
	imie = input()
	print('Hasło?')
	haslo =hash(input())
	uzytkownicy[imie] = {'pass':haslo, 'posty':[]}
def logowanie ():
	global logged
	print('Imię?')
	imie = input()
	print('Hasło?')
	while not logged:
		print("Wpisz poprawne hasło:")
		haslo =hash(input())
		haslozbazy=uzytkownicy[imie]['pass']	
		if haslo == haslozbazy:
			print("Zalogowano")
			logged = imie
	
		else:
			print("Niepoprawne")
			print("Spróbuj ponownie:")

	

funkcje = {'rejestracja': rejestracja, 'logowanie':logowanie}

def main ():
	while 1:
		print(uzytkownicy)
		komenda = input()
		if komenda not in funkcje:
			print("Nie znam takiej funkcji")
		else:
			funkcje[komenda]()
			
				
main()
