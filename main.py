# #projektowanie tablicy
# a = np.array([[0,1], [2, 3]])
# print(a)
# #lub drugi sposób
# a = np.arange(2, 5, 0.1)
# print(a)
# #wypisanie typu zmiennej tablicy (nie jej elementów)
# print(type(a))
# #sprawdzanie typu danych tablicy
# print(a.dtype)
# #inicjowanie tablicy z konkretnym typem danych
# a = np.array(2, dtype='int64')
# print(a.dtype)
# #zapisywanie kopii tablicy jako tablicy z innym typem
# b = a.astype('float')
# print(b)
# print(b.dtype)
# #wypisaywanie rozmiaru tablicy
# print(b.shape)
# #może też sprawdzić ilość wymiarów tablicy
# print(a.ndim)
# #stworzenie tablicy wielowymiarowej może wyglądać tak
# #parametrem przekazywanym do funkcji array jest
#
#
#
#
#
#
# zera = np.zeros((5, 5))
# jedynki = np.ones((4, 4))
# print(zera)
# print(jedynki)
# #warto sprawdzić jaki jest domyślny typ danych takich tablic
# print(zera.dtype)
# print(jedynki.dtype)
# #moża również stworzyć "pusta" macierz o podobnych wymiarach
# #wartości umieszczane są losowe najpierw podana jest
# pusta = np.empty((2, 2))
# print(pusta)
#
# macierz = np.array([[12, 11], [2, 1]])
# print(macierz)
# #do elementów tablicy możemy odwołać się tak jak do elementów ?listy?
# poz_1 = macierz[1, 1]
# poz_2 = macierz[0][1]
# print(poz_1)
# print(poz_2)
# #tworzenie macierzy 2x2 wraz z uzupełnieniem
# #macierz = np.array([])
#
#
# # liczby = np.array(1, 2, 0.1)
# # print(liczby)
# #podobnie działa funkcja linspace, która działnie jest
# liczby_lin = np.linspace(1, 2, 5, endpoint=False)
# print(liczby_lin)
# #a teraz możemy utworzyć dwie macierze, napierw wartości
# z = np.indices((5, 3))
# print(z)
# print(z[0][1][2])
# #podobnie jak w MATLAB-ie możemy tworzyć macierze diagonalne
# mat_diag = np.diag([a for a in range(5)])
# print(mat_diag)
# #w powyższym przykładzie stworzmy wektor wartości zostanie
# #możemy podać drugi parametr funcji diag, który określa
# #która zostanie wypełniona wartościami podanego wektora
# mat_diag_k = np.diag([a for a in range(5)], 1)
# print(mat_diag_k)
# #Numpy jest wstanie stworzyć tablice jednowymiarowe z dwona
# z = np.fromiter(range(5), dtype='int32')
# print(z)
# #
# znaki = b'ogolna'
# z1 = np.frombuffer(znaki, dtype='S1')
# print(z1)
# z2 = np.frombuffer(znaki, dtype='S2')
# print(z2)
# #
# #
# #zmiannej teksowej, można podobne efekty osiagnac
# znaki = 'ogolna'
# z3 = np.array(list(znaki))
# z4 = np.array(list(znaki), dtype='S1')
# z5 = np.array(list(b'ogolna'))
# z6 = np.fromiter(znaki, dtype='S1')
# print(z3)
# print(z4)
# print(z5)
# print(z6)
# #
# a = np.arange(10)
# print(a)
# s = slice(2, 7, 2)
# print(a[s])
# s = range(2, 7, 2)
# print(a[s])
# #możemy ciąć tablice również w sposób znane z cięcia lis
# print(a[2:7:2])
# #lub tak
# print(a[1:])
# print(a[2:5])
# #w podobny sposób postępujemy w przypadku tablic wialowymiarowych
# mat = np.arange(25)
# #teraz zmieniamy kształt tablicy jednowymiarowej na macierzy
# mat = mat.reshape((5,5))
# print(mat)
# print(mat[1:]) #od drugiego wiersza
# print(mat[ : ,1 : 2]) #druga kolumna jako wektor
# print(mat[ : , 4 : 5]) #ostatnia kolumna
# print(mat[2 : 6, 1 : 3]) #2 i 3 kolumna dla 3, 4, 5 wierszy
# print(mat[ : , range(2,6,2)]) #3 i 5 kolumna
# print(' ')
# #
# #
# x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# print(x)
# rows = np.array([[0, 0], [3, 3]])
# cols = np.array([[0, 2], [0, 2]])
# y = x[rows, cols]
# print(y)

