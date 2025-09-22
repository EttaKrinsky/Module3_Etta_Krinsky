"""
Campus Cafe Without Functions
"""
def Campus_Cafe():
#The Cafe Menu:
    print("-Campus Cafe Menu-")
    print("Coffee = $2.25")
    print("Muffin = $2.75")
    print("Bagel = $2.50")
    #Asking the user how many coffees, muffins, and bagels:
    coffee = int(input("How many coffees? "))
    muffin = int(input("How many muffins? "))
    bagel = int(input("How many bagels? "))
    #labeling each item as it's price
    coffee = float(2.25)
    muffin = float(2.75)
    bagel = float(2.50)

    #Asking the user how much of a tip they want to give:
    tipQ = int(input("Enter Tip Percent (e.g., 10 for 10%): "))
    #Calculating the price based on how much of each item the user requests
    coffeePrice = coffee * 2.25
    muffinPrice = muffin * 2.75
    bagelPrice = bagel * 2.50
    tipPercent = tipQ / 100
    #Calculating Totals:
    subtotal = bagelPrice + muffinPrice + coffeePrice
    tax = (subtotal) * .08875
    tip = (subtotal) * tipPercent
    Total = subtotal + tax + tip
    #Printing the Receipt Line by Line:
    print("---Receipt---")
    print(f"{coffee} x Coffee @$2.25   ${coffeePrice}")
    print(f"{muffin} x Muffin @$2.75   ${muffinPrice:.2f}")
    print(f"{bagel} x Bagel @$2.50    ${bagelPrice:.2f}")
    print(f"Subtotal:             ${subtotal:.2f}")
    print(f"Tax (8.875%):         ${tax:.2f}")
    print(f"Tip({tipQ}%):    ${tip:.2f}")
    print(f"TOTAL:                  ${Total:.2f}")
    print("Thank you!")
    #Calling the Function
Campus_Cafe()

