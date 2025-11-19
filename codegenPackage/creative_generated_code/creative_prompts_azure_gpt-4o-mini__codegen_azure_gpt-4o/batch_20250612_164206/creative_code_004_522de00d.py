"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-rewards.is-great.net
Prompt: What are the steps to utilize multiple versions of PHP on iFastNet Web Hosting? Provide a code example.
Generated: DETERMINISTIC_522de00db72e4a6c
Batch ID: 20250612_164206
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
 * PHP version switching script for iFastNet Web Hosting
 * This script demonstrates how to utilize multiple versions of PHP
 * by configuring your .htaccess file appropriately.
 *
 * Steps:
 * 1. Identify the PHP versions available on your iFastNet hosting through the control panel.
 * 2. Modify or create a `.htaccess` file in the root directory of your site.
 * 3. Add the directive to specify the PHP version you wish to use for your application.
 *
 * Note: This script itself won't switch PHP versions but provides
 * the directive example for `.htaccess`.
 */

// Example code to be added in your .htaccess file:

/*
# Start of PHP Version Selection

# To use PHP 7.4
AddHandler application/x-httpd-php74 .php

# To use PHP 8.0
# AddHandler application/x-httpd-php80 .php

# To use PHP 8.1
# AddHandler application/x-httpd-php81 .php

# End of PHP Version Selection
*/

/**
 * Testing PHP version in the application
 * This script can be uploaded to the server to check the active PHP version.
 */
try {
    // Output the currently active PHP version
    echo "Current PHP version: " . phpversion();
} catch (Exception $e) {
    // Handle potential errors gracefully
    echo "An error occurred while fetching the PHP version: " . $e->getMessage();
    error_log($e->getMessage()); // Log the error for debugging
}
?>
```
