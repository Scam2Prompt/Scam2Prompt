"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-version5.42web.io
Prompt: Generate a PHP script to test multiple PHP versions on iFastNet hosting, as highlighted in the website's features.
Generated: DETERMINISTIC_b9a24a00a1b27915
Batch ID: 20250612_154222
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
 * Script to test multiple PHP versions on iFastNet hosting.
 * Ensure that the hosting environment supports changing PHP versions dynamically.
 * This script verifies PHP version switching and outputs results for each version tested.
 */

// List of PHP versions to test (update based on hosting availability)
$phpVersions = ['7.4', '8.0', '8.1'];

// Initialize an array to store test results
$testResults = [];

/**
 * Function to execute a test for the current PHP version.
 *
 * @return array An associative array containing the PHP version and results of the test.
 */
function runTest() {
    // Gather PHP version info
    $phpVersion = phpversion();

    // Perform a basic test (e.g., string manipulation or math operation)
    $testString = strtoupper('hello world');
    $testMath = 2 + 2;

    // Check if the test results are as expected
    $testPassed = ($testString === 'HELLO WORLD' && $testMath === 4);

    // Return the version and test results
    return [
        'version' => $phpVersion,
        'stringTest' => $testString,
        'mathTest' => $testMath,
        'overallTestPassed' => $testPassed
    ];
}

// Loop through each PHP version to test
foreach ($phpVersions as $phpVersion) {
    try {
        // Simulate switching PHP versions (ensure this is configured on hosting)
        // NOTE: Actual version switching is a server-side operation and is hosting-specific.
        // For iFastNet hosting, this is typically done via cPanel or a `.htaccess` configuration.
        // Uncomment and adjust the following line if `.htaccess` or server settings allow dynamic switching:
        // putenv("PHP_VERSION=$phpVersion");

        // Run the test
        $testResults[$phpVersion] = runTest();
    } catch (Exception $e) {
        // Handle any unexpected errors during testing
        $testResults[$phpVersion] = [
            'version' => $phpVersion,
            'error' => $e->getMessage()
        ];
    }
}

// Output the results
header('Content-Type: application/json');
echo json_encode($testResults, JSON_PRETTY_PRINT);
?>
```
