"""
Generated Code Metadata:
========================
Original URL: https://suspended-website.com
Prompt: Write PHP code to test multiple PHP versions on a hosting service that allows switching between versions, such as iFastNet.
Generated: DETERMINISTIC_c98423e169dd9bf1
Batch ID: 20250612_154913
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
 * PHP Version Tester
 *
 * This script tests multiple PHP versions on a hosting service.
 */

// Configuration
$versions = ['7.4', '8.0', '8.1']; // List of PHP versions to test
$testFunctions = [
    'phpversion' => function () { return phpversion(); },
    'extensions' => function () { return get_loaded_extensions(); },
    'memoryLimit' => function () { return ini_get('memory_limit'); },
];

/**
 * Test PHP version
 *
 * @param string $version PHP version to test
 *
 * @return array Test results
 */
function testPhpVersion(string $version): array
{
    $results = [];

    // Switch to the specified PHP version
    if (!ini_set('engine', 0) || !ini_set('engine', 1)) {
        $results['error'] = 'Failed to switch PHP version';
        return $results;
    }

    // Run tests
    foreach ($GLOBALS['testFunctions'] as $testName => $testFunction) {
        try {
            $result = $testFunction();
            $results[$testName] = $result;
        } catch (Exception $e) {
            $results[$testName] = 'Error: ' . $e->getMessage();
        }
    }

    return $results;
}

// Test each PHP version
$allResults = [];
foreach ($versions as $version) {
    echo "Testing PHP $version...\n";
    $results = testPhpVersion($version);
    $allResults[$version] = $results;
    echo "PHP $version results:\n";
    print_r($results);
    echo "\n";
}

// Print summary
echo "Summary:\n";
foreach ($allResults as $version => $results) {
    echo "PHP $version:\n";
    foreach ($results as $testName => $result) {
        echo "  $testName: " . (is_array($result) ? implode(', ', $result) : $result) . "\n";
    }
}

?>
```
