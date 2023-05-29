# python-sort
pada pertemuan kali ini membahas tentang materi Bubble Sort dan Selection Sort

# Bubble Sort
Bubble Sort adalah algoritma pengurutan sederhana yang membandingkan pasangan elemen secara berurutan dan menukar posisinya jika diperlukan. Elemen yang lebih besar akan "menggelembung" ke arah akhir daftar setiap iterasi.
=> Cara kerjanya itu intinya memulai per literasi, lalu membandingkan elemen pertama dengan elemen kedua, jika elemen pertama lebih besar maka bertukar posisi, seterusnya seperti itu sampai selesai (daftar terurut secara benar).
=> Kelebihan: sederhana & mudah dipahami, implementasi yang mudah, stabilitas. Kekurangan: efisiensi yang rendah, jumlah perbandingan dan pertukaran yang banyak, tidak cocok untuk daftar yang kompleks, worst case dan average case yang sama.

# Selection Sort
Selection Sort adalah algoritma pengurutan yang secara berulang mencari elemen terkecil (atau terbesar) dari sisa daftar dan menukar posisinya dengan elemen pada indeks terkini.
=> Cara kerjanya initnya adalah tentukan elemen terkecil pada sisa daftar yang belum diurutkan lalu tukar dengan elemen pada posisi terkini. Pindah ke posisi terkini berikutnya dan tentukan lagi elemen berikutnya lalu tukar, begitu terus sampai selesai (daftar terurut dengan benar).
=> Kelebihan: sederhana dan mudah dipahami, stabilitas, jumlah pertukaran yang rendah. Kekurangan: efisiensi yang rendah, jumlah perbandingan yang banyak, wosrt case dan average case yang sama, tidak cocok untuk daftar yang kompleks.

# Tentang yang dikerjakan
Praktikum kali ini mengerjakan tujuh percobaan dengan fungsi bubble_sort yaitu: 1). mengurutkan daftar angka secara ascending, 2). Mengurutkan daftar string secara ascending, 3). Mengurutkan daftar angka secara descending, 4). Mengurutkan daftar string secara descending, 5). Mengurutkan sublist dalam daftar, 6). Mengurutkan daftar dengan penggunaan flag, 7). Menghitung jumlah iterasi; tujuh percobaan dengan fungsi selection_sort yaitu: 1). Mengurutkan daftar angka secara ascending, 2). Mengurutkan daftar string secara ascending, 3). Mengurutkan daftar angka secara descending, 4). Mengurutkan daftar string secara descending, 5). Mengurutkan sublist dalam daftar, 6). Mengurutkan daftar dengan penggunaan flag, 7). Menghitung jumlah iterasi; dan lima latihan tentang materi ini, yaitu: mengurutkan daftar nilai secara ascending menggunakan fungsi bubble_sort, mengurutkan daftar angka secara descending menggunakan fungsi bubble_sort, mengurutkan daftar buku berdasarkan jumlah halaman secara ascending menggunakan bubble_sort, mengurutkan daftar angka secara ascending menggunakan selection_sort, mengurutkan daftar pemain berdasarkan jumlah gol yang di cetak secara descending menggunakan selection_sort.
