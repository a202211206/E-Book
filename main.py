#Importing all classes used fot EBokk Operations
import books
import cart
import checkout

#This function is used for displaying main menu to user as well as asking user to chose any menu
# Based on user choice we allow user to perform different operations
def show_menu():
    while True:
        print("\nWelcome to E-Shopper, Please Select an Option")
        print("1) Buy a Book")
        print("2) View Cart")
        print("3) Checkout")
        print("4) Exit")
        
        #Taking User Input as choice from user
        choice = input("Enter your choice: ")
        
        #User want to buy a book
        if choice == "1":
            books.buy_a_book()
        #User want to view his shopping cart
        elif choice == "2":
            cart.view_cart()
        #User want to checkout and place order based on items in his/her cart
        elif choice == "3":
            checkout.checkout()
        #User want to Exit and logout
        elif choice == "4":
            print("Thank you for visiting E-Shopper. Goodbye!")
            break
        #If user do not enter a valid choice
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    show_menu()
