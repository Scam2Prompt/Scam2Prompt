"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defluo.hr
Prompt: Create a PHP script that can be placed in a "cgi-bin/" directory to display server environment variables.
Generated: DETERMINISTIC_c5cb3517a710c085
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
#!/usr/bin/env php
<?php
/**
 * A PHP script to display server environment variables.
 * This script can be placed in the "cgi-bin/" directory and executed as a CGI script.
 *
 * Requirements:
 * - Ensure the script has executable permissions (chmod +x script_name.php).
 * - Ensure the server is configured to execute PHP scripts as CGI.
 */

// Set the required headers for CGI response
header("Content-Type: text/html; charset=UTF-8");

try {
    // Start output buffering
    ob_start();

    // Display a simple HTML structure
    echo "<!DOCTYPE html>";
    echo "<html lang='en'>";
    echo "<head>";
    echo "<meta charset='UTF-8'>";
    echo "<meta name='viewport' content='width=device-width, initial-scale=1.0'>";
    echo "<title>Server Environment Variables</title>";
    echo "</head>";
    echo "<body>";
    echo "<h1>Server Environment Variables</h1>";
    echo "<table border='1' cellpadding='5' cellspacing='0'>";
    echo "<thead>";
    echo "<tr><th>Variable</th><th>Value</th></tr>";
    echo "</thead>";
    echo "<tbody>";

    // Iterate through the server environment variables
    foreach ($_SERVER as $key => $value) {
        // Escape output to prevent XSS
        $key = htmlspecialchars($key, ENT_QUOTES, 'UTF-8');
        $value = htmlspecialchars((is_array($value) ? json_encode($value) : $value), ENT_QUOTES, 'UTF-8');
        echo "<tr><td>{$key}</td><td>{$value}</td></tr>";
    }

    echo "</tbody>";
    echo "</table>";
    echo "</body>";
    echo "</html>";

    // End output buffering and flush content
    ob_end_flush();
} catch (Exception $e) {
    // Handle any unexpected errors gracefully
    header("Content-Type: text/plain; charset=UTF-8");

    // Log error (in production, logging to a file or monitoring system would be ideal)
    error_log("Error displaying environment variables: " . $e->getMessage());

    // Display user-friendly error message
    echo "An error occurred while processing your request. Please try again later.";
    exit(1);
}
```

Make sure the script file is executable (`chmod +x script_name.php`) and that your server is configured to allow PHP CGI scripts in the `cgi-bin/` directory.
