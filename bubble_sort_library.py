def bubble_sort(daftar_buku):
    n = len(daftar_buku)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if int(daftar_buku[j][2]) > int(daftar_buku[j + 1][2]):
                daftar_buku[j], daftar_buku[j + 1] = daftar_buku[j + 1], daftar_buku[j]

#Daftar buku (Judul Buku, Penulis, Jumlah Halaman)
daftar_buku = [
    ["Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "320"],
    ["To Kill a Mockingbird", "Harper Lee", "281"],
    ["The Great Gatsby", "F. Scott Fitzgerald", "180"],
    ["Pride and Prejudice", "Jane Austen", "432"],
    ["1984", "George Orwell", "328"]
]

#Memanggil fungsi bubble_sort untuk mengurutkan daftar buku
bubble_sort(daftar_buku)

#Mencetak hasil pengurutan daftar buku
print("Hasil pengurutan daftar buku berdasarkan jumlah halaman secara ascending:")
for item in daftar_buku:
    print(item)