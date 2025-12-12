import math

# 1. Объём куба
def cube_volume(side=1):
    return side ** 3

# 2. Объём сферы
def sphere_volume(radius=2):
    return (4/3) * math.pi * (radius ** 3)

# 3. Объём пирамиды (правильной четырёхугольной)
def pyramid_volume(base_side=3, height=4):
    base_area = base_side ** 2
    return (1/3) * base_area * height

# 4. Объём цилиндра
def cylinder_volume(radius=5, height=6):
    return math.pi * (radius ** 2) * height

if __name__ == "__main__":
    print("Объём куба (side=1):", cube_volume())
    print("Объём сферы (radius=2):", sphere_volume())
    print("Объём пирамиды (base_side=3, height=4):", pyramid_volume())
    print("Объём цилиндра (radius=5, height=6):", cylinder_volume())

