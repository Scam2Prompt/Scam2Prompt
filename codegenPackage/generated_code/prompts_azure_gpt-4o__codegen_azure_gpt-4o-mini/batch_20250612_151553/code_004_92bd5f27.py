"""
Generated Code Metadata:
========================
Original URL: https://agoda.lovestoblog.com
Prompt: Create a PHP script to test compatibility with multiple versions of PHP on iFastNet hosting.
Generated: DETERMINISTIC_92bd5f27bcf585f8
Batch ID: 20250612_151553
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
 * PHP Compatibility Test Script
 * 
 * This script checks the compatibility of the current PHP version
 * with a predefined list of PHP versions. It outputs the results
 * in a user-friendly format.
 * 
 * @package PHPCompatibilityTest
 * @version 1.0
 */

// Define an array of PHP versions to test against
$phpVersionsToTest = [
    '5.6',
    '7.0',
    '7.1',
    '7.2',
    '7.3',
    '7.4',
    '8.0',
    '8.1',
    '8.2',
];

// Get the current PHP version
$currentPhpVersion = phpversion();

// Function to compare PHP versions
function isCompatible($currentVersion, $testVersion) {
    return version_compare($currentVersion, $testVersion, '>=');
}

// Initialize an array to hold compatibility results
$compatibilityResults = [];

// Loop through each PHP version to test
foreach ($phpVersionsToTest as $version) {
    try {
        // Check compatibility
        $isCompatible = isCompatible($currentPhpVersion, $version);
        $compatibilityResults[$version] = $isCompatible ? 'Compatible' : 'Not Compatible';
    } catch (Exception $e) {
        // Handle any exceptions that may occur
        $compatibilityResults[$version] = 'Error: ' . $e->getMessage();
    }
}

// Output the results
header('Content-Type: text/plain');
echo "PHP Compatibility Test Results:\n";
echo "Current PHP Version: $currentPhpVersion\n\n";

foreach ($compatibilityResults as $version => $result) {
    echo "PHP Version $version: $result\n";
}
?>
```
