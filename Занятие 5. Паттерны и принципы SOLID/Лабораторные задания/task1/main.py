class ShoppingCart:
    """Класс, представляющий корзину для покупок в интернет-магазине    """

    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Метод, добавляющий товар в корзину"""
        self.items.append(item)

    def remove_item(self, item):
        """Метод, удаляющий товар из корзины"""
        self.items.remove(item)

    def calculate_total(self):
        """Метод, подсчитывающий общую стоимость товаров в корзине"""
        total = 0
        for item in self.items:
            total += item.price
        return total


class Item:
    """Класс, описывающий товар в интернет-магазине"""

    def __init__(self, name, price):
        self.name = name
        self.price = price


if __name__ == "__main__":
    cart = ShoppingCart()
    item1 = Item("Ноутбук", 1500)
    item2 = Item("Мышь", 50)
    item3 = Item("Клавиатура", 100)
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    cart.remove_item(item2)
    total = cart.calculate_total()
    print(f"Total: {total} руб.")


    class Analytics:  # Пример расширения функционала для сбора новых данных
        """Класс, собирающий аналитические данные о покупках"""

        def __init__(self):
            self.purchased_items = []


    def track_purchase(self, item):
        """Метод, отслеживающий покупку"""
        self.purchased_items.append(item)


    def get_total_purchases(self):
        """Метод для получения общего кол-ва совершенных покупок"""
        return len(self.purchased_items)


    class User:  # Пример расширения функционала для сбора новых данных о пользователе
        """Класс представляет инфо о пользователе в приложении"""

        def __init__(self, name, email):
            self.name = name
            self.email = email


    class Database:  # Пример расширения функциональности для новых хранилищ
        """Класс, представляющий функциональность для работы с БД в приложении"""

        def save_cart(self, cart):
            """Сохранение корзины в хранилище/БД"""
            # Сохранение корзины в базу данных
            pass

        def load_cart(self):
            """Выгрузка корзины из хранилища/БД"""
            # Загрузка корзины из базы данных
            pass
