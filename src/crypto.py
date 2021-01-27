import timeit
import os

path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)


# Pengganti fungsi len()
def sebutSajaLen(kata):
    panjang = 0
    for i in kata:
        panjang += 1
    return panjang


# Mengecheck apakah huruf unik
def isArrayHurufUnique(huruf, arrayHuruf):
    for i in arrayHuruf:
        if (huruf == i):
            return False
    return True


# Mencari posisi huruf pada Index
def findIndex(text, arrayHuruf, panjang):
    arrayIndex = [-1 for i in range(panjang)]
    iterasi = 0
    for i in text:
        index = 0
        for j in arrayHuruf:
            if i == j:
                arrayIndex[iterasi] = index
                iterasi += 1
            index += 1
    return arrayIndex


# Membuat array yang berisi karakter unik dari array kata
def createUniqueChar(arrayKata):
    arrayHuruf = []
    for kata in arrayKata:
        for huruf in kata:
            if isArrayHurufUnique(huruf, arrayHuruf):
                arrayHuruf = arrayHuruf + [huruf]
    return arrayHuruf


# Membuat Matrix karakter unik dan valuenya
def createMatrixChar(arrayUniqueChar):
    kolom = sebutSajaLen(arrayUniqueChar)
    matrixChar = [[-1 for i in range(kolom)] for j in range(2)]
    index = 0
    for i in arrayUniqueChar:
        matrixChar[0][index] = i
        index += 1
    if (kolom != 10):
        matrixChar[1] += [-1 for i in range(10-kolom)]
    return matrixChar


# Membuat matrix yang berisi huruf dan posisinya
def createMatrixPosisiKata(arrayKata, arrayHuruf):
    baris = sebutSajaLen(arrayKata)
    kolom = sebutSajaLen(arrayKata[0])
    for i in range(baris):
        if (kolom < sebutSajaLen(arrayKata[i])):
            kolom = sebutSajaLen(arrayKata[i])
    matrixPosisiKata = [[-1 for i in range(kolom)] for j in range(baris)]
    for i in range(baris):
        arrayPosisiKata = findIndex(arrayKata[i], arrayHuruf, kolom)
        for j in range(kolom):
            matrixPosisiKata[i][j] = arrayPosisiKata[j]
    return matrixPosisiKata


# Mengubah indexPosisi menjadi isi matrix
def indexToString(matrixPosisiKata, arrayAngka):
    baris = sebutSajaLen(matrixPosisiKata)
    kolom = sebutSajaLen(matrixPosisiKata[0])
    arrayIndexToString = [-1 for i in range(baris)]
    for i in range(baris):
        string = ""
        for j in range(kolom):
            if (matrixPosisiKata[i][j] != -1):
                string += str(arrayAngka[matrixPosisiKata[i][j]])
        arrayIndexToString[i] = string
    return arrayIndexToString


# Mengecek angka awal, agar tidak dimulai dengan 0
def cekAngkaAwal(arrayAngka):
    for i in range(sebutSajaLen(arrayAngka)):
        if (int(arrayAngka[i][:1]) == 0):
            return False
    return True


# Membaca file dan mengubah ke array
def bacaFile(namaFile):
    filepath = str(os.getcwd())+"/test/"+str(namaFile)
    array = []
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            if ("{}".format(line.strip())) != "--------":
                array += [("{}".format(line.strip()))]
            line = fp.readline()
    index = sebutSajaLen(array)
    array[index-2] = (array[index-2][:-1])
    return array


# Mengecek hasil jawaban
def cekJawaban(arrayIndexToString):
    index = sebutSajaLen(arrayIndexToString)
    jawaban = 0
    for i in range(index-1):
        jawaban += int(arrayIndexToString[i])
    if (jawaban == int(arrayIndexToString[index-1])):
        return True
    else:
        return False


