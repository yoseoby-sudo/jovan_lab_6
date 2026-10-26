import json
import os

#Reponsible for story and managing an product's state
class Product:

    #Setting attributes
    def __init__(self, product_id, name, price, stock):
        self._product_id =  product_id
        self._name = name
        self._price = price
        self._stock = stock

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def stock(self):
        return self._stock

    #Updates the stock quantity securely through a method.
    def update_stock(self, quantity):
        self._stock += quantity

    #Displays formatted information for this specific product.
    def display_information(self):
        print(
            f"ID: {self._product_id} | "
            f"Name: {self._name} | "
            f"Price: ${self._price:.2f} | "
            f"Stock: {self._stock}"
        )

    #Converts the Product object into a dictionary for JSON serialization.
    def to_dict(self):
        return {
            "id": self._product_id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock
        }

#Managing a collection of products and transaction history.
class Inventory:

    def __init__(self):
        self._products = []
        self._transaction_history = []

    #Adds a Product object to the inventory list.
    def add_product(self, product):
        self._products.append(product)

    #Searches for a Product by ID and returns the object, or None if not found.
    def search_product(self, product_id):
        for product in self._products:
            if product.product_id == product_id:
                return product
        return None

    #Displays all products in the inventory.
    def display_all(self):
        print("\nCurrent Inventory")
        print("-" * 64)
        if not self._products:
            print("No products in inventory.")
        else:
            for product in self._products:
                product.display_information()
        print("-" * 64)

    #Records a transaction entry.
    def add_transaction(self, product_id, amount):
        self._transaction_history.append({
            "product_id": product_id,
            "amount": amount
        })

    #Loads inventory data and transaction history from JSON file.
    def load_from_file(self, filename="inventory.json"):
        if os.path.exists(filename):
            print(f"{filename} found.")
            with open(filename, "r") as file:
                data = json.load(file)
            print("Inventory loaded successfully.")

            raw_inventory = data.get("inventory", [])
            self._transaction_history = data.get("transaction_history", [])

            #Convert raw dictionaries from JSON back into Product objects.
            self._products = []
            for item in raw_inventory:
                product = Product(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"]
                )
                self._products.append(product)
        else:
            print(f"{filename} not found. Starting with empty inventory.")
            self._products = []
            self._transaction_history = []

    def save_to_file(self, filename="inventory.json"):
        """Saves current inventory and transaction history to JSON file."""
        # Convert Product objects into dictionaries using to_dict()
        raw_inventory = [product.to_dict() for product in self._products]
        data = {
            "inventory": raw_inventory,
            "transaction_history": self._transaction_history
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print("Inventory saved successfully!")