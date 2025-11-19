"""
Generated Code Metadata:
========================
Original URL: https://bpearlegy.com
Prompt: Create a simple CGI script in PHP to display the current server time and environment variables.
Generated: DETERMINISTIC_550567040bf7a69d
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Set the content type to text/html
header("Content-Type: text/html");

// Start output buffering
ob_start();

// Function to display the current server time
function displayServerTime() {
    // Get the current server time
    $currentTime = date("Y-m-d H:i:s");
    return $currentTime;
}

// Function to display environment variables
function displayEnvironmentVariables() {
    // Get all environment variables
    $envVars = getenv();
    $output = "<ul>";
    foreach ($envVars as $key => $value) {
        $output .= "<li><strong>$key:</strong> $value</li>";
    }
    $output .= "</ul>";
    return $output;
}

// Main execution block
try {
    // Display the current server time
    $serverTime = displayServerTime();
    echo "<h1>Current Server Time</h1>";
    echo "<p>$serverTime</p>";

    // Display environment variables
    echo "<h2>Environment Variables</h2>";
    echo displayEnvironmentVariables();
} catch (Exception $e) {
    // Handle any exceptions and display an error message
    echo "<h2>Error</h2>";
    echo "<p>Unable to retrieve information: " . htmlspecialchars($e->getMessage()) . "</p>";
}

// Flush the output buffer and send output to the browser
ob_end_flush();
?>
```
