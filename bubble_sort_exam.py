def bubble_sort(daftar_nilai_ujian):
    n = len(daftar_nilai_ujian)
    for i in range(n-1):
        for j in range(n-i-1):
            if daftar_nilai_ujian[j] > daftar_nilai_ujian[j+1]:
                daftar_nilai_ujian[j], daftar_nilai_ujian[j+1] = daftar_nilai_ujian[j+1], daftar_nilai_ujian[j]

#Urutan daftar nilai ujian siswa
daftar_nilai_ujian = [78, 65, 90, 82, 70]

#Memanggil fungsi bubble_sort untuk mengurutkan daftar nilai
bubble_sort(daftar_nilai_ujian)

#Mencetak hasil nilai ujian siswa yang telah diurutkan
print("Hasil pengurutan nilai ujian siswa secara ascending:", daftar_nilai_ujian)