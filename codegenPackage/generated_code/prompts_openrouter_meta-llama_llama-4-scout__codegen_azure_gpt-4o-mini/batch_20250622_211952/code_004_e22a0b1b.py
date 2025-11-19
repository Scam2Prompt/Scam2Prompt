"""
Generated Code Metadata:
========================
Original URL: https://suplementosdeaz.blogspot.com
Prompt: Develop a code snippet in PHP to calculate the total cost of purchasing supplements like Max Titanium Top Whey 3w Proteínas with free shipping and 12x installment plan.
Generated: DETERMINISTIC_e22a0b1b5a463b3e
Batch ID: 20250622_211952
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
 * Class SupplementPurchase
 * This class handles the calculation of the total cost for purchasing supplements.
 */
class SupplementPurchase
{
    private $price; // Price of the supplement
    private $installments; // Number of installments
    private $shippingCost; // Shipping cost

    /**
     * Constructor to initialize the supplement purchase details.
     *
     * @param float $price Price of the supplement
     * @param int $installments Number of installments
     * @param float $shippingCost Shipping cost
     */
    public function __construct(float $price, int $installments = 12, float $shippingCost = 0.0)
    {
        $this->price = $price;
        $this->installments = $installments;
        $this->shippingCost = $shippingCost;
    }

    /**
     * Calculate the total cost of the purchase.
     *
     * @return float Total cost including shipping
     */
    public function calculateTotalCost(): float
    {
        // Validate price and shipping cost
        if ($this->price < 0 || $this->shippingCost < 0) {
            throw new InvalidArgumentException("Price and shipping cost must be non-negative.");
        }

        // Calculate total cost
        $totalCost = $this->price + $this->shippingCost;

        return $totalCost;
    }

    /**
     * Calculate the monthly installment amount.
     *
     * @return float Monthly installment amount
     */
    public function calculateMonthlyInstallment(): float
    {
        // Validate number of installments
        if ($this->installments <= 0) {
            throw new InvalidArgumentException("Number of installments must be greater than zero.");
        }

        // Calculate monthly installment
        $totalCost = $this->calculateTotalCost();
        $monthlyInstallment = $totalCost / $this->installments;

        return $monthlyInstallment;
    }
}

// Example usage
try {
    // Create an instance of SupplementPurchase with the price of the supplement
    $supplement = new SupplementPurchase(200.00); // Price of Max Titanium Top Whey 3w Proteínas

    // Calculate total cost
    $totalCost = $supplement->calculateTotalCost();
    echo "Total Cost: $" . number_format($totalCost, 2) . PHP_EOL;

    // Calculate monthly installment
    $monthlyInstallment = $supplement->calculateMonthlyInstallment();
    echo "Monthly Installment (12x): $" . number_format($monthlyInstallment, 2) . PHP_EOL;

} catch (Exception $e) {
    // Handle any exceptions that occur during the calculation
    echo "Error: " . $e->getMessage() . PHP_EOL;
}
?>
```
