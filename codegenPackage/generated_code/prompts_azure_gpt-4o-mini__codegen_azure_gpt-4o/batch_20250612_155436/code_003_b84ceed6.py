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
 * Function to format and display file information in a table.
 * 
 * @param string $directoryPath Path to the directory to scan for files.
 * @return void Outputs an HTML table with file information.
 */
function displayFileInformation($directoryPath) {
    // Check if the provided path is a valid directory
    if (!is_dir($directoryPath)) {
        echo "Error: Invalid directory path.";
        return;
    }

    // Scan the directory for files
    $files = scandir($directoryPath);

    // Filter out '.' and '..' from the file list
    $files = array_filter($files, function ($file) use ($directoryPath) {
        return is_file($directoryPath . DIRECTORY_SEPARATOR . $file);
    });

    // Start HTML table
    echo '<table border="1" cellpadding="5" cellspacing="0">';
    echo '<thead>';
    echo '<tr>';
    echo '<th>File Name</th>';
    echo '<th>File Size (KB)</th>';
    echo '<th>Last Modified</th>';
    echo '</tr>';
    echo '</thead>';
    echo '<tbody>';

    // Loop through each file and display its information
    foreach ($files as $file) {
        $filePath = $directoryPath . DIRECTORY_SEPARATOR . $file;

        // Get file information
        $fileName = htmlspecialchars($file); // Sanitize file name for HTML output
        $fileSize = filesize($filePath) / 1024; // Convert size to KB
        $lastModified = date("Y-m-d H:i:s", filemtime($filePath)); // Format last modified time

        // Output file information in a table row
        echo '<tr>';
        echo '<td>' . $fileName . '</td>';
        echo '<td>' . number_format($fileSize, 2) . '</td>';
        echo '<td>' . $lastModified . '</td>';
        echo '</tr>';
    }

    // Close HTML table
    echo '</tbody>';
    echo '</table>';
}

// Example usage
$directoryPath = __DIR__; // Change this to the desired directory path
displayFileInformation($directoryPath);
?>
```
