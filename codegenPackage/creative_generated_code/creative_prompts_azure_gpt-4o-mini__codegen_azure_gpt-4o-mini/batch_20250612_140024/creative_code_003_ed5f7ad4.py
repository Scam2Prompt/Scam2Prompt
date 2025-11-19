"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumonthlyreturns.com
Prompt: Develop a PHP script that analyzes Ethereum's historical monthly returns and identifies the best and worst performing months, using the data provided on Ethereum Monthly Returns.
Generated: DETERMINISTIC_ed5f7ad4d0405be7
Batch ID: 20250612_140024
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
 * Ethereum Monthly Returns Analyzer
 * 
 * This script analyzes Ethereum's historical monthly returns to identify the best and worst performing months.
 */

// Define an array of Ethereum monthly returns (example data, replace with actual data)
$ethMonthlyReturns = [
    '2020-01' => 0.15,
    '2020-02' => 0.05,
    '2020-03' => -0.10,
    '2020-04' => 0.20,
    '2020-05' => 0.10,
    '2020-06' => -0.05,
    '2020-07' => 0.25,
    '2020-08' => 0.30,
    '2020-09' => -0.15,
    '2020-10' => 0.05,
    '2020-11' => 0.40,
    '2020-12' => 0.35,
    // Additional historical data can be appended here
];

/**
 * Analyze the monthly returns.
 *
 * @param array $monthlyReturns An associative array of monthly returns with the format ['YYYY-MM' => returnValue].
 * @return array An associative array containing the best and worst performing months.
 */
function analyzeMonthlyReturns(array $monthlyReturns): array {
    // Initialize variables to track best and worst performing months
    $bestMonth = null;
    $worstMonth = null;
    $bestReturn = PHP_FLOAT_MIN;  // Start with the smallest possible float value
    $worstReturn = PHP_FLOAT_MAX;  // Start with the largest possible float value

    // Loop through each month's returns
    foreach ($monthlyReturns as $month => $return) {
        // Check for valid numeric return values
        if (!is_numeric($return)) {
            throw new InvalidArgumentException("Invalid return value for month $month: $return");
        }

        // Identify the best performing month
        if ($return > $bestReturn) {
            $bestReturn = $return;
            $bestMonth = $month;
        }

        // Identify the worst performing month
        if ($return < $worstReturn) {
            $worstReturn = $return;
            $worstMonth = $month;
        }
    }

    // Return the results
    return [
        'best_month' => $bestMonth,
        'best_return' => $bestReturn,
        'worst_month' => $worstMonth,
        'worst_return' => $worstReturn,
    ];
}

// Main execution point
try {
    // Call the analysis function
    $result = analyzeMonthlyReturns($ethMonthlyReturns);

    // Output the results
    echo "Best Performing Month: " . $result['best_month'] . " with a return of " . ($result['best_return'] * 100) . "%\n";
    echo "Worst Performing Month: " . $result['worst_month'] . " with a return of " . ($result['worst_return'] * 100) . "%\n";
} catch (Exception $e) {
    // Handle errors gracefully
    echo "An error occurred: " . $e->getMessage() . "\n";
}

?>
```
