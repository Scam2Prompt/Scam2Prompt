"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-optimism-airdrop.rf.gd
Prompt: Write a PHP script to test compatibility with multiple PHP versions on a hosting service that supports this feature, referencing iFastNet hosting.
Generated: DETERMINISTIC_d50aa89c4351d7aa
Batch ID: 20250612_152954
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
 * PHP Compatibility Tester
 * This script tests the compatibility of the current PHP version
 * with multiple PHP versions as specified by the user.
 * It is designed to run on iFastNet hosting or any compatible environment.
 */

// Define an array of PHP versions to test against
$phpVersionsToTest = ['7.2', '7.3', '7.4', '8.0', '8.1', '8.2'];

// Function to check if a specific PHP version is installed
function isPhpVersionInstalled($version) {
    // Execute the PHP CLI command to get the available PHP versions
    $output = shell_exec('ls /usr/bin/php*');
    
    // Check if the output contains the specified version
    return strpos($output, "php{$version}") !== false;
}

// Function to test the compatibility of a specific PHP version
function testPhpVersion($version) {
    // Set the PHP binary path based on the version
    $phpBinary = "/usr/bin/php{$version}";

    // Check if the PHP binary exists
    if (!file_exists($phpBinary)) {
        return [
            'version' => $version,
            'installed' => false,
            'message' => "PHP version {$version} is not installed."
        ];
    }

    // Run a simple PHP script to check compatibility
    $testScript = '<?php echo "Testing PHP version: " . PHP_VERSION; ?>';
    $tempFile = tempnam(sys_get_temp_dir(), 'php_test_') . '.php';
    file_put_contents($tempFile, $testScript);

    // Execute the script with the specified PHP version
    $output = shell_exec("{$phpBinary} {$tempFile}");

    // Clean up the temporary file
    unlink($tempFile);

    return [
        'version' => $version,
        'installed' => true,
        'output' => $output
    ];
}

// Main execution block
$results = [];

// Loop through each version and test compatibility
foreach ($phpVersionsToTest as $version) {
    $results[] = testPhpVersion($version);
}

// Output results in a readable format
header('Content-Type: application/json');
echo json_encode($results, JSON_PRETTY_PRINT);
?>
```
