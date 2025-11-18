"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sunnyhurghada.com
Prompt: Create a PHP function to calculate the total number of properties available for sale and rent in Hurghada, categorized by type (e.g., apartment, shop, villa).
Generated: DETERMINISTIC_b2de29b1709bfa6a
Batch ID: 20250612_153224
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
 * Class PropertyManager
 *
 * A class to manage property listings and calculate totals based on type.
 */
class PropertyManager {
    private $properties; // Array to store properties

    /**
     * PropertyManager constructor.
     *
     * @param array $properties An array of properties with type and status
     */
    public function __construct(array $properties) {
        $this->properties = $properties; // Initialize the properties array
    }

    /**
     * Calculate the total number of properties available for sale and rent.
     *
     * @return array An associative array containing the count of properties categorized by type
     */
    public function calculateTotals() {
        // Initialize an associative array to hold the totals
        $totals = [
            'apartment' => 0,
            'shop' => 0,
            'villa' => 0,
        ];

        // Iterate through each property and categorize by type
        foreach ($this->properties as $property) {
            // Validate the property structure
            if (!isset($property['type']) || !isset($property['status'])) {
                throw new InvalidArgumentException('Invalid property format. Each property must have a type and status.');
            }

            // Increment the count based on property type
            if (array_key_exists($property['type'], $totals)) {
                $totals[$property['type']]++;
            } else {
                throw new InvalidArgumentException('Unknown property type: ' . $property['type']);
            }
        }

        return $totals; // Return the totals
    }
}

// Sample properties array
$properties = [
    ['type' => 'apartment', 'status' => 'for sale'],
    ['type' => 'villa', 'status' => 'for rent'],
    ['type' => 'shop', 'status' => 'for sale'],
    ['type' => 'apartment', 'status' => 'for rent'],
    ['type' => 'villa', 'status' => 'for sale'],
];

// Create an instance of PropertyManager
try {
    $propertyManager = new PropertyManager($properties);
    // Calculate totals
    $totals = $propertyManager->calculateTotals();
    // Output the results
    echo json_encode($totals);
} catch (Exception $e) {
    // Handle any exceptions
    echo 'Error: ' . $e->getMessage();
}

?>
```
