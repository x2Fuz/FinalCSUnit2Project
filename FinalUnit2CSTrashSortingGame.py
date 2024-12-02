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
falsecount = 0
truecount = 0
for i in range(0,len(itemsChosen)):
    playitem = itemsChosen[random.randint(0,len(itemsChosen))]

    answer = input("where does/do " + playitem + " go: ")

    if answer == "compostable" and (playitem == "Apple core" or "Eggshells" or "Bread Crust" or "Garden clippings" or "Coffee grounds"):
        truecount = truecount + 1
        print("Number of true is", truecount)
        print("Number of false is", falsecount)
    elif answer == "recycling" and (playitem == "Plastic bottle" or "Aluminum can" or "Glass jar" or "Cardboard box" or "Metal can"):
        truecount = truecount + 1
        print("Number of true is", truecount)
        print("Number of false is", falsecount)

    elif answer == "hazardous waste" and (playitem == "Batteries" or "Broken light bulb" or "Paint can" or "Electronics" or "Aerosol can"):
        truecount = truecount + 1
        print("Number of true is", truecount)
        print("Number of false is", falsecount)

    elif answer == "general waste" and (playitem == "Chip bag" or "Chewing gum" or "Clothing tags" or "Broken ceramic plate" or "Cigarette butt"):
        truecount = truecount + 1
        print("Number of true is", truecount)
        print("Number of false is", falsecount)
    else:
        falsecount = falsecount + 1
        print("Number of false is", falsecount)
        print("Number of true is", truecount)