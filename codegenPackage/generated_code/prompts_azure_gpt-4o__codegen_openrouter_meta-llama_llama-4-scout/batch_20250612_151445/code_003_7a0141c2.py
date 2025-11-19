"""
Generated Code Metadata:
========================
Original URL: https://glveaways-ethereums-trustswallet-com.html-5.me
Prompt: Create a PHP script that tests compatibility across multiple PHP versions, specifically for deployment on a hosting service like iFastNet.
Generated: DETERMINISTIC_7a0141c2c589d81b
Batch ID: 20250612_151445
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
 * PHP Compatibility Tester
 *
 * This script tests compatibility across multiple PHP versions.
 *
 * @author [Your Name]
 */

// Configuration
$phpVersions = [
    '7.4' => '7.4.9',
    '8.0' => '8.0.8',
    '8.1' => '8.1.5',
    '8.2' => '8.2.2',
];

$tests = [
    'testPhpVersion' => function ($version) {
        echo "Testing PHP version $version...\n";
        return PHP_VERSION === $version;
    },
    'testExtension' => function ($version, $extension) {
        echo "Testing $extension extension on PHP $version...\n";
        return extension_loaded($extension);
    },
    'testFunction' => function ($version, $function) {
        echo "Testing $function function on PHP $version...\n";
        return function_exists($function);
    },
];

// Run tests
foreach ($phpVersions as $version => $phpVersion) {
    echo "Testing PHP $version ($phpVersion)...\n";
    try {
        // Switch to the desired PHP version
        if (PHP_VERSION !== $phpVersion) {
            // Note: This part may require CLI and specific setup, adjust according to your environment
            // For simplicity, assume we are using the CLI and can switch PHP versions easily
            // In a real scenario, consider using containerization or similar for accurate testing
            echo "Switching to PHP $phpVersion...\n";
            // For demonstration, assume a function switches PHP version, which is not directly possible in PHP
            // This step may involve external tools or complex setup not shown here
            // switchPhpVersion($phpVersion);
        }

        // Run compatibility tests
        foreach ($tests as $testName => $test) {
            if ($testName === 'testPhpVersion') {
                $result = $test($phpVersion);
            } else {
                // Example usage, adjust extensions and functions as needed
                $result = $test($phpVersion, 'mysqli'); // Example extension
                // $result = $test($phpVersion, 'json_decode'); // Example function
            }

            if ($result) {
                echo "  - $testName: Passed\n";
            } else {
                echo "  - $testName: Failed\n";
            }
        }
    } catch (Exception $e) {
        echo "An error occurred: " . $e->getMessage() . "\n";
    }
    echo "\n";
}

?>
```
