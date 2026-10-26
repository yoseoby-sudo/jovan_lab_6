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
    


# --- Test code for Product class ---
if __name__ == "__main__":
    # 1. Create a Product object
    p1 = Product(1, "Laptop", 1200.00, 15)
    
    # 2. Test display_information()
    print("Testing display_information():")
    p1.display_information()
    
    # 3. Test update_stock()
    print("\nTesting update_stock(+5):")
    p1.update_stock(5)
    p1.display_information()
    
    # 4. Test properties
    print(f"\nChecked property -> Product ID: {p1.product_id}, Name: {p1.name}")