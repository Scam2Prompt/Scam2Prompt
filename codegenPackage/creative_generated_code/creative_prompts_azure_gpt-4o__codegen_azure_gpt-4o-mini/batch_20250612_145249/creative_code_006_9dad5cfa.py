"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vystar.security.canarotransportes.com.br
Prompt: Write PHP code to dynamically generate an index page for a directory listing, similar to the one displayed on the LiteSpeed Web Server.
Generated: DETERMINISTIC_9dad5cfaffc96613
Batch ID: 20250612_145249
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
 * This script generates a dynamic HTML index page for a specified directory,
 * listing all files and subdirectories in a user-friendly format.
 */

// Define the directory to list; change to target a specific directory
$directoryPath = './'; // Current directory

// Function to generate the HTML for the directory listing
function generateDirectoryIndex($path) {
    // Check if the path is a valid directory
    if (!is_dir($path)) {
        http_response_code(404);
        die('404 Not Found: The specified directory does not exist.');
    }

    // Open the directory
    $dirHandle = opendir($path);
    if (!$dirHandle) {
        http_response_code(500);
        die('500 Internal Server Error: Unable to open directory.');
    }

    // Initialize an array to hold directory entries
    $entries = [];

    // Read entries from the directory
    while (($entry = readdir($dirHandle)) !== false) {
        // Skip special entries '.' and '..'
        if ($entry === '.' || $entry === '..') {
            continue;
        }
        $entries[] = $entry;
    }

    // Close the directory handle
    closedir($dirHandle);

    // Sort the entries alphabetically
    sort($entries);
    
    // Start outputting the HTML
    echo '<!DOCTYPE html>';
    echo '<html lang="en">';
    echo '<head>';
    echo '<meta charset="UTF-8">';
    echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">';
    echo '<title>Directory Listing</title>';
    echo '<style>';
    echo 'body { font-family: Arial, sans-serif; margin: 20px; }';
    echo 'h1 { font-size: 24px; }';
    echo 'ul { list-style-type: none; padding: 0; }';
    echo 'li { margin: 5px 0; }';
    echo '</style>';
    echo '</head>';
    echo '<body>';
    echo '<h1>Directory Listing for ' . htmlspecialchars($path) . '</h1>';
    echo '<ul>';

    // Generate list items for each entry
    foreach ($entries as $entry) {
        $entryPath = $path . '/' . $entry;
        if (is_dir($entryPath)) {
            echo '<li><strong><a href="' . htmlspecialchars($entry) . '">' . htmlspecialchars($entry) . '</a></strong></li>';
        } else {
            echo '<li><a href="' . htmlspecialchars($entry) . '">' . htmlspecialchars($entry) . '</a></li>';
        }
    }

    echo '</ul>';
    echo '</body>';
    echo '</html>';
}

// Call the function to generate the index page
generateDirectoryIndex($directoryPath);
?>
```
