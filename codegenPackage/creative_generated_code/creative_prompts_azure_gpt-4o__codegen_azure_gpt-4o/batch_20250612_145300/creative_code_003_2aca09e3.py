"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://siemensgamesare.great-site.net
Prompt: Write a PHP script to test compatibility with multiple PHP versions on a hosting service that includes free domain names and unlimited disk space, such as iFastNet.
Generated: DETERMINISTIC_2aca09e32a68f572
Batch ID: 20250612_145300
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
 * This script tests the compatibility of the hosting server's PHP environment
 * by retrieving and displaying the current PHP version and loaded extensions.
 * 
 * Author: Expert Programmer
 * Usage: Upload this script to the root directory of your hosting service and access it via a web browser.
 */

// Set appropriate headers
header('Content-Type: text/plain; charset=utf-8');

// Function to safely print information
function safePrint($message) {
    echo $message . PHP_EOL;
}

try {
    // Display the current PHP version
    safePrint("PHP Version Compatibility Test");
    safePrint("==============================");
    safePrint("Current PHP Version: " . PHP_VERSION);

    // Check if the hosting service allows unlimited disk space (iFastNet may claim this, but it's worth verifying)
    $unlimitedDiskSpaceMessage = disk_free_space("/") === false ? "Unable to determine free disk space." : "Disk space check passed (unlimited claim is not verifiable programmatically).";
    safePrint($unlimitedDiskSpaceMessage);

    // List all loaded PHP extensions
    safePrint("\nLoaded PHP Extensions:");
    $extensions = get_loaded_extensions();
    sort($extensions); // Sort the extensions alphabetically for readability
    foreach ($extensions as $extension) {
        safePrint(" - " . $extension);
    }

    // Test key PHP features for compatibility
    safePrint("\nFeature Compatibility Check:");
    safePrint(" - JSON Support: " . (function_exists('json_encode') ? "Enabled" : "Not Available"));
    safePrint(" - cURL Support: " . (function_exists('curl_version') ? "Enabled" : "Not Available"));
    safePrint(" - PDO Support: " . (class_exists('PDO') ? "Enabled" : "Not Available"));
    safePrint(" - OpenSSL Support: " . (extension_loaded('openssl') ? "Enabled" : "Not Available"));

    // Display a final message
    safePrint("\nCompatibility test completed successfully.");
} catch (Exception $e) {
    // Handle any unexpected errors gracefully
    safePrint("\nAn error occurred during the compatibility test:");
    safePrint($e->getMessage());
}
?>
```
