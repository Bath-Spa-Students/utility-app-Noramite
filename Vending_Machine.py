import os

drinks = {
    1: "Water",
    2: "Coffee",
    3: "Tea",
    4: "Orange Juice",
    5: "Coca-Cola",
    6: "Prim",
    7: "Milkshake",
    8: "Green Smoothie",
    9: "Hot Chocolate",
    10: "Lean"
}
drinks_stock = {
    'water': '5',
    'Coffee'
    'Tea': '5',
    'Orange Juice': '5',
    'Coca-Cola': '5',
    'Prim': '5',
    'Milkshake': '5',
    'Green Smoothie': '5',
    'Hot Chocolate': '5',
    'Lean': '5'
}

drinks_price = {
    1: "2",
    2: "5",
    3: "2",
    4: "4",
    5: "4",
    6: "29",
    7: "20",
    8: "15",
    9: "20",
    10: "25"
}

snacks = {
    1: "Doritos",
    2: "Potato Chips",
    3: "Trail Mix",
    4: "Pretzels",
    5: "Fruit Slices"
}

snacks_price = {
    1: "3",
    2: "5",
    3: "4",
    4: "6",
    5: "9"
}

snacks_stock = {
    'Doritos': '5',
    'Potato Chips'
    'Trail Mix': '5',
    'Pretzels': '5',
    'Fruit Slices': '5',
}

def display_options(category, items):
    print(f"\n{category}")

    for key, value in items.items():
        print(f"{key}: {value}")

#SNAAAACCCKKKSSS
def payment_snacks():
    coin = input("(placeholder) which do you want?: ")
    os.system('cls')    
    
    if coin.isdigit() and int(coin) in snacks:

        selected_item = snacks[int(coin)]
        item_price = snacks_price[int(coin)]
        print(f"Selected: {selected_item}")
        os.system('cls')

        #broken
        money_inserted = input("(placeholder) Enter money: ")

        if money_inserted.isdigit() and int(money_inserted) >= int(item_price):

            Change = int(money_inserted) - int(item_price)
            print(f"(placeholder) Enjoy your {selected_item}.")
            print(f"your change is ${Change}")
        
        else:
            print("(placeholder) canceled.")#no ui fix this

    else:
        print("(placeholder) no selection")#ui later

#DRINKKKKSSSSS WOOOOO YEAAAHH BABY
def payment_drinks():
    coin = input("(placeholder) which do you want?: ")
    os.system('cls')  
    
    if coin.isdigit() and int(coin) in drinks:

        selected_item = drinks[int(coin)]
        print(f"Selected: {selected_item}")
        print("(placeholder)")

        #broken
        money_inserted = input("(placeholder) Enter money: ")

        if money_inserted.isdigit() and int(money_inserted) >= 0:
            print(f"(placeholder) Enjoy your {selected_item}.")
        
        else:
            print("(placeholder) canceled.")#no ui fix this

    else:
        print("(placeholder) no selection")#ui later



#this part is the actual vending machine part
#no ui fix later
while True:
    print("""\n██    ██ ███████ ███    ██ ██████  ██ ███    ██  ██████      ███    ███  █████   ██████ ██   ██ ██ ███    ██ ███████ 
██    ██ ██      ████   ██ ██   ██ ██ ████   ██ ██           ████  ████ ██   ██ ██      ██   ██ ██ ████   ██ ██      
██    ██ █████   ██ ██  ██ ██   ██ ██ ██ ██  ██ ██   ███     ██ ████ ██ ███████ ██      ███████ ██ ██ ██  ██ █████   
 ██  ██  ██      ██  ██ ██ ██   ██ ██ ██  ██ ██ ██    ██     ██  ██  ██ ██   ██ ██      ██   ██ ██ ██  ██ ██ ██      
  ████   ███████ ██   ████ ██████  ██ ██   ████  ██████      ██      ██ ██   ██  ██████ ██   ██ ██ ██   ████ ███████ 
                                                                                                                     
                                                                                                                     """)
    print("1: Drinks")
    print("2: Snacks")
    print("0: Exit")







    user_choice = input("======>: ")
    os.system('cls')

    if user_choice == "0":
        print("(placeholder)")
        break

    if user_choice == "1":
        display_options("""██████  ██████  ██ ███    ██ ██   ██ ███████ 
██   ██ ██   ██ ██ ████   ██ ██  ██  ██      
██   ██ ██████  ██ ██ ██  ██ █████   ███████ 
██   ██ ██   ██ ██ ██  ██ ██ ██  ██       ██ 
██████  ██   ██ ██ ██   ████ ██   ██ ███████ 
                                             
                                             """, drinks)
        
        payment_drinks()

    elif user_choice == "2":
        display_options("""███████ ███    ██  █████   ██████ ██   ██ ███████ 
██      ████   ██ ██   ██ ██      ██  ██  ██      
███████ ██ ██  ██ ███████ ██      █████   ███████ 
     ██ ██  ██ ██ ██   ██ ██      ██  ██       ██ 
███████ ██   ████ ██   ██  ██████ ██   ██ ███████ 
                                                  
                                                  """, snacks)
        payment_snacks()
    else:
        print("(placeholder)")
        continue
