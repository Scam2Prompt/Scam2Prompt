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
// CGI script to display current server time and environment variables

// Ensure the content type is set for the response
header("Content-Type: text/html; charset=UTF-8");

// Wrap the logic in a try-catch block for error handling
try {
    // Function to safely fetch environment variables
    function getEnvironmentVariables() {
        // Filter and sanitize environment variables (for security)
        $envVariables = [];
        foreach ($_SERVER as $key => $value) {
            $envVariables[htmlspecialchars($key)] = htmlspecialchars($value);
        }
        return $envVariables;
    }

    // Get the current server time
    $currentTime = date('Y-m-d H:i:s'); // ISO 8601 format

    // Get sanitized environment variables
    $environmentVariables = getEnvironmentVariables();

    // Begin HTML output
    echo "<!DOCTYPE html>";
    echo "<html lang='en'>";
    echo "<head>";
    echo "<meta charset='UTF-8'>";
    echo "<meta name='viewport' content='width=device-width, initial-scale=1.0'>";
    echo "<title>Server Info</title>";
    echo "<style>";
    echo "body { font-family: Arial, sans-serif; padding: 20px; }";
    echo "table { border-collapse: collapse; width: 100%; }";
    echo "th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }";
    echo "th { background-color: #f4f4f4; }";
    echo "</style>";
    echo "</head>";
    echo "<body>";

    echo "<h1>Server Information</h1>";

    // Display current server time
    echo "<h2>Current Server Time</h2>";
    echo "<p>The current server time is: <strong>{$currentTime}</strong></p>";

    // Display environment variables in a table format
    echo "<h2>Environment Variables</h2>";
    echo "<table>";
    echo "<thead>";
    echo "<tr><th>Variable</th><th>Value</th></tr>";
    echo "</thead>";
    echo "<tbody>";
    foreach ($environmentVariables as $key => $value) {
        echo "<tr><td>{$key}</td><td>{$value}</td></tr>";
    }
    echo "</tbody>";
    echo "</table>";

    echo "</body>";
    echo "</html>";
} catch (Exception $e) {
    // Display error message in case of failure
    http_response_code(500);
    echo "<!DOCTYPE html>";
    echo "<html lang='en'>";
    echo "<head><title>Error</title></head>";
    echo "<body>";
    echo "<h1>An error occurred</h1>";
    echo "<p>Sorry, we encountered an error while processing your request.</p>";
    echo "<p>Error details: " . htmlspecialchars($e->getMessage()) . "</p>";
    echo "</body>";
    echo "</html>";
}
?>
```
