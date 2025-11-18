"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aplanet.in
Prompt: Write a function in PHP to calculate the discount percentage for Apple products listed on the APlanet website based on their original and sale prices.
Generated: DETERMINISTIC_670df6bbc83aea9b
Batch ID: 20250612_154219
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
 * Calculate the discount percentage for Apple products.
 *
 * This function takes the original price and the sale price of a product,
 * and returns the discount percentage. If the original price is zero or
 * less, it throws an InvalidArgumentException to prevent division by zero.
 *
 * @param float $originalPrice The original price of the product.
 * @param float $salePrice The sale price of the product.
 * @return float The discount percentage expressed as a float.
 * @throws InvalidArgumentException If the original price is less than or equal to zero.
 */
function calculateDiscountPercentage(float $originalPrice, float $salePrice): float {
    // Validate the original price
    if ($originalPrice <= 0) {
        throw new InvalidArgumentException('Original price must be greater than zero.');
    }

    // Calculate the discount amount
    $discountAmount = $originalPrice - $salePrice;

    // Calculate the discount percentage
    $discountPercentage = ($discountAmount / $originalPrice) * 100;

    // Return the discount percentage, rounded to two decimal places
    return round($discountPercentage, 2);
}

// Example usage
try {
    $originalPrice = 1500.00; // Original price in dollars
    $salePrice = 1200.00;     // Sale price in dollars

    $discount = calculateDiscountPercentage($originalPrice, $salePrice);
    echo "The discount percentage is: {$discount}%\n";
} catch (InvalidArgumentException $e) {
    echo 'Error: ' . $e->getMessage() . "\n";
}
?>
```
