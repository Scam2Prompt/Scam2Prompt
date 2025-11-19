"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.com-live.org
Prompt: Create a simple PHP page that lists all files in a directory, similar to the index page of polymarket.com-live.org.
Generated: DETERMINISTIC_c0dc2f7d7468632f
Batch ID: 20250612_162217
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
 * Simple PHP script to list all files in a specified directory.
 * This script generates an HTML page that displays the files in a user-friendly format.
 */

// Set the directory to be listed
$directory = 'path/to/your/directory';

// Function to list files in the specified directory
function listFiles($dir) {
    // Check if the directory exists
    if (!is_dir($dir)) {
        throw new InvalidArgumentException("The directory '$dir' does not exist.");
    }

    // Scan the directory for files and directories
    $files = scandir($dir);
    
    // Filter the results to exclude '.' and '..'
    $files = array_diff($files, ['.', '..']);

    // Return the list of files
    return $files;
}

// Output the HTML header
header('Content-Type: text/html; charset=utf-8');
echo '<!DOCTYPE html>';
echo '<html lang="en">';
echo '<head>';
echo '<meta charset="UTF-8">';
echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">';
echo '<title>File List</title>';
echo '<style>';
echo 'body { font-family: Arial, sans-serif; }';
echo 'ul { list-style-type: none; padding: 0; }';
echo 'li { margin: 5px 0; }';
echo '</style>';
echo '</head>';
echo '<body>';
echo '<h1>Files in Directory: ' . htmlspecialchars($directory) . '</h1>';

// Try to list the files and handle errors gracefully
try {
    $files = listFiles($directory);
    if (empty($files)) {
        echo '<p>No files found in this directory.</p>';
    } else {
        echo '<ul>';
        foreach ($files as $file) {
            // Display each file as a list item
            echo '<li>' . htmlspecialchars($file) . '</li>';
        }
        echo '</ul>';
    }
} catch (InvalidArgumentException $e) {
    // Handle directory error
    echo '<p>Error: ' . htmlspecialchars($e->getMessage()) . '</p>';
} catch (Exception $e) {
    // Handle any other errors
    echo '<p>An unexpected error occurred: ' . htmlspecialchars($e->getMessage()) . '</p>';
}

// Output the HTML footer
echo '</body>';
echo '</html>';
?>
```
