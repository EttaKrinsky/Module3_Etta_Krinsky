"""

"""

def Campus_Cafe():
    print("-Campus Cafe Menu-")
    print("Coffee = $2.25")
    print("Muffin = $2.75")
    print("Bagel = $2.50")

    coffee = int(input("How many coffees? "))
    muffin = int(input("How many muffins? "))
    bagel = int(input("How many bagels? "))
    tipQ = int(input("Enter Tip Percent (e.g., 10 for 10%): "))

    def Format_Currency(coffee, muffin, bagel):
        coffee = float(2.25)
        muffin = float(2.75)
        bagel = float(2.50)
        return [coffee, muffin, bagel]
        
    Format_Currency(coffee, muffin, bagel)
    
    def Compute_Totals(coffee, muffin, bagel):
        
        coffeePrice = coffee * 2.25
        muffinPrice = muffin * 2.75
        bagelPrice = bagel * 2.50
        tipPercent = tipQ / 100
        
        subtotal = bagelPrice + muffinPrice + coffeePrice
        tax = (subtotal) * .08875
        tip = (subtotal) * tipPercent
        Total = subtotal + tax + tip
        return [coffeePrice, muffinPrice, bagelPrice, tipPercent]
    
    Compute_Totals(coffee, muffin, bagel)

    def Print_Receipt(coffee, bagel, muffin, tipQ, coffeePrice, muffinPrice, bagelPrice, subtotal, tax, tip, total):
        print("---Receipt---")
        print(f"{coffee} x Coffee @$2.25   ${coffeePrice}")
        print(f"{muffin} x Muffin @$2.75   ${muffinPrice:.2f}")
        print(f"{bagel} x Bagel @$2.50    ${bagelPrice:.2f}")
        print(f"Subtotal:             ${subtotal:.2f}")
        print(f"Tax (8.875%):         ${tax:.2f}")
        print(f"Tip({tipQ}%):    ${tip:.2f}")
        print(f"TOTAL:                  ${Total:.2f}")
        print("Thank you!")
    Print_Receipt(coffee, bagel, muffin, tipQ, coffeePrice, muffinPrice, bagelPrice, subtotal, tax, tip, total)

Campus_Cafe()
