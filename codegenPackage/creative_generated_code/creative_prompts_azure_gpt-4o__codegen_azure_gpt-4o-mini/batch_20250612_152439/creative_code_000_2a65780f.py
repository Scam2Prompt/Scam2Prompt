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
 * 
 * A simple PHP script to handle basic server-side operations,
 * including retrieving and displaying directory contents.
 */

// Set the timezone for consistency
date_default_timezone_set('UTC');

/**
 * Function to get the contents of a directory
 *
 * @param string $dirPath Path to the directory
 * @return array|false Returns an array of files and directories or false on failure
 */
function getDirectoryContents($dirPath) {
    // Check if the directory exists
    if (!is_dir($dirPath)) {
        trigger_error("Directory does not exist: $dirPath", E_USER_WARNING);
        return false;
    }

    // Scan the directory and filter out the current and parent directory links
    $contents = array_diff(scandir($dirPath), array('.', '..'));

    // Return the directory contents
    return $contents;
}

/**
 * Function to display directory contents in a formatted manner
 *
 * @param array $contents Array of directory contents
 * @return void
 */
function displayContents($contents) {
    echo "<h2>Directory Contents:</h2>";
    echo "<ul>";

    foreach ($contents as $item) {
        // Display each item in the directory
        echo "<li>" . htmlspecialchars($item) . "</li>";
    }

    echo "</ul>";
}

// Main execution
try {
    // Define the directory path (can be adjusted according to needs)
    $directoryPath = __DIR__; // Current directory

    // Get the contents of the specified directory
    $directoryContents = getDirectoryContents($directoryPath);

    // Check if the contents were retrieved successfully
    if ($directoryContents !== false) {
        // Display the contents of the directory
        displayContents($directoryContents);
    } else {
        echo "<p>Error retrieving directory contents. Please check the server logs for details.</p>";
    }
} catch (Exception $e) {
    // Handle any exceptions that might occur
    echo "<p>An error occurred: " . htmlspecialchars($e->getMessage()) . "</p>";
}
?>
```
