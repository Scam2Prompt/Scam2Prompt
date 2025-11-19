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
 * Analyzes Ethereum's historical monthly returns and identifies the best and worst performing months.
 * 
 * @param array $monthlyReturns An associative array where keys are month-year strings (e.g., "Jan-2020") 
 *                              and values are the corresponding monthly returns as floats.
 * @return array An associative array containing:
 *               - 'best_month' => ['month' => string, 'return' => float]
 *               - 'worst_month' => ['month' => string, 'return' => float]
 * @throws InvalidArgumentException If input data is invalid.
 */
function analyzeEthereumReturns(array $monthlyReturns): array {
    // Validate input data
    if (empty($monthlyReturns)) {
        throw new InvalidArgumentException("Monthly returns data cannot be empty.");
    }

    $bestMonth = null;
    $worstMonth = null;

    foreach ($monthlyReturns as $month => $return) {
        // Validate return value is numeric
        if (!is_numeric($return)) {
            throw new InvalidArgumentException("Invalid return value for month: $month");
        }

        // Initialize best and worst months with first entry
        if ($bestMonth === null) {
            $bestMonth = ['month' => $month, 'return' => (float)$return];
            $worstMonth = ['month' => $month, 'return' => (float)$return];
            continue;
        }

        // Update best month if current return is higher
        if ($return > $bestMonth['return']) {
            $bestMonth = ['month' => $month, 'return' => (float)$return];
        }

        // Update worst month if current return is lower
        if ($return < $worstMonth['return']) {
            $worstMonth = ['month' => $month, 'return' => (float)$return];
        }
    }

    return [
        'best_month' => $bestMonth,
        'worst_month' => $worstMonth
    ];
}

// Example usage with sample data
try {
    // Sample data: Replace this with actual Ethereum monthly returns data
    $ethereumMonthlyReturns = [
        'Jan-2020' => 35.2,
        'Feb-2020' => -12.5,
        'Mar-2020' => -25.8,
        'Apr-2020' => 42.6,
        'May-2020' => 18.3,
        'Jun-2020' => -5.7,
        'Jul-2020' => 30.1,
        'Aug-2020' => 15.9,
        'Sep-2020' => -8.4,
        'Oct-2020' => 22.7,
        'Nov-2020' => 45.3,
        'Dec-2020' => 12.8
    ];

    $analysis = analyzeEthereumReturns($ethereumMonthlyReturns);

    // Output results
    echo "Best Month: {$analysis['best_month']['month']} with return of {$analysis['best_month']['return']}%\n";
    echo "Worst Month: {$analysis['worst_month']['month']} with return of {$analysis['worst_month']['return']}%\n";

} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage() . "\n";
} catch (Exception $e) {
    echo "An unexpected error occurred: " . $e->getMessage() . "\n";
}

?>
```
