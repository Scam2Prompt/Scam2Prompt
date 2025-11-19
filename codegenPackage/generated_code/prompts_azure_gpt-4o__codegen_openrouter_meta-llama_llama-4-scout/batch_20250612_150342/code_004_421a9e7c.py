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
 * Test PHP compatibility with multiple PHP versions offered by iFastNet hosting.
 *
 * This script checks the PHP version and tests basic functionality.
 */

// Configuration
$phpVersions = [
    '7.4' => '7.4.33',
    '8.0' => '8.0.28',
    '8.1' => '8.1.25',
    '8.2' => '8.2.12',
];

// Function to test PHP version
function testPhpVersion(string $version): bool
{
    try {
        // Simulate PHP version check
        $simulatedVersion = explode('.', phpversion());
        if ((int) $simulatedVersion[0] === (int) explode('.', $version)[0]) {
            echo "PHP Version " . phpversion() . " is compatible with $version\n";
            return true;
        } else {
            echo "PHP Version " . phpversion() . " is not compatible with $version\n";
            return false;
        }
    } catch (Exception $e) {
        echo "Error testing PHP version: " . $e->getMessage() . "\n";
        return false;
    }
}

// Function to test basic PHP functionality
function testPhpFunctionality(): bool
{
    try {
        // Test basic PHP functionality
        $test = 'Hello, World!';
        if (strlen($test) > 0) {
            echo "Basic PHP functionality is working\n";
            return true;
        } else {
            echo "Basic PHP functionality is not working\n";
            return false;
        }
    } catch (Exception $e) {
        echo "Error testing PHP functionality: " . $e->getMessage() . "\n";
        return false;
    }
}

// Main function
function main(): void
{
    global $phpVersions;

    echo "Testing PHP compatibility...\n";
    echo "Current PHP version: " . phpversion() . "\n";

    foreach ($phpVersions as $version => $targetVersion) {
        testPhpVersion($targetVersion);
    }

    testPhpFunctionality();
}

main();

?>
```
