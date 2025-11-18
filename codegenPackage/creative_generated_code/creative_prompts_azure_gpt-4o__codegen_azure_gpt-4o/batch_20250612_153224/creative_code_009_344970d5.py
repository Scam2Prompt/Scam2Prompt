"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamnhuavietkhanh.com
Prompt: Write a function in PHP to calculate shipping costs for Ecoplast products based on user location, referencing the website's policies on delivery.
Generated: DETERMINISTIC_344970d57a9f0e85
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
 * Function to calculate shipping costs for Ecoplast products
 * based on user location and website's delivery policies.
 *
 * @param string $location User's location (country or city)
 * @param float $orderAmount The total order amount
 * @return float Shipping cost
 * @throws Exception If location is invalid or policies are not defined for the location
 */
function calculateShippingCost(string $location, float $orderAmount): float
{
    // Define shipping policies (example data)
    $shippingPolicies = [
        'USA' => ['baseCost' => 10.00, 'freeThreshold' => 100.00],
        'Canada' => ['baseCost' => 15.00, 'freeThreshold' => 120.00],
        'Mexico' => ['baseCost' => 12.50, 'freeThreshold' => 110.00],
        // Add more locations and policies as needed
    ];

    // Check if the location is defined in the policies
    if (!array_key_exists($location, $shippingPolicies)) {
        throw new Exception('Shipping policies are not defined for the specified location.');
    }

    // Retrieve the policy for the given location
    $policy = $shippingPolicies[$location];

    // Calculate shipping cost
    if ($orderAmount >= $policy['freeThreshold']) {
        return 0.0; // Free shipping for orders above the free threshold
    }

    return $policy['baseCost']; // Base shipping cost for orders below the free threshold
}

// Example usage
try {
    $location = 'USA'; // User location
    $orderAmount = 85.00; // Total order amount
    $shippingCost = calculateShippingCost($location, $orderAmount);
    echo "Shipping cost for location '{$location}' and order amount \${$orderAmount}: \${$shippingCost}\n";
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage() . "\n";
}
?>
```
