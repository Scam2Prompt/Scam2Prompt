"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.com-live.org
Prompt: Generate a script in PHP to retrieve and display the contents of `key.php` from a directory listing served by Apache/2.4.52 on Ubuntu.
Generated: DETERMINISTIC_96e460225b9fda79
Batch ID: 20250612_155006
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
 * Script to retrieve and display the contents of key.php
 * from a specified directory. This is intended to be 
 * run on an Apache server.
 * 
 * Important: Ensure appropriate permissions and security 
 * measures are in place to prevent unauthorized access 
 * to sensitive files.
 */

// Define the path to the directory containing key.php
$directoryPath = '/path/to/your/directory'; // Change this to the actual path

// Define the full path to key.php
$keyFilePath = $directoryPath . '/key.php';

// Check if the file exists
if (!file_exists($keyFilePath)) {
    // Log error and return a user-friendly message
    error_log("File not found: " . $keyFilePath);
    die("Error: The requested file does not exist.");
}

// Check if the file is readable
if (!is_readable($keyFilePath)) {
    // Log error and return a user-friendly message
    error_log("File not readable: " . $keyFilePath);
    die("Error: The requested file is not readable.");
}

// Retrieve the contents of the file
try {
    $fileContents = file_get_contents($keyFilePath);

    // Check if the contents were successfully retrieved
    if ($fileContents === false) {
        throw new Exception("Failed to read the file contents.");
    }

    // Display the contents with proper HTML escaping
    echo "<pre>" . htmlspecialchars($fileContents) . "</pre>";
} catch (Exception $e) {
    // Log the exception message and return a user-friendly message
    error_log($e->getMessage());
    die("An error occurred while retrieving the file contents.");
}
?>
```
