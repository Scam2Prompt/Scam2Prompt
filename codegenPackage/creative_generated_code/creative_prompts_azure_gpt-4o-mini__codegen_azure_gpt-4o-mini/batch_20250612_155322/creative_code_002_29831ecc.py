"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://world-liberty-financial.alnagi-group.com
Prompt: Write a code snippet to serve files from a directory index using PHP on a LiteSpeed Web Server.
Generated: DETERMINISTIC_29831eccea701fe7
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
// Set the content type to HTML
header("Content-Type: text/html; charset=UTF-8");

// Directory to serve files from
$directory = 'files/'; // Ensure the directory exists and is accessible

// Check if the directory exists
if (!is_dir($directory)) {
    // Send a 404 Not Found response if the directory doesn't exist
    http_response_code(404);
    echo "<h1>404 Not Found</h1>";
    echo "<p>The requested directory does not exist.</p>";
    exit;
}

// Get list of files in the directory
$files = scandir($directory);

// Filter out the current and parent directory symbols
$files = array_diff($files, array('.', '..'));

// Begin HTML output
echo "<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Directory Index</title>
    <style>
        body { font-family: Arial, sans-serif; }
        h1 { text-align: center; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 10px 0; }
        a { text-decoration: none; color: #007BFF; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Directory Index</h1>
    <ul>";

// Loop through files and create list items
foreach ($files as $file) {
    // Create a safe URL-encoded link to the file
    $filePath = htmlspecialchars($directory . $file);
    echo "<li><a href='{$filePath}'>{$file}</a></li>";
}

// End HTML output
echo "    </ul>
</body>
</html>";
?>
```

**Note:** Ensure that the directory specified in `$directory` exists and is properly set with the necessary permissions for the web server to read its contents. This script serves files in a simple HTML format and includes error handling for cases where the directory does not exist.
