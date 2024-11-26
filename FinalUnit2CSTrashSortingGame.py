import random

allitems = ["Plastic bottle", "Aluminum can", "Glass jar", "Cardboard box", "Metal can", "Apple core", "Eggshells", "Bread crust", "Garden clippings", "Coffee grounds", "Batteries", "Broken light bulb", "Paint can", "Electronics", "Aerosol can", "Chip bag", "Chewing gum", "Clothing tags", "Broken ceramic plate", "Cigarette butt"]
numberOfItems = int(input("Enter the number of trash items you would like to sort (1-20)"))
itemsChosen = []
itemcount = 0
for i in range(0,numberOfItems):
    item = allitems[random.randint(0,19-itemcount)]
    itemcount = itemcount + 1
    allitems.remove(item)
    itemsChosen.append(item)
print(itemsChosen)
