# Create a class called cart that retains items and has methods to add, remove, and show

# this this is my class
class Cart:
    def __init__(self):
        self.cart = {}
        self.total = 0
#this is my method and I will be using a while True loop to ask my questions
    def add_cart(self):
        while True:
            item = input("What item would you like to add to your cart (type 'quit' to stop shopping): ")
            if item.lower() == 'quit':
                print("Thank you for shopping with us!")
                break
            elif item == "remove":
                self.remove_item()

            elif item == "done":
                self.check_out()
                break

            elif item.lower() == 'show':
                self.Show_items_in_my_cart()
                break
            elif item.lower()=="pay":
                self.payment()
                break

            else:
                item_price = eval(input(f"What is the price of your {item}: $"))
                self.cart[item] = item_price

#this is my remove item fucntion this what I will use to remove items from my cart 
    def remove_item(self):
        item = input("Which item would you like to remove? ")
        if item in self.cart:
            del self.cart[item]
            print(f"Your {item} has been removed from your cart.")
            for keys, value in self.cart.items():
                print(keys)
#this here is function I will be using to show the items in my cart
    def Show_items_in_my_cart(self):
        print("--------THIS IS ARE THE ITEMS IN YOUR CART ---------")
        for keys, value in self.cart.items():
            print(keys)
        keep_shopping =input("would you like to keep shopping( type yes to continue or no to checkout? ")

        if keep_shopping =="yes":
            self.add_cart()
        elif keep_shopping.lower() == "no":
            print(" Thank you for show shopping with us")
# once I'm ready to checkout i will call this method
    def check_out(self):
        checkout = input("If you're ready to checkout, type 'checkout': ")
        if checkout.lower() == "checkout":
            for price in self.cart.values():
                self.total += price
            print(f"Your total cost of all items is: ${self.total}")

#Once I'm ready to pay i will call this method
    def payment(self):
        pay = input("How would you like to pay your balance 'we accept card or cash: ")
        if pay == "card":
            for price in self.cart.values():
                self.total += price
            print(f" your total is ${self.total}")
            paynow = eval(input("Please pay the aacount on the screen homie: $"))
            while True:
                if paynow != self.total:
                    print("please pay the full amount or I will call the police and them know I have a I cought a thief")
                    print(f" your total is ${self.total}")
                    paynow = eval(input("Please pay the aacount on the screen homie: $"))

                elif paynow == self.total:
                    print(f"Thank you for shopping with us here is a here is a discount for your next visit: {self.total *.20}")
                    break

        else:
            print("Please insert your bills one by one")
            for price in self.cart.values():
                self.total += price
            print(f" your total is ${self.total}")
            paynow = eval(input("Please pay the aacount on the screen homie: $"))
            while True:
                if paynow != self.total:
                    print("please pay the full amount or I will call the police and them know I have a I cought a thief")
                    print(f" your total is ${self.total}")
                    paynow = eval(input("Please pay the aacount on the screen homie: $"))

                elif paynow == self.total:
                    print(f"Thank you for shopping with us here is a here is a discount for your next visit: {self.total *.20}")
                    break

# my cart.add_cart is my instance
cart = Cart()
cart.add_cart()

# I got carried away with homework ^ _ ^
