def solution(area):
    sub_areas = []
    is_int = isinstance(area, int)
    if not is_int:
        return sub_areas
    while 1000000 >= area > 0:
        biggest_square_side = int(area ** 0.5)
        biggest_square_area = biggest_square_side ** 2
        area -= biggest_square_area
        sub_areas.append(biggest_square_area)

    return sub_areas