#! /usr/bin/env python
from PyQt5.QtGui import QVector3D, QVector2D
import pyassimp
from pyEngine import Model
import numpy as np

def ObjectLoader(fileName = None):
    vertices = []
    uvs = []
    normals = []
    faces = []
    file = open(fileName, "r")
    data = file.readlines()
    file.close()
    for line in data:
        values = line.split()
        if len(values) > 0:
            if values[0] == 'v':
                vertex = QVector3D(float(values[1]), float(values[2]),float(values[3]))
                vertices.append(vertex)
            elif values[0] == 'vn':
                normal = QVector3D(float(values[1]), float(values[2]), float(values[3]))
                normals.append(normal)
            elif values[0] == 'vt':
                texture = QVector2D(float(values[1]), float(values[2]))
                uvs.append(texture)
            elif values[0] == 'f':
                faces.append(values[1])
                faces.append(values[2])
                faces.append(values[3])
            else:
                pass
    triangleVerticesIndex, trianglesTextureIndex, trianglesNormalIndex = parseFaces(faces, uvs, normals)
    # textureCoords = [QVector2D(0.0, 0.0) for i in range(0, len(uvs))]
    # normalCoords = [QVector3D(0.0, 0.0, 0.0) for i in range(0, len(normals))]
    # # print(trianglesTextureIndex)
    #
    # for coord in trianglesTextureIndex:
    #     textureCoords[coord] = uvs[coord]
    #
    # for coord in trianglesNormalIndex:
    #     normalCoords[coord] = normals[coord]

    # print(trianglesNormalIndex)
    # print(normalCoords)
    # triangles = []
    # for i in range(0,len(triangleVerticesIndex) //3):
    #     triangles.append(vertices[triangleVerticesIndex[i*3]])
    #     triangles.append(vertices[triangleVerticesIndex[i * 3 + 1]])
    #     triangles.append(vertices[triangleVerticesIndex[i * 3 + 2]])

    # vertexNormals = []
    # for index in trianglesNormalIndex:
        # vertexNormals.append(normals[index])
    # print(correctedDrawingIndices)
    # print(triangleVertices[9*3], triangleVertices[9*3 + 1], triangleVertices[9*3 + 2])
    # print(vertices[triangleVertices[9*3] - 1 ], vertices[triangleVertices[9*3 + 1] - 1 ], vertices[triangleVertices[9*3 + 2] - 1])
    # print(triangles[27], triangles[28], triangles[29])
    # print(faces)
    # print(triangleVerticesIndex)
    # print(vertices)
    # print(textureCoords)
    # print(normalCoords)
    return vertices, triangleVerticesIndex,  trianglesTextureIndex, trianglesNormalIndex

def parseFaces(facesList, uvs, normals):
    trianglesIndex = []
    trianglesNormalIndex = [QVector2D(0,0) for i in range(0, len(facesList))]
    trianglesTextureIndices = [QVector3D(0,0,0) for i in range(0, len(facesList))]
    for face in facesList:
        values = face.split('/')
        trianglesIndex.append(int(values[0]) - 1)
        trianglesTextureIndices[int(values[1]) - 1] = uvs[int(values[1]) - 1]
        trianglesNormalIndex[int(values[2]) - 1] = normals[int(values[2]) - 1]
    return trianglesIndex, trianglesTextureIndices, trianglesNormalIndex

#
# def loadObj( objfile):
#     drawingVertices = []
#     drawingIndices = []
#     objLoader = ObjectLoader(objfile)
#     vtr = objLoader[0]
#     drawingIndices = objLoader[1]
#     textureCoords = objLoader[2]
#     normals = objLoader[3]
#     verticesAndNormals = [(a, b, c) for (a, b, c) in zip(vtr, textureCoords, normals)]
#     for row in verticesAndNormals:
#         for vector in row:
#             drawingVertices.append(float(vector.x()))
#             drawingVertices.append(float(vector.y()))
#             try:
#                 drawingVertices.append(float(vector.z()))
#             except:
#                 drawingVertices.append(float(0))
#     drawingVertices = Model.Model.listToArray(list=drawingVertices, type=np.float32)
#     # print(drawingVertices)
#     drawingIndices = Model.Model.listToArray(list=drawingIndices, type=np.int32)
#     return drawingVertices, drawingIndices, vtr, textureCoords, normals

# TODO: improve loading
def loadObj( objfile):
    drawingVertices = []
    scene = pyassimp.load(objfile)
    mesh = scene.meshes[0]
    vtr = mesh.vertices
    drawingIndices = [i for i in range(0, len(vtr))]
    textureCoords = mesh.texturecoords[0]
    normals = mesh.normals
    verticesAndNormals = np.hstack((vtr, textureCoords, normals))
    for row in verticesAndNormals:
        for val in row:
            drawingVertices.append(val)
    drawingVertices = Model.Model.listToArray(list=drawingVertices, type=np.float32)
    drawingIndices = Model.Model.listToArray(list=drawingIndices, type=np.int32)
    return drawingVertices, drawingIndices, vtr, textureCoords, normals

if __name__ == "__main__":
    loadObj( '/Users/rui/Desktop/githubStuff/ComputerGraphics/ShaderToy/objs/Cerberus.obj')
    # drawingVertices = objLoader[0]
    # drawingIndices = objLoader[1]
    # drawingNormals = objLoader[3]
    #
    # print(len(drawingVertices), len(drawingIndices), len(drawingNormals))
    # print(drawingVertices)
    # print(drawingNormals)
    # print((drawingIndices))
    # print()
    # print(drawingVertices[4])
    # print(drawingVertices[0])
    # print(drawingVertices[3])
    #
    # print(drawingNormals[0])
    # print(drawingNormals[0])
    # print(drawingNormals[0])


    '''/Users/rui/Desktop/githubStuff/ComputerGraphics/env/bin/python3.5 /Users/rui/Desktop/githubStuff/ComputerGraphics/ShaderToy/pyEngine/ObjLoader.py
[[ 0.134781   -0.14723     0.48805001]
 [ 0.13126101 -0.132153    0.49871999]
 [ 0.14748999 -0.135105    0.48956501]
 ..., 
 [-0.142316   -0.16679101  0.41183999]
 [-0.0730392  -0.218144    0.37234899]
 [-0.126228   -0.116368    0.36052799]]

Process finished with exit code 0
'''