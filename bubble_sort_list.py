def bubble_sort(daftar_angka):
    n = len(daftar_angka)
    for i in range(n-1):
        for j in range(n-i-1):
            if daftar_angka[j] < daftar_angka[j+1]:
                daftar_angka[j], daftar_angka[j+1] = daftar_angka[j+1], daftar_angka[j]

#Urutan daftar angka
daftar_angka = [42, 19, 33, 8, 55]

#Memanggil fungsi bubble_sort untuk mengurutkan daftar angka
bubble_sort(daftar_angka)

#Mencetak hasil daftar angka yang telah diurutkan
print("Hasil pengurutan daftar angka secara descending:", daftar_angka)