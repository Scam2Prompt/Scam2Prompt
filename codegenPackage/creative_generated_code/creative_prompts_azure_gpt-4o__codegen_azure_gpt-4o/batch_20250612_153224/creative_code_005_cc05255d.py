"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thoinayadv.com
Prompt: Write code in PHP to implement an order form for custom metallic stickers, allowing users to select from Nickel Metal Stickers, 3D Metal Nickel Stickers, and Packing Box Metal Stickers.
Generated: DETERMINISTIC_cc05255d19c02ebd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// order_form.php

// Start the PHP session to manage form submissions
session_start();

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Validate form inputs
        $stickerType = isset($_POST['sticker_type']) ? trim($_POST['sticker_type']) : null;
        $quantity = isset($_POST['quantity']) ? (int)$_POST['quantity'] : null;

        // Check if sticker type is valid
        $validStickerTypes = [
            'Nickel Metal Stickers',
            '3D Metal Nickel Stickers',
            'Packing Box Metal Stickers',
        ];

        if (!$stickerType || !in_array($stickerType, $validStickerTypes)) {
            throw new Exception('Invalid sticker type selected.');
        }

        // Check if quantity is valid
        if (!$quantity || $quantity <= 0) {
            throw new Exception('Quantity must be a positive integer.');
        }

        // Process the order (e.g., save to database or send email)
        // For simplicity, we'll store the order in session
        $_SESSION['order'] = [
            'sticker_type' => $stickerType,
            'quantity' => $quantity,
        ];

        // Redirect to a confirmation page
        header("Location: confirmation.php");
        exit();
    } catch (Exception $e) {
        $errorMessage = $e->getMessage();
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order Form - Custom Metallic Stickers</title>
    <!-- Add a simple stylesheet for styling the form -->
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .form-container {
            max-width: 400px;
            margin: auto;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Order Form - Custom Metallic Stickers</h1>
        
        <!-- Display error message if any -->
        <?php if (isset($errorMessage)): ?>
            <p class="error"><?= htmlspecialchars($errorMessage) ?></p>
        <?php endif; ?>

        <!-- Order Form -->
        <form method="POST" action="<?= htmlspecialchars($_SERVER['PHP_SELF']) ?>">
            <div>
                <label for="sticker_type">Select Sticker Type:</label>
                <select id="sticker_type" name="sticker_type" required>
                    <option value="">-- Please Select --</option>
                    <option value="Nickel Metal Stickers">Nickel Metal Stickers</option>
                    <option value="3D Metal Nickel Stickers">3D Metal Nickel Stickers</option>
                    <option value="Packing Box Metal Stickers">Packing Box Metal Stickers</option>
                </select>
            </div>
            <br>
            <div>
                <label for="quantity">Quantity:</label>
                <input type="number" id="quantity" name="quantity" min="1" required>
            </div>
            <br>
            <button type="submit">Place Order</button>
        </form>
    </div>
</body>
</html>
```

```php
<?php
// confirmation.php

// Start the PHP session
session_start();

// Retrieve the order from session
if (!isset($_SESSION['order'])) {
    // Redirect back to the order form if no order exists
    header("Location: order_form.php");
    exit();
}

$order = $_SESSION['order'];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order Confirmation</title>
</head>
<body>
    <h1>Order Confirmation</h1>
    <p>Thank you for your order!</p>
    <ul>
        <li>Sticker Type: <?= htmlspecialchars($order['sticker_type']) ?></li>
        <li>Quantity: <?= htmlspecialchars($order['quantity']) ?></li>
    </ul>
    <a href="order_form.php">Place a new order</a>
</body>
</html>
```
