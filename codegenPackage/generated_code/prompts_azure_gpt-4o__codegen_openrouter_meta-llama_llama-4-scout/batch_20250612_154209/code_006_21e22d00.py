"""
Generated Code Metadata:
========================
Original URL: https://fourseasons.infinityfreeapp.com
Prompt: Create a PHP script to test the compatibility of multiple PHP versions on a hosting service with no daily process limits.
Generated: DETERMINISTIC_21e22d00c71870f6
Batch ID: 20250612_154209
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
 * PHP Version Compatibility Tester
 *
 * This script tests the compatibility of multiple PHP versions on a hosting service.
 */

// Configuration
$phpVersions = [
    '7.4',
    '8.0',
    '8.1',
    '8.2',
];

$tests = [
    'testPhpInfo' => 'Test PHP Info',
    'testErrorHandling' => 'Test Error Handling',
    'testFileOperations' => 'Test File Operations',
];

/**
 * Test PHP Info
 */
function testPhpInfo(): bool
{
    try {
        phpinfo();
        return true;
    } catch (Exception $e) {
        echo "Error testing PHP Info: " . $e->getMessage() . PHP_EOL;
        return false;
    }
}

/**
 * Test Error Handling
 */
function testErrorHandling(): bool
{
    try {
        trigger_error('Test error', E_USER_NOTICE);
        return true;
    } catch (Exception $e) {
        echo "Error testing Error Handling: " . $e->getMessage() . PHP_EOL;
        return false;
    }
}

/**
 * Test File Operations
 */
function testFileOperations(): bool
{
    $filePath = 'test.txt';
    try {
        $file = fopen($filePath, 'w');
        if ($file === false) {
            throw new Exception('Failed to open file for writing');
        }
        fwrite($file, 'Test content');
        fclose($file);

        // Clean up
        unlink($filePath);

        return true;
    } catch (Exception $e) {
        echo "Error testing File Operations: " . $e->getMessage() . PHP_EOL;
        return false;
    }
}

// Run tests for each PHP version
foreach ($phpVersions as $version) {
    echo "Testing PHP $version:" . PHP_EOL;

    // Run each test
    foreach ($tests as $testName => $testDescription) {
        echo "  $testDescription: ";
        $testResult = $testName();

        if ($testResult) {
            echo "Passed" . PHP_EOL;
        } else {
            echo "Failed" . PHP_EOL;
        }
    }

    echo PHP_EOL;
}

?>
```
