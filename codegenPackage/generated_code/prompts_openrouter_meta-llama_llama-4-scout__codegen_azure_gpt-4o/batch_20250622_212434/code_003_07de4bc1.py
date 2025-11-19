"""
Generated Code Metadata:
========================
Original URL: https://wombat-exchange.rf.gd
Prompt: Generate a PHP code snippet that demonstrates how to configure and use multiple versions of PHP on iFastNet Web Hosting.
Generated: DETERMINISTIC_07de4bc149f556f8
Batch ID: 20250622_212434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// This script demonstrates how to configure and use multiple PHP versions on iFastNet Web Hosting.

// Check the current PHP version
echo "Current PHP Version: " . phpversion() . PHP_EOL;

// Example of using a specific PHP version for a script
// iFastNet allows you to configure PHP versions via .htaccess or cPanel.
// Below is an example of how to set PHP version in .htaccess:

/*
# Add the following lines to your .htaccess file in the root directory of your website:

# Use PHP 7.4
AddHandler application/x-httpd-php74 .php

# OR Use PHP 8.1
AddHandler application/x-httpd-php81 .php

# Note: Replace '74' or '81' with the desired PHP version supported by iFastNet.
*/

// To demonstrate, let's execute a PHP script that works across multiple versions.
try {
    // Example function to demonstrate compatibility
    function demonstratePHPCompatibility() {
        // Use a feature available in PHP 7.4+
        $array = ['a' => 1, 'b' => 2, 'c' => 3];
        $filteredArray = array_filter($array, fn($value) => $value > 1); // Arrow function (PHP 7.4+)
        echo "Filtered Array: ";
        print_r($filteredArray);

        // Use a feature available in PHP 8.0+
        if (version_compare(PHP_VERSION, '8.0.0', '>=')) {
            $str = "Hello, World!";
            echo "String contains 'World': " . (str_contains($str, 'World') ? 'Yes' : 'No') . PHP_EOL; // str_contains (PHP 8.0+)
        } else {
            echo "PHP 8.0+ features are not available on this server." . PHP_EOL;
        }
    }

    // Call the function
    demonstratePHPCompatibility();
} catch (Exception $e) {
    // Handle any unexpected errors
    echo "An error occurred: " . $e->getMessage() . PHP_EOL;
}
?>
```
