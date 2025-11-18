"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://world-liberty-financial.alnagi-group.com
Prompt: Generate PHP code to dynamically display files and metadata (e.g., name, size, last modified date) from a specific directory on a web server.
Generated: DETERMINISTIC_b81dc775db9a94ff
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configuration: Set the target directory
$targetDirectory = __DIR__ . '/uploads'; // Change 'uploads' to your desired directory

// Function to format file size in a human-readable format
function formatFileSize($bytes) {
    if ($bytes < 1024) {
        return $bytes . ' B';
    } elseif ($bytes < 1048576) {
        return round($bytes / 1024, 2) . ' KB';
    } elseif ($bytes < 1073741824) {
        return round($bytes / 1048576, 2) . ' MB';
    } else {
        return round($bytes / 1073741824, 2) . ' GB';
    }
}

try {
    // Check if the target directory exists
    if (!is_dir($targetDirectory)) {
        throw new Exception("The directory does not exist: $targetDirectory");
    }

    // Open the directory
    $files = scandir($targetDirectory);

    // Filter out '.' and '..'
    $files = array_filter($files, function ($file) use ($targetDirectory) {
        return !in_array($file, ['.', '..']) && is_file($targetDirectory . '/' . $file);
    });

    // Display the files and metadata in a table
    echo '<table border="1" cellpadding="10" cellspacing="0">';
    echo '<tr><th>File Name</th><th>File Size</th><th>Last Modified Date</th></tr>';

    foreach ($files as $file) {
        $filePath = $targetDirectory . '/' . $file;

        // Get file metadata
        $fileSize = filesize($filePath); // File size in bytes
        $lastModified = date('Y-m-d H:i:s', filemtime($filePath)); // Last modified time

        echo '<tr>';
        echo '<td>' . htmlspecialchars($file) . '</td>'; // Display file name (HTML escaped)
        echo '<td>' . formatFileSize($fileSize) . '</td>'; // Display human-readable file size
        echo '<td>' . $lastModified . '</td>'; // Display last modified date/time
        echo '</tr>';
    }

    echo '</table>';
} catch (Exception $e) {
    // Handle errors gracefully
    echo '<p>Error: ' . htmlspecialchars($e->getMessage()) . '</p>';
}
?>
```

This PHP script dynamically scans a directory, retrieves file metadata (name, size, and last modified date), and displays the information in an HTML table. Adjust the `$targetDirectory` variable as needed to set the directory to scan.
