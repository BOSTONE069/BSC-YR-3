PI = 3.142

radious = int(input("Enter the value of the radious? "))
height = int(input("Enter the height of the cylinder: "))


def main():
    area_of_surfaces()


def area_of_circle():
    circle_area = 2 * PI * (radious ** 2)
    return circle_area


def area_of_rectangle():
    rectangle_area = PI * (radious + radious) * height
    return rectangle_area


def area_of_surfaces():
    surface_area = int(area_of_circle) + int(area_of_rectangle)
    return surface_area


if __name__ == '__main__':
    main()
