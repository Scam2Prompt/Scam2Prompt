"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nkftransporte.com
Prompt: Write a PHP script that could be used in a `system.php` file to handle basic server-side operations, such as retrieving and displaying directory contents.
Generated: DETERMINISTIC_2a65780f70f9f25d
Batch ID: 20250612_152439
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
 * system.php
 * A PHP script to handle basic server-side operations such as retrieving and displaying directory contents.
 * 
 * Author: [Your Name]
 * Date: [Date]
 * 
 * Usage: Include this script in your PHP project to fetch and display directory contents securely.
 */

// Set the base directory (ensure it's secure and limited to your application context)
define('BASE_DIR', __DIR__);

/**
 * Function to fetch directory contents.
 * 
 * @param string $path Relative path to fetch contents from.
 * @return array List of files and directories in the specified path.
 */
function getDirectoryContents($path) {
    // Resolve the full path
    $fullPath = realpath(BASE_DIR . DIRECTORY_SEPARATOR . $path);

    // Validate path to ensure it stays within BASE_DIR
    if (!$fullPath || strpos($fullPath, BASE_DIR) !== 0) {
        throw new InvalidArgumentException("Invalid path provided.");
    }

    // Check if the path is a directory
    if (!is_dir($fullPath)) {
        throw new RuntimeException("The specified path is not a directory.");
    }

    // Fetch directory contents
    $contents = scandir($fullPath);

    // Filter out "." and ".."
    return array_filter($contents, function ($item) {
        return $item !== '.' && $item !== '..';
    });
}

/**
 * Function to display directory contents in a formatted manner.
 * 
 * @param array $contents Array of directory contents.
 * @param string $directory Name of the directory.
 */
function displayDirectoryContents(array $contents, $directory) {
    echo "<h1>Contents of Directory: " . htmlspecialchars($directory) . "</h1>";
    echo "<ul>";
    foreach ($contents as $item) {
        echo "<li>" . htmlspecialchars($item) . "</li>";
    }
    echo "</ul>";
}

// Main Execution
try {
    // Retrieve the 'dir' parameter from the URL query string
    $requestedDir = isset($_GET['dir']) ? $_GET['dir'] : '';

    // Fetch directory contents
    $contents = getDirectoryContents($requestedDir);

    // Display directory contents
    displayDirectoryContents($contents, $requestedDir);
} catch (Exception $e) {
    // Handle errors gracefully
    echo "<p>Error: " . htmlspecialchars($e->getMessage()) . "</p>";
}

?>
```
