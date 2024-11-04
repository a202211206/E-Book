import unittest
from unittest.mock import patch, MagicMock
import json
import main
import books
import cart
import checkout

class TestEBookstore(unittest.TestCase):
    """Test case class for the E-Bookstore application."""

    @patch('builtins.print')
    def test_show_menu_display(self, mock_print):
        """Test that the menu displays the correct options."""
        main.show_menu()
        # Verify that the menu prompts the user correctly.
        mock_print.assert_any_call("Welcome to E-Shopper, Please Select an Option")
        mock_print.assert_any_call("1) Buy a Book")
        mock_print.assert_any_call("2) View Cart")
        mock_print.assert_any_call("3) Checkout")
        mock_print.assert_any_call("4) Exit")

    @patch('builtins.input', side_effect=['1', '1', 'back'])
    @patch('books.buy_a_book')
    def test_buy_a_book(self, mock_buy_a_book, mock_input):
        """Test that selecting to buy a book calls the correct function."""
        main.show_menu()
        # Check if the buy_a_book function is called once.
        mock_buy_a_book.assert_called_once()

    @patch('builtins.input', side_effect=['2'])
    @patch('cart.view_cart')
    def test_view_cart(self, mock_view_cart, mock_input):
        """Test that selecting to view the cart calls the correct function."""
        main.show_menu()
        # Check if the view_cart function is called once.
        mock_view_cart.assert_called_once()

    @patch('builtins.input', side_effect=['3', 'yes'])
    @patch('checkout.checkout')
    def test_checkout(self, mock_checkout, mock_input):
        """Test that selecting to checkout calls the correct function."""
        main.show_menu()
        # Check if the checkout function is called once.
        mock_checkout.assert_called_once()

    @patch('builtins.input', side_effect=['4'])
    @patch('builtins.print')
    def test_exit(self, mock_print, mock_input):
        """Test that selecting to exit prints the farewell message."""
        main.show_menu()
        # Verify the farewell message is printed.
        mock_print.assert_called_with("Thank you for visiting E-Shopper. Goodbye!")

    @patch('builtins.input', side_effect=['5'])
    @patch('builtins.print')
    def test_invalid_input(self, mock_print, mock_input):
        """Test that selecting an invalid option prints an error message."""
        main.show_menu()
        # Verify the error message for invalid input is printed.
        mock_print.assert_called_with("Invalid choice. Please try again.")

    @patch('books.load_books', return_value=[
        {"id": 1, "name": "Test Book", "price": 10.0},
    ])
    @patch('cart.add_to_cart')
    @patch('builtins.input', side_effect=['1', '1', 'back'])
    def test_buy_a_book_valid_id(self, mock_input, mock_add_to_cart, mock_load_books):
        """Test buying a book with a valid ID successfully adds it to the cart."""
        books.buy_a_book()
        # Verify that the correct book is added to the cart.
        mock_add_to_cart.assert_called_once_with({"id": 1, "name": "Test Book", "price": 10.0})

    @patch('books.load_books', return_value=[
        {"id": 1, "name": "Test Book", "price": 10.0},
    ])
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1', 'invalid_id'])
    def test_buy_a_book_invalid_id(self, mock_input, mock_print, mock_load_books):
        """Test that an invalid book ID prompts an error message."""
        books.buy_a_book()
        # Verify that an error message is displayed for an invalid ID.
        mock_print.assert_called_with("Invalid book ID. Please try again.")

    @patch('cart.cart_items', new_callable=list)
    @patch('builtins.print')
    def test_view_cart_empty(self, mock_print, mock_cart_items):
        """Test viewing the cart when it is empty."""
        cart.view_cart()
        # Verify the message indicating the cart is empty is printed.
        mock_print.assert_called_with("\nYour cart is empty. Please add some books to your cart before checking out.")

    @patch('cart.cart_items', new_callable=list)
    @patch('builtins.print')
    def test_view_cart_non_empty(self, mock_print, mock_cart_items):
        """Test viewing the cart when it contains items."""
        # Simulate adding a book to the cart.
        mock_cart_items.append({"name": "Test Book", "price": 10.0})
        cart.view_cart()
        # Verify the book details are printed correctly.
        mock_print.assert_called_with("Test Book - $10.00")

    @patch('cart.cart_items', new_callable=list)
    @patch('builtins.input', side_effect=['yes'])
    @patch('builtins.print')
    def test_checkout_proceed_with_order(self, mock_print, mock_input, mock_cart_items):
        """Test proceeding with checkout when the cart has items."""
        # Simulate a non-empty cart.
        mock_cart_items.extend([{"name": "Test Book", "price": 10.0}])
        checkout.checkout()
        # Verify the total amount and thank you message are printed.
        mock_print.assert_any_call("Total amount: $10.00")
        mock_print.assert_any_call("\nThank you for your purchase! Your order has been placed.")
        # Ensure the cart is emptied after checkout.
        self.assertEqual(mock_cart_items, [])

    @patch('cart.cart_items', new_callable=list)
    @patch('builtins.input', side_effect=['no'])
    @patch('builtins.print')
    def test_checkout_cancel_order(self, mock_print, mock_input, mock_cart_items):
        """Test canceling the checkout process when prompted."""
        # Simulate a non-empty cart.
        mock_cart_items.extend([{"name": "Test Book", "price": 10.0}])
        checkout.checkout()
        # Verify the total amount and cancellation message are printed.
        mock_print.assert_any_call("Total amount: $10.00")
        mock_print.assert_any_call("\nCheckout canceled.")
        # Ensure the cart remains unchanged after cancellation.
        self.assertEqual(mock_cart_items, [{"name": "Test Book", "price": 10.0}])

    @patch('cart.cart_items', new_callable=list)
    @patch('builtins.print')
    def test_checkout_empty_cart(self, mock_print, mock_cart_items):
        """Test the checkout process when the cart is empty."""
        checkout.checkout()
        # Verify the message indicating the cart is empty is printed.
        mock_print.assert_called_with("\nYour cart is empty. Please add some books to your cart before checking out.")

if __name__ == '__main__':
    unittest.main()
