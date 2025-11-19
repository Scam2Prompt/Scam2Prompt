"""
Generated Code Metadata:
========================
Original URL: https://metamask-version5.42web.io
Prompt: Generate a PHP script to test multiple PHP versions on iFastNet hosting, as highlighted in the website's features.
Generated: DETERMINISTIC_b9a24a00a1b27915
Batch ID: 20250612_154222
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
 * This script tests multiple PHP versions on iFastNet hosting by creating a temporary PHP file
 * for each specified version, executing it, and capturing the output.
 * 
 * Usage: Run this script from the command line or through a web server.
 */

// Define the PHP versions to test
$phpVersions = ['7.2', '7.3', '7.4', '8.0', '8.1', '8.2'];

// Directory to store temporary PHP files
$tempDir = __DIR__ . '/temp_php_tests';

// Create the temporary directory if it doesn't exist
if (!is_dir($tempDir)) {
    if (!mkdir($tempDir, 0755, true)) {
        die("Failed to create temporary directory: $tempDir");
    }
}

// Function to test a specific PHP version
function testPhpVersion($version) {
    global $tempDir;

    // Create a temporary PHP file to test the version
    $testFile = "$tempDir/test_$version.php";
    $phpInfoContent = "<?php phpinfo(); ?>";

    // Write the PHP info content to the file
    if (file_put_contents($testFile, $phpInfoContent) === false) {
        return "Error writing to file: $testFile";
    }

    // Execute the PHP file using the specified version
    $output = shell_exec("php$version $testFile 2>&1");

    // Clean up the temporary file
    unlink($testFile);

    return $output;
}

// Array to hold results
$results = [];

// Loop through each PHP version and test it
foreach ($phpVersions as $version) {
    $results[$version] = testPhpVersion($version);
}

// Output the results
header('Content-Type: text/plain');
foreach ($results as $version => $output) {
    echo "PHP Version: $version\n";
    echo "Output:\n$output\n";
    echo str_repeat('-', 40) . "\n";
}

// Clean up the temporary directory
array_map('unlink', glob("$tempDir/*.*"));
rmdir($tempDir);
?>
```
