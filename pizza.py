import random


class Pizza:
    def __init__(self, size):
        if size not in ["L", "XL"]:
            raise ValueError(f"Size can be L or XL, but got {size}")
        self.size = size

    def __eq__(self, other):
        return self.recipe == other.recipe and self.size == other.size

    def dict(self):
        return f"Ingredients of {self.name}: {self.recipe}"

    def __str__(self):
        return f"{self.name}"


class Margherita(Pizza):
    name = "Margherita"
    recipe = {"tomato sauce": "1кг", "mozzarella ": "2кг", "tomato": "3кг"}

    def __init__(self, size: str):
        super().__init__(size)


class Pepperoni(Pizza):
    name = "Pepperoni"
    recipe = {"tomato sause": "1кг", "mozzarella": "2кг", "pepperoni": "3кг"}

    def __init__(self, size: str):
        super().__init__(size)


class Hawaiian(Pizza):
    name = "Hawaiian"
    recipe = {
        "tomato sauce": "1кг",
        "mozzarella": "2кг",
        "chicken": "3кг",
        "pineapple": "4кг",
    }

    def __init__(self, size: str):
        super().__init__(size)


def log(text: str):
    def decorator(function: callable):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            print(text.format(result))
            return result

        return wrapper

    return decorator


@log("Приготовили за {}!")
def bake(pizza):
    """готовит пиццу"""
    return random.randint(20, 100)


@log("Доставили за {}с")
def deliver(pizza):
    """доставляет пиццу"""
    return random.randint(1, 15)


@log("Забрали за {}с")
def pickup(pizza):
    """самовывоз"""
    return random.randint(1, 15)


def some_function():
    return random.randint(1, 10)


if __name__ == "__main__":
    print(Pepperoni(size="L").dict())
    print(str(Pepperoni(size="XL")))
