import unittest
from stack_5 import Stack

#Модульные тесты для класса "стек"
class TestStack(unittest.TestCase):

    def setUp(self):
        # Каждый тест создает пустой стек
        self.stack = Stack()

    # Поэтапный вывод
    def check_result(self, description, expected, actual):
        print(f"    Тест: {description}")
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
        print() #Пустая строка для отступа между тестами или \n

    # Проверка начального состоянаия стека

    def test_new_stack_is_empty(self):
        """Новый стек должен быть пустым."""
        self.check_result("is_empty() нового стека", True, self.stack.is_empty())

    def test_new_stack_size_is_zero(self):
        """Размер нового стека = 0."""
        self.check_result("size() нового стека", 0, self.stack.size())

    # Проверка push 

    def test_push_increases_size(self):
        """После push размер инкрементируется"""
        self.stack.push(10)
        self.check_result("size() после одного push", 1, self.stack.size())

    #Тут не пустой
    def test_push_makes_stack_not_empty(self):
        """После push стек перестаёт быть пустым.""" 
        self.stack.push(42)
        self.check_result("is_empty() после push", False, self.stack.is_empty())

    def test_push_multiple_increases_size(self):
        """Несколько push увеличивают размер соответственно"""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.check_result("size() после трёх push", 3, self.stack.size())

    # Last in first out 

    def test_pop_returns_last_pushed(self):
        """pop возвращает последний добавленный элемент"""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.check_result("pop() после push 1,2,3", 3, self.stack.pop())

    def test_pop_reduces_size(self):
        """После pop размер уменьшается."""
        self.stack.push(5)
        self.stack.push(6)
        self.stack.pop()
        self.check_result("size() после pop", 1, self.stack.size())

    def test_pop_multiple_in_lifo_order(self):
        """Несколько pop возвращают элементы в обратном порядке (LIFO)"""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        first_out = self.stack.pop()
        second_out = self.stack.pop()
        third_out = self.stack.pop()
        self.check_result("порядок pop (LIFO)", [3, 2, 1], [first_out, second_out, third_out])

    # Обработчик -    pop на пустом стеке выбрасывает IndexError
    def test_pop_from_empty_raises_error(self):
        self.check_raises("pop() на пустом стеке", IndexError, self.stack.pop)

    #  Проверка peek

    def test_peek_returns_top_without_removing(self):
        """peek возвращает верхний элемент, но не удаляет его."""
        self.stack.push(100)
        self.stack.push(200)
        top = self.stack.peek()
        self.check_result("peek() после push 100,200", 200, top)
        self.check_result("size() после peek (не изменился)", 2, self.stack.size())

    def test_peek_returns_same_element_on_repeat(self):
        """Повторный peek возвращает тот же элемент"""
        self.stack.push(7)
        first_peek = self.stack.peek()
        second_peek = self.stack.peek()
        self.check_result("два подряд peek() возвращают одно и то же", [7, 7], [first_peek, second_peek])

    # Обработчик -    peek на пустом стеке выбрасывает IndexError
    def test_peek_on_empty_raises_error(self):
        self.check_raises("peek() на пустом стеке", IndexError, self.stack.peek)

    # Проверка clear

    def test_clear_empties_stack(self):
        """После clear стек пуст."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.clear()
        self.check_result("size() после clear", 0, self.stack.size())
        self.check_result("is_empty() после clear", True, self.stack.is_empty())

    def test_clear_on_empty_stack_is_safe(self):
        """clear на пустом стеке не вызывает ошибок"""
        self.stack.clear()
        self.check_result("size() после clear пустого стека", 0, self.stack.size())

    # Обработчик -    push после clear работает как на новом стеке
    def test_push_after_clear_works(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.clear()
        self.stack.push(99)
        self.check_result("push после clear", [99], [self.stack.peek()])

    # Проверка поддержки len() и str()

    def test_len_supports_builtin(self):
        """len(stack) работает через __len__"""
        self.stack.push(1)
        self.stack.push(2)
        self.check_result("len(stack) после двух push", 2, len(self.stack))

    def test_str_representation(self):
        """str(stack) показывает содержимое"""
        self.stack.push(1)
        self.stack.push(2)
        self.check_result("str(stack)", "Stack([1, 2])", str(self.stack))

    # Проверка, что стек работает с любыми типами значений

    def test_push_float_value(self):
        """Стек принимает float"""
        self.stack.push(3.14)
        self.check_result("pop() после push float", 3.14, self.stack.pop())

    def test_push_string_value(self):
        """Стек принимает строки"""
        self.stack.push("hello")
        self.check_result("pop() после push строки", "hello", self.stack.pop())

    def test_push_none_value(self):
        """Стек принимает None как значение"""
        self.stack.push(None)
        self.check_result("pop() после push None", None, self.stack.pop())

    def test_push_list_value(self):
        """Стек принимает списки (как объекты)"""
        self.stack.push([1, 2, 3])
        self.check_result("pop() после push списка", [1, 2, 3], self.stack.pop())

    # Обработчик -    переполнение стека выбрасывает OverflowError
    def test_push_over_max_size_raises_error(self):
        #Наполняем стек до предела и пробуем добавить ещё один элемент
        for index in range(self.stack.MAX_SIZE):
            self.stack.push(index)
        self.check_raises("push() при полном стеке", OverflowError, self.stack.push, 999)

    # Обработчик -    push без аргумента выбрасывает TypeError 
    def test_push_without_argument_raises_error(self):
        self.check_raises("push() без аргумента", TypeError, self.stack.push)

    # Обработчик -    push с лишними аргументами выбрасывает TypeError
    def test_push_with_extra_arguments_raises_error(self):
        self.check_raises("push(1, 2)", TypeError, self.stack.push, 1, 2)


if __name__ == "__main__":
    print("=" * 60)
    print("  МОДУЛЬНЫЕ ТЕСТЫ ДЛЯ КЛАССА Stack")
    print("=" * 60)
    unittest.main(verbosity=0)