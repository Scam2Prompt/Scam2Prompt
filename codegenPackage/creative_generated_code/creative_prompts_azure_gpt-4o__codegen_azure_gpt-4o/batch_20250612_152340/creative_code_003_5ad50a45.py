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
 * Function to display a list of Panasonic electrical switches and their discounted prices, sorted by category.
 *
 * @return void
 */
function displayPanasonicSwitches()
{
    // Sample data: List of Panasonic switches with category, name, price, and discount percentage
    $switches = [
        [
            'category' => 'Wide Series',
            'name' => 'Mặt Công Tắc Đôi Panasonic Wide WEV68020SW',
            'price' => 120000, // Original price in VND
            'discount' => 10 // Discount percentage
        ],
        [
            'category' => 'Wide Series',
            'name' => 'Công Tắc Đơn Panasonic Wide WEV50010SW',
            'price' => 80000,
            'discount' => 5
        ],
        [
            'category' => 'Slim Series',
            'name' => 'Mặt Công Tắc Đôi Panasonic Slim WES68020W',
            'price' => 140000,
            'discount' => 15
        ],
        [
            'category' => 'Slim Series',
            'name' => 'Công Tắc Đơn Panasonic Slim WES50010W',
            'price' => 90000,
            'discount' => 10
        ]
    ];

    // Sort switches by category
    usort($switches, function ($a, $b) {
        return strcmp($a['category'], $b['category']);
    });

    // Display the switches
    echo "Panasonic Electrical Switches:\n\n";

    foreach ($switches as $switch) {
        try {
            // Calculate discounted price
            if (!is_numeric($switch['price']) || !is_numeric($switch['discount'])) {
                throw new Exception("Invalid price or discount value for {$switch['name']}.");
            }
            $discountedPrice = $switch['price'] * (1 - $switch['discount'] / 100);

            // Format output
            echo "Category: {$switch['category']}\n";
            echo "Name: {$switch['name']}\n";
            echo "Original Price: " . number_format($switch['price'], 0, ',', '.') . " VND\n";
            echo "Discounted Price: " . number_format($discountedPrice, 0, ',', '.') . " VND\n";
            echo "-------------------------\n";
        } catch (Exception $e) {
            // Handle errors gracefully
            echo "Error: " . $e->getMessage() . "\n";
        }
    }
}

// Call the function to display the switches
displayPanasonicSwitches();

?>
```
