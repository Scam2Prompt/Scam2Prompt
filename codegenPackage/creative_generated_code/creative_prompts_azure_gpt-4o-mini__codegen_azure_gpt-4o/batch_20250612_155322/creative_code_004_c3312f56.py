"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://world-liberty-financial.alnagi-group.com
Prompt: What are the best practices for file management in a PHP application hosted on LiteSpeed?
Generated: DETERMINISTIC_c3312f563a256038
Batch ID: 20250612_155322
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
 * File Management Best Practices in a PHP Application Hosted on LiteSpeed
 *
 * This script demonstrates clean, efficient file management practices
 * for a PHP application. It includes file creation, reading, writing, 
 * and deletion with proper error handling and security measures.
 */

// Define file path constants
define('FILE_DIRECTORY', __DIR__ . '/files');
define('FILE_PATH', FILE_DIRECTORY . '/example.txt');

// Ensure the file directory exists, create it if it doesn't
if (!is_dir(FILE_DIRECTORY)) {
    if (!mkdir(FILE_DIRECTORY, 0755, true)) {
        die("Failed to create directory: " . FILE_DIRECTORY);
    }
}

// Function to write content to a file
function writeToFile($filePath, $content) {
    // Open the file for writing (create if not exists)
    $fileHandle = fopen($filePath, 'w');
    if (!$fileHandle) {
        throw new Exception("Failed to open file for writing: " . $filePath);
    }

    // Write content to the file
    if (fwrite($fileHandle, $content) === false) {
        fclose($fileHandle); // Close the file before throwing an error
        throw new Exception("Failed to write to file: " . $filePath);
    }

    fclose($fileHandle);
}

// Function to read content from a file
function readFromFile($filePath) {
    // Ensure the file exists
    if (!file_exists($filePath)) {
        throw new Exception("File does not exist: " . $filePath);
    }

    // Read and return the file contents
    $content = file_get_contents($filePath);
    if ($content === false) {
        throw new Exception("Failed to read file: " . $filePath);
    }

    return $content;
}

// Function to safely delete a file
function deleteFile($filePath) {
    // Ensure the file exists
    if (!file_exists($filePath)) {
        throw new Exception("File does not exist: " . $filePath);
    }

    // Delete the file
    if (!unlink($filePath)) {
        throw new Exception("Failed to delete file: " . $filePath);
    }
}

try {
    // Example usage of the file management functions

    // Write content to a file
    writeToFile(FILE_PATH, "This is an example file managed by PHP on LiteSpeed.");
    echo "File written successfully.\n";

    // Read the content from the file
    $content = readFromFile(FILE_PATH);
    echo "File content: " . $content . "\n";

    // Delete the file
    deleteFile(FILE_PATH);
    echo "File deleted successfully.\n";

} catch (Exception $e) {
    // Handle errors gracefully
    error_log($e->getMessage()); // Log the error for debugging
    echo "An error occurred: " . $e->getMessage();
}

?>
```
