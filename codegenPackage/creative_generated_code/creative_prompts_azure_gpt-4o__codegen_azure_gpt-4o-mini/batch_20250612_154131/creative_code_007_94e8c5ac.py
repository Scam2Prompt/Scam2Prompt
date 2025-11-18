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
 * Directory Listing Script
 * This script dynamically fetches and displays the contents of a specified directory
 * on a LiteSpeed web server. It includes basic error handling and sanitization.
 */

// Set the desired directory path (make sure it is a valid directory)
$directory = 'path/to/your/directory'; // Update with your directory path

// Function to fetch and display directory contents
function listDirectoryContents($dir) {
    // Check if the directory exists
    if (!is_dir($dir)) {
        // Return an error message if the directory does not exist
        http_response_code(404);
        echo "<h1>404 Not Found</h1>";
        echo "<p>The directory does not exist.</p>";
        return;
    }

    // Attempt to open the directory
    if ($handle = opendir($dir)) {
        echo "<h1>Contents of Directory: $dir</h1>";
        echo "<ul>";

        // Loop through the directory contents
        while (false !== ($entry = readdir($handle))) {
            // Skip the current and parent directory entries
            if ($entry != "." && $entry != "..") {
                // Sanitize output to prevent XSS
                $safeEntry = htmlspecialchars($entry, ENT_QUOTES, 'UTF-8');
                echo "<li>$safeEntry</li>";
            }
        }

        echo "</ul>";
        closedir($handle); // Close the directory handle
    } else {
        // Return an error message if the directory cannot be opened
        http_response_code(500);
        echo "<h1>500 Internal Server Error</h1>";
        echo "<p>Unable to open the directory.</p>";
    }
}

// Call the function to list directory contents
listDirectoryContents($directory);
?>
```
