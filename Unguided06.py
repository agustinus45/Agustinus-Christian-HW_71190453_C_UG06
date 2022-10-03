class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None

    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self.next = None
    
class SLNC: 
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def insert_head(self,no_rekening,nama,saldo):
        baru = NodeTabungan(no_rekening,nama,saldo)
        if self.isEmpty():
            self._head = baru
            self._tail = baru
        else:
            baru.next = self._head
            self._head = baru
        self._size += 1
    
    def deleteHead(self):
        if self.isEmpty() == False:
            if self._head.next == None:
                self._head = None
                self._tail = None
            else:
                hapus = self._head
                self._head = self._head.next
                hapus.next = None
                del hapus
            self._size -=1


    def deleteTail(self):
        if self.isEmpty() == False:
            bantu = self._head
            if(self._head != self._tail):
                while bantu.next != self._tail:
                    bantu = bantu.next
                hapus = self._tail
                self._tail = bantu
                del hapus
                self._tail.next = None
            else:
                self._head=tail=None
            self._size -= 1

    def filter(self,n):
        if self.saldo < n:


    def print(self):
        bantu = self._head
        while bantu != None:
            print('Norek:',bantu.no_rekening)
            print('Nama:',bantu.nama)
            print('Saldo:',bantu.saldo)
            bantu = bantu.next
        print()




slnc=SLNC()
slnc.insert_head(201,'Hanif',250000)
slnc.insert_head(100,'Yudha',250000)
slnc.print()