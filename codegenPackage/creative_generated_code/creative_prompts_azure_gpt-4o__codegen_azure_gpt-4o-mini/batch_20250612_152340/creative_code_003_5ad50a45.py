"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.panasonics.com.vn
Prompt: Write a function in PHP to display a list of Panasonic electrical switches (e.g., "Mặt Công Tắc Đôi Panasonic Wide WEV68020SW") and their discounted prices, sorted by category.
Generated: DETERMINISTIC_5ad50a45365ee1dc
Batch ID: 20250612_152340
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
 * Class to manage Panasonic electrical switches and their prices.
 */
class PanasonicSwitches
{
    private $switches = [];

    /**
     * Constructor to initialize the switches array.
     */
    public function __construct()
    {
        $this->initializeSwitches();
    }

    /**
     * Initialize the list of Panasonic switches with categories and prices.
     */
    private function initializeSwitches()
    {
        // Example data: category => [switch name => price]
        $this->switches = [
            'Standard' => [
                'Mặt Công Tắc Đôi Panasonic Wide WEV68020SW' => 100000,
                'Mặt Công Tắc Đơn Panasonic WEV68010SW' => 60000,
            ],
            'Premium' => [
                'Mặt Công Tắc Đôi Panasonic WEV68025SW' => 150000,
                'Mặt Công Tắc Đơn Panasonic WEV68015SW' => 80000,
            ],
            'Smart' => [
                'Mặt Công Tắc Thông Minh Panasonic WEV68030SW' => 200000,
            ],
        ];
    }

    /**
     * Apply discounts to the prices.
     *
     * @param float $discountPercentage The discount percentage to apply.
     * @return void
     * @throws Exception If the discount percentage is invalid.
     */
    public function applyDiscount(float $discountPercentage)
    {
        if ($discountPercentage < 0 || $discountPercentage > 100) {
            throw new Exception('Invalid discount percentage. It must be between 0 and 100.');
        }

        // Apply the discount to each switch
        foreach ($this->switches as $category => &$switches) {
            foreach ($switches as $name => &$price) {
                $price = $price - ($price * ($discountPercentage / 100));
            }
        }
    }

    /**
     * Display the list of switches sorted by category with their discounted prices.
     *
     * @return void
     */
    public function displaySwitches()
    {
        // Sort categories alphabetically
        ksort($this->switches);

        foreach ($this->switches as $category => $switches) {
            echo "Category: " . $category . "\n";
            foreach ($switches as $name => $price) {
                echo " - " . $name . ": " . number_format($price, 0, ',', '.') . " VND\n";
            }
            echo "\n";
        }
    }
}

// Main execution
try {
    // Create an instance of PanasonicSwitches
    $panasonicSwitches = new PanasonicSwitches();

    // Apply a discount of 10%
    $panasonicSwitches->applyDiscount(10);

    // Display the switches
    $panasonicSwitches->displaySwitches();
} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage();
}
```
