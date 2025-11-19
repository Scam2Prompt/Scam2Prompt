"""
Generated Code Metadata:
========================
Original URL: https://help-community.42web.io
Prompt: Write code to test the compatibility of multiple PHP versions on a hosting service like iFastNet, which supports various PHP versions.
Generated: DETERMINISTIC_00684224b762db00
Batch ID: 20250612_151513
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
 * This script checks the compatibility of a given PHP script with multiple PHP versions
 * on a hosting service like iFastNet.
 */

// List of PHP versions to test
$phpVersions = [
    '7.2',
    '7.3',
    '7.4',
    '8.0',
    '8.1',
    '8.2'
];

// Path to the PHP script to test
$scriptPath = 'path/to/your/script.php';

// Function to test PHP script compatibility
function testPhpVersionCompatibility($scriptPath, $phpVersion) {
    // Command to execute the PHP script with the specified version
    $command = "php{$phpVersion} -l " . escapeshellarg($scriptPath);
    
    // Execute the command and capture the output and return status
    exec($command, $output, $returnVar);
    
    // Check for errors in the output
    if ($returnVar !== 0) {
        // Return error message if the script is not compatible
        return [
            'version' => $phpVersion,
            'status' => 'incompatible',
            'message' => implode("\n", $output)
        ];
    }
    
    // Return success message if the script is compatible
    return [
        'version' => $phpVersion,
        'status' => 'compatible',
        'message' => 'No syntax errors detected.'
    ];
}

// Array to hold results
$results = [];

// Loop through each PHP version and test compatibility
foreach ($phpVersions as $version) {
    $results[] = testPhpVersionCompatibility($scriptPath, $version);
}

// Output the results
foreach ($results as $result) {
    echo "PHP Version: {$result['version']} - Status: {$result['status']}\n";
    echo "Message: {$result['message']}\n\n";
}

?>
```
