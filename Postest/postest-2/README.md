Deskripsi Program
Program Stickyfy Percetakan merupakan sistem pengelolaan pemesanan jasa percetakan berbasis Object-Oriented Programming (OOP). Sistem ini mengintegrasikan empat entitas utama:

1. Pelanggan: Mengelola data pelanggan, nama toko, serta proses pemesanan produk.
2. Produk: Mengelola jenis cetakan dan harga, yang terbagi menjadi produk stiker dan produk spanduk.
3. Pesanan: Memproses transaksi pemesanan, menghitung total harga, serta menyimpan status pesanan.
4. ManajemenPesanan: Menyimpan dan menampilkan daftar pesanan yang masuk.

Penerapan Konsep OOP & Relasi UML
1. Inheritance (Pewarisan)

* Superclass (`Produk`): Menyimpan data dasar produk seperti jenis percetakan (`__jenis_percetakan`) dan harga (`_harga`).
* Subclass 1 (`ProdukStiker`): Turunan dari `Produk` yang memiliki atribut spesifik `ukuran`.
* Subclass 2 (`ProdukSpanduk`): Turunan dari `Produk` yang memiliki atribut spesifik `ukuran_m2`.
* Penggunaan `super()`: Dipanggil pada konstruktor subclass untuk menginisialisasi atribut dari superclass.
* Method Overriding: Method `hitung_harga()` di-override pada `ProdukSpanduk` dengan perhitungan `harga * ukuran_m2 * jumlah`. Method `tampilkan()` juga di-override pada kedua subclass untuk menampilkan detail spesifik tiap produk.
* Access Modifier:
   * Protected (`_harga`): Dapat diakses oleh superclass dan subclass.
   * Private (`__jenis_percetakan`): Eksklusif hanya dapat diakses di dalam class `Produk`.

2. Relasi UML

* Asosiasi (`Pelanggan` - `ManajemenPesanan`): Method `pesan()` pada `Pelanggan` menggunakan objek `ManajemenPesanan` dan `Produk` sebagai parameter untuk memproses pemesanan, tanpa menyimpannya sebagai atribut.
* Agregasi (`Pesanan` - `Pelanggan` dan `Produk`): Class `Pesanan` menampung objek `Pelanggan` dan `Produk` yang dikirim lewat konstruktor. Kedua objek dibuat secara terpisah di luar class dan tetap ada meskipun pesanan atau manajemen dihapus.
* Komposisi (`ManajemenPesanan` - `Pesanan`): Objek `Pesanan` dibuat langsung di dalam method `tambah()` pada `ManajemenPesanan`. Keberadaan `Pesanan` sangat bergantung pada keberadaan objek `ManajemenPesanan`.

Output Program

```
=== Info Toko & Atribut Kelas ===
Nama Toko             : Stickyfy
Daftar Status Pesanan : ['Menunggu', 'Diproses', 'Selesai']

=== Inheritance ===
Pelanggan : Rega
Toko      : Stickyfy
Produk : Stiker Custom A6 | Ukuran: A6 | Harga: Rp2500/pcs
Produk : Spanduk Vinyl | Ukuran: 2 m2 | Harga: Rp25000/m2
True
False
True

=== Asosiasi & Komposisi ===
Rega memesan 50 x Stiker Custom A6
[OK] Pesanan #1 berhasil ditambahkan
Wahyu memesan 2 x Spanduk Vinyl
[OK] Pesanan #2 berhasil ditambahkan

=== Tampilkan Pesanan ===
Pesanan   : #1
Toko      : Stickyfy
Pelanggan : Rega
Produk    : Stiker Custom A6
Jumlah    : 50
Harga     : Rp2500
Total     : Rp125000
Status    : Menunggu
---------------------------------------------
Pesanan   : #2
Toko      : Stickyfy
Pelanggan : Wahyu
Produk    : Spanduk Vinyl
Jumlah    : 2
Harga     : Rp25000
Total     : Rp100000
Status    : Menunggu
---------------------------------------------

=== Class Method & Static Method ===
Produk : Kartu Nama Matte | Harga: Rp1000
True
False

=== Setter & Akses Private ===
[DITERIMA] Jumlah baru: 100
[DITOLAK] Jumlah harus bilangan bulat dan harus lebih dari 0
[DITERIMA] Harga baru: Rp3000
[DITOLAK] Harga harus angka dan harus lebih dari 0
[ERROR] 'Pesanan' object has no attribute '__jumlah'

=== Siklus Hidup Relasi ===
Pelanggan tetap ada : Rega
Produk tetap ada    : Stiker Custom A6
Total Pesanan Masuk di Stickyfy: 2
```
