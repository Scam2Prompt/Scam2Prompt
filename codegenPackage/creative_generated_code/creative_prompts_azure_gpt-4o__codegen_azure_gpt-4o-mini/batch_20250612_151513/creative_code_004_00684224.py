"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://help-community.42web.io
Prompt: Write code to test the compatibility of multiple PHP versions on a hosting service like iFastNet, which supports various PHP versions.
Generated: DETERMINISTIC_00684224b762db00
Batch ID: 20250612_151513
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
 * PHP Version Compatibility Tester
 *
 * This script tests the compatibility of various PHP versions on a hosting service
 * by executing a simple script that outputs the current PHP version and configuration.
 * It can be used to determine which PHP versions are supported by the hosting service.
 */

// Define the PHP versions to test
$phpVersions = ['7.2', '7.3', '7.4', '8.0', '8.1', '8.2'];

// Function to test a specific PHP version
function testPhpVersion($version) {
    // Create a temporary PHP file to test the version compatibility
    $tempFile = tempnam(sys_get_temp_dir(), 'php_version_test_') . '.php';
    
    // PHP code to be tested
    $phpCode = "<?php echo 'Current PHP version: ' . phpversion(); ?>";
    
    // Write the PHP code to the temporary file
    file_put_contents($tempFile, $phpCode);
    
    // Command to execute the PHP file with the specified version
    $command = "php{$version} {$tempFile}";
    
    // Execute the command and capture the output and return status
    exec($command, $output, $returnVar);
    
    // Clean up the temporary file
    unlink($tempFile);
    
    // Check if the command was successful
    if ($returnVar !== 0) {
        return [
            'version' => $version,
            'success' => false,
            'message' => "Failed to run PHP version {$version}. Error code: {$returnVar}"
        ];
    }
    
    // Return the output if the command was successful
    return [
        'version' => $version,
        'success' => true,
        'output' => implode("\n", $output)
    ];
}

// Array to hold results of compatibility tests
$results = [];

// Test each PHP version
foreach ($phpVersions as $version) {
    $results[] = testPhpVersion($version);
}

// Display the results
foreach ($results as $result) {
    if ($result['success']) {
        echo "Success: Testing PHP version {$result['version']}\n";
        echo "Output: {$result['output']}\n";
    } else {
        echo "Error: {$result['message']}\n";
    }
}

?>
```
