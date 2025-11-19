"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-protocol.42web.io
Prompt: How can I configure multiple PHP versions on iFastNet's web hosting platform?
Generated: DETERMINISTIC_38ac6401554c1b18
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// This script demonstrates how to dynamically set the PHP version
// for specific web applications hosted on iFastNet's web hosting platform.

// Check if the required environment variable exists
if (!isset($_SERVER['PHPRC'])) {
    // If not set, define a default PHP version
    $_SERVER['PHPRC'] = '/usr/local/php74'; // Default PHP version (e.g., PHP 7.4)
}

// Function to set PHP version dynamically
function setPHPVersion(string $version): void
{
    // Define the mapping of PHP versions to their installation paths
    $phpVersions = [
        '7.4' => '/usr/local/php74',
        '8.0' => '/usr/local/php80',
        '8.1' => '/usr/local/php81',
        '8.2' => '/usr/local/php82',
    ];

    // Validate the provided PHP version
    if (!array_key_exists($version, $phpVersions)) {
        // Throw an exception if the PHP version is invalid
        throw new InvalidArgumentException("Invalid PHP version specified: $version. Supported versions are: " . implode(', ', array_keys($phpVersions)));
    }

    // Set the environment variable to point to the correct PHP version path
    $_SERVER['PHPRC'] = $phpVersions[$version];
}

try {
    // Example usage: Setting the PHP version to 8.1 for the current application
    setPHPVersion('8.1');

    // Output the current PHP version to verify
    echo "PHP version configured successfully. Current PHP path: " . $_SERVER['PHPRC'] . PHP_EOL;

    // Test by displaying the PHP version using the 'phpversion()' function
    echo "PHP version reported by server: " . phpversion() . PHP_EOL;

} catch (Exception $e) {
    // Handle any errors that occur
    echo "Error: " . $e->getMessage() . PHP_EOL;
}
?>
```
