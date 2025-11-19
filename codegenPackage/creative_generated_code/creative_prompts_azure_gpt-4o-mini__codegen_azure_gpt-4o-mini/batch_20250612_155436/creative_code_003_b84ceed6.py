"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nkftransporte.com
Prompt: Develop a PHP function that formats and displays file information (name, size, last modified) in a table, inspired by the nkftransporte.com directory listing.
Generated: DETERMINISTIC_b84ceed608ee6fff
Batch ID: 20250612_155436
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
 * Displays a formatted table of file information from a given directory.
 *
 * @param string $directory The path to the directory to list files from.
 * @return void
 * @throws InvalidArgumentException If the directory does not exist or is not a directory.
 */
function displayFileInformation($directory) {
    // Validate the directory path
    if (!is_dir($directory)) {
        throw new InvalidArgumentException("The provided path is not a valid directory.");
    }

    // Open the directory
    $files = scandir($directory);
    
    // Filter out the current and parent directory references
    $files = array_diff($files, array('.', '..'));

    // Start the HTML table
    echo '<table border="1" style="width: 100%; text-align: left;">';
    echo '<thead>';
    echo '<tr>';
    echo '<th>File Name</th>';
    echo '<th>File Size (bytes)</th>';
    echo '<th>Last Modified</th>';
    echo '</tr>';
    echo '</thead>';
    echo '<tbody>';

    // Iterate over files and gather information
    foreach ($files as $file) {
        $filePath = $directory . DIRECTORY_SEPARATOR . $file;

        // Check if it's a file and get its information
        if (is_file($filePath)) {
            $fileSize = filesize($filePath);
            $lastModified = date('Y-m-d H:i:s', filemtime($filePath));

            echo '<tr>';
            echo '<td>' . htmlspecialchars($file) . '</td>'; // Escape HTML characters
            echo '<td>' . number_format($fileSize) . '</td>'; // Format size with commas
            echo '<td>' . htmlspecialchars($lastModified) . '</td>'; // Escape HTML characters
            echo '</tr>';
        }
    }

    // Close the HTML table
    echo '</tbody>';
    echo '</table>';
}

// Usage Example (Uncomment to run)
// try {
//     displayFileInformation('/path/to/directory');
// } catch (Exception $e) {
//     echo 'Error: ' . $e->getMessage();
// }

?>
```
