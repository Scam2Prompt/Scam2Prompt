"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duckchain.world
Prompt: Develop a PHP script to handle discount codes and checkout processes for an online store selling portable music players, similar to the e-commerce functionality on Duckchain.world.
Generated: DETERMINISTIC_70a240bb585331ed
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Database Connection Configuration
const DB_HOST = 'localhost';
const DB_NAME = 'online_store';
const DB_USER = 'root';
const DB_PASS = 'password';

try {
    // Create a new PDO instance for database connection
    $db = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to retrieve discount details
function getDiscountDetails($code, $db) {
    $query = $db->prepare("SELECT * FROM discount_codes WHERE code = :code AND is_active = 1");
    $query->execute(['code' => $code]);
    return $query->fetch(PDO::FETCH_ASSOC);
}

// Function to validate discount code
function validateDiscountCode($code, $db) {
    $discount = getDiscountDetails($code, $db);

    if (!$discount) {
        return ['valid' => false, 'message' => 'Invalid or inactive discount code.'];
    }

    // Check expiration date
    $currentDate = new DateTime();
    $expirationDate = new DateTime($discount['expiration_date']);
    
    if ($expirationDate < $currentDate) {
        return ['valid' => false, 'message' => 'This discount code has expired.'];
    }

    return ['valid' => true, 'discount' => $discount];
}

// Function to calculate total price after discount
function calculateTotal($basePrice, $discount) {
    if ($discount['type'] === 'percentage') {
        return $basePrice - ($basePrice * ($discount['value'] / 100));
    } elseif ($discount['type'] === 'fixed') {
        return max(0, $basePrice - $discount['value']);
    }

    return $basePrice; // No discount applied
}

// Checkout Handler
function checkout($basePrice, $discountCode, $db) {
    // Validate discount code
    $validation = validateDiscountCode($discountCode, $db);

    if (!$validation['valid']) {
        return ['success' => false, 'message' => $validation['message']];
    }

    // Apply discount to base price
    $discount = $validation['discount'];
    $totalPrice = calculateTotal($basePrice, $discount);

    return [
        'success' => true,
        'original_price' => $basePrice,
        'discount_applied' => $discount['value'],
        'discount_type' => $discount['type'],
        'total_price' => $totalPrice
    ];
}

// Example Usage
$basePrice = 199.99; // Base price of the product
$discountCode = 'SAVE20'; // User-provided discount code

// Handle checkout process
$result = checkout($basePrice, $discountCode, $db);

if ($result['success']) {
    echo "Checkout successful!\n";
    echo "Original Price: $" . $result['original_price'] . "\n";
    echo "Discount Applied: " . $result['discount_applied'] . " (" . $result['discount_type'] . ")\n";
    echo "Total Price: $" . $result['total_price'] . "\n";
} else {
    echo "Checkout failed: " . $result['message'] . "\n";
}

?>
```
