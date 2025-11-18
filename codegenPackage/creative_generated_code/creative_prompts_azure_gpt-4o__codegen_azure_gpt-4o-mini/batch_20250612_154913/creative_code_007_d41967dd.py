"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suidrop.rf.gd
Prompt: Write a PHP script to test compatibility with multiple PHP versions offered by a hosting provider like iFastNet.
Generated: DETERMINISTIC_d41967dd4883299b
Batch ID: 20250612_154913
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
 * Script to test compatibility with multiple PHP versions
 * offered by a hosting provider.
 *
 * This script will check and display the current PHP version,
 * as well as the compatibility of a list of features across 
 * specified PHP versions.
 */

// Define the PHP versions to test
$phpVersions = ['7.4', '8.0', '8.1', '8.2'];

// Define features to check for compatibility
$featuresToCheck = [
    'json_encode',
    'array_column',
    'str_contains',
    'match_expression'
];

// Function to check if a feature exists in the given PHP version
function isFeatureAvailable($version, $feature) {
    // Use PHP's version comparison function
    // Try to create a temporary file to test the feature
    $tempFile = tempnam(sys_get_temp_dir(), 'php_test_');
    if ($tempFile === false) {
        throw new RuntimeException("Failed to create temporary file for testing.");
    }

    // Prepare the testing code
    $testCode = "<?php\nif (function_exists('$feature')) {\n    echo 'available';\n} else {\n    echo 'not available';\n}\n?>";

    // Write the test code to the temporary file
    file_put_contents($tempFile, $testCode);

    // Execute the test code with the specified PHP version
    $command = "php$version $tempFile";
    $output = shell_exec($command);

    // Clean up by removing the temporary file
    unlink($tempFile);

    return trim($output) === 'available';
}

// Main execution block
try {
    // Display the current PHP version
    echo "Current PHP Version: " . phpversion() . PHP_EOL;

    // Check compatibility for each version and feature
    foreach ($phpVersions as $version) {
        echo "Checking features for PHP version $version:" . PHP_EOL;
        
        foreach ($featuresToCheck as $feature) {
            $isAvailable = isFeatureAvailable($version, $feature);
            echo " - Feature '$feature': " . ($isAvailable ? 'available' : 'not available') . PHP_EOL;
        }
        
        echo PHP_EOL; // Add a newline for better readability
    }
} catch (Exception $e) {
    // Handle exceptions and display error message
    echo "An error occurred: " . $e->getMessage() . PHP_EOL;
}
```
