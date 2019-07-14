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
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math
class Trapezium:
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def proverka(self):
        c = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        d = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))

        if c == d:
            return("Трапеция равнобокая")
        else:
            return("Трапеция неравнобокая")

    def area(self):
        '''
        Определение площади
        :return:
        '''
        c = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        d = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))
        a = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        b = math.sqrt(((self.x4 - self.x1) ** 2) + ((self.y4 - self.y1) ** 2))
        return f'Площадь равна: {((a+b)/2)*(math.sqrt((c**2)-((((b-a)**2)+(c**2)-(d**2))/(2*(b-a)))))}'

    def perimeter(self):
        """
        Определение периметра
        :return:
        """
        c = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        d = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))
        a = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        b = math.sqrt(((self.x4 - self.x1) ** 2) + ((self.y4 - self.y1) ** 2))
        return f'Периметр равен: {a+b+c+d}'

    def side(self):
        '''
        Определение длин сторон
        :return:
        '''
        c = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
        d = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
        a = math.sqrt(((self.x3-self.x2) ** 2) + ((self.y3-self.y2) ** 2))
        b = math.sqrt(((self.x4-self.x1) ** 2) + ((self.y4-self.y1) ** 2))
        return f'Длина сторон: \nAB: {a} \nBC: {c} \nCD: {d} \nDC: {b}'
point = Trapezium(0,1,2,3,4,5,6,7)

print(point.proverka())
print(point.perimeter())
print(point.area())
print(point.side())
