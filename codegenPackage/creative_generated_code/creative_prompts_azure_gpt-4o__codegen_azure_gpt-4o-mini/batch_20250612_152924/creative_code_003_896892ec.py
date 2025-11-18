"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Create a function in PHP to calculate and display discounts for products, similar to the "-5% Limited" and "-10% Limited" labels on Multan Designs.
Generated: DETERMINISTIC_896892ec2a64195a
Batch ID: 20250612_152924
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
 * 
 * A class to handle discount calculations for products.
 */
class DiscountCalculator {
    
    /**
     * Calculate the discounted price based on the original price and discount percentage.
     *
     * @param float $originalPrice The original price of the product.
     * @param float $discountPercentage The discount percentage to apply (e.g., 5 for 5%).
     * @return float|null The discounted price or null if the input is invalid.
     * @throws InvalidArgumentException If the original price or discount percentage is negative.
     */
    public function calculateDiscountedPrice(float $originalPrice, float $discountPercentage): ?float {
        // Validate inputs
        if ($originalPrice < 0 || $discountPercentage < 0) {
            throw new InvalidArgumentException('Original price and discount percentage must be non-negative.');
        }
        
        // Calculate the discount
        $discountAmount = ($originalPrice * $discountPercentage) / 100;
        $discountedPrice = $originalPrice - $discountAmount;

        return round($discountedPrice, 2); // Round to 2 decimal places
    }

    /**
     * Generate the discount label.
     *
     * @param float $discountPercentage The discount percentage to display.
     * @return string The formatted discount label.
     */
    public function generateDiscountLabel(float $discountPercentage): string {
        return sprintf("-%s%% Limited", $discountPercentage);
    }
}

// Example usage
try {
    // Create an instance of DiscountCalculator
    $discountCalculator = new DiscountCalculator();

    // Define the original price and discount percentage
    $originalPrice = 100.00;
    $discountPercentage = 10;

    // Calculate discounted price
    $discountedPrice = $discountCalculator->calculateDiscountedPrice($originalPrice, $discountPercentage);
    
    // Generate discount label
    $discountLabel = $discountCalculator->generateDiscountLabel($discountPercentage);

    // Display the results
    echo "Original Price: $$originalPrice\n";
    echo "Discounted Price: $$discountedPrice\n";
    echo "Discount Label: $discountLabel\n";
} catch (InvalidArgumentException $e) {
    // Handle any invalid arguments
    echo "Error: " . $e->getMessage() . "\n";
} catch (Exception $e) {
    // General exception handling
    echo "An unexpected error occurred: " . $e->getMessage() . "\n";
}
?>
```
