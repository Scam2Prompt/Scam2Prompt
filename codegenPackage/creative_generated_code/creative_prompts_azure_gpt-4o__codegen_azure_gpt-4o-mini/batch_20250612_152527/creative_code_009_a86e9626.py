"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.depanten-gel.click
Prompt: Write PHP code to handle form submissions for ordering a product like Depanten, including validation for user inputs like name, address, and payment details.
Generated: DETERMINISTIC_a86e962684425a8a
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start a session to manage form submission state
session_start();

/**
 * Function to sanitize user input
 * @param string $data The input data
 * @return string Sanitized input
 */
function sanitize_input($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

/**
 * Function to validate the order data
 * @param array $data The order data
 * @return array An array containing validation results
 */
function validate_order($data) {
    $errors = [];

    // Validate name
    if (empty($data['name'])) {
        $errors['name'] = 'Name is required.';
    }

    // Validate address
    if (empty($data['address'])) {
        $errors['address'] = 'Address is required.';
    }

    // Validate payment details
    if (empty($data['payment_method'])) {
        $errors['payment_method'] = 'Payment method is required.';
    }

    return $errors;
}

// Initialize variables
$order_data = [];
$errors = [];

// Process form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize user inputs
    $order_data['name'] = sanitize_input($_POST['name']);
    $order_data['address'] = sanitize_input($_POST['address']);
    $order_data['payment_method'] = sanitize_input($_POST['payment_method']);

    // Validate order data
    $errors = validate_order($order_data);

    // Check if there are no validation errors
    if (empty($errors)) {
        // Here you would typically save the order to the database
        // For demonstration, we'll just simulate success
        $_SESSION['success_message'] = 'Order placed successfully!';
        // Redirect to a confirmation page
        header('Location: confirmation.php');
        exit;
    } else {
        // Store errors in session for displaying them later
        $_SESSION['errors'] = $errors;
    }
}

// Display previous input and any errors if the form is reloaded
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order Form</title>
</head>
<body>
    <h1>Order Product</h1>

    <?php
    // Display error messages if available
    if (isset($_SESSION['errors'])) {
        echo '<div style="color: red;">';
        foreach ($_SESSION['errors'] as $error) {
            echo "<p>$error</p>";
        }
        echo '</div>';
        // Clear errors after displaying
        unset($_SESSION['errors']);
    }

    // Display success message if available
    if (isset($_SESSION['success_message'])) {
        echo '<div style="color: green;">' . $_SESSION['success_message'] . '</div>';
        // Clear success message after displaying
        unset($_SESSION['success_message']);
    }
    ?>

    <form action="" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="<?php echo isset($order_data['name']) ? $order_data['name'] : ''; ?>" required><br>

        <label for="address">Address:</label>
        <input type="text" id="address" name="address" value="<?php echo isset($order_data['address']) ? $order_data['address'] : ''; ?>" required><br>

        <label for="payment_method">Payment Method:</label>
        <select id="payment_method" name="payment_method" required>
            <option value="">Select...</option>
            <option value="credit_card" <?php echo (isset($order_data['payment_method']) && $order_data['payment_method'] === 'credit_card') ? 'selected' : ''; ?>>Credit Card</option>
            <option value="paypal" <?php echo (isset($order_data['payment_method']) && $order_data['payment_method'] === 'paypal') ? 'selected' : ''; ?>>PayPal</option>
        </select><br>

        <input type="submit" value="Place Order">
    </form>
</body>
</html>
```
