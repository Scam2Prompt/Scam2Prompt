"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxfuili.epizy.com
Prompt: Write a PHP script to test compatibility across multiple PHP versions on a hosting platform that offers unlimited bandwidth.
Generated: DETERMINISTIC_6b2a7fe993a4c25a
Batch ID: 20250612_151126
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
 * Compatibility Test Script for Multiple PHP Versions
 *
 * This script checks the compatibility of a given feature across multiple PHP versions.
 * It will output whether each version supports the feature and provide a summary at the end.
 */

// List of PHP versions to test
$phpVersions = ['7.4', '8.0', '8.1', '8.2'];

// Feature to test
$featureToTest = 'array_filter'; // Example feature for testing

// Store results
$results = [];

/**
 * Checks if a feature is supported in a given PHP version.
 *
 * @param string $version The PHP version to test.
 * @param string $feature The feature to test for compatibility.
 * @return bool Returns true if the feature is supported, false otherwise.
 */
function isFeatureSupported($version, $feature) {
    // Use PHP's built-in function to check the version
    if (version_compare(PHP_VERSION, $version, '<')) {
        return false; // Skip testing if the current version is lower than the version being tested
    }

    // Use eval to test if the feature exists (this is a risky operation; should be used cautiously)
    try {
        eval("return function_exists('$feature');");
        return true;
    } catch (Throwable $e) {
        return false; // Catch any errors that occur during eval
    }
}

// Testing compatibility across specified PHP versions
foreach ($phpVersions as $version) {
    $isSupported = isFeatureSupported($version, $featureToTest);
    $results[$version] = $isSupported ? 'Supported' : 'Not Supported';
}

// Output results
echo "Compatibility Test Results for Feature: $featureToTest\n";
echo "-------------------------------------------\n";
foreach ($results as $version => $status) {
    echo "PHP Version $version: $status\n";
}
echo "-------------------------------------------\n";

// Summary of results
$summary = array_count_values($results);
echo "Summary:\n";
echo "Supported: " . ($summary['Supported'] ?? 0) . "\n";
echo "Not Supported: " . ($summary['Not Supported'] ?? 0) . "\n";
?>
```
