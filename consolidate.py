# DiskV class defines a disk
class diskV:
    def __init__(self, n):
        self.lst = [bytearray(100)] * n

    def read(self, no):
        return self.lst[no]

    def write(self, no, data):
        self.lst[no] = data
        
    def size(self):
        return len(self.lst)

# Main class
class consolidate():
    def __init__(self, hdisks):
        self.disks = []
        for i in hdisks:
            self.disks.append(diskV(i))
        # self.disk1 = diskV(200)
        # self.disk2 = diskV(300)

    def readDisk(self,blockNo):
        total = 0
        prev = diskV(0)
        for i in self.disks:
            total += i.size()
            if(blockNo < total):
                return i.read(blockNo-(total-prev.size()))
            prev = i
        print("out of bounds")
        return
        # if blockNo < 200:
        #     return self.disk1.read(blockNo)
        # else:
        #     return self.disk2.read(blockNo-200)

    def writeDisk(self, blockNo, info):
        total = 0
        prev = diskV(0)
        for i in self.disks:
            total += i.size()
            if(blockNo < total):
                return i.write(blockNo-(total-prev.size()),info)
            prev = i
        # if blockNo < 200:
        #     self.disk1.write(blockNo, info)
        # else:
        #     self.disk2.write(blockNo-200, info)

cns = consolidate([200,300,500])
cns.writeDisk(730, "Hello")
print(type(cns.readDisk(730)))
