## Запуск тестов
```
python3 -m unittest -v tests.py
test_bake_wo_log (tests.TestPizza.test_bake_wo_log)
Тест функции bake без декоратора. ... Приготовили за 50!
ok
test_deco_log (tests.TestPizza.test_deco_log)
Тест функции bake после декоратора. ... Приготовили за 50!
Приготовили за 50!
ok
test_dict (tests.TestPizza.test_dict)
Тест метода, возвращающего словарь рецепта. ... ok
test_equality (tests.TestPizza.test_equality)
Тест метода сравнения пицц. ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```