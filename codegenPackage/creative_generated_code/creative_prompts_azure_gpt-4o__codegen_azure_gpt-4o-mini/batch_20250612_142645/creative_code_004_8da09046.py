"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syr-whistler.com
Prompt: Create a PHP script that interacts with a CGI script located in the "cgi-bin" directory and retrieves its output.
Generated: DETERMINISTIC_8da09046ed5eecf3
Batch ID: 20250612_142645
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
 * This PHP script interacts with a CGI script located in the "cgi-bin" directory
 * and retrieves its output.
 * 
 * @package CGIInteraction
 */

// Define the path to the CGI script
$cgiScript = __DIR__ . '/cgi-bin/example.cgi';

// Ensure the CGI script exists
if (!file_exists($cgiScript)) {
    // Log error and exit if the CGI script is not found
    error_log("CGI script not found: $cgiScript");
    die("Error: CGI script not found.");
}

// Set the necessary headers to indicate that the output is coming from a CGI script
header('Content-Type: text/plain');

// Execute the CGI script and capture its output
$output = [];
$returnVar = 0;

// Use escapeshellarg to safely pass the script path to the shell
exec(escapeshellarg($cgiScript), $output, $returnVar);

// Handle execution errors
if ($returnVar !== 0) {
    // Log error and show user-friendly message
    error_log("CGI script execution failed with return code: $returnVar");
    die("Error: Unable to retrieve data from the CGI script.");
}

// Output the CGI script's response
echo implode("\n", $output);
?>
```
