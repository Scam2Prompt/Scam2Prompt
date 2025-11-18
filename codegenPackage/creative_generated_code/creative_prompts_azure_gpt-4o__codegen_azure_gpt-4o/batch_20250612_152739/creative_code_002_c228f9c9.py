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
 * Calculate discounted price for a product.
 *
 * @param float $originalPrice The original price of the product.
 * @param float $discountValue The discount value (can be an absolute amount like "-560 Kč" or percentage like "20%").
 * 
 * @return float The final price after applying the discount.
 * @throws InvalidArgumentException If input values are invalid or malformed.
 */
function calculateDiscountedPrice(float $originalPrice, string $discountValue): float
{
    // Validate original price
    if ($originalPrice <= 0) {
        throw new InvalidArgumentException("Original price must be a positive number.");
    }

    // Normalize and validate discount value
    $discountValue = trim($discountValue);

    // Handle absolute discount (e.g., "-560 Kč")
    if (preg_match('/^-?\d+(\.\d+)? Kč$/', $discountValue)) {
        // Remove the currency symbol and convert to float
        $discountAmount = (float)str_replace(['Kč', ' '], '', $discountValue);

        // Calculate final price after applying the absolute discount
        $finalPrice = $originalPrice + $discountAmount; // Adding because discount is negative (e.g., "-560")
        return max($finalPrice, 0); // Ensure price is not negative
    }

    // Handle percentage discount (e.g., "20%")
    if (preg_match('/^\d+(\.\d+)?%$/', $discountValue)) {
        // Remove the percentage symbol and convert to float
        $discountPercent = (float)str_replace('%', '', $discountValue);

        if ($discountPercent < 0 || $discountPercent > 100) {
            throw new InvalidArgumentException("Percentage discount must be between 0% and 100%.");
        }

        // Calculate final price after applying the percentage discount
        $finalPrice = $originalPrice - ($originalPrice * ($discountPercent / 100));
        return max($finalPrice, 0); // Ensure price is not negative
    }

    // If format is invalid, throw an error
    throw new InvalidArgumentException("Invalid discount format. Supported formats: '-560 Kč', '20%'.");
}

// Example usage
try {
    $originalPrice = 1500; // Original price of the product in Kč
    $discountValue = '-560 Kč'; // Discount value in ActiveSport.cz format
    $finalPrice = calculateDiscountedPrice($originalPrice, $discountValue);

    echo "Original Price: {$originalPrice} Kč\n";
    echo "Discount: {$discountValue}\n";
    echo "Final Price: {$finalPrice} Kč\n";
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
