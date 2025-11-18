"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlayer.eigenda.cc
Prompt: Write a PHP script that interacts with a file named `key.php` on an Apache server running Ubuntu. Ensure the script includes secure handling of file operations.
Generated: DETERMINISTIC_f2586cdbddfec44d
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// key.php handler script

// Define the path to the key file
define('KEY_FILE', 'key.php');

// Function to read the key from the file securely
function readKeyFromFile($filePath) {
    // Check if the file exists and is readable
    if (!file_exists($filePath) || !is_readable($filePath)) {
        throw new Exception("File does not exist or is not readable: " . htmlspecialchars($filePath));
    }

    // Use file_get_contents to read the contents of the file
    $key = file_get_contents($filePath);

    // Ensure we handle potential errors during reading
    if ($key === false) {
        throw new Exception("Failed to read the file: " . htmlspecialchars($filePath));
    }

    // Return the key after trimming any whitespace
    return trim($key);
}

// Function to write a new key to the file securely
function writeKeyToFile($filePath, $key) {
    // Check if the key is a valid string
    if (!is_string($key) || empty($key)) {
        throw new InvalidArgumentException("Invalid key provided.");
    }

    // Securely write the key to the file
    // Use file_put_contents with FILE_APPEND flag to prevent data loss
    if (file_put_contents($filePath, $key) === false) {
        throw new Exception("Failed to write to the file: " . htmlspecialchars($filePath));
    }

    // Set appropriate permissions for security
    chmod($filePath, 0600); // Read/Write for owner only
}

// Exception handling
try {
    // Example: Read the key from the file
    $key = readKeyFromFile(KEY_FILE);
    echo "Key read successfully: " . htmlspecialchars($key) . "\n";

    // Example: Write a new key to the file (for demonstration)
    // You can replace 'new_secret_key' with the actual key you want to write
    writeKeyToFile(KEY_FILE, 'new_secret_key');
    echo "Key written successfully.\n";

} catch (Exception $e) {
    // Handle exceptions and output error message
    echo "Error: " . htmlspecialchars($e->getMessage()) . "\n";
}
```
