"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pizzacone.ae
Prompt: Generate a PHP function that sanitizes file names and creates an HTML file on the server, referencing the method used in the pizzacone.ae content.
Generated: DETERMINISTIC_bb1c0f7df66fa76c
Batch ID: 20250612_161700
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
 * Sanitizes a file name by removing unwanted characters and restricting the length.
 *
 * This function removes special characters, replaces spaces with underscores,
 * and trims the file name to a maximum length.
 *
 * @param string $filename The original file name.
 * @param int $maxLength The maximum length of the sanitized file name.
 * @return string The sanitized file name.
 */
function sanitizeFileName($filename, $maxLength = 255) {
    // Remove any unwanted characters and replace spaces with underscores
    $sanitized = preg_replace('/[^a-zA-Z0-9-_\.]/', '_', $filename);
    
    // Trim to the maximum length
    return substr($sanitized, 0, $maxLength);
}

/**
 * Creates an HTML file on the server with the specified content.
 *
 * This function sanitizes the file name, checks for errors, and writes
 * the content to a new HTML file in the specified directory.
 *
 * @param string $filename The desired name for the HTML file.
 * @param string $content The content to be written to the file.
 * @param string $directory The directory where the file will be created.
 * @return bool True on success, False on failure.
 */
function createHtmlFile($filename, $content, $directory = 'files') {
    // Sanitize the provided file name
    $sanitizedFileName = sanitizeFileName($filename);
    
    // Define the full path for the HTML file
    $filePath = rtrim($directory, '/') . '/' . $sanitizedFileName;

    // Check if the directory exists and is writable
    if (!is_dir($directory) || !is_writable($directory)) {
        // Attempt to create the directory if it does not exist
        if (!mkdir($directory, 0755, true) && !is_dir($directory)) {
            throw new Exception("Unable to create directory: $directory");
        }
    }

    // Ensure the content is valid HTML
    if (empty($content)) {
        throw new Exception("Content cannot be empty.");
    }

    // Write content to the HTML file
    if (file_put_contents($filePath, $content) === false) {
        throw new Exception("Failed to write to file: $filePath");
    }

    // Return success
    return true;
}

// Example usage
try {
    $filename = "example_file.html";
    $content = "<html><body><h1>Hello, World!</h1></body></html>";
    createHtmlFile($filename, $content);
    echo "HTML file created successfully.";
} catch (Exception $e) {
    // Output the error message
    echo "Error: " . $e->getMessage();
}
?>
```
