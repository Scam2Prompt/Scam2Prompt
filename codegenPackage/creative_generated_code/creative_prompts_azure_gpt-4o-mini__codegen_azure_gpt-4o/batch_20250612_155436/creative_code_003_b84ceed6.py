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
 * Formats and displays file information in a table.
 * 
 * @param string $directoryPath Path to the directory to list files.
 * @return void Outputs an HTML table displaying file details.
 */
function displayFileInformation($directoryPath)
{
    // Ensure the provided directory exists
    if (!is_dir($directoryPath)) {
        echo "Error: The provided path is not a valid directory.";
        return;
    }

    // Open the directory
    $directory = opendir($directoryPath);

    if ($directory === false) {
        echo "Error: Failed to open the directory.";
        return;
    }

    // Start building the HTML table
    echo '<table border="1" cellpadding="5" cellspacing="0">';
    echo '<thead>';
    echo '<tr>';
    echo '<th>File Name</th>';
    echo '<th>File Size (KB)</th>';
    echo '<th>Last Modified</th>';
    echo '</tr>';
    echo '</thead>';
    echo '<tbody>';

    // Iterate through the directory entries
    while (($file = readdir($directory)) !== false) {
        // Skip special entries '.' and '..'
        if ($file === '.' || $file === '..') {
            continue;
        }

        // Build the full path to the file
        $filePath = $directoryPath . DIRECTORY_SEPARATOR . $file;

        // Ensure the entry is a file (not a subdirectory)
        if (is_file($filePath)) {
            // Retrieve file details
            $fileSize = filesize($filePath); // File size in bytes
            $lastModified = date("Y-m-d H:i:s", filemtime($filePath)); // Last modified date

            // Convert file size to KB
            $fileSizeInKB = number_format($fileSize / 1024, 2);

            // Output the file details in a table row
            echo '<tr>';
            echo '<td>' . htmlspecialchars($file) . '</td>';
            echo '<td>' . $fileSizeInKB . '</td>';
            echo '<td>' . $lastModified . '</td>';
            echo '</tr>';
        }
    }

    // Close the table
    echo '</tbody>';
    echo '</table>';

    // Close the directory
    closedir($directory);
}

// Example usage
$directoryPath = __DIR__; // Modify the path as needed
displayFileInformation($directoryPath);
?>
```
