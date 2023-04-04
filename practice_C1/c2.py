class SquareFactory:
    @staticmethod
    def create_squre(self, side):
        return Square(side)
    
class Square:
    _a = None
    def __init__(self, a):
        if a>0:
            self._a = a
    @property
    def a(self):
        return self._a
    @a.setter
    def a(self, value):
        if value>0:
            self._a=value