"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allorashopping.com
Prompt: Write a PHP script to handle user input for numeric size values (e.g., XXS, XS, 2XL) and update the product search results accordingly.
Generated: DETERMINISTIC_abcd052dca56e388
Batch ID: 20250612_155115
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
 * Script to handle user input for size values and update product search results.
 *
 * This script accepts size inputs (e.g., XXS, XS, 2XL), validates them,
 * and filters product search results accordingly.
 */

// Define valid size options
$validSizes = [
    'XXS', 'XS', 'S', 'M', 'L', 'XL', '2XL', '3XL', '4XL'
];

try {
    // Function to sanitize user input
    function sanitizeInput($input) {
        return htmlspecialchars(trim($input));
    }

    // Check if size has been provided via GET or POST
    $size = $_GET['size'] ?? $_POST['size'] ?? null;

    // Sanitize input
    $size = sanitizeInput($size);

    // Validate size
    if ($size === null || $size === '') {
        throw new Exception('Size input is required.');
    }

    if (!in_array($size, $validSizes)) {
        throw new Exception('Invalid size provided.');
    }

    // Mock product data for demonstration purposes
    $products = [
        ['id' => 1, 'name' => 'T-Shirt', 'sizes' => ['S', 'M', 'L']],
        ['id' => 2, 'name' => 'Sweater', 'sizes' => ['M', 'L', 'XL']],
        ['id' => 3, 'name' => 'Jacket', 'sizes' => ['L', 'XL', '2XL']],
        ['id' => 4, 'name' => 'Jeans', 'sizes' => ['XXS', 'XS', 'S', 'M']],
    ];

    // Filter products based on the user-provided size
    $filteredProducts = array_filter($products, function ($product) use ($size) {
        return in_array($size, $product['sizes']);
    });

    // Display filtered results
    if (!empty($filteredProducts)) {
        echo "Products available in size '{$size}':<br>";
        foreach ($filteredProducts as $product) {
            echo "ID: {$product['id']}, Name: {$product['name']}<br>";
        }
    } else {
        echo "No products found for size '{$size}'.";
    }
} catch (Exception $e) {
    // Handle exceptions and display error messages
    echo "Error: " . $e->getMessage();
}
?>
```
