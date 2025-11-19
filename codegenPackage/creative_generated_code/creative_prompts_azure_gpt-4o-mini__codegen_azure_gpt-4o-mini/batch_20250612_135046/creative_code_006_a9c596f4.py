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
 * Diving Gear Catalog Script
 * This script generates a catalog of diving gear, including filters for wetsuits, masks, and underwater lights.
 */

// Sample diving gear data
$divingGear = [
    [
        'id' => 1,
        'type' => 'wetsuit',
        'brand' => 'Aqualung',
        'size' => 'M',
        'price' => 199.99,
        'description' => 'A high-quality wetsuit for divers.'
    ],
    [
        'id' => 2,
        'type' => 'mask',
        'brand' => 'Scubapro',
        'color' => 'black',
        'price' => 59.99,
        'description' => 'A comfortable mask for clear vision underwater.'
    ],
    [
        'id' => 3,
        'type' => 'underwater light',
        'brand' => 'Light & Motion',
        'lumens' => 1200,
        'price' => 299.99,
        'description' => 'A powerful underwater light for night diving.'
    ],
    // Add more diving gear as needed
];

/**
 * Filter diving gear by type
 *
 * @param array $gearList The list of diving gear to filter.
 * @param string $type The type of diving gear to filter by.
 * @return array The filtered list of diving gear.
 */
function filterDivingGearByType(array $gearList, string $type): array {
    return array_filter($gearList, function($item) use ($type) {
        return isset($item['type']) && $item['type'] === $type;
    });
}

// Handle user input for filtering
$typeFilter = isset($_GET['type']) ? $_GET['type'] : '';

// Validate the type filter
$validTypes = ['wetsuit', 'mask', 'underwater light'];
if ($typeFilter && !in_array($typeFilter, $validTypes)) {
    die('Invalid filter type provided.');
}

// Filter the diving gear based on user input
$filteredGear = $typeFilter ? filterDivingGearByType($divingGear, $typeFilter) : $divingGear;

/**
 * Display the diving gear catalog
 *
 * @param array $gearList The list of diving gear to display.
 */
function displayDivingGearCatalog(array $gearList) {
    echo "<h1>Diving Gear Catalog</h1>";
    if (empty($gearList)) {
        echo "<p>No diving gear available.</p>";
        return;
    }
    
    echo "<ul>";
    foreach ($gearList as $gear) {
        echo "<li>";
        echo "<strong>Type:</strong> {$gear['type']}<br>";
        echo "<strong>Brand:</strong> {$gear['brand']}<br>";
        echo "<strong>Price:</strong> \${$gear['price']}<br>";
        echo "<strong>Description:</strong> {$gear['description']}<br>";
        if (isset($gear['size'])) {
            echo "<strong>Size:</strong> {$gear['size']}<br>";
        }
        if (isset($gear['color'])) {
            echo "<strong>Color:</strong> {$gear['color']}<br>";
        }
        if (isset($gear['lumens'])) {
            echo "<strong>Lumens:</strong> {$gear['lumens']}<br>";
        }
        echo "</li><br>";
    }
    echo "</ul>";
}

// Display the filtered diving gear catalog
displayDivingGearCatalog($filteredGear);
?>
```
