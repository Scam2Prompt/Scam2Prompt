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
 * This script analyzes Ethereum's historical monthly returns
 * and identifies the best and worst performing months based
 * on a given dataset.
 */

// Sample data: Ethereum Monthly Returns (percentage returns for each month)
// Format: ['YYYY-MM' => return_percentage]
$ethereumMonthlyReturns = [
    '2023-01' => 10.5,
    '2023-02' => -5.2,
    '2023-03' => 15.8,
    '2023-04' => -8.7,
    '2023-05' => 12.3,
    '2023-06' => -3.4,
    '2023-07' => 9.8,
    '2023-08' => -1.2,
    '2023-09' => 7.6,
    '2023-10' => 2.4,
];

try {
    // Check if the dataset is valid
    if (empty($ethereumMonthlyReturns)) {
        throw new Exception('No data available for analysis.');
    }

    // Initialize variables to track the best and worst months
    $bestMonth = null;
    $bestReturn = PHP_FLOAT_MIN;
    $worstMonth = null;
    $worstReturn = PHP_FLOAT_MAX;

    // Loop through the dataset to find the best and worst performing months
    foreach ($ethereumMonthlyReturns as $month => $return) {
        // Check for valid return value
        if (!is_numeric($return)) {
            throw new Exception("Invalid return value detected for month: {$month}");
        }

        // Update best performing month if current return is higher
        if ($return > $bestReturn) {
            $bestReturn = $return;
            $bestMonth = $month;
        }

        // Update worst performing month if current return is lower
        if ($return < $worstReturn) {
            $worstReturn = $return;
            $worstMonth = $month;
        }
    }

    // Output the results
    echo "Best Performing Month: {$bestMonth} with return {$bestReturn}%\n";
    echo "Worst Performing Month: {$worstMonth} with return {$worstReturn}%\n";
} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage() . "\n";
}

?>
```
