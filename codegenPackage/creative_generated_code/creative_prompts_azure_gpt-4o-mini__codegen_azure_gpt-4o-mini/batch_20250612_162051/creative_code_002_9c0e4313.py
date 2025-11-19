"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://londonce.com
Prompt: Can you provide a code snippet to check if a required file exists before using the require function in PHP?
Generated: DETERMINISTIC_9c0e43139d443d4d
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
/**
 * Checks if a required file exists before including it.
 *
 * @param string $filePath The path to the file to be included.
 * @throws Exception If the file does not exist.
 */
function requireFileIfExists($filePath) {
    // Check if the file exists
    if (!file_exists($filePath)) {
        // Throw an exception if the file is not found
        throw new Exception("Required file not found: " . $filePath);
    }
    
    // Safely require the file
    require $filePath;
}

// Example usage
try {
    // Specify the path to the required file
    $requiredFile = 'path/to/your/file.php';
    
    // Attempt to require the file
    requireFileIfExists($requiredFile);
    
    // File included successfully; proceed with your logic
} catch (Exception $e) {
    // Handle the exception (e.g., log the error, show a user-friendly message)
    error_log($e->getMessage());
    echo "An error occurred while including the file. Please check the logs.";
}
?>
```
