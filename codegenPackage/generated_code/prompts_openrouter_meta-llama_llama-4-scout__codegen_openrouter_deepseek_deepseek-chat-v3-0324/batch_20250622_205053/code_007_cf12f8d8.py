"""
Generated Code Metadata:
========================
Original URL: https://coastalboatrentals.co.za
Prompt: "Generate a code snippet in PHP to calculate the total rental cost for a boat based on the rental duration and type of boat."
Generated: DETERMINISTIC_cf12f8d8d400145e
Batch ID: 20250622_205053
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
 * Calculates the total rental cost for a boat based on duration and boat type.
 *
 * @param string $boatType Type of boat (e.g., 'speedboat', 'yacht', 'pontoon')
 * @param int $duration Rental duration in hours
 * @return float Total rental cost
 * @throws InvalidArgumentException If invalid boat type or negative duration provided
 */
function calculateBoatRentalCost(string $boatType, int $duration): float
{
    // Validate input parameters
    if ($duration <= 0) {
        throw new InvalidArgumentException('Duration must be a positive integer');
    }

    // Define hourly rates for different boat types
    $hourlyRates = [
        'speedboat' => 50.00,
        'yacht' => 150.00,
        'pontoon' => 75.00,
        'jetski' => 40.00
    ];

    // Check if boat type exists in rates
    if (!array_key_exists($boatType, $hourlyRates)) {
        throw new InvalidArgumentException("Invalid boat type: $boatType");
    }

    // Calculate total cost
    $hourlyRate = $hourlyRates[$boatType];
    $totalCost = $hourlyRate * $duration;

    // Apply discounts for longer durations
    if ($duration >= 8) {
        $totalCost *= 0.9; // 10% discount for rentals 8+ hours
    } elseif ($duration >= 4) {
        $totalCost *= 0.95; // 5% discount for rentals 4+ hours
    }

    return round($totalCost, 2);
}

// Example usage:
try {
    $boatType = 'yacht';
    $duration = 6;
    $totalCost = calculateBoatRentalCost($boatType, $duration);
    echo "Total rental cost for $boatType for $duration hours: \$" . number_format($totalCost, 2);
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage();
}

?>
```
