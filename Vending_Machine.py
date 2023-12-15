import os,time 
#dictionary for every item sold in the vending machine
drinks_dict = {
    "D1": {"name": "Water", "stock": 5, "price": "2"},
    "D2": {"name": "Coffee", "stock": 5, "price": "5"},
    "D3": {"name": "Tea", "stock": 5, "price": "2"},
    "D4": {"name": "Orange Juice", "stock": 5, "price": "4"},
    "D5": {"name": "Coca Cola", "stock": 5, "price": "4"},
    "D6": {"name": "Prime", "stock": 5, "price": "29"},
    "D7": {"name": "Milkshake", "stock": 5, "price": "15"},
    "D8": {"name": "Green Smoothie", "stock": 5, "price": "20"},
    "D9": {"name": "Hot Chocolate", "stock": 5, "price": "20"},
    "D10": {"name": "Liquid Death", "stock": 5, "price": "25"}
    }

snacks_dict = {
    "S1": {"name": "Doritos", "stock": 5, "price": "3"},
    "S2": {"name": "Potato Chips", "stock": 5, "price": "5"},
    "S3": {"name": "Trail Mix", "stock": 5, "price": "4"},
    "S4": {"name": "Pretzels", "stock": 5, "price": "6"},
    "S5": {"name": "Fruit Slices", "stock": 5, "price": "9"}
    }
#Client's balance that can be changed
Client_balance = 0

#Ascii art for titles
def Big_Drinks_list():
    print("""\n  ██╗██████╗ ██████╗ ██╗███╗   ██╗██╗  ██╗███████╗██╗  
 ██╔╝██╔══██╗██╔══██╗██║████╗  ██║██║ ██╔╝██╔════╝╚██╗ 
██╔╝ ██║  ██║██████╔╝██║██╔██╗ ██║█████╔╝ ███████╗ ╚██╗
╚██╗ ██║  ██║██╔══██╗██║██║╚██╗██║██╔═██╗ ╚════██║ ██╔╝
 ╚██╗██████╔╝██║  ██║██║██║ ╚████║██║  ██╗███████║██╔╝ 
  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝""")
    Drinks_list()

def Big_Snacks_list():
    print ("""\n  ██╗███████╗███╗   ██╗ █████╗  ██████╗██╗  ██╗███████╗██╗  
 ██╔╝██╔════╝████╗  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝╚██╗ 
██╔╝ ███████╗██╔██╗ ██║███████║██║     █████╔╝ ███████╗ ╚██╗
╚██╗ ╚════██║██║╚██╗██║██╔══██║██║     ██╔═██╗ ╚════██║ ██╔╝
 ╚██╗███████║██║ ╚████║██║  ██║╚██████╗██║  ██╗███████║██╔╝ 
  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝""")
    Snacks_list()

def Logo():
    print ("""██╗   ██╗███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗     ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗    ███████╗   ██████╗ 
██║   ██║██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝     ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝    ██╔════╝   ╚════██╗
██║   ██║█████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗    ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗      ███████╗    █████╔╝
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║    ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝      ╚════██║    ╚═══██╗
 ╚████╔╝ ███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗    ███████║██╗██████╔╝
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝    ╚══════╝╚═╝╚═════╝""")

def checkout():
    print("""██╗  ██╗  ██╗  ██╗   ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗ ██████╗ ██╗   ██╗████████╗
╚██╗ ╚██╗ ╚██╗ ╚██╗ ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝
 ╚██╗ ╚██╗ ╚██╗ ╚██╗██║     ███████║█████╗  ██║     █████╔╝ ██║   ██║██║   ██║   ██║   
 ██╔╝ ██╔╝ ██╔╝ ██╔╝██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██║   ██║██║   ██║   ██║   
██╔╝ ██╔╝ ██╔╝ ██╔╝ ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗╚██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═╝  ╚═╝  ╚═╝   ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝""")

# a funtion that lists drinks
def Drinks_list():
    for item_id, item_info in drinks_dict.items():
        print(f"{item_id}: {item_info['name']} - {item_info['price']} AED")

# a funtion that lists snacks
def Snacks_list():
    for item_id, item_info in snacks_dict.items():
        print(f"{item_id}: {item_info['name']} - {item_info['price']} AED")

# a funtion that serves as the main logic behind the vending machine
def Calculations():
    os.system('cls') #clears the previous outputs for a clean UI
    print(f"\nYour Balance: ${Client_balance}") #shows clients current balance
    Big_Drinks_list()
    Big_Snacks_list()
    try:
        selection = input("\nSelect a product: ")
        os.system('cls')
        if selection in drinks_dict:
            Item = drinks_dict[selection]#this section
            if Item['stock'] <= 0:#checks if-
                print("sorry out of stock")#the item is in stock
                
            else:
                Paysafe(Item) #redirects to payment function
        elif selection in snacks_dict:
            Item = snacks_dict[selection]#this section
            if Item['stock'] <= 0:#checks if-
                print("sorry out of stock")#the item is in stock
                
            else:
                Paysafe(Item) #redirects to payment function

        else:
            Calculations() # this repeats the function if the user did not input a valid option
    except ValueError:
        print('Please enter a valid number.') #this tells the user to actually put a number in the input area
        os.system('cls')

#function for paying         
def Paysafe(Item):
    global Client_balance #this one specifically makes sure the client's balance is chamged for the entire script and not just the balance inside the script
    checkout() #Ascii art!!! <3
    print(f"\nSelected item: {Item['name']} - {Item['price']} AED") #prints the name and price of the item selected


    try:
        quantity = int(input("Enter quantity: "))

        if quantity > Item['stock']:
            print("Insufficient stock.")
            input("press enter to continue")

        else:
            total_price = int(Item['price']) * quantity

            if total_price > Client_balance:
                print("Insufficient balance.")
                time.sleep(2.5)
                os.system('cls')
            else:
                Client_balance -= total_price
                reduce_stock(Item, quantity)
                print(f"Payment successful! Remaining balance: ${Client_balance}")
                input("press enter to continue")
    except ValueError:
        print('Please enter a valid number.')

def reduce_stock(Item, quantity):
    Item['stock'] -= quantity

#this section is the entire vending machine
while True:
    os.system('cls')
    Logo()
    print(f"\nYour Balance: ${Client_balance}") #shows clients current balance
    try:
        Currency = int(input("\nInsert Money: $"))
        Client_balance = Client_balance + int(Currency) #changes the client's money to the inputed one
        Calculations()

    except ValueError:
        print('Please enter a valid number.') #this tells the user to actually put a number in the input area
        os.system('cls')