
class Ray:
    def __init__(self, origin, dir):
        self.origin = origin
        self.dir = dir
    
    def get_intersection_points(self, environment):
        points = []
        for object in environment:
            if isinstance(object, Rect):
                points.extend(self.intersect_rect(object))
        
        return self.sort_by_distance(points)

    
    def intersect_rect(self, rect):
        return [(1, 2), (0, 0), (0, -1)]
    

    def sort_by_distance(self, points):
        points.sort(key = lambda p: (p[0] - self.origin[0])**2 + (p[1] - self.origin[1])**2)
        return points


class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


# test Ray.sort_by_distance

env = [Rect(0, 0, 1, 1)]
r = Ray((0, 0), 0)
print(r.get_intersection_points(env))