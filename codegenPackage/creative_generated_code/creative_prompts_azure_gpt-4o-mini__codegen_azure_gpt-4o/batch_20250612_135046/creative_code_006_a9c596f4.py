"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.ru
Prompt: Construct a PHP script that generates a catalog of diving gear, including filters for wetsuits, masks, and underwater lights.
Generated: DETERMINISTIC_a9c596f4fbd664ad
Batch ID: 20250612_135046
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
 * Diving Gear Catalog Generator
 * 
 * This script generates a catalog of diving gear with filters for wetsuits, masks, and underwater lights.
 * It uses a sample dataset to demonstrate functionality.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Sample dataset of diving gear items
$catalog = [
    ['name' => 'UltraFlex Wetsuit', 'type' => 'wetsuit', 'price' => 199.99],
    ['name' => 'AquaVision Diving Mask', 'type' => 'mask', 'price' => 79.99],
    ['name' => 'HydroGlow Underwater Light', 'type' => 'underwater-light', 'price' => 89.99],
    ['name' => 'ProDive Full Wetsuit', 'type' => 'wetsuit', 'price' => 249.99],
    ['name' => 'ClearView Mask', 'type' => 'mask', 'price' => 59.99],
    ['name' => 'OceanShine Dive Light', 'type' => 'underwater-light', 'price' => 99.99],
];

/**
 * Filters the catalog by item type
 *
 * @param array $catalog The diving gear catalog
 * @param string $filterType The type of item to filter ('wetsuit', 'mask', 'underwater-light')
 * @return array Filtered list of items
 */
function filterCatalog(array $catalog, string $filterType): array
{
    return array_filter($catalog, function ($item) use ($filterType) {
        return $item['type'] === $filterType;
    });
}

/**
 * Displays the catalog in a formatted manner
 *
 * @param array $catalog The catalog of diving gear items
 */
function displayCatalog(array $catalog): void
{
    echo "Diving Gear Catalog:\n";
    echo "--------------------\n";
    foreach ($catalog as $item) {
        echo "Name: {$item['name']}, Type: {$item['type']}, Price: $ {$item['price']}\n";
    }
    echo "\n";
}

// Main Script Logic
try {
    // Display the full catalog
    echo "Full Catalog:\n";
    displayCatalog($catalog);

    // Filter by wetsuits
    echo "Filtered Catalog - Wetsuits:\n";
    $wetsuits = filterCatalog($catalog, 'wetsuit');
    displayCatalog($wetsuits);

    // Filter by masks
    echo "Filtered Catalog - Masks:\n";
    $masks = filterCatalog($catalog, 'mask');
    displayCatalog($masks);

    // Filter by underwater lights
    echo "Filtered Catalog - Underwater Lights:\n";
    $underwaterLights = filterCatalog($catalog, 'underwater-light');
    displayCatalog($underwaterLights);

} catch (Exception $e) {
    // Handle unexpected errors
    echo "An error occurred: " . $e->getMessage();
}

?>
```
