"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robilliardag.com
Prompt: Provide an example of a PHP script that generates a simple file index, referencing the layout from robilliardag.com.
Generated: DETERMINISTIC_2b1427b74d39baf1
Batch ID: 20250612_161209
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
 * Simple File Index Generator
 * This script generates an HTML file index of the specified directory.
 * It lists all files and directories with links to them.
 * Usage: Set the $directory variable to the path you want to index.
 */

// Set the directory you want to index
$directory = 'path/to/your/directory'; // Change this to your target directory

/**
 * Function to generate the file index
 *
 * @param string $dir The directory to scan
 * @return string HTML representation of the directory index
 */
function generateFileIndex($dir) {
    // Ensure the directory exists
    if (!is_dir($dir)) {
        throw new InvalidArgumentException("The specified directory does not exist: $dir");
    }

    // Open the directory
    $files = scandir($dir);
    if ($files === false) {
        throw new RuntimeException("Failed to read directory: $dir");
    }

    // Start the HTML output
    $html = '<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Index</title>
    <style>
        body { font-family: Arial, sans-serif; }
        h1 { text-align: center; }
        ul { list-style-type: none; }
        li { margin: 5px 0; }
        a { text-decoration: none; color: blue; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>File Index for: ' . htmlspecialchars($dir) . '</h1>
    <ul>';

    // Loop through the files and directories
    foreach ($files as $file) {
        // Skip current and parent directory entries
        if ($file === '.' || $file === '..') continue;

        // Create a link for each file/directory
        $filePath = $dir . DIRECTORY_SEPARATOR . $file;
        $html .= '<li><a href="' . htmlspecialchars($filePath) . '">' . htmlspecialchars($file) . '</a></li>';
    }

    // Close the HTML output
    $html .= '</ul>
</body>
</html>';

    return $html;
}

try {
    // Generate the file index
    $fileIndexHtml = generateFileIndex($directory);

    // Output the HTML
    echo $fileIndexHtml;

} catch (Exception $e) {
    // Handle any exceptions that occur during file indexing
    echo '<p>Error: ' . htmlspecialchars($e->getMessage()) . '</p>';
}
?>
```