# Mengecek apakah ada nilai yang sama
def checkSama(a, b, c, d, e, f, g, h, i, j):
    if (a == b or a == c or a == d or a == e or a == f or a == g or a == h or a == i or a == j):
        return False
    elif (b == c or b == d or b == e or b == f or b == g or b == h or b == i or b == j):
        return False
    elif (c == d or c == e or c == f or c == g or c == h or c == i or c == j):
        return False
    elif (d == e or d == f or d == g or d == h or d == i or d == j):
        return False
    elif (e == f or e == g or e == h or e == i or e == j):
        return False
    elif (f == g or f == h or f == i or f == j):
        return False
    elif (g == h or g == i or g == j):
        return False
    elif (h == i or h == j):
        return False
    elif (i == j):
        return False
    else:
        return True


# Buat ngeprint soal
def cetakSoal(arrayKata):
    index = sebutSajaLen(arrayKata)
    for i in range(index):
        if (i == index-1):
            print("+ ----------")
        print(f'{arrayKata[i]:>12}')


# Main Menu
print("Cryptarithmetic Solver\n")
print("Menu : ")
print("1. Manual Input")
print("2. File Input\n")
option = int(input("Your option : "))

state = True
while state:
    if option == 1:
        arrayKata = []
        banyak = int(input("Masukkan banyak kata : "))
        for i in range(banyak):
            arrayKata += [input("Masukkan kata : ")]
        print("\n")
        state = False
    elif option == 2:
        namaFile = input("Masukkan nama file : ")
        arrayKata = bacaFile(namaFile)
        state = False
    else:
        print("Invalid input")
        option = int(input("Your option : "))


# Mulai menghitung waktu
start_time = timeit.default_timer()

# Cetak kata
cetakSoal(arrayKata)
print("\n")

# Membuat array berisi karakter unik dari arrayKata
arrayHuruf = createUniqueChar(arrayKata)

# Membuat matrix dari array huruf dan arrayAngka
matrixKarakter = (createMatrixChar(arrayHuruf))

# Mecari posisi dari arrayKata
matrixPosisi = (createMatrixPosisiKata(arrayKata, arrayHuruf))


jumlahTest = 0
totalTest = 0


# Memulai Brute Force
for a in range(10):
    for b in range(10):
        if (checkSama(a, b, "c", "d", "e", "f", "g", "h", "i", "j")):
            for c in range(10):
                if (checkSama(a, b, c, "d", "e", "f", "g", "h", "i", "j")):
                    for d in range(10):
                        if (checkSama(a, b, c, d, "e", "f", "g", "h", "i", "j")):
                            for e in range(10):
                                if (checkSama(a, b, c, d, e, "f", "g", "h", "i", "j")):
                                    for f in range(10):
                                        if (checkSama(a, b, c, d, e, f, "g", "h", "i", "j")):
                                            for g in range(10):
                                                if (checkSama(a, b, c, d, e, f, g, "h", "i", "j")):
                                                    for h in range(10):
                                                        if (checkSama(a, b, c, d, e, f, g, h, "i", "j")):
                                                            for i in range(10):
                                                                if (checkSama(a, b, c, d, e, f, g, h, i, "j")):
                                                                    for j in range(10):
                                                                        jumlahTest += 1
                                                                        if (checkSama(a, b, c, d, e, f, g, h, i, j)):
                                                                            matrixKarakter[1] = [
                                                                                a, b, c, d, e, f, g, h, i, j]
                                                                            if (cekJawaban(indexToString(matrixPosisi, matrixKarakter[1]))):
                                                                                if (cekAngkaAwal(indexToString(matrixPosisi, matrixKarakter[1]))):
                                                                                    totalTest = jumlahTest
                                                                                    cetakSoal(indexToString(
                                                                                        matrixPosisi, matrixKarakter[1]))
                                                                                    print(
                                                                                        "\n")

# Mencetak banyak test
print(f"Banyak percobaan : {totalTest}")

# Mencetak Waktu
print("Waktu yang dibutuhkan : "+str(timeit.default_timer() - start_time))
