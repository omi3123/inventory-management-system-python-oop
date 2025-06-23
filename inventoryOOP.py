class Item:
    def __init__(self,price,quantity,name):
        self.price=price
        self.quantity=quantity
        self.name=name
    def __str__(self):
        return f"{self.name} - {self.price} - {self.quantity}"
class Inventory:
    def __init__(self):
        self.items=[]
    def add_item(self,item):
        self.items.append(item)
        print(f"{item} added to the inventory")
    def remove_item(self,item_name):
        self.items=[item for item in self.items!=item_name]
        print(f"{item_name} is removed from the inventory")
    def update_item(self,item_name,new_quantity):
        for item in self.items:
            if item.name==item_name:
                item.quantity=new_quantity
                print(f"{item.name} update as {new_quantity}")
    def display_item(self):
        if not self.items:
            print("Inventory is empty")
        else:
            for item in self.items:
                print(item)
inventory=Inventory()
item1=Item("Laptop", 1200, 10)
item2=Item("Headphones", 150, 30)
inventory.add_item(item1)
inventory.add_item(item2)
inventory.display_item()