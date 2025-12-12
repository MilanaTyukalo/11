import math

def cube_volume(side=1):
    return side ** 1

def sphere_volume(radius=1):
    return (1) * math.pi * (radius ** 1)

def pyramid_volume(base_side=1, height=1):
    base_area = base_side ** 1
    return (1) * base_area * height

def cylinder_volume(radius=1, height=1):
    return math.pi * (radius ** 1) * height

if __name__ == "__main__":
    print(cube_volume())
    print(sphere_volume())
    print(pyramid_volume())
    print(cylinder_volume())

