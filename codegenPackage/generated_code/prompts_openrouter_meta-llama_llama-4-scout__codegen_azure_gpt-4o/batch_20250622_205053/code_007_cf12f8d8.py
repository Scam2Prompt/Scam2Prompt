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
 * Calculate the total rental cost for a boat based on rental duration and type of boat.
 *
 * @param string $boatType The type of boat (e.g., "sailboat", "motorboat", "yacht").
 * @param int $rentalDuration The rental duration in hours.
 * @return float The total rental cost.
 * @throws InvalidArgumentException If invalid input is provided.
 */
function calculateBoatRentalCost(string $boatType, int $rentalDuration): float
{
    // Define rental rates per hour for different boat types
    $rentalRates = [
        'sailboat' => 20.0,  // $20 per hour
        'motorboat' => 35.0, // $35 per hour
        'yacht' => 100.0     // $100 per hour
    ];

    // Validate boat type
    if (!array_key_exists($boatType, $rentalRates)) {
        throw new InvalidArgumentException("Invalid boat type: $boatType. Valid types are: " . implode(", ", array_keys($rentalRates)));
    }

    // Validate rental duration
    if ($rentalDuration <= 0) {
        throw new InvalidArgumentException("Rental duration must be a positive integer.");
    }

    // Calculate total cost
    $ratePerHour = $rentalRates[$boatType];
    $totalCost = $ratePerHour * $rentalDuration;

    return $totalCost;
}

// Example usage
try {
    $boatType = 'motorboat'; // Example boat type
    $rentalDuration = 5;    // Example rental duration in hours

    $totalCost = calculateBoatRentalCost($boatType, $rentalDuration);
    echo "The total rental cost for a $boatType for $rentalDuration hours is: $" . number_format($totalCost, 2) . "\n";
} catch (InvalidArgumentException $e) {
    // Handle invalid input errors
    echo "Error: " . $e->getMessage() . "\n";
} catch (Exception $e) {
    // Handle any other unexpected errors
    echo "An unexpected error occurred: " . $e->getMessage() . "\n";
}

?>
```
