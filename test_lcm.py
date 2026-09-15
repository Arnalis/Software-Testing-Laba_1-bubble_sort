import unittest
from lcm_4 import LCMCalc


class TestLCMCalc(unittest.TestCase):

    def setUp(self):
        self.calculator = LCMCalc()

    # Помощник для поэтапного вывода: что проверяем, что ожидалось и что получили
    def check_result(self, description, expected, actual):
        print(f"  Тест: {description}")
        print(f"    Ожидалось: {expected}")
        print(f"    Получено:  {actual}")
        print() #Пустая строка для отступа между тестами
        self.assertEqual(actual, expected)

    # Помощник для проверки исключения с поэтапным выводом
    def check_raises(self, description, exception_type, func, *args, **kwargs):
        print(f"  Тест: {description} должен выбросить {exception_type.__name__}")
        with self.assertRaises(exception_type) as context:
            func(*args, **kwargs)
        print(f"    Получено исключение: {type(context.exception).__name__}: {context.exception}")
        print() #Пустая строка для отступа между тестами

    # Тесты для gcd 

    def test_gcd_positive_numbers(self):
        """НОД(12, 18) должен быть равен 6."""
        self.check_result("НОД(12, 18)", 6, self.calculator.gcd(12, 18))

    def test_gcd_coprime_numbers(self):
        """НОД(7, 13) = 1, так как числа взаимно простые."""
        self.check_result("НОД(7, 13)", 1, self.calculator.gcd(7, 13))

    def test_gcd_same_numbers(self):
        """НОД(a, a) = a."""
        self.check_result("НОД(15, 15)", 15, self.calculator.gcd(15, 15))

    def test_gcd_with_zero(self):
        """НОД(0, 5) = 5 — для НОД нуль допустим."""
        self.check_result("НОД(0, 5)", 5, self.calculator.gcd(0, 5))

    def test_gcd_negative_numbers(self):
        """НОД должен работать с отрицательными числами."""
        self.check_result("НОД(-12, 18)", 6, self.calculator.gcd(-12, 18))

    # Тесты для lcm_two

    def test_lcm_two_simple(self):
        """НОК(4, 6) = 12."""
        self.check_result("НОК(4, 6)", 12, self.calculator.lcm_two(4, 6))

    def test_lcm_two_coprime(self):
        """НОК(5, 7) = 35."""
        self.check_result("НОК(5, 7)", 35, self.calculator.lcm_two(5, 7))

    def test_lcm_two_when_one_divides_other(self):
        """НОК(3, 9) = 9."""
        self.check_result("НОК(3, 9)", 9, self.calculator.lcm_two(3, 9))

    def test_lcm_two_negative(self):
        """НОК(-4, 6) = 12 (НОК всегда неотрицательно)."""
        self.check_result("НОК(-4, 6)", 12, self.calculator.lcm_two(-4, 6))

    # Обработчик.  НОК с нулём не определён математически
    def test_lcm_two_with_zero_raises_error(self):
        self.check_raises("НОК(0, 5)", ValueError, self.calculator.lcm_two, 0, 5)

    # Обработчик.   НОК определён только для целых, float отклоняется TypeError
    def test_lcm_two_with_float_raises_error(self):
        self.check_raises("НОК(4.5, 6)", TypeError, self.calculator.lcm_two, 4.5, 6)

    # Обработчик. bool — подкласс int, но как аргумент НОК бессмысленен
    def test_lcm_two_with_bool_raises_error(self):
        self.check_raises("НОК(True, 6)", TypeError, self.calculator.lcm_two, True, 6)

    # Обработчик.   строка вместо числа
    def test_lcm_two_with_string_raises_error(self):
        self.check_raises("НОК('4', 6)", TypeError, self.calculator.lcm_two, "4", 6)

    # Обработчик.    None вместо числа
    def test_lcm_two_with_none_raises_error(self):
        self.check_raises("НОК(None, 6)", TypeError, self.calculator.lcm_two, None, 6)

    # Обработчик.    комплексное число отклоняется
    def test_lcm_two_with_complex_raises_error(self):
        self.check_raises("НОК(2+3j, 6)", TypeError, self.calculator.lcm_two, 2+3j, 6)

    # Обработчик.  список вместо числа
    def test_lcm_two_with_list_raises_error(self):
        self.check_raises("НОК([4], 6)", TypeError, self.calculator.lcm_two, [4], 6)

    # Обработчик.   гигантское число выходит за предел MAX_VALUE
    def test_lcm_two_over_max_value_raises_error(self):
        self.check_raises("НОК(10**10, 6)", ValueError, self.calculator.lcm_two, 10**10, 6)

    # Тесты для lcm_list 

    def test_lcm_list_typical(self):
       #НОК [2,3,4] = 12
        self.check_result("НОК([2, 3, 4])", 12, self.calculator.lcm_list([2, 3, 4]))

    def test_lcm_list_single_element(self):
        #Нок [7] = 7
        self.check_result("НОК([7])", 7, self.calculator.lcm_list([7]))

    # Проверка, что НОК одиночного отрицательного числа берётся по модулю
    def test_lcm_list_single_negative(self):
        #НОК [-7] = 7, знак отбрасывается
        self.check_result("НОК([-7])", 7, self.calculator.lcm_list([-7]))

    # Проверка, что список из отрицательных чисел даёт положительный НОК
    def test_lcm_list_all_negative(self):
        #НОК [-2,-3,-4] = 12
        self.check_result("НОК([-2, -3, -4])", 12, self.calculator.lcm_list([-2, -3, -4]))

    # Проверка, что смешанные знаки не влияют на результат
    def test_lcm_list_mixed_signs(self):
        #НОК [-2, 3, -4] = 12
        self.check_result("НОК([-2, 3, -4])", 12, self.calculator.lcm_list([-2, 3, -4]))

    # Обработчик.    пустой список
    def test_lcm_list_empty_raises_error(self):
        self.check_raises("НОК([])", ValueError, self.calculator.lcm_list, [])

    # Обработчик.    список из одного нуля
    def test_lcm_list_single_zero_raises_error(self):
        self.check_raises("НОК([0])", ValueError, self.calculator.lcm_list, [0])

    # Обработчик.   два нуля в списке
    def test_lcm_list_two_zeros_raises_error(self):
        self.check_raises("НОК([0, 0])", ValueError, self.calculator.lcm_list, [0, 0])

    # Обработчик.  нуль среди обычных чисел
    def test_lcm_list_with_zero_among_numbers_raises_error(self):
        self.check_raises("НОК([2, 0, 4])", ValueError, self.calculator.lcm_list, [2, 0, 4])

    # Обработчик.   дробное число внутри списка
    def test_lcm_list_with_float_raises_error(self):
        self.check_raises("НОК([2, 3.5, 4])", TypeError, self.calculator.lcm_list, [2, 3.5, 4])

    # Обработчик.   строка внутри списка
    def test_lcm_list_with_string_raises_error(self):
        self.check_raises("НОК([2, '3', 4])", TypeError, self.calculator.lcm_list, [2, "3", 4])

    # Обработчик.    None внутри списка
    def test_lcm_list_with_none_raises_error(self):
        self.check_raises("НОК([2, None, 4])", TypeError, self.calculator.lcm_list, [2, None, 4])

    # Обработчик.   bool внутри списка
    def test_lcm_list_with_bool_raises_error(self):
        self.check_raises("НОК([2, True, 4])", TypeError, self.calculator.lcm_list, [2, True, 4])

    # Обработчик. None вместо списка
    def test_lcm_list_with_none_container_raises_error(self):
        self.check_raises("НОК(None)", TypeError, self.calculator.lcm_list, None)

    # Обработчик.  строка вместо списка
    def test_lcm_list_with_string_container_raises_error(self):
        self.check_raises("НОК('2 3 4')", TypeError, self.calculator.lcm_list, "2 3 4")

    # Обработчик.    кортеж вместо списка
    def test_lcm_list_with_tuple_container_raises_error(self):
        self.check_raises("НОК((2, 3, 4))", TypeError, self.calculator.lcm_list, (2, 3, 4))

    # Обработчик.   число вместо списка
    def test_lcm_list_with_int_container_raises_error(self):
        self.check_raises("НОК(42)", TypeError, self.calculator.lcm_list, 42)

    # Обработчик.   гигантское число внутри списка выходит за предел
    def test_lcm_list_over_max_value_raises_error(self):
        self.check_raises("НОК([2, 10**10])", ValueError, self.calculator.lcm_list, [2, 10**10])

    # Обработчик.    слишком длинный список
    def test_lcm_list_too_long_raises_error(self):
        big_list = list(range(1, self.calculator.MAX_LIST_SIZE + 2))
        self.check_raises("НОК(список > MAX_LIST_SIZE)", ValueError, self.calculator.lcm_list, big_list)


if __name__ == "__main__":
    print("=" * 60)
    print("  МОДУЛЬНЫЕ ТЕСТЫ ДЛЯ КЛАССА LCMCalc (НОК)")
    print("=" * 60)
    unittest.main(verbosity=0)