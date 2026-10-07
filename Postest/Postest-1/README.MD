# README.md

## Penjelasan Program

## Struktur Class

Program ini terdiri dari 3 class utama:

### 1. Class `Pelanggan`
Mengelola informasi data pembeli.
* **Atribut Kelas**:
  * `nama_toko`: Menyimpan nama toko ("Stickyfy").
* **Atribut Instance**:
  * `nama`: Nama dari pelanggan.
* **Method**:
  * `__init__(nama)`: Constructor untuk menginstansiasi pelanggan serta memeriksa kevalidan nama.
  * `tampilkan()`: Menampilkan nama pelanggan dan nama toko.
  * `cek_nama(nama)` (`@staticmethod`): Memastikan input nama bertipe `str` dan tidak berupa string kosong.

### 2. Class `Produk`
Mengelola barang/layanan percetakan beserta harganya.
* **Atribut Instance**:
  * `jenis_percetakan`: Nama barang/layanan cetak.
  * `__harga`: Atribut private untuk menyimpan harga produk.
* **Encapsulation (Getter & Setter)**:
  * `@property harga`: Mengembalikan nilai private `__harga`.
  * `@harga.setter`: Memvalidasi agar nilai harga bertipe angka (`int` atau `float`) dan bernilai lebih besar dari 0.
* **Method**:
  * `tampilkan()`: Menampilkan jenis percetakan dan harga produk.
  * `dari_dict(data)` (`@classmethod`): Alternative constructor untuk membuat objek `Produk` langsung dari dictionary.

### 3. Class `Pesanan`
Mengintegrasikan objek `Pelanggan` dan `Produk` ke dalam satu transaksi.
* **Atribut Kelas**:
  * `total_pesanan`: Menghitung total transaksi pesanan yang terbuat secara akumulatif.
  * `daftar_status`: List pilihan status transaksi (`["Menunggu", "Diproses", "Selesai"]`).
* **Atribut Instance**:
  * `id_pesanan`: Kode urutan pesanan otomatis berbasis `total_pesanan`.
  * `pelanggan`: Objek dari class `Pelanggan`.
  * `produk`: Objek dari class `Produk`.
  * `harga_satuan`: Menyimpan nilai harga produk saat pesanan dibuat.
  * `status`: Status pengerjaan pesanan (default: "Menunggu").
  * `__jumlah`: Atribut private untuk menyimpan kuantitas pesanan.
* **Encapsulation (Getter & Setter)**:
  * `@property jumlah`: Mengembalikan nilai private `__jumlah`.
  * `@jumlah.setter`: Memvalidasi agar jumlah pesanan bertipe integer (`int`) dan bernilai lebih dari 0.
  * `@property total_harga`: Properti hitung otomatis yang mengembalikan hasil kalkulasi dari method `hitung_total()`.
* **Method**:
  * `hitung_total()`: Menghitung total biaya (`harga_satuan * jumlah`).
  * `tampilkan()`: Menampilkan rincian lengkap dari transaksi pesanan.

---

## Panduan Pengujian Program

Eksekusi program pada `Main Code` menjalankan 6 tahapan pengujian berikut:

1. **Info Toko & Atribut Kelas**:
   * Menampilkan nilai atribut kelas `Pelanggan.nama_toko` dan `Pesanan.daftar_status`.
2. **Tes Bikin Objek & Metode**:
   * Membuat objek pelanggan (`pelanggan1`, `pelanggan2`) dan produk (`produk1`, `produk2`).
   * Membuat objek transaksi (`pesanan1`, `pesanan2`).
   * Memanggil method `tampilkan()` pada setiap objek untuk memeriksa tampilan detailnya.
3. **Tes Class Method**:
   * Membuat objek `produk3` memanfaatkan class method `Produk.dari_dict()`.
4. **Tes Static Method**:
   * Menguji fungsi `Pelanggan.cek_nama()` untuk memvalidasi string nama valid dan string kosong (`""`).
5. **Tes Setter & Validasi**:
   * **Uji Nilai Valid**: Pengujian `pesanan1.jumlah = 100` dan `produk1.harga = 3000` (berhasil diperbarui).
   * **Uji Nilai Negatif**: Pengujian `pesanan1.jumlah = -10` dan `produk1.harga = -5000` (ditolak oleh setter dan ditangkap oleh blok `try-except`).
   * **Uji Proteksi Enkapsulasi**: Mencoba mengakses langsung `pesanan1.__jumlah` dari luar kelas yang menghasilkan `AttributeError`.
6. **Ringkasan Data**:
   * Menampilkan total pesanan akhir menggunakan `Pesanan.total_pesanan`.