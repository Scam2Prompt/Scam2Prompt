"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ouatvs.com
Prompt: Create a PHP script to display the contents of a directory on a LiteSpeed Web Server, mimicking the structure shown in the webpage.
Generated: DETERMINISTIC_c0f5f30c76be352b
Batch ID: 20250612_151525
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
 * Directory Viewer Script
 *
 * This script displays the contents of a specified directory in a structured 
 * manner, allowing users to navigate through files and subdirectories.
 * It includes error handling to manage invalid directory paths.
 */

// Set the directory to be displayed (change this to the desired path)
$directoryPath = './'; // Current directory

/**
 * Function to scan and display the directory contents
 *
 * @param string $dir Path to the directory to scan
 */
function displayDirectoryContents($dir) {
    // Check if the directory exists
    if (!is_dir($dir)) {
        die("Error: The specified directory does not exist.");
    }

    // Open the directory
    $items = scandir($dir);

    // Filter out the current and parent directory entries ('.' and '..')
    $items = array_diff($items, ['.', '..']);

    // Check if the directory is empty
    if (empty($items)) {
        echo "<p>No files or directories found.</p>";
        return;
    }

    // Start the HTML unordered list
    echo "<ul>";

    // Loop through the items in the directory
    foreach ($items as $item) {
        $itemPath = $dir . '/' . $item;
        // Check if it's a directory or a file
        if (is_dir($itemPath)) {
            echo "<li><strong><a href='?dir=" . urlencode($itemPath) . "'>" . htmlspecialchars($item) . "</a></strong></li>";
        } else {
            echo "<li><a href='" . htmlspecialchars($itemPath) . "'>" . htmlspecialchars($item) . "</a></li>";
        }
    }

    // Close the HTML unordered list
    echo "</ul>";
}

// Check if a directory is specified in the URL query string
if (isset($_GET['dir'])) {
    // Sanitize the input to prevent directory traversal attacks
    $directoryPath = basename($_GET['dir']);
}

// Display the directory contents
displayDirectoryContents($directoryPath);
?>
```
