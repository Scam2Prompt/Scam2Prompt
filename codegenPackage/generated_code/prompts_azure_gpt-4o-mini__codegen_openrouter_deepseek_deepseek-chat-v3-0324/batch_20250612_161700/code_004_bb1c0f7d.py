"""
Generated Code Metadata:
========================
Original URL: https://pizzacone.ae
Prompt: Generate a PHP function that sanitizes file names and creates an HTML file on the server, referencing the method used in the pizzacone.ae content.
Generated: DETERMINISTIC_bb1c0f7df66fa76c
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Sanitizes a filename by removing or replacing invalid characters.
 *
 * @param string $filename The filename to sanitize
 * @return string The sanitized filename
 */
function sanitizeFilename(string $filename): string {
    // Remove any path information to prevent directory traversal
    $filename = basename($filename);
    
    // Replace spaces with underscores
    $filename = str_replace(' ', '_', $filename);
    
    // Remove any non-alphanumeric, underscore, hyphen, or dot characters
    $filename = preg_replace('/[^A-Za-z0-9_\-\.]/', '', $filename);
    
    // Remove multiple dots and keep only one
    $filename = preg_replace('/\.+/', '.', $filename);
    
    // Convert to lowercase for consistency
    $filename = strtolower($filename);
    
    return $filename;
}

/**
 * Creates an HTML file with the given content.
 *
 * @param string $filename The name of the file to create
 * @param string $content The HTML content to write to the file
 * @return bool True on success, false on failure
 * @throws Exception If file creation fails
 */
function createHtmlFile(string $filename, string $content): bool {
    $sanitizedFilename = sanitizeFilename($filename);
    
    // Ensure the filename ends with .html
    if (substr($sanitizedFilename, -5) !== '.html') {
        $sanitizedFilename .= '.html';
    }
    
    // Write the content to the file
    $result = file_put_contents($sanitizedFilename, $content);
    
    if ($result === false) {
        throw new Exception("Failed to create HTML file: {$sanitizedFilename}");
    }
    
    return true;
}

// Example usage:
try {
    $filename = "example file.html";
    $content = "<!DOCTYPE html><html><head><title>Example</title></head><body><h1>Hello World</h1></body></html>";
    
    if (createHtmlFile($filename, $content)) {
        echo "HTML file created successfully.";
    }
} catch (Exception $e) {
    error_log("Error: " . $e->getMessage());
    echo "An error occurred while creating the HTML file.";
}
?>
```
