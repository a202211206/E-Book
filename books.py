#Importing JSon Library to read books from Array of books
import json
import cart

# Load books from the JSON file
def load_books():
    with open("books.json", "r") as file:
        return json.load(file)

#this function will be called when user wants to add a book to cart by viewing book
def buy_a_book():
    books = load_books()
    
    print("\nAvailable Books:")
    for book in books:
        print(f"{book['id']}. {book['name']} by {book['author']} - ${book['price']}")

    book_id = input("Enter the ID of the book you want to buy (or type 'back' to return to menu): ")
    
    if book_id.lower() == 'back':
        return
    
    # Find the selected book
    selected_book = next((book for book in books if str(book["id"]) == book_id), None)
    
    if selected_book:
        cart.add_to_cart(selected_book)
        print(f"\n'{selected_book['name']}' has been added to your cart.")
    else:
        print("Invalid book ID. Please try again.")
