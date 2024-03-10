import csv

from typing import NoReturn


class Products:
    def __init__(self) -> None:
        self.products_dict: dict[str, float] = {}
        self.product_income: dict[str, int] = {}
        self.gross_income = 0
        self.staff_expenses = 0
        self.other_expenses = 0
        self.net_income = 0

    def add_product(self, filename: str) -> None:
        """
        Add products from CSV
        Args:
            filename (str): The path to the CSV file with product data.
        """
        with open(filename, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # noinspection PyTypeChecker
                product, price = row['Product'], float(row['Price'])
                self.products_dict[product] = price

    def initialize_product_income(self) -> None:
        """
        Initialize hard-coded product income.
        Only adds income for products that exist in the products_dict.
        """
        initial_income = {
            "Bubblegum": 202,
            "Toffee": 118,
            "Ice cream": 2250,
            "Milk chocolate": 1680,
            "Doughnut": 1075,
            "Pancake": 80
        }
        for product, income in initial_income.items():
            if product in self.products_dict:
                self.product_income[product] = income
            else:
                print(f"Warning: {product} not in inventory, income data not added.")

    def calculate_product_income(self) -> int:
        total_income = 0
        for item_income in self.product_income.values():
            total_income += item_income
        self.gross_income = total_income
        return self.gross_income

    def add_staff_expenses(self) -> None:
        print("Staff expenses:")
        self.staff_expenses = int(input())

    def add_other_expenses(self) -> None:
        print("Other expenses:")
        self.other_expenses = int(input())

    def calculate_net_income(self) -> None:
        self.add_staff_expenses()
        self.add_other_expenses()
        self.net_income = (self.gross_income
                           - self.staff_expenses
                           - self.other_expenses)
        print(f"Net income: ${self.net_income}")

    def print_menu(self) -> None:
        """
        Prints the menu, casting prices to int if no decimal value
        """
        print("Prices:")
        for product, price in self.products_dict.items():
            if price.is_integer():
                print(f'{product}: ${int(price)}')
            else:
                print(f'{product}: ${price}')

    def print_income(self) -> None:
        """
        Prints the product incomes, casting values to int if no decimal value
        """
        print("Earned amount:")
        for product, income in self.product_income.items():
            print(f'{product}: ${income}')
        print(f"\nIncome: ${self.calculate_product_income()}")


def main() -> NoReturn:
    products = Products()
    products.add_product('products.csv')
    # products.print_menu()
    products.initialize_product_income()
    products.print_income()
    products.calculate_net_income()


if __name__ == "__main__":
    main()
