def area(a):
    """ 
    Вычисляет площадь квадрата по заданной длине стороны.
    
        Параметры:
        a (float): длина стороны квадрата
    
    Возвращает:
        float: площадь квадрата
    
    Примеры:
        area(3) // 9
    """
    
    if not isinstance(a, (float, int)):
        raise TypeError("Длина стороны должена быть числом (int или float)")

    if a < 0:
        raise ValueError("Длина стороны не может быть отрицательной")
    return a * a

def perimeter(a):
    """ 
    Вычисляет периметр квадрата по заданной длине стороны.
    
        Параметры:
        a (float): длина стороны квадрата
    
    Возвращает:
        float: периметр квадрата
    
    Примеры:
        perimeter(3) // 12
    """

    if not isinstance(a, (float, int)):
        raise TypeError("Длина стороны должена быть числом (int или float)")

    if a < 0:
        raise ValueError("Длина стороны не может быть отрицательной")

    return 4 * a