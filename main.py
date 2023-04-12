import numpy as np
#projektowanie tablicy
a = np.array([[0,1], [2, 3]])
print(a)
#lub drugi sposób
a = np.arange(2, 5, 0.1)
print(a)
#wypisanie typu zmiennej tablicy (nie jej elementów)
print(type(a))
#sprawdzanie typu danych tablicy
print(a.dtype)
#inicjowanie tablicy z konkretnym typem danych
a = np.array(2, dtype='int64')
print(a.dtype)
#zapisywanie kopii tablicy jako tablicy z innym typem
b = a.astype('float')
print(b)
print(b.dtype)
#wypisaywanie rozmiaru tablicy
print(b.shape)
#może też sprawdzić ilość wymiarów tablicy
print(a.ndim)
#stworzenie tablicy wielowymiarowej może wyglądać tak
#parametrem przekazywanym do funkcji array jest






zera = np.zeros((5, 5))
jedynki = np.ones((4, 4))
print(zera)
print(jedynki)
#warto sprawdzić jaki jest domyślny typ danych takich tablic
print(zera.dtype)
print(jedynki.dtype)
#moża również stworzyć "pusta" macierz o podobnych wymiarach
#wartości umieszczane są losowe najpierw podana jest
pusta = np.empty((2, 2))
print(pusta)

macierz = np.array([[12, 11], [2, 1]])
print(macierz)
#do elementów tablicy możemy odwołać się tak jak do elementów ?listy?
poz_1 = macierz[1, 1]
poz_2 = macierz[0][1]
print(poz_1)
print(poz_2)
#tworzenie macierzy 2x2 wraz z uzupełnieniem
#macierz = np.array([])


# liczby = np.array(1, 2, 0.1)
# print(liczby)
#podobnie działa funkcja linspace, która działnie jest
liczby_lin = np.linspace(1, 2, 5, endpoint=False)
print(liczby_lin)
#a teraz możemy utworzyć dwie macierze, napierw wartości
z = np.indices((5, 3))
print(z)
print(z[0][1][2])
#podobnie jak w MATLAB-ie możemy tworzyć macierze diagonalne
mat_diag = np.diag([a for a in range(5)])
print(mat_diag)
#w powyższym przykładzie stworzmy wektor wartości zostanie
#możemy podać drugi parametr funcji diag, który określa
#która zostanie wypełniona wartościami podanego wektora
mat_diag_k = np.diag([a for a in range(5)], 1)
print(mat_diag_k)
#Numpy jest wstanie stworzyć tablice jednowymiarowe z dwona
z = np.fromiter(range(5), dtype='int32')
print(z)
#
znaki = b'ogolna'
z1 = np.frombuffer(znaki, dtype='S1')
print(z1)
z2 = np.frombuffer(znaki, dtype='S2')
print(z2)
#
#
#zmiannej teksowej, można podobne efekty osiagnac
znaki = 'ogolna'
z3 = np.array(list(znaki))
z4 = np.array(list(znaki), dtype='S1')
z5 = np.array(list(b'ogolna'))
z6 = np.fromiter(znaki, dtype='S1')
print(z3)
print(z4)
print(z5)
print(z6)
#
a = np.arange(10)
print(a)
s = slice(2, 7, 2)
print(a[s])
s = range(2, 7, 2)
print(a[s])
#możemy ciąć tablice również w sposób znane z cięcia lis
print(a[2:7:2])
#lub tak
print(a[1:])
print(a[2:5])
#w podobny sposób postępujemy w przypadku tablic wialowymiarowych
mat = np.arange(25)
#teraz zmieniamy kształt tablicy jednowymiarowej na macierzy
mat = mat.reshape((5,5))
print(mat)
print(mat[1:]) #od drugiego wiersza
print(mat[ : ,1 : 2]) #druga kolumna jako wektor
print(mat[ : , 4 : 5]) #ostatnia kolumna
print(mat[2 : 6, 1 : 3]) #2 i 3 kolumna dla 3, 4, 5 wierszy
print(mat[ : , range(2,6,2)]) #3 i 5 kolumna
print(' ')
#
#
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print(y)
