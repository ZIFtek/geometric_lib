def area(a, b):
    """ 
    Вычисляет площадь прямоугольника по заданным сторонам.
    
        Параметры:
    
        a (float): длина первой стороны прямоугольника
        b (float): длина второй стороны прямоугольника
    
    Возвращает:
        float: площадь прямоугольника
    
    Примеры:
        area(2, 3) // 6
    """ 

    if not isinstance(a, (float, int)) or not isinstance(b, (float, int)):
        raise TypeError("Длина стороны должена быть числом (int или float)")

    if a < 0 or b < 0:
        raise ValueError("Длина стороны не может быть отрицательной")

    return a * b 

def perimeter(a, b):
    """ 
    Вычисляет периметр прямоугольника по заданным сторонам.
    
        Параметры:
        a (float): длина первой стороны прямоугольника
        b (float): длина второй стороны прямоугольника
    
    Возвращает:
        float: Периметр прямоугольника
    
    Примеры:
        perimeter(3, 4) // 14
    """ 

    if not isinstance(a, (float, int)) or not isinstance(b, (float, int)):
        raise TypeError("Длина стороны должена быть числом (int или float)")

    if a < 0 or b < 0:
        raise ValueError("Длина стороны не может быть отрицательной")

    return (a + b) * 2