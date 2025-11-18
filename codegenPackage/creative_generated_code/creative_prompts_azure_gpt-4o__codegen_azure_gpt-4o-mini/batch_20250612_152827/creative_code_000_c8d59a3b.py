"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imaginrayones.com
Prompt: Write a script using Plesk's FastCGI test page to verify server-side scripting functionality for a web application.
Generated: DETERMINISTIC_c8d59a3b6a8d3160
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// fastcgi_test.php

/**
 * FastCGI Test Page
 * 
 * This script is designed to verify the server-side scripting functionality
 * for web applications hosted on a Plesk server using FastCGI. It outputs
 * relevant PHP configuration information and tests for basic script execution.
 */

// Set the content type to text/html
header('Content-Type: text/html; charset=utf-8');

// Function to display server and PHP information
function displayInfo() {
    // Output a header
    echo '<h1>FastCGI Test Page</h1>';
    echo '<p>This page verifies server-side scripting functionality.</p>';

    // Display PHP version
    echo '<h2>PHP Version</h2>';
    echo '<p>' . phpversion() . '</p>';

    // Display server information
    echo '<h2>Server Information</h2>';
    echo '<p>' . htmlspecialchars($_SERVER['SERVER_SOFTWARE']) . '</p>';
    echo '<p>' . htmlspecialchars($_SERVER['SERVER_NAME']) . '</p>';
    echo '<p>' . htmlspecialchars($_SERVER['REQUEST_URI']) . '</p>';
    
    // Display loaded PHP modules
    echo '<h2>Loaded PHP Modules</h2>';
    echo '<ul>';
    foreach (get_loaded_extensions() as $extension) {
        echo '<li>' . htmlspecialchars($extension) . '</li>';
    }
    echo '</ul>';
}

// Function to handle errors
function handleError($errno, $errstr, $errfile, $errline) {
    // Log the error details
    error_log("Error [$errno]: $errstr in $errfile on line $errline", 0);
    
    // Display a user-friendly error message
    echo '<h2>Error Occurred</h2>';
    echo '<p>We encountered a technical issue. Please try again later.</p>';
}

// Set custom error handler
set_error_handler("handleError");

// Start output buffering
ob_start();

// Display information
displayInfo();

// Flush the output buffer and send output to the browser
ob_end_flush();

?>
```

Make sure to save this code in a file named `fastcgi_test.php` on your Plesk server and access it via your web browser to verify the server-side scripting functionality.
