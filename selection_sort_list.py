def selection_sort(daftar_angka):
    n = len(daftar_angka)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if daftar_angka[j] < daftar_angka[min_index]:
                min_index = j
        daftar_angka[i], daftar_angka[min_index] = daftar_angka[min_index], daftar_angka[i]

#Daftar angka
daftar_angka = [9, 5, 3, 8, 2]

#Memanggil fungsi selection_sort untuk mengurutkan daftar angka
selection_sort(daftar_angka)

#Mencetak hasil daftar angka yang diurutkan secara ascending
print("Hasil pengurutan:", daftar_angka)