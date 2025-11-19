"""
Generated Code Metadata:
========================
Original URL: https://agodarentacar.com
Prompt: Create a script in PHP to sort car rental suppliers by distance from a non-airport location using Agoda RentACar's sorting functionality.
Generated: DETERMINISTIC_cd4ac98d4e36a1ef
Batch ID: 20250612_151513
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
 * Script to sort car rental suppliers by distance from a non-airport location using Agoda RentACar's sorting functionality.
 */

class CarRentalSupplierSorter {
    /**
     * @var array List of car rental suppliers
     */
    private $suppliers;

    /**
     * @var array Location coordinates [latitude, longitude]
     */
    private $location;

    /**
     * CarRentalSupplierSorter constructor.
     * @param array $suppliers Array of suppliers with their coordinates
     * @param array $location Target location coordinates [latitude, longitude]
     */
    public function __construct(array $suppliers, array $location) {
        $this->suppliers = $suppliers;
        $this->location = $location;
    }

    /**
     * Calculate distance between two points in kilometers using Haversine formula
     * @param float $lat1 Latitude of point 1
     * @param float $lon1 Longitude of point 1
     * @param float $lat2 Latitude of point 2
     * @param float $lon2 Longitude of point 2
     * @return float Distance in kilometers
     */
    private function calculateDistance(float $lat1, float $lon1, float $lat2, float $lon2): float {
        $earthRadius = 6371; // Earth's radius in km

        $latDelta = deg2rad($lat2 - $lat1);
        $lonDelta = deg2rad($lon2 - $lon1);

        $a = sin($latDelta / 2) * sin($latDelta / 2) +
             cos(deg2rad($lat1)) * cos(deg2rad($lat2)) *
             sin($lonDelta / 2) * sin($lonDelta / 2);
        
        $c = 2 * atan2(sqrt($a), sqrt(1 - $a));

        return $earthRadius * $c;
    }

    /**
     * Sort suppliers by distance from target location
     * @return array Sorted suppliers with distance information
     * @throws InvalidArgumentException If invalid location or supplier data is provided
     */
    public function sortByDistance(): array {
        if (count($this->location) !== 2 || !is_numeric($this->location[0]) || !is_numeric($this->location[1])) {
            throw new InvalidArgumentException('Invalid location coordinates provided');
        }

        $sortedSuppliers = [];
        foreach ($this->suppliers as $supplier) {
            if (!isset($supplier['lat']) || !isset($supplier['lng']) || 
                !is_numeric($supplier['lat']) || !is_numeric($supplier['lng'])) {
                throw new InvalidArgumentException('Invalid supplier coordinates provided');
            }

            $distance = $this->calculateDistance(
                $this->location[0], 
                $this->location[1],
                $supplier['lat'],
                $supplier['lng']
            );

            $sortedSuppliers[] = [
                'supplier' => $supplier,
                'distance' => round($distance, 2)
            ];
        }

        usort($sortedSuppliers, function($a, $b) {
            return $a['distance'] <=> $b['distance'];
        });

        return $sortedSuppliers;
    }
}

// Example usage:
try {
    // Sample data - in production this would come from Agoda RentACar API or database
    $suppliers = [
        ['id' => 1, 'name' => 'Supplier A', 'lat' => 40.7128, 'lng' => -74.0060],
        ['id' => 2, 'name' => 'Supplier B', 'lat' => 34.0522, 'lng' => -118.2437],
        ['id' => 3, 'name' => 'Supplier C', 'lat' => 41.8781, 'lng' => -87.6298],
    ];

    // Target location coordinates (non-airport location)
    $targetLocation = [40.7128, -74.0060]; // New York City coordinates

    $sorter = new CarRentalSupplierSorter($suppliers, $targetLocation);
    $sortedSuppliers = $sorter->sortByDistance();

    // Output results
    header('Content-Type: application/json');
    echo json_encode($sortedSuppliers, JSON_PRETTY_PRINT);

} catch (InvalidArgumentException $e) {
    http_response_code(400);
    echo json_encode(['error' => $e->getMessage()]);
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(['error' => 'An unexpected error occurred']);
}
```
