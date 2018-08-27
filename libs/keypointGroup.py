
from libs.keypoint import Keypoint

class KeypointGroup(object):
    def __init__(self):
        self.keypoints = []
    
    def paint(self, painter):
        for kp in self.keypoints:
            kp.paint(painter)
    
    def nearestVertex(self, point, epsilon):
        for i, p in enumerate(self.keypoints):
            pos = p.nearestVertex(point, epsilon)
            if pos is not None:
                return (i, pos) # return first match

        return None

    def moveBy(self, offset):
        for p in self.keypoints:
            p.moveBy(offset)

    def moveVertexBy(self, i, offset):
        if i is None:
            return
        self.keypoints[i[0]].moveVertexBy(i[1], offset)

    def updateBound(self, xmin, ymin, xmax, ymax):
        for p in self.keypoints:
            p.updateBound(xmin, ymin, xmax, ymax)

    def highlightVertex(self, i, action):
        if i is None:
            return
        self.keypoints[i[0]].highlightVertex(i[1], action)

    def highlightClear(self):
        for p in self.keypoints:
            p.highlightClear()

    def copy(self):
        kpg = KeypointGroup()
        kpg.keypoints = [p.copy() for p in self.keypoints]
        return kpg

    def __getitem__(self, key):
        return self.keypoints[key[0]][key[1]]

    def __setitem__(self, key, value):
        self.keypoints[key[0]][key[1]] = value