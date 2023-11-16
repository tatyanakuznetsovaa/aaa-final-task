import unittest
from unittest.mock import patch
from pizza import Pepperoni, Margherita, Hawaiian, bake, log


class TestPizza(unittest.TestCase):
    def test_equality(self):
        """Тест метода сравнения пицц."""
        hawaiian_1 = Hawaiian(size="L")
        hawaiian_2 = Hawaiian(size="L")
        margherita_1 = Margherita(size="XL")
        pepperoni_2 = Pepperoni(size="XL")
        assert hawaiian_1 == hawaiian_2 and margherita_1 != pepperoni_2

    def test_dict(self):
        """Тест метода, возвращающего словарь рецепта."""
        dct = {"tomato sauce": "1кг", "mozzarella ": "2кг", "tomato": "3кг"}
        assert Margherita(size="L").dict() == f"Ingredients of Margherita: {dct}"

    def test_bake_wo_log(self):
        """Тест функции bake без декоратора."""
        with patch("random.randint") as randint_mock:
            got_randint = 50
            randint_mock.return_value = got_randint
            self.assertEqual(bake(Hawaiian(size="L")), got_randint)

    def test_deco_log(self):
        """Тест функции bake после декоратора."""
        got_randint = 50
        with patch("random.randint") as rt:
            rt.return_value = got_randint
            self.assertEqual(
                log("Приготовили за {}!")(bake)(Hawaiian(size="L")), got_randint
            )


if __name__ == "__main__":
    unittest.main()
