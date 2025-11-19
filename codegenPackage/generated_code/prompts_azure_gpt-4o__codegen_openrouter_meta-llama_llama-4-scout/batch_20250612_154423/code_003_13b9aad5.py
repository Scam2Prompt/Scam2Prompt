"""
Generated Code Metadata:
========================
Original URL: https://metamask-a.infinityfreeapp.com
Prompt: Write a PHP script to test the compatibility of different PHP versions on a hosting platform like iFastNet.
Generated: DETERMINISTIC_13b9aad5b5c6a851
Batch ID: 20250612_154423
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
 * This script tests the compatibility of different PHP versions on a hosting platform.
 *
 * @author [Your Name]
 */

// Configuration
$phpVersions = [
    '7.4' => '7.4.0',
    '8.0' => '8.0.0',
    '8.1' => '8.1.0',
];

// Function to test PHP version compatibility
function testPhpVersion($version) {
    try {
        // Create a temporary file to test PHP version
        $file = 'php_version_test.php';
        $content = '<?php echo PHP_VERSION; ?>';
        file_put_contents($file, $content);

        // Execute the temporary file using the specified PHP version
        $output = shell_exec("php-$version $file");

        // Remove the temporary file
        unlink($file);

        // Check if the PHP version matches
        if (trim($output) === $version) {
            return true;
        } else {
            return false;
        }
    } catch (Exception $e) {
        // Log the error
        error_log("Error testing PHP version $version: " . $e->getMessage());
        return false;
    }
}

// Test PHP version compatibility
$results = [];
foreach ($phpVersions as $version => $targetVersion) {
    $compatible = testPhpVersion($version);
    $results[$version] = [
        'compatible' => $compatible,
        'target_version' => $targetVersion,
    ];
}

// Display results
echo "# PHP Version Compatibility Test Results\n";
echo "| PHP Version | Compatible | Target Version |\n";
echo "| --- | --- | --- |\n";
foreach ($results as $version => $result) {
    $compatibleStatus = $result['compatible'] ? 'Yes' : 'No';
    echo "| $version | $compatibleStatus | $result[target_version] |\n";
}

?>
```
