PI = 3.142


def main():
    radii = int(input("Enter the value of the radious? "))
    height = int(input("Enter the height of the cylinder: "))
    area_of_circle(radii)
    area_of_rectangle(radii, height)
    area_of_surfaces()


def area_of_circle(x):
    circle_area = 2 * PI * (x ** 2)
    return circle_area


def area_of_rectangle(x, y):
    rectangle_area = PI * (x + x) * y
    return rectangle_area


def area_of_surfaces():
    surface_area = int(area_of_circle) + int(area_of_rectangle)
    return surface_area


main()
