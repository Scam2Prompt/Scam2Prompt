"""
Generated Code Metadata:
========================
Original URL: https://nkftransporte.com
Prompt: Develop a PHP function that formats and displays file information (name, size, last modified) in a table, inspired by the nkftransporte.com directory listing.
Generated: DETERMINISTIC_b84ceed608ee6fff
Batch ID: 20250612_155436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Formats and displays file information in an HTML table.
 *
 * @param string $directory The path to the directory to list files from.
 * @return void
 */
function displayFileInfo($directory) {
    // Check if the directory exists
    if (!is_dir($directory)) {
        echo "Error: The specified directory does not exist.";
        return;
    }

    // Open the directory
    $dirHandle = opendir($directory);
    if ($dirHandle === false) {
        echo "Error: Unable to open the directory.";
        return;
    }

    // Start the HTML table
    echo '<table border="1">';
    echo '<tr><th>File Name</th><th>File Size (bytes)</th><th>Last Modified</th></tr>';

    // Loop through the files in the directory
    while (($file = readdir($dirHandle)) !== false) {
        // Skip the current and parent directory entries
        if ($file === '.' || $file === '..') {
            continue;
        }

        // Get the full path of the file
        $filePath = $directory . DIRECTORY_SEPARATOR . $file;

        // Check if it's a file
        if (is_file($filePath)) {
            // Get file size and last modified time
            $fileSize = filesize($filePath);
            $lastModified = date("Y-m-d H:i:s", filemtime($filePath));

            // Display the file information in a table row
            echo '<tr>';
            echo '<td>' . htmlspecialchars($file) . '</td>';
            echo '<td>' . number_format($fileSize) . '</td>';
            echo '<td>' . htmlspecialchars($lastModified) . '</td>';
            echo '</tr>';
        }
    }

    // Close the directory handle
    closedir($dirHandle);

    // End the HTML table
    echo '</table>';
}

// Example usage
// displayFileInfo('/path/to/your/directory');
?>
```
