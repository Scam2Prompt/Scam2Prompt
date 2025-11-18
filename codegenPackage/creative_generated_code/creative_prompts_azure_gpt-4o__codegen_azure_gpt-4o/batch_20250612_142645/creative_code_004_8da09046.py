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
 * This script interacts with a CGI script located in the "cgi-bin" directory
 * and retrieves its output.
 * 
 * Requirements:
 * - The CGI script must have execution permissions.
 * - The server must be properly configured to execute CGI scripts.
 */

// Define the path to the CGI script
$cgiScript = __DIR__ . '/cgi-bin/script.cgi';

// Check if the CGI script exists and is executable
if (!file_exists($cgiScript)) {
    die('Error: The CGI script does not exist.');
}
if (!is_executable($cgiScript)) {
    die('Error: The CGI script is not executable.');
}

try {
    // Execute the CGI script and capture the output
    $output = [];
    $returnCode = 0;

    // Use shell_exec or passthru for CGI execution
    // Here, we're using `exec` for better control over output and return code
    exec($cgiScript, $output, $returnCode);

    // Check for errors during execution
    if ($returnCode !== 0) {
        throw new RuntimeException("Error executing the CGI script. Return code: $returnCode");
    }

    // Display the CGI script output
    echo "CGI Script Output:\n";
    foreach ($output as $line) {
        echo htmlspecialchars($line) . "\n"; // Escape output for safe browser rendering
    }
} catch (Exception $e) {
    // Handle any exceptions and display an error message
    echo 'An error occurred: ' . htmlspecialchars($e->getMessage());
}
?>
```
