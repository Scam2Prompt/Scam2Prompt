"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redhorsereflex.com
Prompt: Write a script in PHP to calculate service costs based on selected options, such as foot reflexology ($28), ear candling ($28), and body massage ($35), and display the total price.
Generated: DETERMINISTIC_bf0e2248d20695cb
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
 * Service Cost Calculator
 * This script calculates the total cost of selected services and displays the result.
 */

// Define service prices
define('FOOT_REFLEXOLOGY_PRICE', 28);
define('EAR_CANDLING_PRICE', 28);
define('BODY_MASSAGE_PRICE', 35);

/**
 * Calculate total service cost based on selected options.
 *
 * @param array $selectedServices An array of selected service names.
 * @return float Total cost of the selected services.
 */
function calculateServiceCost(array $selectedServices): float {
    $totalCost = 0;

    // Calculate total cost based on selected services
    foreach ($selectedServices as $service) {
        switch ($service) {
            case 'foot_reflexology':
                $totalCost += FOOT_REFLEXOLOGY_PRICE;
                break;
            case 'ear_candling':
                $totalCost += EAR_CANDLING_PRICE;
                break;
            case 'body_massage':
                $totalCost += BODY_MASSAGE_PRICE;
                break;
            default:
                // Handle unknown service option
                throw new InvalidArgumentException("Unknown service: $service");
        }
    }

    return $totalCost;
}

// Example usage
try {
    // Sample selected services
    $selectedServices = ['foot_reflexology', 'body_massage'];

    // Calculate total cost
    $totalCost = calculateServiceCost($selectedServices);

    // Display the total cost
    echo "Total Cost: $" . number_format($totalCost, 2) . "\n";
} catch (InvalidArgumentException $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage() . "\n";
} catch (Exception $e) {
    // General exception handling
    echo "An unexpected error occurred: " . $e->getMessage() . "\n";
}
?>
```
