"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://360fuel.network
Prompt: Create a script in PHP to dynamically generate an index page for a directory listing, inspired by the structure at https://360fuel.network.
Generated: DETERMINISTIC_d2f72a2a4e3dacc6
Batch ID: 20250612_154138
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
 * Directory Index Generator
 * This script dynamically generates an index page for a directory listing.
 * It lists all files and directories within the specified path, formatted as HTML.
 */

// Set the target directory (change this to the directory you want to list)
$directory = './'; // Current directory

// Function to scan the directory and generate HTML
function generateDirectoryIndex($dir) {
    // Check if the directory exists
    if (!is_dir($dir)) {
        http_response_code(404);
        echo "<h1>404 Not Found</h1>";
        echo "<p>The directory does not exist.</p>";
        return;
    }

    // Open the directory
    $files = scandir($dir);

    // Start outputting HTML
    echo "<!DOCTYPE html>";
    echo "<html lang='en'>";
    echo "<head>";
    echo "<meta charset='UTF-8'>";
    echo "<meta name='viewport' content='width=device-width, initial-scale=1.0'>";
    echo "<title>Directory Index of $dir</title>";
    echo "<style>";
    echo "body { font-family: Arial, sans-serif; margin: 20px; }";
    echo "h1 { color: #333; }";
    echo "ul { list-style-type: none; padding: 0; }";
    echo "li { margin: 5px 0; }";
    echo "a { text-decoration: none; color: #0066cc; }";
    echo "a:hover { text-decoration: underline; }";
    echo "</style>";
    echo "</head>";
    echo "<body>";
    echo "<h1>Directory Index of $dir</h1>";
    echo "<ul>";

    // Loop through each item in the directory
    foreach ($files as $file) {
        // Ignore '.' and '..' entries
        if ($file === '.' || $file === '..') {
            continue;
        }

        // Determine if the item is a file or a directory
        $fullPath = $dir . '/' . $file;
        if (is_dir($fullPath)) {
            // Output directory link
            echo "<li><a href='" . htmlspecialchars($file) . "'>📁 $file</a></li>";
        } else {
            // Output file link
            echo "<li><a href='" . htmlspecialchars($file) . "'>📄 $file</a></li>";
        }
    }

    echo "</ul>";
    echo "</body>";
    echo "</html>";
}

// Call the function to generate the directory index
generateDirectoryIndex($directory);
?>
```
