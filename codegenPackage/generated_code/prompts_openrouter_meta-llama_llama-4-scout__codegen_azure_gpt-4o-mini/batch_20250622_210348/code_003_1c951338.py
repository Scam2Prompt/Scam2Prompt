"""
Generated Code Metadata:
========================
Original URL: https://imaginrayones.com
Prompt: Write a FastCGI test page using Plesk's test pages feature.
Generated: DETERMINISTIC_1c951338b07de6f5
Batch ID: 20250622_210348
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
 * FastCGI Test Page
 * 
 * This script serves as a test page for FastCGI using Plesk's test pages feature.
 * It demonstrates basic functionality and error handling.
 * 
 * @package FastCGI_Test_Page
 * @author Your Name
 * @version 1.0
 */

// Set the content type to HTML
header('Content-Type: text/html; charset=utf-8');

// Start output buffering to capture any errors
ob_start();

// Function to display a message
function displayMessage($message) {
    echo "<h1>FastCGI Test Page</h1>";
    echo "<p>$message</p>";
}

// Check if the script is running under FastCGI
if (php_sapi_name() === 'cgi-fcgi') {
    displayMessage("This script is running under FastCGI.");
} else {
    displayMessage("This script is NOT running under FastCGI.");
}

// Capture any output and check for errors
$output = ob_get_contents();
ob_end_clean();

// Check for errors in output
if ($output === false) {
    // Log the error (in a production environment, consider logging to a file or monitoring system)
    error_log("Error capturing output.");
    displayMessage("An error occurred while generating the output.");
} else {
    // Output the captured content
    echo $output;
}

// End of script
?>
```
