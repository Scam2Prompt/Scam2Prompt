"""
Generated Code Metadata:
========================
Original URL: https://garudassociates.com
Prompt: Write a PHP function for calculating investigation costs based on resources, services, and time requirements, as described in the FAQ section of Garud Associates.
Generated: DETERMINISTIC_92cdaafcd6e8c90a
Batch ID: 20250612_153225
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
 * Calculates investigation costs based on resources, services, and time requirements.
 *
 * @param array $resources Array of resource types and quantities
 * @param array $services Array of services required
 * @param int $estimatedHours Estimated hours for the investigation
 * @param float $discountPercentage Optional discount percentage (0-100)
 * @return array Returns an array with cost breakdown and total
 * @throws InvalidArgumentException If input validation fails
 */
function calculateInvestigationCost(
    array $resources,
    array $services,
    int $estimatedHours,
    float $discountPercentage = 0.0
): array {
    // Validate inputs
    if ($estimatedHours <= 0) {
        throw new InvalidArgumentException('Estimated hours must be greater than 0');
    }

    if ($discountPercentage < 0 || $discountPercentage > 100) {
        throw new InvalidArgumentException('Discount percentage must be between 0 and 100');
    }

    // Resource rates (per hour)
    $resourceRates = [
        'standard' => 75.00,
        'senior' => 120.00,
        'expert' => 200.00,
        'technical' => 150.00,
    ];

    // Service fees (fixed)
    $serviceFees = [
        'surveillance' => 500.00,
        'background_check' => 300.00,
        'digital_forensics' => 800.00,
        'legal_documentation' => 450.00,
    ];

    // Calculate resource costs
    $resourceCost = 0.0;
    foreach ($resources as $type => $quantity) {
        if (!isset($resourceRates[$type])) {
            throw new InvalidArgumentException("Invalid resource type: $type");
        }
        if (!is_int($quantity) || $quantity <= 0) {
            throw new InvalidArgumentException("Invalid quantity for resource $type");
        }
        $resourceCost += $resourceRates[$type] * $quantity * $estimatedHours;
    }

    // Calculate service costs
    $serviceCost = 0.0;
    foreach ($services as $service) {
        if (!isset($serviceFees[$service])) {
            throw new InvalidArgumentException("Invalid service: $service");
        }
        $serviceCost += $serviceFees[$service];
    }

    // Calculate subtotal
    $subtotal = $resourceCost + $serviceCost;

    // Apply discount if any
    $discountAmount = $subtotal * ($discountPercentage / 100);
    $total = $subtotal - $discountAmount;

    // Return detailed cost breakdown
    return [
        'resource_cost' => round($resourceCost, 2),
        'service_cost' => round($serviceCost, 2),
        'subtotal' => round($subtotal, 2),
        'discount_percentage' => $discountPercentage,
        'discount_amount' => round($discountAmount, 2),
        'total_cost' => round($total, 2),
        'estimated_hours' => $estimatedHours,
    ];
}

?>
```
