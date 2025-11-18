"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wombat-exchange.rf.gd
Prompt: Write a script to test multiple versions of PHP on iFastNet hosting and explain how to switch between PHP versions using their cPanel.
Generated: DETERMINISTIC_73b7ca98157db056
Batch ID: 20250612_145200
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
 * Script to test different PHP versions on iFastNet hosting.
 * 
 * This script checks the current PHP version and displays it.
 * It can be used as a basis for testing code compatibility across different PHP versions.
 * 
 * Usage:
 * 1. Upload this script to your iFastNet hosting.
 * 2. Access the script via your web browser to see the PHP version.
 */

// Set error reporting for development
error_reporting(E_ALL);
ini_set('display_errors', 1);

/**
 * Function to get the current PHP version and display it.
 *
 * @return void
 */
function displayPhpVersion() {
    // Fetch the current PHP version
    $phpVersion = phpversion();
    
    // Display the PHP version
    echo "<h1>Current PHP Version: $phpVersion</h1>";
}

// Function to test specific PHP functionality
/**
 * Function to perform a simple test of PHP features.
 *
 * @return void
 */
function runPhpTests() {
    // Check if the 'json_encode' function exists (Available in PHP 5.2.0 and later)
    if (function_exists('json_encode')) {
        $array = ['key' => 'value'];
        $jsonOutput = json_encode($array);
        echo "<p>JSON Encode Test: " . htmlspecialchars($jsonOutput) . "</p>";
    } else {
        echo "<p>JSON Encode function is not available in this PHP version.</p>";
    }

    // Check if the 'mysqli_connect' function exists (Available in PHP 5.0.0 and later)
    if (function_exists('mysqli_connect')) {
        echo "<p>MySQLi is available in this PHP version.</p>";
    } else {
        echo "<p>MySQLi function is not available in this PHP version.</p>";
    }
}

// Execute the functions to display PHP version and run tests
displayPhpVersion();
runPhpTests();
?>
```

### Instructions for Switching PHP Versions in iFastNet cPanel

1. **Login to your iFastNet cPanel**: Use your credentials to access your hosting account.
  
2. **Locate the PHP Selector**: In the cPanel dashboard, look for an option labeled "Select PHP Version" or "PHP Configuration".

3. **Select the Desired Version**: In the PHP Selector, you will see a dropdown menu or a list of available PHP versions. Choose the version you wish to switch to.

4. **Apply Changes**: After selecting the desired PHP version, make sure to click the "Save" or "Apply" button to confirm your changes.

5. **Verify the Version**: You can use the provided PHP script to verify that the new PHP version is active by accessing it through your web browser.
