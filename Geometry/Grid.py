#!/usr/bin/env python
import numpy as np
from pyEngine.Model import Model
from PyQt5.QtGui import QMatrix4x4, QVector3D, QVector2D


class Grid(Model):
    def __init__(self, scale=1):
        super().__init__()
        self.computeGrid()
        self.makeGrid()

    def computeGrid(self, scale=1):
        mainLine = [QVector3D(0, 0, 0), QVector3D(1, 0, 0)]
        T = QMatrix4x4()
        self._vertices = mainLine[:]
        numLines = 12
        for i in range(0, numLines - 1):
            self._vertices.append(T * mainLine[0])
            self._vertices.append(T * mainLine[1])
            T.translate(0.0, 0.0, 0.1)

        T.setToIdentity()
        T.translate(0.0, 0.0, 1.0)
        T.rotate(90, 0, 1, 0)
        for i in range(0, numLines - 1):
            self._vertices.append(T * mainLine[0])
            self._vertices.append(T * mainLine[1])
            T.translate(0.0, 0.0, 0.1)

        T.setToIdentity()
        T.scale(scale)
        for i in range(0, len(self.vertices)):
            self._vertices[i] = T * self._vertices[i]

        self._verticesIndices = [i for i in range(0, len(self.vertices))]
        self._textureCoords = [QVector2D(0.0, 0.0) for i in range(0, len(self.vertices))]
        self._normals = [QVector3D(0, 0, 0) for i in range(0, len(self.vertices))]

    def makeGrid(self):
        gridVericesAndNormals = [(a, b, c) for (a, b, c) in zip(self.vertices, self.textureCoords, self.normals)]
        for row in gridVericesAndNormals:
            for vector in row:
                # print(vector)
                self._drawingVertices.append(float(vector.x()))
                self._drawingVertices.append(float(vector.y()))
                if hasattr(vector, 'z'):
                    self._drawingVertices.append(float(vector.z()))
        self._drawingVertices = Model.listToArray(list=self._drawingVertices, type=np.float32)
        self._verticesIndices = Model.listToArray(list=self._verticesIndices, type=np.int32)
