#  класс стек вариант№5

class Stack:

    #Обработка переполнения памяти
    MAX_SIZE = 10000

    def __init__(self): #Инциализация пустого стека
        self._items = []

    def push(self, item): #Кладёт элемент наверх. Отклоняет переполнение стека
        if self.MAX_SIZE is not None and len(self._items) >= self.MAX_SIZE:
            raise OverflowError(f"Стек переполнен: превышен предел {self.MAX_SIZE}")
        self._items.append(item)

    def pop(self): #Удаляет и возвращает верхний элемент, обрабатывает пустой стек  
        if self.is_empty():
            raise IndexError("Нельзя извлечь элемент из пустого стека")
        return self._items.pop()

    def peek(self): #  Возвращает верхний элемент без удаления.Выбрасывает индекс ерор, если стек пуст
        if self.is_empty():
            raise IndexError("Вершина пустого стека недоступна")
        return self._items[-1]

    def is_empty(self): # True if stack == 0
        return len(self._items) == 0

    def size(self): # count in stack
        return len(self._items)

    def clear(self): # full clear stack
        self._items = []

    def __len__(self): #Встроенная поддержка len(stack) 
        return len(self._items)

    def __str__(self): 
        return f"Stack({self._items})"