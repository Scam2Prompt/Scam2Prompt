"""
Generated Code Metadata:
========================
Original URL: https://ethereumonthlyreturns.com
Prompt: Develop a PHP script that analyzes Ethereum's historical monthly returns and identifies the best and worst performing months, using the data provided on Ethereum Monthly Returns.
Generated: DETERMINISTIC_ed5f7ad4d0405be7
Batch ID: 20250612_140024
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
 * Ethereum Monthly Returns Analyzer
 * 
 * This script analyzes Ethereum's historical monthly returns and identifies
 * the best and worst performing months based on the provided data.
 * 
 * Requirements:
 * - PHP 7.4 or higher
 * - Data should be provided as an associative array with months as keys and returns as values.
 */

// Sample Ethereum Monthly Returns Data (replace with actual data)
$ethereumMonthlyReturns = [
    "2023-01" => 12.5,
    "2023-02" => -8.3,
    "2023-03" => 5.7,
    "2023-04" => 18.2,
    "2023-05" => -3.4,
    "2023-06" => 7.1,
    "2023-07" => 10.0,
    "2023-08" => -15.6,
    "2023-09" => 2.3,
    "2023-10" => 6.8,
    "2023-11" => -1.2,
    "2023-12" => 4.5
];

try {
    // Validate the input data
    if (empty($ethereumMonthlyReturns) || !is_array($ethereumMonthlyReturns)) {
        throw new InvalidArgumentException("Invalid data provided for Ethereum monthly returns.");
    }

    // Initialize variables to track best and worst months
    $bestMonth = null;
    $worstMonth = null;
    $highestReturn = PHP_FLOAT_MIN;
    $lowestReturn = PHP_FLOAT_MAX;

    // Analyze the data
    foreach ($ethereumMonthlyReturns as $month => $return) {
        // Validate the return value
        if (!is_numeric($return)) {
            throw new UnexpectedValueException("Non-numeric return value detected for month: $month");
        }

        // Update best month
        if ($return > $highestReturn) {
            $highestReturn = $return;
            $bestMonth = $month;
        }

        // Update worst month
        if ($return < $lowestReturn) {
            $lowestReturn = $return;
            $worstMonth = $month;
        }
    }

    // Output the results
    echo "Ethereum Monthly Returns Analysis:\n";
    echo "----------------------------------\n";
    echo "Best Performing Month: $bestMonth with a return of $highestReturn%\n";
    echo "Worst Performing Month: $worstMonth with a return of $lowestReturn%\n";

} catch (Exception $e) {
    // Handle errors gracefully
    echo "An error occurred: " . $e->getMessage() . "\n";
}
?>
```
