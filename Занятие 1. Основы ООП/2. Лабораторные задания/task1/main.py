import doctest


class ModernBook:
    def __init__(self, author: str, public_year: float):
        """
        Поиск и чтение объекта современная книга

        :param author: автор книги
        :param public_year: год издания книги

        Примеры:
        >>> book = ModernBook('Не ной', 2019)  # инициализация экземпляра класса
        """
        if not isinstance(author, str):
            raise TypeError('Введите автора в строковом формате')
        if not author.isalpha():
            raise ValueError('Введенное значение должно состоять только из букв.')
        self.author = author

        if not isinstance(public_year, int):
            raise TypeError("Введите год издания в формате целого числа")
        if public_year < 2011 or public_year > 2023:
            raise ValueError("Введите год издания современной книги от 2011 до 2023 года")
        self.public_year = public_year

    def is_popular(self) -> bool:
        """
        Функция, которая проверяет, является ли книга популярной

        : return Является ли популярной
        Примеры:
        >>> book = ModernBook("Не ной", 2019)
        >>> book.is_popular()
        """
        ...

    def last_read_page(self, read_pages: int) -> None:
        """
        Указание последней прочитанной страницы

        :param read_pages: Кол-во прочитанных страниц
        Примеры:
        >>> book = ModernBook("Не ной", 2019)
        >>> book.last_read_page(36)
        """
        if not isinstance(read_pages, int):
            raise TypeError("Введите целое число прочитанных страниц")
        if read_pages < 0 or read_pages > 2000:
            raise ValueError("Введите прочитанное положительное кол-во страниц не превышающее 2000")

class Person:
    def __init__(self, name: str, age: float, gender: str):
        """
        Метод описания человека

        :param name: имя человека
        :param age: возраст человека
        :parem gender: пол человека

        Примеры:
        >>> person = Person(Мария, 22, женский)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError('Введите имя в строковом формате')
        if len(name) < 2:
            raise ValueError("Имя должно содержать как минимум 2 символа.")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Введите возраст в формате целого числа")
        if age < 0:
            raise ValueError("Введите возраст в виде положительного числа")

        if not isinstance(gender, str):
            raise TypeError("Введите пол в строковом формате")
        if gender not in ["женский", "мужской"]:
            raise ValueError("Выберите пол женский или мужской")

    def birthday(self) -> int:
        """
            Функция, которая прибавляет год к возрасту

            : return f"С днем рождения, {self.name}! Еще не старый"
            Примеры:
            >>> person = Person(Мария, 23, женский)
            >>> person.birthday(23)
                """
        self.age += 1
        return f"С днем рождения, {self.name}! {self.age} - еще не старый"

class Car:
    def __init__(self, brand_model: str, horsepower: float, year: float):
        """
        Метод описания машины

        :param brand: марка и модель машины
        :param horsepower: лошадиные силы
        :param year: год выпуска авто

        Примеры:
        >>> car = Car(Kia Rio, 120, 2017)  # инициализация экземпляра класса
        """
        if not isinstance(brand_model, str):
            raise TypeError('Введите марку и модель в строковом формате')
        if not brand_model.isalpha():
            raise ValueError('Введенное значение должно состоять только из букв.')
        self.brand_model = brand_model

        if not isinstance(horsepower, float):
            raise TypeError('Введите кол-во лошадиных сил в виде целого числа')
        if horsepower < 0:
            raise ValueError('Введенное значение должно быть положительным')
        self.horsepower = horsepower

        if not isinstance(year, float):
            raise TypeError('Введите год выпуска в виде целого числа')
        if year < 0:
            raise ValueError('Введенное значение должно быть положительным')
        self.year = year

    def add_speed(self, add_speed: int):
        """
        Метод увеличивает скорость

        :param add_speed: ускорение авто в км\ч
       :return новая скорость автомобиля

       Примеры:
       >>> car = Car(Kia Rio, 120, 2017) # инициализация экземпляра класса
       >>> car.speed = 50
       >>> car.add_speed(45)
       95
       """
        ...

    def change_color(self, new_colour: float) -> None:
        """
        Метод выбора нового цвета из каталога

        :param new_colour: номер цвета в каталоге
       :return None

       Примеры:
       >>> car = Car(Kia Rio, 120, 2017) # инициализация экземпляра класса
       >>> car.change_color("Y1209")
       """
        ...


if __name__ == "__main__":
    doctest.testmod()
