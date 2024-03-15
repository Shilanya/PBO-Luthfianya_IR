class Dagangan:
    jumlah_barang = 0
    list_barang = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        Dagangan.jumlah_barang += 1
        Dagangan.list_barang.append((nama, stok, harga))

    def lihat_barang():
        print("Jumlah barang dagangan pada toko:", Dagangan.jumlah_barang, "buah")
        for i, barang in enumerate(Dagangan.list_barang, 1):
            nama, stok, harga = barang
            print(f"{i}. {nama} seharga Rp {harga} (stok: {stok})")

    lihat_barang = staticmethod(lihat_barang)

    def __del__(self):
        Dagangan.jumlah_barang -= 1
        for i, barang in enumerate(Dagangan.list_barang):
            nama, _, _ = barang
            if nama == self.__nama:
                del Dagangan.list_barang[i]
                print(f"{self.__nama} dihapus dari toko!")
                break


Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)
Dagangan.lihat_barang()

del Dagangan1
print()

Dagangan.lihat_barang()
