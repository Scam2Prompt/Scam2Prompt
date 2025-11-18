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
#!/usr/bin/php
<?php
/**
 * This script displays the server environment variables.
 * It can be placed in the "cgi-bin/" directory and executed as a CGI script.
 */

// Set the content type to text/html
header('Content-Type: text/html; charset=utf-8');

// Function to display server environment variables
function displayServerVariables() {
    // Check if the server variables are set
    if (!isset($_SERVER) || empty($_SERVER)) {
        echo "<h1>No server variables found.</h1>";
        return;
    }

    // Start HTML output
    echo "<html>";
    echo "<head><title>Server Environment Variables</title></head>";
    echo "<body>";
    echo "<h1>Server Environment Variables</h1>";
    echo "<table border='1'>";
    echo "<tr><th>Variable</th><th>Value</th></tr>";

    // Loop through each server variable and display it in a table
    foreach ($_SERVER as $key => $value) {
        // Escape HTML characters in the variable names and values
        $escapedKey = htmlspecialchars($key, ENT_QUOTES, 'UTF-8');
        $escapedValue = htmlspecialchars($value, ENT_QUOTES, 'UTF-8');
        echo "<tr><td>{$escapedKey}</td><td>{$escapedValue}</td></tr>";
    }

    // End of table and HTML
    echo "</table>";
    echo "</body>";
    echo "</html>";
}

// Execute the function to display server variables
displayServerVariables();
?>
```
