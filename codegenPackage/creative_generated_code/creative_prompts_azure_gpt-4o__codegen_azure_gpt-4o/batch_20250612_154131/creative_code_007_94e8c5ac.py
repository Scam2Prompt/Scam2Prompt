"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fivefootgaming.com
Prompt: Create a PHP script to interact with a LiteSpeed Web Server, like the one hosting fivefootgaming.com, to fetch and display directory contents dynamically.
Generated: DETERMINISTIC_94e8c5aca7c85df4
Batch ID: 20250612_154131
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
 * Script to fetch and display directory contents dynamically from a LiteSpeed Web Server.
 * 
 * Requirements:
 * - PHP-enabled LiteSpeed Web Server
 * - Directory path accessible to the server
 * 
 * Best Practices:
 * - Proper error handling
 * - Security measures to prevent directory traversal
 * - Clean and efficient code
 */

// Set the directory path to fetch contents from (for demonstration purposes, a relative path is used)
$directoryPath = './'; // Change to your desired directory path, relative or absolute.

// Function to validate and sanitize the directory path
function sanitizeDirectoryPath($path) {
    // Realpath ensures no directory traversal issues
    $realPath = realpath($path);
    if ($realPath === false || !is_dir($realPath)) {
        throw new Exception('Invalid directory path.');
    }
    return $realPath;
}

try {
    // Sanitize the directory path
    $safeDirectoryPath = sanitizeDirectoryPath($directoryPath);

    // Open the directory
    $directoryHandle = opendir($safeDirectoryPath);
    if (!$directoryHandle) {
        throw new Exception('Unable to open directory: ' . $safeDirectoryPath);
    }

    // Initialize an array to hold directory contents
    $directoryContents = [];

    // Read contents of the directory
    while (($entry = readdir($directoryHandle)) !== false) {
        // Exclude "." and ".." entries
        if ($entry !== '.' && $entry !== '..') {
            $directoryContents[] = $entry;
        }
    }

    // Close the directory handle
    closedir($directoryHandle);

    // Display directory contents dynamically
    echo '<h1>Directory Contents</h1>';
    echo '<ul>';
    foreach ($directoryContents as $item) {
        echo '<li>' . htmlspecialchars($item, ENT_QUOTES, 'UTF-8') . '</li>';
    }
    echo '</ul>';
} catch (Exception $e) {
    // Handle exceptions gracefully
    echo '<h1>Error</h1>';
    echo '<p>' . htmlspecialchars($e->getMessage(), ENT_QUOTES, 'UTF-8') . '</p>';
}

?>
```
