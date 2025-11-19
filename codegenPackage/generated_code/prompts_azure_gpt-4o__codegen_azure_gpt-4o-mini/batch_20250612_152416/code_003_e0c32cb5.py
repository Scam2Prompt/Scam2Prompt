"""
Generated Code Metadata:
========================
Original URL: https://moneypak.thsite.top
Prompt: Create a PHP script that checks the compatibility of multiple PHP versions supported by iFastNet hosting.
Generated: DETERMINISTIC_e0c32cb5032cf493
Batch ID: 20250612_152416
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
 * PHP Version Compatibility Checker for iFastNet Hosting
 *
 * This script checks the compatibility of multiple PHP versions
 * supported by iFastNet hosting. It verifies if the specified
 * PHP versions are installed and returns their status.
 */

// Define the PHP versions to check
$phpVersionsToCheck = [
    '7.2',
    '7.3',
    '7.4',
    '8.0',
    '8.1',
    '8.2'
];

/**
 * Check if a specific PHP version is installed
 *
 * @param string $version The PHP version to check
 * @return bool True if the version is installed, false otherwise
 */
function isPhpVersionInstalled($version) {
    // Execute the command to check the PHP version
    $output = [];
    $returnVar = 0;
    exec("php{$version} -v", $output, $returnVar);

    // Return true if the command was successful, indicating the version is installed
    return $returnVar === 0;
}

// Initialize an array to hold the results
$results = [];

// Loop through each PHP version and check its status
foreach ($phpVersionsToCheck as $version) {
    try {
        // Check if the PHP version is installed
        $isInstalled = isPhpVersionInstalled($version);
        $results[$version] = $isInstalled ? 'Installed' : 'Not Installed';
    } catch (Exception $e) {
        // Handle any exceptions that may occur
        $results[$version] = 'Error: ' . $e->getMessage();
    }
}

// Output the results
header('Content-Type: application/json');
echo json_encode($results, JSON_PRETTY_PRINT);
?>
```
