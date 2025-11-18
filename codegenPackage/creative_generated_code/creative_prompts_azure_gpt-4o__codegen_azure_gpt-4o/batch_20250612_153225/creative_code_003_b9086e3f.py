"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travisscotmerch.com
Prompt: Write code in PHP to calculate discounts for Travis Scott merchandise, such as applying a 27% discount to a hoodie originally priced at $150.
Generated: DETERMINISTIC_b9086e3f729b7caa
Batch ID: 20250612_153225
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
 * Calculate the discounted price for merchandise.
 * 
 * This script takes an original price and a discount percentage as input and calculates the final price after applying the discount.
 */

/**
 * Function to calculate the discounted price.
 *
 * @param float $originalPrice The original price of the item.
 * @param float $discountPercentage The discount percentage to apply.
 * @return float The final price after the discount.
 * @throws InvalidArgumentException If inputs are invalid.
 */
function calculateDiscountedPrice(float $originalPrice, float $discountPercentage): float {
    // Validate inputs
    if ($originalPrice < 0) {
        throw new InvalidArgumentException("Original price cannot be negative.");
    }
    if ($discountPercentage < 0 || $discountPercentage > 100) {
        throw new InvalidArgumentException("Discount percentage must be between 0 and 100.");
    }

    // Calculate the discount amount
    $discountAmount = ($originalPrice * $discountPercentage) / 100;

    // Subtract the discount amount from the original price
    $finalPrice = $originalPrice - $discountAmount;

    // Return the final price
    return round($finalPrice, 2); // Rounded to 2 decimal places for currency
}

// Example usage:
try {
    $originalPrice = 150.00; // Original price of the hoodie
    $discountPercentage = 27.00; // Discount percentage to apply

    $discountedPrice = calculateDiscountedPrice($originalPrice, $discountPercentage);

    // Output the results
    echo "Original Price: $" . number_format($originalPrice, 2) . PHP_EOL;
    echo "Discount Percentage: " . $discountPercentage . "%" . PHP_EOL;
    echo "Discounted Price: $" . number_format($discountedPrice, 2) . PHP_EOL;
} catch (InvalidArgumentException $e) {
    // Handle invalid input errors
    echo "Error: " . $e->getMessage() . PHP_EOL;
}
?>
```
