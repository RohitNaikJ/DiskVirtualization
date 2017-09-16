from consolidate import consolidate
import bisect

class Snapshot:
    def __init__(self):
        self.physical = consolidate()
        self.free = []
        for i in range(0,500):
            self.free.append(i)
        self.disks = {}

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
        # self.free.extend(self.disks[id])
        for i in self.free[id]:
            bisect.insort(self.free, i)
        del self.disks[id]

    def readFromDisk(self, id, blockNo):
        if(id not in self.disks):
            print("No such Disk")
            return
        if blockNo > len(self.disks[id]) or blockNo < 0:
            print("Invalid Block No")
            return
        data = self.physical.readDisk(self.disks[id][blockNo-1])
        return data

    def writeToDisk(self, id, blockNo, info):
        self.physical.writeDisk(self.disks[id][blockNo-1], info)

    def checkpoint(self, diskID):
        return len(self.log[diskID])

    def rollBack(self, diskID, checkpointID):
        while len(self.log[diskID]) > checkpointID:
            lastUpdate = self.log[diskID].pop()
            self.physical.writeDisk(self.disks[diskID][lastUpdate[0]], lastUpdate[1])
