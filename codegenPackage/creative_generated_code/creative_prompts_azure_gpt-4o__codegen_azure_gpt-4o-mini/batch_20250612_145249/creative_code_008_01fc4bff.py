"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitkub-btc.free.nf
Prompt: Write a PHP script optimized for hosting environments with unlimited bandwidth and multiple PHP versions, as offered by iFastNet.
Generated: DETERMINISTIC_01fc4bff173e682c
Batch ID: 20250612_145249
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
 * Simple PHP application for displaying server information.
 * This script is optimized for hosting environments like iFastNet
 * that support multiple PHP versions and provide unlimited bandwidth.
 * 
 * PHP Version: 8.0 or higher
 */

// Set error reporting for development
error_reporting(E_ALL);
ini_set('display_errors', '1');

/**
 * Function to display server information
 * 
 * @return void
 */
function displayServerInfo() {
    echo "<h1>Server Information</h1>";
    echo "<h2>PHP Version: " . phpversion() . "</h2>";
    
    // Display server variables
    echo "<h3>Server Variables:</h3><pre>";
    print_r($_SERVER);
    echo "</pre>";
    
    // Display loaded PHP configuration
    echo "<h3>Loaded PHP Configuration:</h3>";
    echo "<pre>";
    echo phpinfo();
    echo "</pre>";
}

/**
 * Function to handle unexpected errors gracefully
 * 
 * @param int $errno The level of the error raised
 * @param string $errstr The error message
 * @param string $errfile The filename that the error was raised in
 * @param int $errline The line number the error was raised at
 * @return void
 */
function errorHandler($errno, $errstr, $errfile, $errline) {
    // Log error to a file
    error_log("Error [$errno]: $errstr in $errfile on line $errline", 3, 'error_log.txt');
    
    // Display user-friendly message
    echo "<h3>Oops! Something went wrong.</h3>";
    exit();
}

// Set custom error handler
set_error_handler("errorHandler");

// Run the server information display function
try {
    displayServerInfo();
} catch (Exception $e) {
    // Handle any exceptions that may occur
    errorHandler(E_ERROR, $e->getMessage(), $e->getFile(), $e->getLine());
}
?>
```

This PHP script is structured to be simple yet functional for displaying server information while implementing error handling and logging best practices.
