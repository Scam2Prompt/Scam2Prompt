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
 * A PHP script to display the contents of a directory in a structured format.
 * This script is designed to run effectively on LiteSpeed Web Server.
 */

// Set the target directory. Change to the desired directory path.
$targetDirectory = __DIR__; // Default to the current directory

try {
    // Check if the directory exists
    if (!is_dir($targetDirectory)) {
        throw new Exception("The specified directory does not exist: $targetDirectory");
    }

    // Open the directory
    $directoryHandle = opendir($targetDirectory);
    if (!$directoryHandle) {
        throw new Exception("Failed to open the directory: $targetDirectory");
    }

    // Start the HTML output
    echo "<!DOCTYPE html>\n";
    echo "<html lang='en'>\n";
    echo "<head>\n";
    echo "    <meta charset='UTF-8'>\n";
    echo "    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n";
    echo "    <title>Directory Contents</title>\n";
    echo "    <style>\n";
    echo "        body { font-family: Arial, sans-serif; }\n";
    echo "        ul { list-style-type: none; padding: 0; }\n";
    echo "        li { margin: 5px 0; }\n";
    echo "        a { text-decoration: none; color: blue; }\n";
    echo "        a:hover { text-decoration: underline; }\n";
    echo "    </style>\n";
    echo "</head>\n";
    echo "<body>\n";
    echo "    <h1>Contents of Directory: " . htmlspecialchars($targetDirectory) . "</h1>\n";
    echo "    <ul>\n";

    // Loop through the directory contents
    while (($entry = readdir($directoryHandle)) !== false) {
        // Skip the current directory (.) and parent directory (..)
        if ($entry === '.' || $entry === '..') {
            continue;
        }

        // Build the full path for the entry
        $entryPath = $targetDirectory . DIRECTORY_SEPARATOR . $entry;

        // Check if the entry is a file or a directory
        if (is_dir($entryPath)) {
            // Display directory with a folder icon
            echo "        <li>📁 <a href='" . htmlspecialchars($entry) . "'>" . htmlspecialchars($entry) . "</a></li>\n";
        } elseif (is_file($entryPath)) {
            // Display file with a file icon
            echo "        <li>📄 <a href='" . htmlspecialchars($entry) . "'>" . htmlspecialchars($entry) . "</a></li>\n";
        }
    }

    // Close the HTML output
    echo "    </ul>\n";
    echo "</body>\n";
    echo "</html>\n";

    // Close the directory handle
    closedir($directoryHandle);
} catch (Exception $e) {
    // Handle errors gracefully
    echo "<!DOCTYPE html>\n";
    echo "<html lang='en'>\n";
    echo "<head>\n";
    echo "    <meta charset='UTF-8'>\n";
    echo "    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n";
    echo "    <title>Error</title>\n";
    echo "</head>\n";
    echo "<body>\n";
    echo "    <h1>An error occurred</h1>\n";
    echo "    <p>" . htmlspecialchars($e->getMessage()) . "</p>\n";
    echo "</body>\n";
    echo "</html>\n";
}
?>
```
