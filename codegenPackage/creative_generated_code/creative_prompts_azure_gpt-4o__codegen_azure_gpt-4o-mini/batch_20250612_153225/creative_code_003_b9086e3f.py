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
 * Class DiscountCalculator
 * This class handles the calculation of discounts for merchandise.
 */
class DiscountCalculator {
    
    /**
     * Calculates the discounted price based on the original price and discount percentage.
     *
     * @param float $originalPrice The original price of the merchandise.
     * @param float $discountPercentage The discount percentage to be applied.
     * @return float The price after applying the discount.
     * @throws InvalidArgumentException If the original price or discount percentage is negative.
     */
    public function calculateDiscountedPrice(float $originalPrice, float $discountPercentage): float {
        // Validate input parameters
        if ($originalPrice < 0) {
            throw new InvalidArgumentException('Original price cannot be negative.');
        }
        if ($discountPercentage < 0 || $discountPercentage > 100) {
            throw new InvalidArgumentException('Discount percentage must be between 0 and 100.');
        }

        // Calculate the discount amount
        $discountAmount = $originalPrice * ($discountPercentage / 100);
        
        // Calculate the final price after discount
        $discountedPrice = $originalPrice - $discountAmount;
        
        // Return the discounted price
        return round($discountedPrice, 2); // Round to 2 decimal places for currency format
    }
}

// Example usage
try {
    $originalPrice = 150.00; // Original price of the hoodie
    $discountPercentage = 27; // Discount percentage

    // Create an instance of DiscountCalculator
    $calculator = new DiscountCalculator();

    // Calculate the discounted price
    $finalPrice = $calculator->calculateDiscountedPrice($originalPrice, $discountPercentage);

    // Display the result
    echo "The final price after a {$discountPercentage}% discount is: \$$finalPrice\n";
} catch (Exception $e) {
    // Handle any exceptions that occurred during calculation
    echo 'Error: ' . $e->getMessage() . "\n";
}
?>
```
