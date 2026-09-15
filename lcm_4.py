#  НОК ВАРИАНТ №4

class LCMCalc: #Формула: НОК(a, b) = |a * b| / НОД(a, b).

    #Предел модуля аргумента — защита от случайных гигантских чисел. None = без предела
    MAX_VALUE = 10**9
    #Предел длины списка — защита от случайного миллиона элементов. None = без предела
    MAX_LIST_SIZE = 10000

    #Проверка: только целые числа, bool не считается (он подкласс int)
    @staticmethod
    def check_int(value):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"Ожидалось целое число, получено {type(value).__name__}: {value!r}")

    #Проверка: аргумент должен быть списком (не строкой, не кортежем, не None)
    @staticmethod
    def check_list(value):
        if value is None:
            raise TypeError("Список не может быть None")
        if not isinstance(value, list):
            raise TypeError(f"Ожидался список, получено {type(value).__name__}: {value!r}")

    #Проверка: модуль числа не превышает MAX_VALUE (если предел задан)
    @staticmethod
    def check_range(value):
        if LCMCalc.MAX_VALUE is not None and abs(value) > LCMCalc.MAX_VALUE:
            raise ValueError(f"Модуль числа {value} превышает допустимый предел {LCMCalc.MAX_VALUE}")

    #Комплексная проверка одного числа: тип + диапазон
    @staticmethod
    def validate_number(value):
        LCMCalc.check_int(value)
        LCMCalc.check_range(value)

    #НОД
    @staticmethod
    def gcd(first, second):
        LCMCalc.validate_number(first)
        LCMCalc.validate_number(second)
        first, second = abs(first), abs(second)
        while second != 0:
            first, second = second, first % second
        return first

    def lcm_two(self, first, second): # Возвращает НОК двух чисел. Отклоняет нецелые, нули и выход за предел
        self.validate_number(first)
        self.validate_number(second)
        if first == 0 or second == 0:
            raise ValueError("НОК с нулём не определён")
        return abs(first * second) // self.gcd(first, second)

    def lcm_list(self, numbers): # Возвращает НОК для списка. Отклоняет не-список, пустой, с нулём, с нецелыми, с выходом за предел
        self.check_list(numbers)
        if not numbers:
            raise ValueError("Список не может быть пустым")
        if self.MAX_LIST_SIZE is not None and len(numbers) > self.MAX_LIST_SIZE:
            raise ValueError(f"Длина списка {len(numbers)} превышает допустимый предел {self.MAX_LIST_SIZE}")
        for number in numbers: #Проверяем каждый элемент до расчётов
            self.validate_number(number)
        if numbers[0] == 0: #Первый элемент проверяем отдельно
            raise ValueError("НОК с нулём не определён")
        result = abs(numbers[0]) #НОК всегда неотрицателен
        for number in numbers[1:]:
            result = self.lcm_two(result, number)
        return result