import numpy as np

#zad1
a = np.arange(0, 4*20+1, 4)
print(a)

#zad2
lista = [1.5, 2.3, 4.7, 3.6, 6,7]
a = np.array(lista)
print(a)
b = a.astype(dtype='int32')
print(b)
c = np.array(lista, dtype='int32')
print(b)

#zad3
def tablica(n):
    a = np.zeros((n*n), dtype='int32')
    for i in range(0, len(a)):
        a[i] = 2**i
    tab = a.reshape((n, n))
    return tab
#
print(tablica(5))

#zad4
def generuj(liczba, ilosc):
    return np.logspace(1, ilosc, num=ilosc, base=liczba)

print(generuj(2,4))

#zad5
def diagonalna(n):
    a = np.arange(n, -1, -1)
    diag = np.diag(a, 2)
    return diag

print(diagonalna(4))

#zad6
malina = np.array(list('malina'))
mrowka = np.array(list('mrówka'))
armata = np.array(list('armata'))
armata = np.flip(armata)

wykreslanka = np.zeros((6,6), dtype='str')

print(wykreslanka)

wykreslanka = np.diag(mrowka)
wykreslanka[:, 0] = malina
#wykreslanka[5,::-1] = armata
wykreslanka[5,:] = armata
print(wykreslanka)
print("")
wykreslanka[:, 0] = mrowka
wykreslanka[5,::-1] = armata
for a in range(6):
    wykreslanka[a,a] = malina[a]
print(wykreslanka)

#zad7
def macierz(n):
    mac = np.zeros((n, n), dtype='int32')
    mac += np.diag([2 for _ in range(n)])
    for i in range(1, n):
        mac += np.diag([2+(2*i) for _ in range(n-i)], k=i)
        mac += np.diag([2+(2*i) for _ in range(n-i)], k=-i)
    print(mac)

macierz(3)

#zad8
def podziel(tab, kierunek='poziomo'):
    print(tab)
    if kierunek == 'poziomo':
        # nieparzysta liczba wierszy
        if tab.shape[0] % 2 != 0:
            print("Tablica posiada nieprzystą liczbę wierszy")
            return
        p1 = tab[0:int(tab.shape[0]/2), :]
        p2 = tab[int(tab.shape[0]/2):, :]
        print("***** część 1 *****")
        print(p1)
        print("***** część 2 *****")
        print(p2)
    elif kierunek == "pionowo":
        if tab.shape[1] % 2 != 0:
            print("Tablica posiada nieprzystą liczbę kolumn")
            return
        p1 = tab[:, 0:int(tab.shape[1]/2)]
        p2 = tab[:, int(tab.shape[1] / 2):]
        print("***** część 1 *****")
        print(p1)
        print("***** część 2 *****")
        print(p2)


podziel(np.arange(36).reshape((6,6)), kierunek='pionowo')

#zad9
def n_ty_wyraz(a1, n, r):
    return a1 + (n-1)*r
#
#
macierz = np.ones(25, dtype='int32')
print(macierz)
for a in range(0, len(macierz), 1):
    element = n_ty_wyraz(4, a+1, 4)
    macierz[a] = element

macierz = macierz.reshape((5, 5))
print(macierz)
