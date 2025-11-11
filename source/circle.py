import math


def area(r):
    """ 
    Вычисляет площадь круга по заданному радиусу.

        Параметры:
            r (float): Радиус круга

        Возвращает:
            float: площадь круга

        Примеры:
            area(2) // 12.566370614359172
    """ 
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом (int или float)")

    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")

    return math.pi * r * r


def perimeter(r):
    """ 
    Вычисляет длину окружности (периметр круга) по заданному радиусу.
    
        Параметры:
            r (float): радиус окружности
        
        Возвращает:
            float: длина окружности
    
        Примеры:
            perimeter(2) // 12.566370614359172
    """
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом (int или float)")

    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")

    return 2 * math.pi * r