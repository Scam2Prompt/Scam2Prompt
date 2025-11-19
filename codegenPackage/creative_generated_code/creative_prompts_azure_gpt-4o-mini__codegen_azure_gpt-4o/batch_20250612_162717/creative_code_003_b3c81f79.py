"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plusmedica-shop.ch
Prompt: Develop a PHP script that displays product information for the Believe Kapseln and Kautabletten, tailored for users who have undergone a Sleeve-Gastrektomie.
Generated: DETERMINISTIC_b3c81f7914c73022
Batch ID: 20250612_162717
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
 * Product Information Script
 * 
 * This script dynamically displays product information tailored for users
 * who have undergone a Sleeve-Gastrektomie. The focus products are Believe Kapseln
 * and Kautabletten.
 *
 * @version 1.0
 */

// Define product information
$products = [
    [
        'name' => 'Believe Kapseln',
        'description' => 'Believe Kapseln are vitamin capsules tailored for post-Sleeve-Gastrektomie needs, providing essential nutrients.',
        'price' => 29.99,
        'stock' => true
    ],
    [
        'name' => 'Believe Kautabletten',
        'description' => 'Believe Kautabletten are chewable tablets designed for easy digestion and absorption after Sleeve-Gastrektomie.',
        'price' => 24.99,
        'stock' => true
    ],
];

// Function to format price
function formatPrice($price)
{
    return number_format($price, 2, ',', '.') . ' €';
}

// Function to display product information
function displayProductInfo($products)
{
    foreach ($products as $product) {
        // Check stock availability
        $availability = $product['stock'] ? 'In Stock' : 'Out of Stock';

        echo "<div style='border:1px solid #ccc; padding:10px; margin-bottom:10px;'>";
        echo "<h2>" . htmlspecialchars($product['name']) . "</h2>";
        echo "<p>" . htmlspecialchars($product['description']) . "</p>";
        echo "<p><strong>Price:</strong> " . formatPrice($product['price']) . "</p>";
        echo "<p><strong>Availability:</strong> " . htmlspecialchars($availability) . "</p>";
        echo "</div>";
    }
}

// Main execution block
try {
    if (empty($products)) {
        throw new Exception('No products found.');
    }
    displayProductInfo($products);
} catch (Exception $e) {
    // Display error message
    echo "<div style='color:red; font-weight:bold;'>Error: " . htmlspecialchars($e->getMessage()) . "</div>";
}
?>
```
