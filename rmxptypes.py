import struct
from . import Reader

class RMXPDecodeError(RuntimeError):
    pass

class Tone():

    def __init__(self, r, g, b, gr):
        self.r = r
        self.g = g
        self.b = b
        self.gr = gr

    @Reader.register_load("Tone")
    def _load(data):
        return Tone(*struct.unpack("<dddd", data))

class Color():

    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    @Reader.register_load("Color")
    def _load(data):
        return Color(*struct.unpack("<dddd", data))

class Table():

    __slots__ = ["data", "w", "h", "d"]
    def __init__(self, w, h, d):
        self.data = [0 for _ in range(w * h * d)]
        self.w = w
        self.h = h
        self.d = d

    def __getitem__(self, xyz):
        x, y, z = xyz
        return self.data[z * self.w * self.h + y * self.w + x]

    def __setitem__(self, xyz, v):
        self.data[z * self.w * self.h + y * self.w + x] = v

    @Reader.register_load("Table")
    def frombytes(b):
        dim, w, h, d, size = struct.unpack("<IIIII", b[:20])
        if w * h * d != size:
            raise RMXPDecodeError("Table size doesn't match w * h * d")
        obj = Table(w, h, d)
        obj.data = struct.unpack("<" + "H" * w * h * d, b[20:])
        return obj
