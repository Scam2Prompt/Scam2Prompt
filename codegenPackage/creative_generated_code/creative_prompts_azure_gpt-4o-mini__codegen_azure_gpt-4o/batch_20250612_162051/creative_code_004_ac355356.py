"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ev-informatique.com
Prompt: How can I modify my PHP application to log errors instead of displaying them when encountering file inclusion issues?
Generated: DETERMINISTIC_ac3553564eb29ab2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Enable error reporting for development purposes during debugging phase
error_reporting(E_ALL);

// Set custom error handler to log errors instead of displaying them
set_error_handler(function ($errno, $errstr, $errfile, $errline) {
    // Log the error to a file
    $logMessage = "[" . date("Y-m-d H:i:s") . "] Error: ${errstr} in ${errfile} on line ${errline}" . PHP_EOL;
    error_log($logMessage, 3, __DIR__ . '/error_log.txt');

    // Prevent the PHP default error handler from running
    return true;
});

// Function to safely include files
function safeInclude($filePath) {
    if (file_exists($filePath)) {
        include $filePath;
    } else {
        // Trigger a custom PHP warning if the file doesn't exist
        trigger_error("File not found: $filePath", E_USER_WARNING);
    }
}

// Example usage
safeInclude('somefile.php');

// Restore the previous error handler when done (optional)
restore_error_handler();
?>
```
