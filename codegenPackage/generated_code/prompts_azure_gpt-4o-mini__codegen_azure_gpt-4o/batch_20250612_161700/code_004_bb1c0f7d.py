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
 * Sanitizes a file name and creates an HTML file on the server.
 *
 * @param string $fileName The desired file name (unsanitized).
 * @param string $htmlContent The HTML content to write into the file.
 * @return string|null Returns the path to the created file, or null on failure.
 */
function createSanitizedHtmlFile(string $fileName, string $htmlContent): ?string
{
    try {
        // Sanitize the file name by removing invalid characters and ensuring a safe format
        $sanitizedFileName = preg_replace('/[^a-zA-Z0-9_\-\.]/', '', $fileName); // Remove invalid characters
        $sanitizedFileName = trim($sanitizedFileName); // Remove leading/trailing whitespace
        $sanitizedFileName = $sanitizedFileName ?: 'default'; // Fallback to 'default' if the name is empty
        $sanitizedFileName .= '.html'; // Ensure the file has an .html extension

        // Define the directory where the file will be saved
        $directory = __DIR__ . '/html_files/';
        if (!is_dir($directory)) {
            // Create the directory if it doesn't exist
            if (!mkdir($directory, 0755, true)) {
                throw new Exception('Failed to create directory: ' . $directory);
            }
        }

        // Full path to the file
        $filePath = $directory . $sanitizedFileName;

        // Write the HTML content to the file
        if (file_put_contents($filePath, $htmlContent) === false) {
            throw new Exception('Failed to write content to file: ' . $filePath);
        }

        // Return the path to the created file
        return $filePath;
    } catch (Exception $e) {
        // Log the error message (in production, use a logging library)
        error_log($e->getMessage());
        return null; // Return null on failure
    }
}

// Example usage
$htmlContent = '<!DOCTYPE html>
<html>
<head>
    <title>Pizza Cone</title>
</head>
<body>
    <h1>Welcome to Pizza Cone!</h1>
    <p>Delicious pizza in a cone shape.</p>
</body>
</html>';

$filePath = createSanitizedHtmlFile('pizza_cone', $htmlContent);

if ($filePath) {
    echo "HTML file created successfully: $filePath";
} else {
    echo "Failed to create HTML file.";
}
?>
```
