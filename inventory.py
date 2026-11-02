import json
import os
from product import Product

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
    
    #Saves current inventory and transaction history to JSON file.
    def save_to_file(self, filename="inventory.json"):
        #Convert Product objects into dictionaries using to_dict().
        raw_inventory = [product.to_dict() for product in self._products]
        data = {
            "inventory": raw_inventory,
            "transaction_history": self._transaction_history
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print("Inventory saved successfully!")
