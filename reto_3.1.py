import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.length = self.compute_length()
        self.slope = self.compute_slope()
    
    def compute_length(self):
            dx = self.end.x - self.start.x
            dy = self.end.y - self.start.y
            return math.sqrt(dx**2 + dy**2)

    def compute_slope(self):
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        if dx == 0:
            return 90.0
        angle_rad = math.atan2(dy, dx)
        return math.degrees(angle_rad)

    def compute_horizontal_cross(self):
        return (self.start.y * self.end.y) <= 0 and self.start.y != self.end.y

    def compute_vertical_cross(self):
        return (self.start.x * self.end.x) <= 0 and self.start.x != self.end.x

class Rectangle:
    def __init__(self, line1, line2, line3, line4):
        self.lines = [line1, line2, line3, line4]
