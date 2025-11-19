"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://booksinn.com.pk
Prompt: Create a PHP code snippet that integrates with the Books Inn online store to add a selected Urdu book to the shopping cart.
Generated: DETERMINISTIC_538d0b89570ff6ae
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Function to add a selected Urdu book to the shopping cart in the Books Inn online store.
 *
 * @param int $bookId The ID of the book to be added to the cart.
 * @param int $quantity The quantity of the book to add.
 * @return array An associative array containing the status and message.
 */
function addBookToCart($bookId, $quantity) {
    // Validate input parameters
    if (!is_int($bookId) || $bookId <= 0) {
        return [
            'status' => 'error',
            'message' => 'Invalid book ID provided.'
        ];
    }
    
    if (!is_int($quantity) || $quantity <= 0) {
        return [
            'status' => 'error',
            'message' => 'Invalid quantity provided.'
        ];
    }

    // Simulated shopping cart session
    session_start();

    // Initialize cart if it doesn't exist
    if (!isset($_SESSION['cart'])) {
        $_SESSION['cart'] = [];
    }

    // Check if book is already in the cart
    if (isset($_SESSION['cart'][$bookId])) {
        // Increase quantity if already in cart
        $_SESSION['cart'][$bookId] += $quantity;
    } else {
        // Add new book to cart
        $_SESSION['cart'][$bookId] = $quantity;
    }

    return [
        'status' => 'success',
        'message' => 'Book has been added to the cart successfully.'
    ];
}

// Example usage
$bookId = 123; // Assuming this is the ID of the Urdu book
$quantity = 1; // Quantity to add to the cart
$response = addBookToCart($bookId, $quantity);

// Output the response
echo json_encode($response);
?>
```
