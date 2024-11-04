# In-memory cart storage using array
cart_items = []

#This function is responsible of storing a book into cart_items array
def add_to_cart(book):
    cart_items.append(book)

#This function is responsible for showing cart of user to show all items added to cart by user
def view_cart():
    #If there is nothing in cart
    if not cart_items:
        print("\nYour cart is empty.")
        return
    #If there exists some items in cart
    print("\nYour Cart:")
    total = 0
    for item in cart_items:
        print(f"{item['name']} by {item['author']} - ${item['price']}")
        total += item["price"]
    
    print(f"\nTotal: ${total:.2f}")
