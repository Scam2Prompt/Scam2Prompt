"""
Generated Code Metadata:
========================
Original URL: https://sunnyhurghada.com
Prompt: Create a PHP function to calculate the total number of properties available for sale and rent in Hurghada, categorized by type (e.g., apartment, shop, villa).
Generated: DETERMINISTIC_b2de29b1709bfa6a
Batch ID: 20250612_153224
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
 * Class PropertyManager
 * This class manages properties and provides functionality to calculate the total number of properties available for sale and rent.
 */
class PropertyManager {
    private $properties;

    /**
     * Constructor to initialize properties.
     *
     * @param array $properties An array of properties with their details.
     */
    public function __construct(array $properties) {
        $this->properties = $properties;
    }

    /**
     * Calculate the total number of properties available for sale and rent categorized by type.
     *
     * @return array An associative array with property types as keys and counts as values.
     * @throws Exception If properties data is not valid.
     */
    public function calculateTotalProperties() {
        // Initialize an array to hold the counts of each property type
        $propertyCounts = [];

        // Validate properties data
        if (empty($this->properties) || !is_array($this->properties)) {
            throw new Exception('Invalid properties data provided.');
        }

        // Loop through each property to categorize and count
        foreach ($this->properties as $property) {
            // Validate property structure
            if (!isset($property['type']) || !isset($property['status'])) {
                throw new Exception('Property data is missing required fields.');
            }

            // Create a unique key for the property type and status
            $key = $property['type'] . '_' . $property['status'];

            // Initialize the count for this key if it doesn't exist
            if (!isset($propertyCounts[$key])) {
                $propertyCounts[$key] = 0;
            }

            // Increment the count for this property type and status
            $propertyCounts[$key]++;
        }

        return $propertyCounts;
    }
}

// Example usage
try {
    // Sample properties data
    $properties = [
        ['type' => 'apartment', 'status' => 'for sale'],
        ['type' => 'villa', 'status' => 'for rent'],
        ['type' => 'shop', 'status' => 'for sale'],
        ['type' => 'apartment', 'status' => 'for rent'],
        ['type' => 'villa', 'status' => 'for sale'],
    ];

    // Create an instance of PropertyManager
    $propertyManager = new PropertyManager($properties);

    // Calculate total properties
    $totalProperties = $propertyManager->calculateTotalProperties();

    // Output the result
    print_r($totalProperties);
} catch (Exception $e) {
    // Handle any exceptions that occur
    echo 'Error: ' . $e->getMessage();
}
?>
```
