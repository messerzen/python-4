import math

def calc_angle_mbc(a, b):
    hypot = math.hypot(a, b)
    return round(math.degrees(math.asin(a/hypot)))

