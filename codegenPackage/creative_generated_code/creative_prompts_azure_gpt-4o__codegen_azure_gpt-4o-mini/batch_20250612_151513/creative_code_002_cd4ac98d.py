"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agodarentacar.com
Prompt: Create a script in PHP to sort car rental suppliers by distance from a non-airport location using Agoda RentACar's sorting functionality.
Generated: DETERMINISTIC_cd4ac98d4e36a1ef
Batch ID: 20250612_151513
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
 * Class CarRentalSupplier
 * Represents a car rental supplier with a name and distance from a location.
 */
class CarRentalSupplier {
    public $name;
    public $distance; // Distance in kilometers

    /**
     * CarRentalSupplier constructor.
     * @param string $name
     * @param float $distance
     */
    public function __construct(string $name, float $distance) {
        $this->name = $name;
        $this->distance = $distance;
    }
}

/**
 * Function to sort car rental suppliers by distance.
 *
 * @param CarRentalSupplier[] $suppliers
 * @return CarRentalSupplier[]
 */
function sortSuppliersByDistance(array $suppliers): array {
    // Validate input suppliers array
    if (empty($suppliers)) {
        throw new InvalidArgumentException('Suppliers array cannot be empty.');
    }

    // Sort suppliers using usort and a custom comparison function
    usort($suppliers, function ($a, $b) {
        return $a->distance <=> $b->distance; // Spaceship operator for comparison
    });

    return $suppliers; // Return sorted array
}

/**
 * Main function to demonstrate sorting of car rental suppliers.
 */
function main() {
    try {
        // Sample data for car rental suppliers
        $suppliers = [
            new CarRentalSupplier('Supplier A', 15.3),
            new CarRentalSupplier('Supplier B', 10.7),
            new CarRentalSupplier('Supplier C', 12.5),
            new CarRentalSupplier('Supplier D', 8.0),
        ];

        // Sort the suppliers by distance
        $sortedSuppliers = sortSuppliersByDistance($suppliers);

        // Display sorted suppliers
        echo "Car Rental Suppliers sorted by distance:\n";
        foreach ($sortedSuppliers as $supplier) {
            printf("%s - %.2f km\n", $supplier->name, $supplier->distance);
        }
    } catch (Exception $e) {
        // Handle exceptions and display error message
        echo "Error: " . $e->getMessage() . "\n";
    }
}

// Execute the main function
main();

?>
```
