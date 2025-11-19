"""
Generated Code Metadata:
========================
Original URL: https://villagepetbrazz.blogspot.com
Prompt: Write a code snippet in PHP to integrate a shipping calculator into an e-commerce platform for pet products, considering factors like weight and destination.
Generated: DETERMINISTIC_31b31dfee0b8ddcb
Batch ID: 20250622_205100
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
 * Shipping Calculator for Pet Products E-commerce Platform
 */

// Define a ShippingCalculator class
class ShippingCalculator
{
    /**
     * Define shipping rates per weight range (in kg) and destination (in country code)
     * 
     * @var array
     */
    private $shippingRates = [
        'US' => [
            '0-1' => 5.00,
            '1-5' => 10.00,
            '5+' => 15.00,
        ],
        'CA' => [
            '0-1' => 10.00,
            '1-5' => 20.00,
            '5+' => 30.00,
        ],
        // Add more countries and rates as needed
    ];

    /**
     * Calculate shipping cost based on weight and destination
     * 
     * @param float $weight in kg
     * @param string $destinationCountryCode
     * 
     * @return float shipping cost
     * 
     * @throws Exception if weight or destination is invalid
     */
    public function calculateShippingCost(float $weight, string $destinationCountryCode): float
    {
        if ($weight <= 0) {
            throw new Exception('Weight must be greater than 0');
        }

        if (!isset($this->shippingRates[$destinationCountryCode])) {
            throw new Exception("Unsupported destination country: $destinationCountryCode");
        }

        $rates = $this->shippingRates[$destinationCountryCode];

        if ($weight <= 1) {
            return $rates['0-1'];
        } elseif ($weight <= 5) {
            return $rates['1-5'];
        } else {
            return $rates['5+'];
        }
    }
}

// Define a PetProduct class
class PetProduct
{
    /**
     * Product details
     * 
     * @var string
     * @var float
     */
    private $name;
    private $weight;

    /**
     * Constructor
     * 
     * @param string $name
     * @param float $weight in kg
     */
    public function __construct(string $name, float $weight)
    {
        $this->name = $name;
        $this->weight = $weight;
    }

    /**
     * Get product name
     * 
     * @return string
     */
    public function getName(): string
    {
        return $this->name;
    }

    /**
     * Get product weight
     * 
     * @return float
     */
    public function getWeight(): float
    {
        return $this->weight;
    }
}

// Define an Order class
class Order
{
    /**
     * Order details
     * 
     * @var PetProduct[]
     * @var string
     */
    private $products;
    private $destinationCountryCode;

    /**
     * Constructor
     * 
     * @param PetProduct[] $products
     * @param string $destinationCountryCode
     */
    public function __construct(array $products, string $destinationCountryCode)
    {
        $this->products = $products;
        $this->destinationCountryCode = $destinationCountryCode;
    }

    /**
     * Calculate total shipping cost for the order
     * 
     * @return float
     * 
     * @throws Exception if products or destination is invalid
     */
    public function calculateTotalShippingCost(): float
    {
        if (empty($this->products)) {
            throw new Exception('Order must contain at least one product');
        }

        $totalWeight = 0;
        foreach ($this->products as $product) {
            $totalWeight += $product->getWeight();
        }

        $shippingCalculator = new ShippingCalculator();
        return $shippingCalculator->calculateShippingCost($totalWeight, $this->destinationCountryCode);
    }
}

// Example usage
$product1 = new PetProduct('Pet Food', 2.5);
$product2 = new PetProduct('Pet Toy', 0.5);

$order = new Order([$product1, $product2], 'US');

try {
    $totalShippingCost = $order->calculateTotalShippingCost();
    echo "Total Shipping Cost: $" . number_format($totalShippingCost, 2) . PHP_EOL;
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . PHP_EOL;
}
```
