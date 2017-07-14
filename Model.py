#! /usr/bin/env python

import numpy as np
from PyQt5.QtGui import QVector2D, QVector3D, QMatrix4x4
from pyEngine.ObjLoader import loadObj

class Model:
    def __init__(self, objfile=None):
        super(Model, self).__init__()
        self._objFile = objfile
        self._vertices = []
        self._verticesIndices = []
        self._textureCoords = []
        self._normals = []
        self._drawingVertices = []
        self._transformationMatrix = QMatrix4x4()
        if objfile:
            self.loadModel()

    def __str__(self):
        return '{}'.format(self.drawingVertices)

    def loadModel(self):
        self._drawingVertices,\
        self._verticesIndices,\
        self._vertices,\
        self._textureCoords,\
        self._normals = loadObj(self.modelFile)

    @property
    def modelFile(self):
        return self._objFile

    @property
    def vertices(self):
        return self._vertices

    @property
    def verticesIndices(self):
        return self._verticesIndices

    @property
    def textureCoords(self):
        return self._textureCoords

    @property
    def normals(self):
        return self._normals

    @property
    def drawingVertices(self):
        return self._drawingVertices

    @drawingVertices.setter
    def drawingVertices(self, vertices):
        self.drawingVertices = vertices

    @property
    def transformationMatrix(self):
        return self._transformationMatrix

    @transformationMatrix.setter
    def transformationMatrix(self, transformationMatrix):
        if type(QMatrix4x4()) == type(transformationMatrix):
            self._transformationMatrix = transformationMatrix

    @staticmethod
    def listToArray(list, type):
        vertices = np.asarray(list, dtype=type)
        return vertices

    @staticmethod
    def cubeWithColors():
        return [-1.0, -1.0, -1.0,        0.5, 0.5, 0.5,  # // triangle 1 : begin
                -1.0, -1.0, 1.0,         0.5, 0.0, 0.5,
                -1.0, 1.0, 1.0,         0.2, 0.0, 1.0,  # // triangle 1 : end
                1.0, 1.0, -1.0,         0.0, 0.3, 1.0,  # // triangle 2 : begin
                -1.0, -1.0, -1.0,        1.0, 0.6, 0.0,
                -1.0, 1.0, -1.0,        1.0, 0.0, 1.0,  # // triangle 2 : end
                1.0, -1.0, 1.0,         0.0, 0.0, 0.0,
                -1.0, -1.0, -1.0,        0.0, 0.0, 0.0,
                1.0, -1.0, -1.0,        1.0, 1.0, 1.0,
                1.0, 1.0, -1.0,         0.8, 0.6, 0.0,
                1.0, -1.0, -1.0,         0.5, 0.9, 0.0,
                -1.0, -1.0, -1.0,        0.5, 0.0, 0.0,
                -1.0, -1.0, -1.0,       0.5, 1.0, 1.0,
                -1.0, 1.0, 1.0,      1.0, 1.0, 1.0,
                -1.0, 1.0, -1.0,         1.0, 1.0, 1.0,
                1.0, -1.0, 1.0,         0.6, 0.6, 1.0,
                -1.0, -1.0, 1.0,         0.0, 0.6, 1.0,
                -1.0, -1.0, -1.0,        0.0, 1.0, 1.0,
                -1.0, 1.0, 1.0,         0.0, 1.0, 1.0,
                -1.0, -1.0, 1.0,         0.0, 1.0, 1.0,
                1.0, -1.0, 1.0,      0.0, 0.0, 0.0,
                1.0, 1.0, 1.0,      1.0, 0.0, 1.0,
                1.0, -1.0, -1.0,        1.0, 0.0, 1.0,
                1.0, 1.0, -1.0,      0.0, 1.0, 1.0,
                1.0, -1.0, -1.0,         0.0, 1.0, 1.0,
                1.0, 1.0, 1.0,       0.0, 1.0, 1.0,
                1.0, -1.0, 1.0,         1.0, 1.0, 1.0,
                1.0, 1.0, 1.0,      1.0, 0.0, 0.0,
                1.0, 1.0, -1.0,      1.0, 0.0, 0.0,
                -1.0, 1.0, -1.0,        1.0, 0.0, 0.0,
                1.0, 1.0, 1.0,       1.0, 1.0, 0.0,
                -1.0, 1.0, -1.0,         1.0, 1.0, 0.0,
                -1.0, 1.0, 1.0,      1.0, 1.0, 0.0,
                1.0, 1.0, 1.0,       1.0, 0.0, 1.0,
                -1.0, 1.0, 1.0,      1.0, 0.0, 1.0,
                1.0, -1.0, 1.0,        1.0, 0.0, 1.0]


    '''TODO: delete'''
    @staticmethod
    def testCube():
        vtr = [QVector3D(-0.5, 0.5, -0.5),
               QVector3D(-0.5, -0.5, -0.5),
               QVector3D(0.5, -0.5, -0.5),
               QVector3D(0.5, 0.5, -0.5),

               QVector3D(-0.5, 0.5, 0.5),
               QVector3D(-0.5, -0.5, 0.5),
               QVector3D(0.5, -0.5, 0.5),
               QVector3D(0.5, 0.5, 0.5),

               QVector3D(0.5, 0.5, -0.5),
               QVector3D(0.5, -0.5, -0.5),
               QVector3D(0.5, -0.5, 0.5),
               QVector3D(0.5, 0.5, 0.5),

               QVector3D(-0.5, 0.5, -0.5),
               QVector3D(-0.5, -0.5, -0.5),
               QVector3D(-0.5, -0.5, 0.5),
               QVector3D(-0.5, 0.5, 0.5),

               QVector3D(-0.5, 0.5, 0.5),
               QVector3D(-0.5, 0.5, -0.5),
               QVector3D(0.5, 0.5, -0.5),
               QVector3D(0.5, 0.5, 0.5),

               QVector3D(-0.5, -0.5, 0.5),
               QVector3D(-0.5, -0.5, -0.5),
               QVector3D(0.5, -0.5, -0.5),
               QVector3D(0.5, -0.5, 0.5),
               ]

        drawingIndices = [0, 1, 3,
                               3, 1, 2,
                               4, 5, 7,
                               7, 5, 6,
                               8, 9, 11,
                               11, 9, 10,
                               12, 13, 15,
                               15, 13, 14,
                               16, 17, 19,
                               19, 17, 18,
                               20, 21, 23,
                               23, 21, 22]

        textureCoords = [
            QVector2D(0, 0),
            QVector2D(0, 1),
            QVector2D(1, 1),
            QVector2D(1, 0),
            QVector2D(0, 0),
            QVector2D(0, 1),
            QVector2D(1, 1),
            QVector2D(1, 0),
            QVector2D(0, 0),
            QVector2D(0, 1),
            QVector2D(1, 1),
            QVector2D(1, 0),
            QVector2D(0, 0),
            QVector2D(0, 1),
            QVector2D(1, 1),
            QVector2D(1, 0),
            QVector2D(0, 0),
            QVector2D(0, 1),
            QVector2D(1, 1),
            QVector2D(1, 0),
            QVector2D(0, 0),
            QVector2D(0, 1),
            QVector2D(1, 1),
            QVector2D(1, 0)
        ]
        return vtr, drawingIndices, textureCoords

    @staticmethod
    def testRec():
        vtr = [QVector3D(-1.0, 1.0, 0.0),
               QVector3D(-1.0, -1.0, 0.0),
               QVector3D(1.0, -1.0, 0.0),
               QVector3D(1.0, 1.0, 0.0)]

        drawingIndices=[0, 1, 3, 3, 1, 2]

        textureCoords = [ QVector2D(0, 0),
                        QVector2D(1, 0),
                        QVector2D(1, 1),
                        QVector2D(1, 0) ]
        return vtr, drawingIndices, textureCoords

    def normalsPerVertex(faces = None, numberOfVertices = 0):
        # make sublist of vertices and triangles tahta affect the
        li =[]
        for index in range(0, numberOfVertices, 1):
            inli = []
            for face in faces:
                if index == face[1][0]:
                    inli.append(face[0])
                if index == face[1][1]:
                     inli.append(face[0])
                if index == face[1][2]:
                     inli.append(face[0])
            li.append([index, inli])

        verticesNormals = []
        for row in li:
            normalsAvg = QVector3D(0,0,0)
            for index in row[1]:
                normalsAvg += faces[index][2]
            normalsAvg = normalsAvg / len(row[1])
            normalsAvg = normalsAvg.normalized()
            verticesNormals.append(normalsAvg)
        return verticesNormals


    def normalsPerTriangle(vertices=None, indices=None):
        triangleNormals = []
        i = 0
        for index in range(0, len(indices) - 2, 1):
            if indices[index] != indices[index - 1] and indices[index] != indices[index + 1] and indices[index - 1] != \
                    indices[index + 1]:
                a = (vertices[indices[index - 1]] - vertices[indices[index]])
                b = (vertices[indices[index + 1]] - vertices[indices[index]])
                # if index % 2 == 0:
                normal = QVector3D.crossProduct(b, a)
                # else:
                #     normal = QVector3D.crossProduct(a, b)
                triangleNormals.append([i, (indices[index], indices[index - 1], indices[index + 2]), normal])
                i += 1
        return triangleNormals


if __name__ == "__main__":
    print(bool(GL.glGenFramebuffers()))
    tempVao = GL.GLuint(0)
    GL.glGenVertexArrays(1, tempVao)
    GL.glBindVertexArray(tempVao)
    # objLoader = ObjectLoader("Cube.obj")
    # # objLoader = ObjectLoader("sphere.obj")
    # vtr = objLoader[0]
    # drawingVertices = []
    # for value in vtr:
    #     drawingVertices.append(float(value.x()))
    #     drawingVertices.append(float(value.y()))
    #     drawingVertices.append(float(value.z()))
    #
    # model = Model(0, drawingVertices)
    # print(model.vaoID)