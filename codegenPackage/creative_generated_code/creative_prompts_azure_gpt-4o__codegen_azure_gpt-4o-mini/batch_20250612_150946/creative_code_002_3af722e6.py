"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://extensiontoken.rf.gd
Prompt: Generate a PHP script that utilizes a hosting service with multiple versions of PHP and no daily hit limit, as described on iFastNet's hosting platform.
Generated: DETERMINISTIC_3af722e6ef85fafc
Batch ID: 20250612_150946
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
 * PHP Script Example for iFastNet Hosting Platform
 * This script demonstrates the use of multiple PHP versions
 * and is designed to run without daily hit limits on iFastNet.
 * 
 * Make sure to adjust PHP version in the .htaccess file as per your requirement.
 * 
 * @version 1.0
 * @author Your Name
 */

// Define the path to the directory where this script resides
define('SCRIPT_DIR', __DIR__);

/**
 * Function to display the current PHP version
 * 
 * @return void
 */
function displayPhpVersion() {
    // Output the current PHP version
    echo "Current PHP version: " . phpversion() . PHP_EOL;
}

/**
 * Main execution block
 */
try {
    // Display the current PHP version
    displayPhpVersion();

    // Example of a basic operation
    $number = 10;
    $result = factorial($number);
    echo "Factorial of {$number} is {$result}" . PHP_EOL;

} catch (Exception $e) {
    // Handle exceptions by displaying an error message
    echo "An error occurred: " . $e->getMessage() . PHP_EOL;
}

/**
 * Calculate factorial of a number
 * 
 * @param int $n The number to calculate the factorial for
 * @return int The factorial of the number
 * @throws InvalidArgumentException if the input is negative
 */
function factorial($n) {
    // Validate the input
    if ($n < 0) {
        throw new InvalidArgumentException("Input must be a non-negative integer.");
    }

    // Base case
    if ($n === 0) {
        return 1;
    }

    // Recursive case
    return $n * factorial($n - 1);
}
?>
```
