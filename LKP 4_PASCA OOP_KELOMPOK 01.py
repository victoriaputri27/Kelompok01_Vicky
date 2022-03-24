# #inheritance

print("------inheritance-----")
class DealerMobil :
        def __init__(self,merk,tahun):
            self.merk = merk
            self.tahun = tahun
    
        def keterangan(self):
            return(f'saya mau beli mobil dengan merk {self.merk} tahun {self.tahun}' )
            
class stok(DealerMobil):
    def __init__(self,merk,tahun,warna):
            self.merk = merk
            self.tahun = tahun
            self.warna = warna
            super().__init__(merk,tahun)
            DealerMobil.__init__(self,merk,tahun)

    def keterangan(self):
        return(f"saya mau beli mobil dengan merk {self.merk} tahun {self.tahun} dengan warna {self.warna}")

mobil = stok('honda','2002','hitam')
print(mobil.keterangan())

print("-----override------")
#override
class DealerMobil :
    def __init__(self,merk,tahun) :
        self.merk = merk
        self.tahun = tahun

    def keterangan(self) :
        return(f'saya mau beli mobil dengan merk {self.merk} tahun {self.tahun}')

class stok(DealerMobil) :
    def __init__(self,merk,tahun,warna) :
        self.merk = merk
        self.tahun = tahun
        super().__init__(merk,tahun)
        DealerMobil.__init__(self,merk,tahun)
        self.warna = warna
    
    def keterangan(self):
        return(f"saya mau beli mobil dengan merk {self.merk} tahun {self.tahun} dengan warna {self.warna}")

class mesin (DealerMobil) :
    def __init__(self,merk,tahun,harga) :
        super().__init__(merk,tahun)
        self.harga = harga  

    def keterangan(self):
        return (f'mobil dengan merk {self.merk} memiliki harga {self.harga} untuk yang tahun {self.tahun}')

honda = stok('honda', '2022', 'hitam')  
toyota = mesin('toyota', '300 jt', '2022')

print (honda.keterangan())
print (toyota.keterangan())

            
