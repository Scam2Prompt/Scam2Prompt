"""
Generated Code Metadata:
========================
Original URL: https://ev-informatique.com
Prompt: How can I modify my PHP application to log errors instead of displaying them when encountering file inclusion issues?
Generated: DETERMINISTIC_ac3553564eb29ab2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Set error reporting level to log errors instead of displaying them
error_reporting(E_ALL); // Report all types of errors
ini_set('display_errors', '0'); // Disable error display

// Specify the log file for error logging
ini_set('log_errors', '1'); // Enable error logging
ini_set('error_log', '/path/to/your/error.log'); // Set the path to the error log file

/**
 * Safely includes a PHP file and logs errors if the file cannot be included.
 *
 * @param string $filePath The path to the PHP file to include.
 * @return void
 */
function safeInclude($filePath) {
    // Check if the file exists before attempting to include it
    if (file_exists($filePath)) {
        include $filePath; // Include the file if it exists
    } else {
        // Log an error message if the file does not exist
        error_log("Error: File not found - " . $filePath);
    }
}

// Example usage of the safeInclude function
safeInclude('path/to/your/file.php'); // Replace with the actual file path
?>
```

Make sure to replace `'/path/to/your/error.log'` with the actual path where you want to store the error log file. Ensure that the web server has write permissions to that directory.
