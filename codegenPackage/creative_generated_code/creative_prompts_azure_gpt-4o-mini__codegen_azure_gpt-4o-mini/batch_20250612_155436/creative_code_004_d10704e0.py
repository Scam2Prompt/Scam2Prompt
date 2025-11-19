"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nkftransporte.com
Prompt: How can I implement a lightweight web server in PHP that shows an index of files like the one on nkftransporte.com?
Generated: DETERMINISTIC_d10704e0342f0004
Batch ID: 20250612_155436
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
 * Simple Lightweight Web Server in PHP
 * This script will generate an index of files in the current directory.
 * It will serve as the main entry point for the server.
 */

// Set the content type to HTML
header('Content-Type: text/html; charset=utf-8');

/**
 * Function to generate the HTML for the file index
 * 
 * @param array $files An array of files to list
 * @return string HTML string containing the file list
 */
function generateFileList(array $files): string {
    $html = '<h1>File Index</h1>';
    $html .= '<ul>';

    foreach ($files as $file) {
        // Skip directories and hidden files
        if (is_dir($file) || strpos($file, '.') === 0) {
            continue;
        }

        // Escape the file name for safe display
        $fileName = htmlspecialchars($file);
        $html .= "<li><a href=\"$fileName\">$fileName</a></li>";
    }

    $html .= '</ul>';
    return $html;
}

/**
 * Main code execution
 */
try {
    // Get all files in the current directory
    $files = scandir('.');

    // Check if scanning the directory was successful
    if ($files === false) {
        throw new Exception('Failed to read the directory.');
    }

    // Generate the file list HTML
    $fileListHtml = generateFileList($files);

    // Output the complete HTML page
    echo <<<HTML
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>File Index</title>
        <style>
            body { font-family: Arial, sans-serif; }
            h1 { color: #333; }
            ul { list-style-type: none; padding: 0; }
            li { margin: 5px 0; }
            a { text-decoration: none; color: #007BFF; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        $fileListHtml
    </body>
    </html>
    HTML;

} catch (Exception $e) {
    // Handle any exceptions and display an error message
    echo '<h1>Error</h1>';
    echo '<p>' . htmlspecialchars($e->getMessage()) . '</p>';
}
?>
```
