"""
Generated Code Metadata:
========================
Original URL: https://www.panasonics.com.vn
Prompt: Write a function in PHP to display a list of Panasonic electrical switches (e.g., "Mặt Công Tắc Đôi Panasonic Wide WEV68020SW") and their discounted prices, sorted by category.
Generated: DETERMINISTIC_5ad50a45365ee1dc
Batch ID: 20250612_152340
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
 * Displays a list of Panasonic electrical switches with discounted prices, sorted by category.
 *
 * @return void
 */
function displayPanasonicSwitches() {
    // Define the switch data with categories, names, original prices, and discounts
    $switches = [
        'Wide Series' => [
            [
                'name' => 'Mặt Công Tắc Đôi Panasonic Wide WEV68020SW',
                'original_price' => 250000,
                'discount_percent' => 10
            ],
            [
                'name' => 'Mặt Công Tắc Đơn Panasonic Wide WEV68010SW',
                'original_price' => 150000,
                'discount_percent' => 15
            ]
        ],
        'Premium Series' => [
            [
                'name' => 'Mặt Công Tắc Đôi Panasonic Premium WEP68020SW',
                'original_price' => 300000,
                'discount_percent' => 20
            ],
            [
                'name' => 'Mặt Công Tắc Đơn Panasonic Premium WEP68010SW',
                'original_price' => 200000,
                'discount_percent' => 10
            ]
        ],
        'Standard Series' => [
            [
                'name' => 'Mặt Công Tắc Đôi Panasonic Standard WES68020SW',
                'original_price' => 180000,
                'discount_percent' => 5
            ],
            [
                'name' => 'Mặt Công Tắc Đơn Panasonic Standard WES68010SW',
                'original_price' => 120000,
                'discount_percent' => 8
            ]
        ]
    ];

    // Display the switches sorted by category
    foreach ($switches as $category => $items) {
        echo "<h2>$category</h2>";
        echo "<ul>";
        
        foreach ($items as $item) {
            $discountedPrice = $item['original_price'] * (1 - $item['discount_percent'] / 100);
            $formattedPrice = number_format($discountedPrice, 0, ',', '.') . ' VND';
            $originalPriceFormatted = number_format($item['original_price'], 0, ',', '.') . ' VND';
            
            echo "<li>";
            echo "<strong>{$item['name']}</strong><br>";
            echo "Original Price: <del>$originalPriceFormatted</del><br>";
            echo "Discounted Price: <span style='color:red;'>$formattedPrice</span> ";
            echo "(Save {$item['discount_percent']}%)";
            echo "</li>";
        }
        
        echo "</ul>";
    }
}

// Call the function to display the switches
displayPanasonicSwitches();

?>
```
