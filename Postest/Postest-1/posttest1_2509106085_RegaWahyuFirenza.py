class Pelanggan:
    nama_toko = "Stickyfy"

    def __init__(self, nama):
        if not Pelanggan.cek_nama(nama):
            raise ValueError("Nama Pelanggan Tidak Boleh Kosong..")
        self.nama = nama

    def tampilkan(self):
        print(f"Pelanggan : {self.nama}")
        print(f"Toko      : {Pelanggan.nama_toko}")

    @staticmethod
    def cek_nama(nama):
        return isinstance(nama, str) and nama.strip() != ""


class Produk:
    def __init__(self, jenis_percetakan, harga):
        self.jenis_percetakan = jenis_percetakan
        self.harga = harga

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, harga_baru):
        if not isinstance(harga_baru, (int, float)) or harga_baru <= 0:
            raise ValueError("Harga harus angka dan harus lebih dari 0")
        self.__harga = harga_baru

    def tampilkan(self):
        print(f"Produk : {self.jenis_percetakan} | Harga: Rp{self.harga}")

    @classmethod
    def dari_dict(cls, data):
        return cls(data["jenis_percetakan"], data["harga"])


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
        return self.harga_satuan * self.jumlah

    def tampilkan(self):
        print(f"Pesanan   : #{self.id_pesanan}")
        print(f"Toko      : {Pelanggan.nama_toko}")
        print(f"Pelanggan : {self.pelanggan.nama}")
        print(f"Produk    : {self.produk.jenis_percetakan}")
        print(f"Jumlah    : {self.jumlah}")
        print(f"Harga     : Rp{self.harga_satuan}")
        print(f"Total     : Rp{self.total_harga}")
        print(f"Status    : {self.status}")


print(f"{'='*45}")
print(f"{'1. INFO TOKO & ATRIBUT KELAS':^45}")
print(f"{'='*45}")
print(f"Nama Toko             : {Pelanggan.nama_toko}")
print(f"Daftar Status Pesanan : {Pesanan.daftar_status}")

print(f"\n{'='*45}")
print(f"{'2. TES BIKIN OBJEK & METODE':^45}")
print(f"{'='*45}")
pelanggan1 = Pelanggan("Rega")
pelanggan2 = Pelanggan("Wahyu")

produk1 = Produk("Stiker Custom A6", 2500)
produk2 = Produk("Spanduk Vinyl", 25000)

pesanan1 = Pesanan(pelanggan1, produk1, 50)
pesanan2 = Pesanan(pelanggan2, produk2, 2)

pelanggan1.tampilkan()
print(f"{'-'*45}")
produk1.tampilkan()
print(f"{'-'*45}")
pesanan1.tampilkan()
print(f"{'-'*45}")
pesanan2.tampilkan()

print(f"\n{'='*45}")
print(f"{'3. TES CLASS METHOD':^45}")
print(f"{'='*45}")
data_produk = {"jenis_percetakan": "Kartu Nama Matte", "harga": 1000}
produk3 = Produk.dari_dict(data_produk)
print("Bikin produk3 pake Produk.dari_dict():")
produk3.tampilkan()

print(f"\n{'='*45}")
print(f"{'4. TES STATIC METHOD':^45}")
print(f"{'='*45}")
print(f"Cek 'Rega'          : {Pelanggan.cek_nama('Rega')}")
print(f"Cek 'Wahyu'         : {Pelanggan.cek_nama('Wahyu')}")
print(f"Cek string kosong   : {Pelanggan.cek_nama('')}")

print(f"\n{'='*45}")
print(f"{'5. TES SETTER & VALIDASI':^45}")
print(f"{'='*45}")

print(">>> Coba ubah jumlah pesanan")
try:
    pesanan1.jumlah = 100
    print(f"[DITERIMA] Jumlah baru: {pesanan1.jumlah}")
except ValueError as e:
    print(f"[DITOLAK] {e}")

try:
    pesanan1.jumlah = -10
    print(f"[BERHASIL DIPROSES] Jumlah baru: {pesanan1.jumlah}")
except ValueError as e:
    print(f"[DITOLAK] Input -10 ditolak > {e}")

print(f"Total harga sekarang di Stickyfy: Rp{pesanan1.total_harga}")

print(f"\n{'-'*45}")
print(">>> Coba ubah harga produk")
try:
    produk1.harga = 3000
    print(f"[DITERIMA] Harga baru produk1: Rp{produk1.harga}")
except ValueError as e:
    print(f"[DITOLAK] {e}")

try:
    produk1.harga = -5000
    print(f"[BERHASIL DIPROSES] Harga baru produk1: Rp{produk1.harga}")
except ValueError as e:
    print(f"[DITOLAK] Input -5000 ditolak > {e}")

print(f"\n{'-'*45}")
print(">>> Tes akses variabel private langsung")
try:
    print(pesanan1.__jumlah)
except AttributeError as e:
    print(f"[Kehalang Enkapsulasi] Gak bisa diakses langsung > {e}")

print(f"\n{'='*45}")
print(f"{'6. RINGKASAN DATA':^45}")
print(f"{'='*45}")
print(f"Total Pesanan Masuk di {Pelanggan.nama_toko}: {Pesanan.total_pesanan}")
print(f"{'='*45}")