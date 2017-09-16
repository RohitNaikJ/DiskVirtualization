from consolidate import consolidate
import bisect
import random

class replication:
    def __init__(self):
        self.physical = consolidate()
        self.free = []
        for i in range(0,500):
            self.free.append(i)
        self.disks = {}
        self.invalidBlocks = []

    def createDisk(self, id, size):
        if(id in self.disks):
            print("diskId already exists")
            return
        d = []
        j = 0
        if(len(self.free) >= size):
            for i in self.free:
                d.append(i)
                j += 1
                if(j==size):
                    break
        else:
            print("Space not Available!")
        self.free = [x for x in self.free if x not in d]
        self.disks[id] = d

    def deleteDisk(self,id):
        # self.free.extend(self.disks[id])
        for i in self.disks[id]:
            bisect.insort(self.free, i)
        del self.disks[id]

    def readFromDisk(self, id, blockNo):
        if id not in self.disks:
            print("No such Disk")
            return
        if blockNo > len(self.disks[id]) or blockNo <= 0:
            print("Invalid Block No")
            return
        data = self.physical.readDisk(self.disks[id][blockNo-1])
        return data


    def writeToDisk(self, id, blockNo, info):
        self.physical.writeDisk(self.disks[id][blockNo-1], info)

    # Replication
    def createDiskR(self, id, size):
        if (id <= 0):
            print("ERROR: DiskID must be greater than 0")
            return
        if (len(self.free) >= 2 * size):
            self.createDisk(id, size)
            self.createDisk(-id, size)
        else:
            print("ERROR: Space not available")

    def writeToDiskR(self, id, blockNo, info):
        if id not in self.disks or id<=0:
            print("Invalid Disk ID")
            return
        if blockNo > len(self.disks[id]) or blockNo <= 0:
            print("Invalid Block No")
            return
        self.writeToDisk(id, blockNo, info)
        self.writeToDisk(-id, blockNo, info)

    def readFromDiskR(self, id, blockNo):
        if(id<=0):
            print("Invalid Disk ID")
            return
        if (blockNo > len(self.disks[id])):
            print("Invalid Block No")
            return
        if random.randint(1,100)<=10 or self.disks[id][blockNo-1] in self.invalidBlocks:
            # self.free.append((self.disks[id])[blockNo])
            print('Invalid Block')
            if self.disks[id][blockNo-1] not in self.invalidBlocks:
                self.invalidBlocks.append(self.disks[id][blockNo-1])

            data = self.readFromDisk(-id, blockNo)

            if len(self.free) == 0:
                print('ERROR: Insufficent Space to re-replicate an invalid block. This block will now have a replication factor of 1 until another block is deallocated')
            else:
                self.disks[id][blockNo-1] = self.free[0]
                self.free = self.free[1:]
                self.writeToDisk(id, blockNo, data)
            return data
        else:
            return self.readFromDisk(id, blockNo)

    def deleteDiskR(self, id):
        if id<=0 or id not in self.disks:
            print("Invalid Disk ID")
            return
        self.deleteDisk(id)
        self.deleteDisk(-id)

prt = replication()
prt.createDiskR(1,140)
prt.createDiskR(2,110)
prt.writeToDiskR(1, 110, "lol")
prt.writeToDiskR(2, 110, "lol1")
print(prt.readFromDiskR(2, 110))
