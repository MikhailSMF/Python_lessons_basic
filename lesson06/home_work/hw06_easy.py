# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math
class Triangle:
    def __init__(self, x1,y1,x2,y2,x3,y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.b = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
        self.c = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)

    def area(self):
        '''
        Определение площади
        :return:
        '''
        return abs(self.x1*(self.y2 - self.y3) + self.x2*(self.y3 - self.y1) + self.x3*(self.y1 - self.y2)) / 2.0

    def perimeter(self):
        """
        Определение периметра
        :return:
        """
        return self.a + self.b + self.c

    def height(self):
        """
        Определение высоты
        :return:
        """
        return f'a= {round(2*self.area()/self.a,1)} \n Высота: b= {round(2*self.area()/self.b,1)} \n Высота: c= {round(2*self.area()/self.c,1)}'

point = Triangle(1,1,2,4,3,2)

print(f'Площадь: {point.area()}')
print(f'Периметр: {point.perimeter()}')
print(f'Высота: {point.height()}')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
