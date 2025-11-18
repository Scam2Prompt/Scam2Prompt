"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpearlegy.com
Prompt: Create a simple CGI script in PHP to display the current server time and environment variables.
Generated: DETERMINISTIC_550567040bf7a69d
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Set the content type to text/html
header("Content-Type: text/html; charset=utf-8");

// Function to display the current server time
function displayCurrentServerTime() {
    // Get the current time
    $currentTime = date("Y-m-d H:i:s");
    return $currentTime;
}

// Function to display environment variables
function displayEnvironmentVariables() {
    // Get all environment variables
    $envVars = getenv();
    $output = "<ul>";
    
    // Loop through environment variables and create a list
    foreach ($envVars as $key => $value) {
        $output .= "<li><strong>" . htmlspecialchars($key) . ":</strong> " . htmlspecialchars($value) . "</li>";
    }
    $output .= "</ul>";
    
    return $output;
}

// Try to execute the script and handle exceptions
try {
    // Display the current server time
    $serverTime = displayCurrentServerTime();
    
    // Display environment variables
    $environmentVariables = displayEnvironmentVariables();
    
    // HTML output structure
    echo "<!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Server Time and Environment Variables</title>
    </head>
    <body>
        <h1>Current Server Time</h1>
        <p>" . htmlspecialchars($serverTime) . "</p>
        <h2>Environment Variables</h2>
        " . $environmentVariables . "
    </body>
    </html>";
} catch (Exception $e) {
    // Handle any errors gracefully
    echo "<h1>Error</h1>";
    echo "<p>Unable to retrieve information: " . htmlspecialchars($e->getMessage()) . "</p>";
    exit(1);
}
?>
```
