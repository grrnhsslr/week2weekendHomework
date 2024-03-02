# Develop a versatile shopping cart program with the following functionalities:
# Upon starting the program, initialize an empty list or dictionary to represent the shopping cart.
# Present a user-friendly menu that includes the following options:
# Allow users to add items to the shopping cart. For each item, prompt the user to input a name, quantity, and price.
# Store these details and add it to the shopping cart.
# Provide the ability to remove items from the shopping cart.
# Prompt the user to input the name of the item they wish to remove.
# Ensure to handle cases where the item is not found in the cart.
# Display the current contents of the shopping cart.
# Include the name, quantity, and price of each item, as well as a running total of the cost.
# Allow the user to exit the program.
# Upon quitting, print a summary of all items in the cart, including their details and the total cost.
# Implement a loop that continuously prompts the user for their choice until they decide to quit.
# Include appropriate error handling to deal with scenarios such as invalid input when adding or removing items.
# Ensure that the program provides a clear and user-friendly experience.
# Include informative messages and prompts to guide the user through each step.
# After the user quits, display a friendly closing message
# along with the final list of items in the cart and the total cost.

items = {
    "apple": {
        "price": 1.49
    },
    "banana": {
        "price": .89
    },
    "eggs": {
        "price": 3.50
    }
}

cart = {}

def shopping_cart():
    item_name = input('To add an item please enter a name ')
    if item_name not in items.keys():
        print("item not available... returning")
    else:
        print(f'The price is {items.get(item_name)}')
        if item_name in cart:
            answer = input(f'''{item_name} is already inside of your cart would you like to add more? 
    y for yes n for no ''')
            if answer == 'y':
                added_item = input('how many would you like to add? ')
                cart[item_name]['quantity'] = int(cart[item_name]['quantity']) + int(added_item)

        else:
            quantity = input("how many would you like? ")
            cart[item_name] = items[item_name]
            cart[item_name]['quantity'] = quantity

def checkout():
    total = 0.0
    for item in cart:
        total = total + cart[item]['price'] * int(cart[item]['quantity'])
    print('''.
.
.
. Thanks for shopping! Here is your receipt: ''', '$', total, 'for', cart, '''.
.
.''')


def main():
    booler = True
    while booler is True:
        prompt = input('''Type add to add to cart, type show cart to show your cart. Type checkout to checkout, 
type remove to remove items from your cart, type show to see available items or type quit to quit ''')
        if prompt == 'remove':
            print(cart)
            delete_item = input("which items would you like to remove? ")
            if delete_item in cart:
                deleted_quantity = input(f'How many of {cart[delete_item]} would you like to remove? ')
                items[delete_item]['quantity'] = int(items[delete_item]['quantity']) - int(deleted_quantity)
                print(f'deleted {cart[delete_item]["quantity"]} {cart[delete_item]}')
            else:
                print('That item is not in your cart... Returning')

        if prompt == 'add':
            shopping_cart()

        elif prompt == 'show':
            print(items)

        elif prompt == 'show cart':
            print(cart)

        elif prompt == 'checkout':
            checkout()
            booler = False

        elif prompt == 'quit':
            print('Thank you for shopping here')
            booler = False

main()
