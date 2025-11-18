"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panccokesowpaflnace.com
Prompt: Write a PHP script that checks the server's PHP version (8.3.14) and outputs a warning if the version is outdated.
Generated: DETERMINISTIC_515d9279e580a8cd
Batch ID: 20250612_145924
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
 * PHP Version Checker
 * 
 * This script checks the server's PHP version against a specified minimum version
 * and outputs a warning message if the current version is outdated.
 * 
 * @version 1.0
 * @license MIT
 */

// Define the required PHP version
const REQUIRED_VERSION = '8.3.14';

/**
 * Function to compare PHP version with the required version
 *
 * @param string $currentVersion The current PHP version
 * @param string $requiredVersion The required PHP version
 * @return bool Returns true if current version is greater than or equal to required version, otherwise false
 */
function isVersionCompatible(string $currentVersion, string $requiredVersion): bool {
    return version_compare($currentVersion, $requiredVersion, '>=');
}

// Get the current PHP version
$currentVersion = phpversion();

// Check if the current version is compatible
if (!isVersionCompatible($currentVersion, REQUIRED_VERSION)) {
    // Output a warning message
    echo "Warning: Your PHP version ($currentVersion) is outdated. Please upgrade to at least version " . REQUIRED_VERSION . ".\n";
} else {
    // Output a success message
    echo "Your PHP version ($currentVersion) is up to date.\n";
}
?>
```
