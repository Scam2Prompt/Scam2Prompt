"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://garudassociates.com
Prompt: Write a PHP function for calculating investigation costs based on resources, services, and time requirements, as described in the FAQ section of Garud Associates.
Generated: DETERMINISTIC_92cdaafcd6e8c90a
Batch ID: 20250612_153225
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
 * Calculate investigation costs based on resources, services, and time requirements.
 *
 * @param array $resources An associative array of resource costs. Example: ['investigator' => 50, 'equipment' => 100].
 * @param array $services An associative array of service costs. Example: ['background_check' => 200, 'surveillance' => 300].
 * @param int $hours Number of hours required for the investigation process.
 * @param float $hourlyRate Hourly rate for labor (resource usage per hour).
 *
 * @return float The total investigation cost.
 * @throws InvalidArgumentException If invalid input arguments are provided.
 */
function calculateInvestigationCost(array $resources, array $services, int $hours, float $hourlyRate): float
{
    // Validate inputs
    if ($hours < 0 || $hourlyRate < 0) {
        throw new InvalidArgumentException("Hours and hourly rate must be non-negative values.");
    }

    if (empty($resources) || empty($services)) {
        throw new InvalidArgumentException("Resources and services arrays cannot be empty.");
    }

    // Calculate resource costs
    $resourceCost = 0;
    foreach ($resources as $resource => $cost) {
        if ($cost < 0) {
            throw new InvalidArgumentException("Resource cost for '{$resource}' must be a non-negative value.");
        }
        $resourceCost += $cost;
    }

    // Calculate service costs
    $serviceCost = 0;
    foreach ($services as $service => $cost) {
        if ($cost < 0) {
            throw new InvalidArgumentException("Service cost for '{$service}' must be a non-negative value.");
        }
        $serviceCost += $cost;
    }

    // Calculate total cost
    $laborCost = $hours * $hourlyRate; // Labor cost based on hourly rate and time
    $totalCost = $resourceCost + $serviceCost + $laborCost;

    return $totalCost;
}

// Example usage:
try {
    $resources = ['investigator' => 50, 'equipment' => 100];
    $services = ['background_check' => 200, 'surveillance' => 300];
    $hours = 5;
    $hourlyRate = 20.0;

    $totalCost = calculateInvestigationCost($resources, $services, $hours, $hourlyRate);
    echo "Total investigation cost: $" . number_format($totalCost, 2);
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage();
}

?>
```
