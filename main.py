from Ray import Ray
from Rect import Rect

# test Ray.sort_by_distance
env = [Rect(0, 0, 1, 1)]
r = Ray((0, 0), 0)
print(r.get_intersection_points(env))