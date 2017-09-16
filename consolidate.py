# DiskV class defines a disk
class diskV:
    def __init__(self, n):
        self.lst = [bytearray(100)] * n

    def read(self, no):
        return self.lst[no]

    def write(self, no, data):
        self.lst[no] = data

# Main class
class consolidate():
    def __init__(self):
        self.disk1 = diskV(200)
        self.disk2 = diskV(300)

    def readDisk(self,blockNo):
        if(blockNo <= 200):
            return self.disk1.read(blockNo)
        else:
            return self.disk2.read(blockNo-200)

    def writeDisk(self, blockNo, info):
        if(blockNo <= 200):
            self.disk1.write(blockNo, info)
        else:
            self.disk2.write(blockNo-200, info)

cns = consolidate()
cns.writeDisk(430, "Hello")
print(type(cns.readDisk(430)))
