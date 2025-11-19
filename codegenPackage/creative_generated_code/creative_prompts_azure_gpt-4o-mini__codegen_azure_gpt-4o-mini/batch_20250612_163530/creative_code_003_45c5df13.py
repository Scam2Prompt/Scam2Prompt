"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-zendesk.rf.gd
Prompt: Create a configuration example for using multiple versions of PHP on iFastNet Web Hosting.
Generated: DETERMINISTIC_45c5df131b93f252
Batch ID: 20250612_163530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configuration for using multiple PHP versions on iFastNet Web Hosting

// Define an array to hold the available PHP versions
$phpVersions = [
    '7.2' => 'PHP 7.2',
    '7.3' => 'PHP 7.3',
    '7.4' => 'PHP 7.4',
    '8.0' => 'PHP 8.0',
    '8.1' => 'PHP 8.1',
];

// Function to set the PHP version for a specific directory
/**
 * Sets the PHP version for the specified directory.
 *
 * @param string $version The PHP version to set.
 * @param string $directory The path to the directory.
 * @return void
 * @throws InvalidArgumentException If the PHP version is not supported.
 */
function setPhpVersion($version, $directory)
{
    global $phpVersions;

    // Check if the requested PHP version is supported
    if (!array_key_exists($version, $phpVersions)) {
        throw new InvalidArgumentException("Unsupported PHP version: " . $version);
    }

    // Create the .user.ini file to set the PHP version
    $filePath = rtrim($directory, '/') . '/.user.ini';

    // Write the selected PHP version to the .user.ini file
    file_put_contents($filePath, "extension=php_$version.ini");

    // Provide feedback to the user
    echo "PHP version $version has been set for directory: $directory\n";
}

// Example usage
try {
    // Set PHP version for the specified directory
    setPhpVersion('7.4', '/home/username/public_html');
    setPhpVersion('8.0', '/home/username/public_html/projectA');
    setPhpVersion('7.3', '/home/username/public_html/projectB');
} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
