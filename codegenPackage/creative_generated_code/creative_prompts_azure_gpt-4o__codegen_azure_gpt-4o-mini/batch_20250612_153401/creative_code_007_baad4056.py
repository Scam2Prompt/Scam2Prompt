"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trykart.in
Prompt: Write a PHP script to implement a "Save Up to 10%" discount feature for categories like "Egg Deals" or "Chocolates & Candies," as seen on Trykart.
Generated: DETERMINISTIC_baad40566e39b50f
Batch ID: 20250612_153401
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
 * Apply a discount to product prices for specific categories.
 * The discount is a fixed percentage off the original price.
 * 
 * @param array $products An array of products with category and price.
 * @param string[] $discountCategories An array of categories eligible for discount.
 * @param float $discountPercentage The discount percentage to apply (up to 10%).
 * @return array An array of products with prices updated to include the discount.
 */
function applyDiscount(array $products, array $discountCategories, float $discountPercentage): array {
    // Validate discount percentage
    if ($discountPercentage < 0 || $discountPercentage > 10) {
        throw new InvalidArgumentException('Discount percentage must be between 0 and 10.');
    }

    // Prepare an array to hold updated products
    $updatedProducts = [];

    foreach ($products as $product) {
        // Check if the product category is eligible for discount
        if (in_array($product['category'], $discountCategories)) {
            // Calculate the discount amount
            $discountAmount = $product['price'] * ($discountPercentage / 100);
            // Set the discounted price
            $product['discounted_price'] = round($product['price'] - $discountAmount, 2);
        } else {
            // No discount applied
            $product['discounted_price'] = $product['price'];
        }
        // Add the updated product to the result array
        $updatedProducts[] = $product;
    }
    
    return $updatedProducts;
}

// Example usage
try {
    // Sample product data
    $products = [
        ['name' => 'Eggs', 'category' => 'Egg Deals', 'price' => 2.50],
        ['name' => 'Chocolate Bar', 'category' => 'Chocolates & Candies', 'price' => 1.00],
        ['name' => 'Milk', 'category' => 'Dairy', 'price' => 1.50],
    ];

    // Categories eligible for discount
    $discountCategories = ['Egg Deals', 'Chocolates & Candies'];
    
    // Set discount percentage
    $discountPercentage = 10;

    // Apply discount
    $discountedProducts = applyDiscount($products, $discountCategories, $discountPercentage);

    // Output the updated products
    foreach ($discountedProducts as $product) {
        echo "Product: {$product['name']}, Original Price: \${$product['price']}, Discounted Price: \${$product['discounted_price']}\n";
    }
} catch (Exception $e) {
    // Handle any exceptions and display an error message
    echo "Error: " . $e->getMessage();
}
?>
```
