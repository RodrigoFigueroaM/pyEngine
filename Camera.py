#! /usr/bin/env python
from PyQt5.QtGui import (QMatrix4x4, QVector3D, QVector4D)
import math


class Camera(object):
    """docstring for Camera"""
    def __init__(self, position=QVector3D(0, 0, 1),
                 lookAt=QVector3D(0, 0, 0),
                 up=QVector3D(0, 1, 0),
                 fov = 90):
        super(Camera, self).__init__()
        self._pos = position
        self._lookAt = lookAt
        self._dir = (lookAt - self._pos).normalized()
        # self._dir = direction.normalized()
        self._up = up
        self._fov = fov
        self._right = QVector3D.crossProduct(self.direction, self.position)
        self._center = self.position + self.direction
        self._projectionMatrix = QMatrix4x4()
        self._modelViewMatrix = QMatrix4x4()
        self._normalMatrix = QMatrix4x4()

    def setOrthographic(self,  left=-1.0, right=1.0, bottom=-1.0, top=1.0, near=0.1, far=20.0):
        self.projectionMatrix.setToIdentity()
        self.projectionMatrix.ortho( left, right, bottom, top, near, far)

    def setPerspective(self, fov=90, ratio=100, near=1.0, far=2.0):
        self.fov = fov
        self._projectionMatrix.setToIdentity()
        self._projectionMatrix.perspective(fov, ratio, near, far)

    def setFrustum(self, left=-1, right=1, bottom=-1, top=1, near=1, far=2.0):
        self._projectionMatrix.setToIdentity()
        self._projectionMatrix.frustum(left, right, bottom, top, near, far)

    def setProjectionMatrixToIdentity(self):
        self._projectionMatrix.setToIdentity()

    def setModelViewMatrixToIdentityt(self):
        self._modelViewMatrix.setToIdentity()

    def lookAtCenter(self):
        self.lookAtTarget(QVector3D(0, 0, 0))

    def lookAtTarget(self, target):
        self._modelViewMatrix.setToIdentity()
        self._modelViewMatrix.lookAt(self._pos, target, self._up)

    def moveUp(self):
        self._modelViewMatrix.setToIdentity()
        self.position += QVector3D(0.0, 0.1, 0.0)
        self.direction += QVector3D(0.0, 0.1, 0.0)

    def moveDown(self):
        self._modelViewMatrix.setToIdentity()
        self.position -= QVector3D(0.0, 0.1, 0.0)
        self.direction -= QVector3D(0.0, 0.1, 0.0)

    def moveRight(self):
        self._modelViewMatrix.setToIdentity()
        self.position += QVector3D(0.1, 0.0, 0.0)
        self.direction += QVector3D(0.1, 0.0, 0.0)

    def moveLeft(self):
        self._modelViewMatrix.setToIdentity()
        self.position -= QVector3D(0.1, 0.0, 0.0)
        self.direction -= QVector3D(0.1, 0.0, 0.0)

    def moveForward(self):
        self._modelViewMatrix.setToIdentity()
        self.position -= QVector3D(0.0, 0.0, 0.1)
        self.direction -= QVector3D(0.0, 0.0, 0.1)

    def moveBackward(self):
        self._modelViewMatrix.setToIdentity()
        self.position += QVector3D(0.0, 0.0, 0.1)
        self.direction += QVector3D(0.0, 0.0, 0.1)

    def rotate(self, xangle, yangle, zangle):
        self._modelViewMatrix.rotate(xangle, 1, 0, 0)
        self._modelViewMatrix.rotate(yangle, 0, 1, 0)
        self._modelViewMatrix.rotate(zangle, 0, 0, 1)

    def rotate(self, mat):
        self.position = mat * self.position

    def zoom(self, increment):
        self.fov -= increment

    def translate(self, x, y, z):
        T = QMatrix4x4()
        T.translate(QVector3D(x, y, z))
        self.position = T * self.position
        del T

    def mouseRay(self, xin, yin, width, height):
        near = -1.0
        far = 0.0
        rayBegin = self._rayDirection(xin, yin, width, height, near)
        rayEnd = self._rayDirection(xin, yin, width, height, far)
        return rayBegin, rayEnd

    def _rayDirection(self, xin, yin, width, height, plane):
        x, y, z = self.devicePortCoordinates(xin, yin, width, height)
        clipCoord = QVector4D(x, y, plane, 1.0)
        eyeCoord = self._eyeSpace(clipCoord)
        ray = self._worldCoord(eyeCoord)
        return ray

    def _eyeSpace(self, clipCoord):
        invertedProjectionMatrix = self.projectionMatrix.inverted()[0]
        eye = invertedProjectionMatrix * clipCoord
        return eye / eye.w()

    def _worldCoord(self, eyeCoord):
        invertedViewMatrix = self.modelViewMatrix.inverted()[0]
        worldCoord = invertedViewMatrix * eyeCoord
        return worldCoord / worldCoord.w()

    def mouseWorld(self, xin, yin, width, height):
        mouse = self._mouseDirection(xin, yin, width, height, -1.0)
        return mouse

    def _mouseDirection(self, xin, yin, width, height, plane):
        x, y, z = self.devicePortCoordinates(xin, yin, width, height)
        clipCoord = QVector4D(x, y, plane, 0.0)
        eyeCoord = self._mouseEyeSpace(clipCoord)
        ray = self._mouseWorldCoord(eyeCoord)
        return ray

    def _mouseEyeSpace(self, clipCoord):
        invertedProjectionMatrix = self.projectionMatrix.inverted()[0]
        eye = invertedProjectionMatrix * clipCoord
        return QVector4D(eye.x(), eye.y(), -1.0, 0.0)

    def _mouseWorldCoord(self, eyeCoord):
        invertedViewMatrix = self.modelViewMatrix.inverted()[0]
        worldCoord = invertedViewMatrix * eyeCoord
        return QVector3D(worldCoord.x(), worldCoord.y(), worldCoord.z())

    @property
    def position(self):
        return self._pos

    @position.setter
    def position(self, position):
        self._pos = position

    @property
    def direction(self):
        self._dir = self._lookAt - self._pos
        return self._dir.normalized()

    @direction.setter
    def direction(self, direction):
        self._dir = direction

    @property
    def fov(self):
        return self._fov

    @fov.setter
    def fov(self, fov):
        if 180.0 > fov > 5.0:
            self._fov = fov

    @property
    def up(self):
        self._up = QVector3D.crossProduct(self.direction, self._right)
        return self._up.normalized()

    @up.setter
    def up(self, up):
        self._up = up

    @property
    def center(self):
        self._center = self.position + self.direction
        return self._center

    @property
    def right(self):
        self._right = QVector3D.crossProduct(self._up, self.direction)
        return self._right

    @property
    def projectionMatrix(self):
        return self._projectionMatrix

    @projectionMatrix.setter
    def projectionMatrix(self, projectionMatrix):
        self._projectionMatrix.setToIdentity()
        self._projectionMatrix = projectionMatrix

    @property
    def modelViewMatrix(self):
        return self._modelViewMatrix

    @modelViewMatrix.setter
    def modelViewMatrix(self, modelViewMatrix):
        self._modelViewMatrix.setToIdentity()
        self._modelViewMatrix = modelViewMatrix

    @property
    def normalMatrix(self):
        self._normalMatrix = self.modelViewMatrix.inverted()[0].transposed()
        return self._normalMatrix

    @normalMatrix.setter
    def normalMatix(self, normalMat):
        self._normalMatrix = normalMat

    def __str__(self):
        return 'position:{}\ndirection: {}\nup:{}\n'.format(self._pos, self._dir, self._up)

    @staticmethod
    def devicePortCoordinates(x, y, width, height):
        # bring mouse to device coordinates to opengl coordinates ranges [-1:1,xy]
        x -= width / 2
        y -= height / 2

        y /= (height / 2)
        x /= (width / 2)
        return x, y, -1.0

    class Ray:
        """generate a ray = e + td"""
        def __init__(self, origin, direction):
            self.e = origin
            self.d = direction

        def __str__(self):
            return "e = {}\nd = {}".format(self.e, self.d)

    # @staticmethod
    def devicePortCoordinatesRayTracing(self, x, y, width, height):
        # xratio = 1.0
        # yratio = 1.0
        # if width > height:
        #     xratio = width / height
        #     yratio = 1.0
        # elif width < height:
        #     xratio = 1.0
        #     yratio = width / height
        pixelScreenX = (x + 0.5) / width
        pixelScreenY = (y + 0.5) / height
        mx = (2 * pixelScreenX - 1) * math.tan(self._fov / 2 * math.pi / 180) # 0.5 so that it passes through the center
        my = (1 - 2 * pixelScreenY) * math.tan(self._fov / 2 * math.pi / 180)
        return mx, my

    def _makeCoordianteSystem(self):
        pass

    def rayCast(self, i, j, width, height):
        # Eye Coordinate System
        origin = self.position
        n = (origin - QVector3D(0, 0, 0)).normalized()
        u = QVector3D.crossProduct(self._up, n).normalized()
        v = QVector3D.crossProduct(n, u).normalized()

        # Image Plane setup
        planeCenter = origin + n
        d = (origin - planeCenter).length()
        aspectRatio = width / height
        H = math.tan(aspectRatio * self.fov) * 2 * d
        W = H * aspectRatio
        C = origin - n * d
        L = C - u * W / 2 - v * H/2
        pixelWidth = W / width
        pixelHeight = H / height

        s = L + u * i * pixelWidth + v * j * pixelHeight
        print(s)
        return Camera.Ray(origin, (s - origin).normalized())

    def rayCastBook(self):
        pass

    def rayCastStack(self, i, j, width, height):
        direction = self.direction
        right = QVector3D.crossProduct(direction, self._up).normalized()
        up = QVector3D.crossProduct(direction, right) * -1.0
        center = self.position + direction
        print(up)
        # normalizedI = (i/width)- 0.5
        # normalizedJ = (j /height) - 0.5
        s = center + i * right + j * up
        # print((self.position - center).length())
        return Camera.Ray(self.position, (s - self.position))






if __name__ == '__main__':
    camera = Camera()
    print(camera)
    camera.rotate(60, 60, 60)
    print(camera)
