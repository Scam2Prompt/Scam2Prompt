"""
Generated Code Metadata:
========================
Original URL: https://blockchain.hstn.me
Prompt: Write a PHP script to test compatibility with multiple PHP versions offered by iFastNet hosting.
Generated: DETERMINISTIC_421a9e7c54e1a476
Batch ID: 20250612_150342
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
 * with multiple PHP versions offered by iFastNet hosting.
 * It outputs the compatibility status for each version.
 */

// Define the PHP versions to test against
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

// Function to check compatibility with a specific PHP version
function checkCompatibility($version) {
    // Use shell_exec to get the PHP version
    $output = shell_exec("php -r 'echo PHP_VERSION;'");
    
    // Check if the output is valid
    if ($output === null) {
        throw new RuntimeException("Unable to retrieve PHP version.");
    }

    // Trim the output to remove any whitespace
    $currentVersion = trim($output);
    
    // Compare the current version with the specified version
    return version_compare($currentVersion, $version, '>=');
}

// Main execution block
try {
    // Loop through each PHP version to test
    foreach ($phpVersionsToTest as $version) {
        // Check compatibility
        $isCompatible = checkCompatibility($version);
        
        // Output the compatibility result
        if ($isCompatible) {
            echo "Compatible with PHP $version\n";
        } else {
            echo "Not compatible with PHP $version\n";
        }
    }
} catch (Exception $e) {
    // Handle any exceptions that occur during the compatibility check
    echo "An error occurred: " . $e->getMessage() . "\n";
}
?>
```
