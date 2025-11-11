def area(a, h):
    """ 
    Вычисляет площадь треугольника по основанию и высоте.
    
        Параметры:
        a (float): длина основания треугольника
        h (float): высота треугольника, проведенная к основанию
    
    Возвращает:
        float: Площадь треугольника.
    
    Примеры:
        area(6, 2) // 6.0
    """

    if not isinstance(a, (float, int)):
        raise TypeError("Длина основания должена быть числом (int или float)")

    if not isinstance(h, (float, int)):
        raise TypeError("Высота должена быть числом (int или float)")

    if a < 0:
        raise ValueError("Длина основания не может быть отрицательной")

    if h < 0:
        raise ValueError("Высота не может быть отрицательной")

    return a * h / 2

def perimeter(a, b, c):
    """ 
    Вычисляет периметр треугольника по длинам трех сторон.
    
        Параметры:
        a (float): длина первой стороны треугольника
        b (float): длина второй стороны треугольника
        c (float): длина третьей стороны треугольника
    
    Возвращает:
        float: периметр треугольника.
    
    Примеры:
        perimeter(2, 3, 4) // 9
    """ 

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("Длины сторон должены быть числами (int или float)")

    if a < 0 or b < 0 or c < 0:
        raise ValueError("Длины сторон не могут быть отрицательными")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Нарушено неравенство треугольника: сумма любых двух сторон должна быть больше третьей")

    return a + b + c