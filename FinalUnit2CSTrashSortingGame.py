import random
difficulty = input("Would you like to try the harder version, you are not allowed to make a mistake? (yes or no): ")
allitems = ["Plastic bottle", "Aluminum can", "Glass jar", "Cardboard box", "Metal can", "Apple core", "Eggshells", "Bread crust", "Garden clippings", "Coffee grounds", "Batteries", "Broken light bulb", "Paint can", "Electronics", "Aerosol can", "Chip bag", "Chewing gum", "Clothing tags", "Broken ceramic plate", "Cigarette butt"]

numberOfItems = 0
while numberOfItems < 1 or numberOfItems > 20:
    numberOfItems = int(input("Enter the number of trash items you would like to sort (1-20): "))

itemsChosen = []
itemcount = 0
correct = True
for i in range(0,numberOfItems):
    item = allitems[random.randint(0,19-itemcount)]
    itemcount = itemcount + 1
    allitems.remove(item)
    itemsChosen.append(item)
print(itemsChosen)
falsecount = 0
truecount = 0


if difficulty == "yes":
        for i in range(0, len(itemsChosen)):
            playitem = itemsChosen[0]

            answer = input(
                "where does/do " + playitem + " go (compostable, recycling, hazardous waste, general waste) : ")
            itemsChosen.pop(0)

            if answer == "compostable" and (
                    playitem == "Apple core" or "Eggshells" or "Bread Crust" or "Garden clippings" or "Coffee grounds"):
                truecount = truecount + 1
                print("Number of true is", truecount)
                print("Number of false is", falsecount)
            elif answer == "recycling" and (
                    playitem == "Plastic bottle" or "Aluminum can" or "Glass jar" or "Cardboard box" or "Metal can"):
                truecount = truecount + 1
                print("Number of true is", truecount)
                print("Number of false is", falsecount)

            elif answer == "hazardous waste" and (
                    playitem == "Batteries" or "Broken light bulb" or "Paint can" or "Electronics" or "Aerosol can"):
                truecount = truecount + 1
                print("Number of true is", truecount)
                print("Number of false is", falsecount)

            elif answer == "general waste" and (
                    playitem == "Chip bag" or "Chewing gum" or "Clothing tags" or "Broken ceramic plate" or "Cigarette butt"):
                truecount = truecount + 1
                print("Number of true is", truecount)
                print("Number of false is", falsecount)
            else:
                falsecount = falsecount + 1
                print("Number of true is", truecount)
                print("Number of false is", falsecount)

                correct = False
            if correct == False:
                print("Whoops you lost!")
                exit()


if difficulty == "no":
    for i in range(0, len(itemsChosen)):
        playitem = itemsChosen[0]

        answer = input("where does/do " + playitem + " go (compostable, recycling, hazardous waste, general waste) : ")
        itemsChosen.pop(0)

        if answer == "compostable" and (
                playitem == "Apple core" or "Eggshells" or "Bread Crust" or "Garden clippings" or "Coffee grounds"):
            truecount = truecount + 1
            print("Number of true is", truecount)
            print("Number of false is", falsecount)
        elif answer == "recycling" and (
                playitem == "Plastic bottle" or "Aluminum can" or "Glass jar" or "Cardboard box" or "Metal can"):
            truecount = truecount + 1
            print("Number of true is", truecount)
            print("Number of false is", falsecount)

        elif answer == "hazardous waste" and (
                playitem == "Batteries" or "Broken light bulb" or "Paint can" or "Electronics" or "Aerosol can"):
            truecount = truecount + 1
            print("Number of true is", truecount)
            print("Number of false is", falsecount)

        elif answer == "general waste" and (
                playitem == "Chip bag" or "Chewing gum" or "Clothing tags" or "Broken ceramic plate" or "Cigarette butt"):
            truecount = truecount + 1
            print("Number of true is", truecount)
            print("Number of false is", falsecount)
        else:
            falsecount = falsecount + 1
            print("Number of false is", falsecount)
            print("Number of true is", truecount)
