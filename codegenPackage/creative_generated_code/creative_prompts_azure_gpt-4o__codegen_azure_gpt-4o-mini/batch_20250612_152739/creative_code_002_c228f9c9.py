"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activesport.cz
Prompt: Create a function in PHP to calculate discounted prices for products, referencing the discount logic displayed on ActiveSport.cz (e.g., "-560 Kč" for a jacket).
Generated: DETERMINISTIC_c228f9c9e6c004cb
Batch ID: 20250612_152739
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
 * Class DiscountCalculator
 * A class to handle discount calculations for products.
 */
class DiscountCalculator
{
    /**
     * Calculate the discounted price based on the original price and discount amount.
     *
     * @param float $originalPrice The original price of the product.
     * @param float $discountAmount The amount to be discounted from the original price.
     * @return float The final price after applying the discount.
     * @throws InvalidArgumentException If the original price or discount amount is negative.
     */
    public function calculateDiscountedPrice(float $originalPrice, float $discountAmount): float
    {
        // Validate inputs
        if ($originalPrice < 0) {
            throw new InvalidArgumentException('Original price cannot be negative.');
        }
        if ($discountAmount < 0) {
            throw new InvalidArgumentException('Discount amount cannot be negative.');
        }

        // Calculate the discounted price
        $finalPrice = $originalPrice - $discountAmount;

        // Ensure the final price is not negative
        if ($finalPrice < 0) {
            return 0.0; // Return zero if the discount exceeds the original price
        }

        return $finalPrice;
    }
}

// Example usage
try {
    $calculator = new DiscountCalculator();

    // Original price of the jacket
    $originalPrice = 1000.00; // Example price in currency
    // Discount amount
    $discountAmount = 560.00; // Example discount amount

    // Calculate the discounted price
    $discountedPrice = $calculator->calculateDiscountedPrice($originalPrice, $discountAmount);

    // Output the discounted price
    echo "The discounted price is: " . number_format($discountedPrice, 2, ',', '') . " Kč\n";
} catch (InvalidArgumentException $e) {
    // Handle any invalid argument exceptions
    echo 'Error: ' . $e->getMessage() . "\n";
}

?>
```
