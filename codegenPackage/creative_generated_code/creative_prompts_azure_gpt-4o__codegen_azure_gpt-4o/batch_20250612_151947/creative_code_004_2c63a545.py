"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panam.su
Prompt: Write a script in PHP to generate a transparent renovation cost estimate, factoring in discounts for families with children as described on the ПАНАМ website.
Generated: DETERMINISTIC_2c63a545ee132927
Batch ID: 20250612_151947
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
 * Renovation Cost Estimation Script
 * This script calculates a transparent renovation cost estimate based on given inputs.
 * Families with children are eligible for discounts according to specified rules.
 */

// Function to calculate renovation cost estimate
function calculateRenovationCost($baseCost, $hasChildren, $numberOfChildren) {
    try {
        // Validate inputs
        if (!is_numeric($baseCost) || $baseCost <= 0) {
            throw new Exception("Base cost must be a positive number.");
        }
        if (!is_bool($hasChildren)) {
            throw new Exception("The 'hasChildren' parameter must be a boolean.");
        }
        if ($hasChildren && (!is_int($numberOfChildren) || $numberOfChildren < 0)) {
            throw new Exception("Number of children must be a non-negative integer.");
        }

        // Discount rules for families with children
        $discount = 0;
        if ($hasChildren) {
            // Families with children get a 5% discount per child, capped at 20%
            $discount = min(0.05 * $numberOfChildren, 0.20);
        }

        // Calculate final cost after applying the discount
        $finalCost = $baseCost * (1 - $discount);

        return [
            "baseCost" => round($baseCost, 2),
            "discountPercent" => $discount * 100,
            "finalCost" => round($finalCost, 2)
        ];
    } catch (Exception $e) {
        // Handle errors gracefully
        return [
            "error" => $e->getMessage()
        ];
    }
}

// Example usage
$baseCost = 10000; // Example base cost in currency units
$hasChildren = true; // Indicate if the family has children
$numberOfChildren = 3; // Number of children

$estimate = calculateRenovationCost($baseCost, $hasChildren, $numberOfChildren);

// Output the result
echo json_encode($estimate, JSON_PRETTY_PRINT);
?>
```
