class Pelanggan:
    nama_toko = "Stickyfy"

    def __init__(self, nama):
        if not Pelanggan.cek_nama(nama):
            raise ValueError("Nama Pelanggan Tidak Boleh Kosong..")
        self.nama = nama

    def tampilkan(self):
        print(f"Pelanggan : {self.nama}")
        print(f"Toko      : {Pelanggan.nama_toko}")

    def pesan(self, manajemen, produk, jumlah):
        print(f"{self.nama} memesan {jumlah} x {produk.jenis_percetakan}")
        return manajemen.tambah(self, produk, jumlah)

    @staticmethod
    def cek_nama(nama):
        return isinstance(nama, str) and nama.strip() != ""


class Produk:
    def __init__(self, jenis_percetakan, harga):
        self.__jenis_percetakan = jenis_percetakan
        self.harga = harga

    @property
    def jenis_percetakan(self):
        return self.__jenis_percetakan

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, harga_baru):
        if not isinstance(harga_baru, (int, float)) or harga_baru <= 0:
            raise ValueError("Harga harus angka dan harus lebih dari 0")
        self._harga = harga_baru

    def hitung_harga(self, jumlah):
        return self._harga * jumlah

    def tampilkan(self):
        print(f"Produk : {self.jenis_percetakan} | Harga: Rp{self.harga}")

    @classmethod
    def dari_dict(cls, data):
        return cls(data["jenis_percetakan"], data["harga"])


class ProdukStiker(Produk):
    def __init__(self, jenis_percetakan, harga, ukuran):
        super().__init__(jenis_percetakan, harga)
        self.ukuran = ukuran

    def tampilkan(self):
        print(f"Produk : {self.jenis_percetakan} | Ukuran: {self.ukuran} | Harga: Rp{self.harga}/pcs")


class ProdukSpanduk(Produk):
    def __init__(self, jenis_percetakan, harga, ukuran_m2):
        super().__init__(jenis_percetakan, harga)
        self.ukuran_m2 = ukuran_m2

    def hitung_harga(self, jumlah):
        return self._harga * self.ukuran_m2 * jumlah

    def tampilkan(self):
        print(f"Produk : {self.jenis_percetakan} | Ukuran: {self.ukuran_m2} m2 | Harga: Rp{self.harga}/m2")


class Pesanan:
    total_pesanan = 0
    daftar_status = ["Menunggu", "Diproses", "Selesai"]

    def __init__(self, pelanggan, produk, jumlah):
        self.pelanggan = pelanggan
        self.produk = produk
        self.harga_satuan = produk.harga
        self.status = "Menunggu"
        self.jumlah = jumlah

        Pesanan.total_pesanan += 1
        self.id_pesanan = Pesanan.total_pesanan

    @property
    def jumlah(self):
        return self.__jumlah

    @jumlah.setter
    def jumlah(self, jumlah_baru):
        if not isinstance(jumlah_baru, int) or jumlah_baru <= 0:
            raise ValueError("Jumlah harus bilangan bulat dan harus lebih dari 0")
        self.__jumlah = jumlah_baru

    @property
    def total_harga(self):
        return self.hitung_total()

    def hitung_total(self):
        return self.produk.hitung_harga(self.jumlah)

    def tampilkan(self):
        print(f"Pesanan   : #{self.id_pesanan}")
        print(f"Toko      : {Pelanggan.nama_toko}")
        print(f"Pelanggan : {self.pelanggan.nama}")
        print(f"Produk    : {self.produk.jenis_percetakan}")
        print(f"Jumlah    : {self.jumlah}")
        print(f"Harga     : Rp{self.harga_satuan}")
        print(f"Total     : Rp{self.total_harga}")
        print(f"Status    : {self.status}")


class ManajemenPesanan:
    def __init__(self):
        self._daftar_pesanan = []

    def tambah(self, pelanggan, produk, jumlah):
        pesanan = Pesanan(pelanggan, produk, jumlah)
        self._daftar_pesanan.append(pesanan)
        print(f"[OK] Pesanan #{pesanan.id_pesanan} berhasil ditambahkan")
        return pesanan

    def tampilkan(self):
        if not self._daftar_pesanan:
            print("(belum ada pesanan)")
        for pesanan in self._daftar_pesanan:
            pesanan.tampilkan()
            print("-" * 45)


pelanggan1 = Pelanggan("Rega")
pelanggan2 = Pelanggan("Wahyu")
produk1 = ProdukStiker("Stiker Custom A6", 2500, "A6")
produk2 = ProdukSpanduk("Spanduk Vinyl", 25000, 2)

print("=== Info Toko & Atribut Kelas ===")
print(f"Nama Toko             : {Pelanggan.nama_toko}")
print(f"Daftar Status Pesanan : {Pesanan.daftar_status}")

print("\n=== Inheritance ===")
pelanggan1.tampilkan()
produk1.tampilkan()
produk2.tampilkan()
print(isinstance(produk1, Produk))
print(isinstance(produk2, ProdukStiker))
print(issubclass(ProdukSpanduk, Produk))

print("\n=== Asosiasi & Komposisi ===")
manajemen = ManajemenPesanan()
pesanan1 = pelanggan1.pesan(manajemen, produk1, 50)
pelanggan2.pesan(manajemen, produk2, 2)

print("\n=== Tampilkan Pesanan ===")
manajemen.tampilkan()

print("\n=== Class Method & Static Method ===")
produk3 = Produk.dari_dict({"jenis_percetakan": "Kartu Nama Matte", "harga": 1000})
produk3.tampilkan()
print(Pelanggan.cek_nama("Rega"))
print(Pelanggan.cek_nama(""))

print("\n=== Setter & Akses Private ===")
try:
    pesanan1.jumlah = 100
    print(f"[DITERIMA] Jumlah baru: {pesanan1.jumlah}")
    pesanan1.jumlah = -10
except ValueError as e:
    print(f"[DITOLAK] {e}")

try:
    produk1.harga = 3000
    print(f"[DITERIMA] Harga baru: Rp{produk1.harga}")
    produk1.harga = -5000
except ValueError as e:
    print(f"[DITOLAK] {e}")

try:
    print(pesanan1.__jumlah)
except AttributeError as e:
    print(f"[ERROR] {e}")

print("\n=== Siklus Hidup Relasi ===")
del manajemen
print(f"Pelanggan tetap ada : {pelanggan1.nama}")
print(f"Produk tetap ada    : {produk1.jenis_percetakan}")
print(f"Total Pesanan Masuk di {Pelanggan.nama_toko}: {Pesanan.total_pesanan}")