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
 * Sanitizes a file name to remove unsafe characters and generates an HTML file on the server.
 * This function is production-ready, handles errors, and ensures the file name is safe.
 *
 * @param string $fileName The desired file name.
 * @param string $htmlContent The HTML content to be written into the file.
 * @return string|bool Returns the path to the generated file on success, or false on failure.
 */
function createSanitizedHtmlFile($fileName, $htmlContent) {
    // Define the directory where files will be created
    $directory = __DIR__ . '/html_files/';
    
    // Ensure the directory exists; create if not
    if (!is_dir($directory)) {
        if (!mkdir($directory, 0755, true)) {
            error_log('Failed to create directory: ' . $directory);
            return false; // Return false if directory creation fails
        }
    }

    // Sanitize the file name by removing unsafe characters
    $sanitizedFileName = preg_replace('/[^a-zA-Z0-9_\.-]/', '_', $fileName);

    // Prevent empty file names after sanitization
    if (empty($sanitizedFileName)) {
        error_log('Sanitized file name is empty.');
        return false; // Return false if the file name becomes empty
    }

    // Append .html extension to the sanitized file name
    $sanitizedFileName .= '.html';

    // Full path for the generated file
    $filePath = $directory . $sanitizedFileName;

    // Write the HTML content to the file
    if (file_put_contents($filePath, $htmlContent) === false) {
        error_log('Failed to write HTML content to file: ' . $filePath);
        return false; // Return false if file writing fails
    }

    // Return the file path of the created HTML file
    return $filePath;
}

// Example usage
$htmlContent = "<!DOCTYPE html>\n<html>\n<head>\n<title>Example</title>\n</head>\n<body>\n<p>Hello, world!</p>\n</body>\n</html>";
$filePath = createSanitizedHtmlFile('example-file!@#', $htmlContent);

if ($filePath) {
    echo "HTML file created successfully: $filePath";
} else {
    echo "Failed to create HTML file.";
}

?>
```
