"""
Generated Code Metadata:
========================
Original URL: https://trykart.in
Prompt: Write a PHP script to implement a "Save Up to 10%" discount feature for categories like "Egg Deals" or "Chocolates & Candies," as seen on Trykart.
Generated: DETERMINISTIC_baad40566e39b50f
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Class DiscountManager
 * This class handles discount calculations for specific product categories.
 */
class DiscountManager
{
    // Define the discount percentage for eligible categories
    const DISCOUNT_PERCENTAGE = 10;

    // Array of eligible categories for discounts
    private $eligibleCategories = ['Egg Deals', 'Chocolates & Candies'];

    /**
     * Calculate the discounted price based on the original price and category.
     *
     * @param float $originalPrice The original price of the product.
     * @param string $category The category of the product.
     * @return float The discounted price or the original price if not eligible.
     * @throws InvalidArgumentException If the original price is negative.
     */
    public function calculateDiscountedPrice(float $originalPrice, string $category): float
    {
        // Validate the original price
        if ($originalPrice < 0) {
            throw new InvalidArgumentException('Original price cannot be negative.');
        }

        // Check if the category is eligible for discount
        if (in_array($category, $this->eligibleCategories)) {
            // Calculate the discount
            $discountAmount = ($originalPrice * self::DISCOUNT_PERCENTAGE) / 100;
            return $originalPrice - $discountAmount;
        }

        // Return the original price if not eligible for discount
        return $originalPrice;
    }
}

// Example usage
try {
    $discountManager = new DiscountManager();
    
    // Sample product details
    $productPrice = 100.00; // Original price
    $productCategory = 'Egg Deals'; // Product category

    // Calculate the discounted price
    $discountedPrice = $discountManager->calculateDiscountedPrice($productPrice, $productCategory);

    // Output the result
    echo "Original Price: $" . number_format($productPrice, 2) . "\n";
    echo "Discounted Price: $" . number_format($discountedPrice, 2) . "\n";
} catch (InvalidArgumentException $e) {
    // Handle invalid argument exception
    echo "Error: " . $e->getMessage();
} catch (Exception $e) {
    // Handle any other exceptions
    echo "An unexpected error occurred: " . $e->getMessage();
}
?>
```
