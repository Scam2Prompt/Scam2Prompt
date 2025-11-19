"""
Generated Code Metadata:
========================
Original URL: https://dappsconnect.42web.io
Prompt: Create a PHP script to test multiple PHP versions on a hosting platform with unlimited bandwidth and no daily hit limit, such as iFastNet hosting.
Generated: DETERMINISTIC_5575dc5d2a1ead0a
Batch ID: 20250612_154740
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
 * PHP Version Tester Script
 *
 * This script tests multiple PHP versions on a hosting platform.
 *
 * @author [Your Name]
 */

// Configuration
$phpVersions = [
    '7.4' => '7.4',
    '8.0' => '8.0',
    '8.1' => '8.1',
    '8.2' => '8.2',
];

// Set output buffer to capture PHP version info
ob_start();

try {
    // Loop through each PHP version
    foreach ($phpVersions as $version => $phpVersion) {
        echo "Testing PHP $version...\n";
        
        // Get current PHP version
        $currentVersion = phpversion();
        echo "Current PHP Version: $currentVersion\n";
        
        // Check if PHP version matches
        if ($currentVersion === $phpVersion) {
            echo "PHP $version is being used.\n";
        } else {
            echo "PHP $version is not being used.\n";
        }
        
        // Get PHP configuration
        $phpConfig = phpinfo();
        echo "PHP Configuration:\n";
        echo $phpConfig;
        
        // Clear output buffer
        ob_clean();
    }
} catch (Exception $e) {
    // Handle any exceptions
    echo "An error occurred: " . $e->getMessage() . "\n";
} finally {
    // Flush output buffer
    ob_flush();
}

?>
```
