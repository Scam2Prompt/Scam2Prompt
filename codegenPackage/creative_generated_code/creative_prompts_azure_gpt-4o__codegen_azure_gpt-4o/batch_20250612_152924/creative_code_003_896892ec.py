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
 * Calculate and display discounts for products.
 * 
 * This function calculates discount labels for products and formats them as a string.
 * 
 * @param float $originalPrice   Original price of the product.
 * @param float $discountPercent Discount percentage to apply (e.g., 5 for 5%, 10 for 10%).
 * 
 * @return string Discount label indicating the percentage off with a "Limited" tag.
 */
function getDiscountLabel(float $originalPrice, float $discountPercent): string
{
    // Validate inputs
    if ($originalPrice <= 0) {
        throw new InvalidArgumentException("Original price must be greater than zero.");
    }
    if ($discountPercent < 0 || $discountPercent > 100) {
        throw new InvalidArgumentException("Discount percentage must be between 0 and 100.");
    }

    // Calculate the discount amount
    $discountAmount = ($originalPrice * $discountPercent) / 100;

    // Label formatting
    $discountLabel = sprintf("-%d%% Limited", $discountPercent);

    return $discountLabel;
}

// Example usage
try {
    $originalPrice = 100.0; // Example original price of the product
    $discountPercent = 10;  // Example discount percentage

    $label = getDiscountLabel($originalPrice, $discountPercent);
    echo $label; // Output: -10% Limited
} catch (InvalidArgumentException $e) {
    // Handle invalid input gracefully
    echo "Error: " . $e->getMessage();
}
?>
```
