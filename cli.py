import click
import pizza
from pizza import Pepperoni, Margherita, Hawaiian, bake, deliver, pickup


@click.group()
def cli():
    pass


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizza_name", nargs=1)
@click.argument("size", default="L")
def order(pizza_name: str, size: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    if pizza_name == pizza.Margherita.name:
        order_pizza = Margherita(size)
    elif pizza_name == pizza.Pepperoni.name:
        order_pizza = Pepperoni(size)
    elif pizza_name == pizza.Hawaiian.name:
        order_pizza = Hawaiian(size)
    else:
        print("Available menu: Margherita, Pepperoni, Hawaiian")
        return

    bake(order_pizza)

    if delivery:
        deliver(order_pizza)
    else:
        pickup(order_pizza)


@cli.command()
def menu():
    """Показывает меню"""
    available = [pizza.Margherita.name, pizza.Pepperoni.name, pizza.Hawaiian.name]
    print("Наше меню сегодня:")
    for p in available:
        print(p)


if __name__ == "__main__":
    cli()