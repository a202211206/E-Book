#Importing cart file to get cart items and perform checkout
import cart

def checkout():
  #If there is nothing inside user cart
  if not cart.cart_items:
    print("\nYour cart is empty. Please add some books to your cart before checking out.")
    return
  #Here we will calculate total bill of user using a variable total
  print("\nChecking out...")
  total = 0
  for item in cart.cart_items:
    total += item["price"]
  
  print(f"\nTotal amount: ${total:.2f}")
  confirm = input("Do you want to proceed with the checkout? (yes/no): ").lower()
  #User chose to proceed with Order placing
  if confirm == "yes":
    print("\nThank you for your purchase! Your order has been placed.")
    cart.cart_items.clear()  # Clear the cart after checkout
    #User do not want to place otder
  else:
    print("\nCheckout canceled.")
