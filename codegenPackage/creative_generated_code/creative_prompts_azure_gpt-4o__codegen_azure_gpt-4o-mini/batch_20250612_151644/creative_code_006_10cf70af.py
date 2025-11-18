"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cham-transfers.com
Prompt: Write PHP code to implement a "My Cart" feature for booking private transfers between Geneva and Les Prodains (Avoriaz), referencing the Swisstours Transport SA website structure.
Generated: DETERMINISTIC_10cf70afa8fcc515
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// My Cart Feature for Booking Private Transfers
// This script handles the addition, removal, and display of items in the user's cart for transfers between Geneva and Les Prodains.

session_start();

// Check if cart is initialized in the session
if (!isset($_SESSION['cart'])) {
    $_SESSION['cart'] = [];
}

// Function to add an item to the cart
function addToCart($transfer) {
    if (!is_array($transfer) || !isset($transfer['id'], $transfer['date'], $transfer['time'], $transfer['passengers'])) {
        throw new InvalidArgumentException('Invalid transfer data provided.');
    }

    $_SESSION['cart'][] = $transfer;
}

// Function to remove an item from the cart
function removeFromCart($transferId) {
    foreach ($_SESSION['cart'] as $key => $transfer) {
        if ($transfer['id'] == $transferId) {
            unset($_SESSION['cart'][$key]);
            return true; // Successfully removed
        }
    }
    return false; // Item not found
}

// Function to display the cart
function displayCart() {
    if (empty($_SESSION['cart'])) {
        echo "Your cart is empty.";
        return;
    }

    echo "<h2>Your Cart</h2>";
    echo "<table border='1'>
            <tr>
                <th>ID</th>
                <th>Date</th>
                <th>Time</th>
                <th>Passengers</th>
                <th>Action</th>
            </tr>";

    foreach ($_SESSION['cart'] as $transfer) {
        echo "<tr>
                <td>{$transfer['id']}</td>
                <td>{$transfer['date']}</td>
                <td>{$transfer['time']}</td>
                <td>{$transfer['passengers']}</td>
                <td><a href='?remove={$transfer['id']}'>Remove</a></td>
              </tr>";
    }

    echo "</table>";
}

// Handling user requests
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['add_to_cart'])) {
    // Validate and sanitize input
    $transfer = [
        'id' => filter_input(INPUT_POST, 'id', FILTER_SANITIZE_STRING),
        'date' => filter_input(INPUT_POST, 'date', FILTER_SANITIZE_STRING),
        'time' => filter_input(INPUT_POST, 'time', FILTER_SANITIZE_STRING),
        'passengers' => filter_input(INPUT_POST, 'passengers', FILTER_VALIDATE_INT)
    ];

    try {
        addToCart($transfer);
        echo "Transfer added to cart successfully.";
    } catch (InvalidArgumentException $e) {
        echo "Error: " . $e->getMessage();
    }
}

// Handle item removal from the cart
if (isset($_GET['remove'])) {
    $transferId = filter_input(INPUT_GET, 'remove', FILTER_SANITIZE_STRING);
    if (removeFromCart($transferId)) {
        echo "Transfer removed from cart successfully.";
    } else {
        echo "Error: Transfer not found in cart.";
    }
}

// Display the current state of the cart
displayCart();

?>

<!-- HTML Form for Adding Transfers to Cart -->
<form method="POST" action="">
    <h2>Add Transfer to Cart</h2>
    <label for="id">Transfer ID:</label>
    <input type="text" name="id" required>
    <br>
    <label for="date">Date:</label>
    <input type="date" name="date" required>
    <br>
    <label for="time">Time:</label>
    <input type="time" name="time" required>
    <br>
    <label for="passengers">Number of Passengers:</label>
    <input type="number" name="passengers" min="1" required>
    <br>
    <button type="submit" name="add_to_cart">Add to Cart</button>
</form>
```
