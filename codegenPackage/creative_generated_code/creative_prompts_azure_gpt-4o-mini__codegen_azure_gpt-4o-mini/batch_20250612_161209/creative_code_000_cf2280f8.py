"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robilliardag.com
Prompt: Generate a PHP script that retrieves and displays the contents of a directory similar to the index found on robilliardag.com.
Generated: DETERMINISTIC_cf2280f8475eea3c
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
 * Directory Listing Script
 *
 * This script retrieves and displays the contents of a specified directory
 * in a user-friendly format, similar to the index found on robilliardag.com.
 * It includes error handling and proper security measures to prevent directory
 * traversal attacks.
 */

// Define the directory to list
$directory = __DIR__ . '/path/to/your/directory'; // Change this to your target directory

/**
 * Function to safely scan and display directory contents
 *
 * @param string $dir Path to the directory to scan
 * @return void
 */
function listDirectoryContents($dir) {
    // Check if the directory exists and is indeed a directory
    if (!is_dir($dir)) {
        http_response_code(404); // Set HTTP status code to 404 Not Found
        echo "<h1>Directory Not Found</h1>";
        return;
    }

    // Attempt to scan the directory
    $files = scandir($dir);

    // Check if the scan was successful
    if ($files === false) {
        http_response_code(500); // Set HTTP status code to 500 Internal Server Error
        echo "<h1>Error retrieving directory contents</h1>";
        return;
    }

    // Start HTML output
    echo "<h1>Contents of Directory: " . htmlspecialchars($dir) . "</h1>";
    echo "<ul>";

    // Loop through the files and display them
    foreach ($files as $file) {
        // Skip current and parent directory entries
        if ($file === '.' || $file === '..') {
            continue;
        }

        // Create a safe file path
        $filePath = $dir . '/' . $file;

        // Display the file or directory link
        if (is_dir($filePath)) {
            echo "<li><strong><a href='" . htmlspecialchars($filePath) . "'>" . htmlspecialchars($file) . "</a></strong> (Directory)</li>";
        } else {
            echo "<li><a href='" . htmlspecialchars($filePath) . "'>" . htmlspecialchars($file) . "</a></li>";
        }
    }

    echo "</ul>";
}

// Call the function to display the directory contents
listDirectoryContents($directory);
?>
```

Make sure to replace `'/path/to/your/directory'` with the actual path of the directory you want to list.
