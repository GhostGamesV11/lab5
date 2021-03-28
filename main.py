# zad 1
# class Material:
#     def __init__(self,rodzaj,dlugosc,szerokosc):
#         self.rodzaj = rodzaj
#         self.dlugodsc = dlugosc
#         self.szerokosc = szerokosc
#
#     def wyswietl_nazwe(self):
#         return "Material: {} {} {}".format(self.rodzaj,self.dlugodsc,self.szerokosc)
#
#
# class Ubrania(Material):
#     def __init__(self, rozmiar, kolor, dla_kogo,rodzaj,dlugosc,szerokosc):
#         super().__init__(rodzaj,dlugosc,szerokosc)
#         self.rozmiar = rozmiar
#         self.kolor = kolor
#         self.dla_kogo = dla_kogo
#
#     def wyswietl_dane(self):
#         return "Dane: rozmiar = {} kolor = {} czyja = {}".format(self.rozmiar,self.kolor,self.dla_kogo)
#
#
# class Sweter(Ubrania):
#     def __init__(self, rodzaj_swetra, rozmiar, kolor, dla_kogo, rodzaj, dlugosc, szerokosc):
#         super().__init__(rozmiar, kolor, dla_kogo, rodzaj, dlugosc, szerokosc)
#         self.rodzaj_swetra = rodzaj_swetra
#
#     def wyswietl(self):
#         return "Dane: rodzaj swetra = "+self.rodzaj_swetra
#
# bawelan = Material("naturalny",40,50)
# ubranie = Ubrania("L","czerwony","Janka","zimowy",40,40)
# sweter = Sweter("Rozpinany","XXL","biały","Radek","letni",40,50)
# print(bawelan.wyswietl_nazwe())
# print(ubranie.wyswietl_dane())
# print(sweter.wyswietl())

#zad 2
# class Kwadrat:
#     def __init__(self,x):
#          self.x = x
#     def __add__(self, other):
#         return  Kwadrat(self.x + (4*other.x))
#     def __str__(self):
#         return "Kwadrat o boku = {}".format(self.x)
#
# kwadrat1 = Kwadrat(4)
# kwadrat2 = Kwadrat(6)
# kwadrat3 = kwadrat1 + kwadrat2
# print(kwadrat3)
#
# #zad3
#
# class Kwadratv2:
#     def __init__(self, x):
#         self.x = x
#
#     def __gt__(self, other):
#         return self.x > other.x
#
#     def __lt__(self, other):
#         return self.x < other.x
#
#     def __ge__(self, other):
#         return self.x >= other.x
#
#     def __le__(self, other):
#         return self.x <= other.x
#
#     def __str__(self):
#         return "Kwadrat o boku = {} \n".format(self.x)
#
# kwadratv1 = Kwadratv2(3)
# kwadratv2 = Kwadratv2(4)
# if kwadratv1 > kwadratv2:
#     print("gt")
# if kwadratv1 < kwadratv2:
#     print("lt")
# if kwadratv1 >= kwadratv2:
#     print("ge")
# if kwadratv1 <= kwadratv2:
#     print("le")


#zad 5
# class Osoba:
#     def __init__(self, imie, nazwisko):
#         self.imie = imie
#         self.nazwisko = nazwisko
#
#     def przedstaw_sie(self):
#         return f"{self.imie, self.nazwisko}"
#
#
# class Pracownik(Osoba):
#     def __init__(self, imie, nazwisko, pensja):
#         super().__init__(imie, nazwisko)
#         self.pensja = pensja
#
#     def przedstaw_sie(self):
#         return "{} {} i zarabiam {}".format(self.imie,self.nazwisko,self.pensja)
#
#
# class Menadzer(Pracownik):
#     def __init__(self, imie, nazwisko, pensja):
#         super().__init__(imie, nazwisko, pensja)
#
#     def przedstaw_sie(self):
#         return "{} {} jestem menadzerem i zarabiam {}".format(self.imie,self.nazwisko,self.pensja)
#
# pracownik = Pracownik("Janusz", "Kowalski", 2500)
# menedzer = Menadzer("Sebastian", "Boss", 10000)
# print("Pracownik issubclass:", issubclass(Pracownik, (Osoba, Pracownik, Menadzer)))
# print("Pracownik isinstance:", isinstance(prac, (Osoba, Pracownik, Menadzer)))
# print("Menadzer issubclass:", issubclass(Menadzer, (Osoba, Pracownik, Menadzer)))
# print("Menadzer isinstance:", isinstance(prac, (Osoba, Pracownik, Menadzer)))

#zad 10
# def ciagarytmetyczny(n,a1,r):
#     for x in range(1,n+1):
#         yield f"a{x}={a1+(x-1)*r}"
#
#
# ciag = ciagarytmetyczny(10,2,2)
#
# while 1:
#     try:
#         print(next(ciag))
#     except StopIteration:
#         break