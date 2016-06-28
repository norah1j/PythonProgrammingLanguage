class ShoppingList:
    products = []

    def __init__(self):
        print('Shopping list created')

    def add(self, name):
        self.products.append(name)

    def show(self):
        print(self.products)

groceries = ShoppingList()
groceries.add('Peanutbutter')
groceries.add('Milk')
groceries.show()