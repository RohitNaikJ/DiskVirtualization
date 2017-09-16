from consolidate import consolidate

class Snapshot:
    def __init__(self):
        self.physical = consolidate()
        self.free = []
        for i in range(0,500):
            self.free.append(i)
        self.disks = {}
        self.log = {}

    def createDisk(self, id, size):
        if(id in self.disks):
            print("diskId already exists")
            return
        d = []
        j = 0
        if(len(self.free)>=size):
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
        self.free.extend(self.disks[id])
        del self.disks[id]

    def readFromDisk(self, id, blockNo):
        if(id not in self.disks):
            print("No such Disk")
            return
        if (blockNo >= len(self.disks[id])):
            print("Invalid Block No")
            return
        data = self.physical.readDisk((self.disks[id])[blockNo])
        return data

    def writeToDisk(self, id, blockNo, info):
        self.physical.writeDisk((self.disks[id])[blockNo], info)

