"""
Generated Code Metadata:
========================
Original URL: https://phpm.ru
Prompt: How can I use the PEAR library in PHP to manage dependencies effectively?
Generated: DETERMINISTIC_c654f16633bcc568
Batch ID: 20250612_163103
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
 * This script demonstrates how to use the PEAR library in PHP
 * to manage dependencies effectively.
 */

// Include the PEAR autoloader
require_once 'PEAR.php';

/**
 * Function to install a PEAR package
 *
 * @param string $packageName The name of the PEAR package to install
 * @return void
 * @throws Exception If the package installation fails
 */
function installPearPackage($packageName) {
    // Check if the PEAR package is already installed
    $installedPackages = PEAR::listPackages();
    if (array_key_exists($packageName, $installedPackages)) {
        echo "Package '$packageName' is already installed.\n";
        return;
    }

    // Attempt to install the package
    $result = PEAR::install($packageName);
    if (PEAR::isError($result)) {
        throw new Exception("Failed to install package '$packageName': " . $result->getMessage());
    }

    echo "Package '$packageName' installed successfully.\n";
}

/**
 * Function to check if a PEAR package is installed
 *
 * @param string $packageName The name of the PEAR package to check
 * @return bool True if installed, false otherwise
 */
function isPackageInstalled($packageName) {
    $installedPackages = PEAR::listPackages();
    return array_key_exists($packageName, $installedPackages);
}

// Example usage
try {
    $packageName = 'Mail'; // Specify the PEAR package you want to manage

    // Check if the package is installed
    if (!isPackageInstalled($packageName)) {
        installPearPackage($packageName);
    } else {
        echo "Package '$packageName' is already installed.\n";
    }
} catch (Exception $e) {
    // Handle any exceptions that occur during package management
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
