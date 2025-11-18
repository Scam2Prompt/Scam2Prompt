"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nkftransporte.com
Prompt: Write a PHP script that scans a directory and outputs file metadata (e.g., name, size, last modified date) in a format similar to the listing on nkftransporte.com.
Generated: DETERMINISTIC_59f744b7c1606ccb
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
 * Script to scan a directory and output file metadata.
 * Metadata includes file name, size, and last modified date.
 */

// Configuration: Set the directory to scan
$directoryPath = './your_directory_path'; // Replace with your target directory path

try {
    // Check if directory exists and is readable
    if (!is_dir($directoryPath)) {
        throw new Exception("The specified directory does not exist.");
    }
    if (!is_readable($directoryPath)) {
        throw new Exception("The specified directory is not readable.");
    }

    // Open the directory
    $directoryHandle = opendir($directoryPath);
    if (!$directoryHandle) {
        throw new Exception("Failed to open the directory.");
    }

    // Fetch file metadata
    $fileMetadata = [];
    while (($file = readdir($directoryHandle)) !== false) {
        // Skip '.' and '..'
        if ($file === '.' || $file === '..') {
            continue;
        }

        // Full file path
        $filePath = $directoryPath . DIRECTORY_SEPARATOR . $file;

        // Only process files (ignore directories)
        if (is_file($filePath)) {
            $fileMetadata[] = [
                'name' => $file,
                'size' => filesize($filePath), // File size in bytes
                'last_modified' => date("Y-m-d H:i:s", filemtime($filePath)) // Last modified date
            ];
        }
    }

    // Close the directory handle
    closedir($directoryHandle);

    // Output the file metadata in a readable format (similar to nkftransporte.com listing)
    echo "<table border='1' style='border-collapse: collapse; width: 100%;'>";
    echo "<tr><th>File Name</th><th>Size (Bytes)</th><th>Last Modified</th></tr>";

    foreach ($fileMetadata as $fileData) {
        echo "<tr>";
        echo "<td>" . htmlspecialchars($fileData['name']) . "</td>";
        echo "<td>" . number_format($fileData['size']) . "</td>";
        echo "<td>" . htmlspecialchars($fileData['last_modified']) . "</td>";
        echo "</tr>";
    }

    echo "</table>";
} catch (Exception $e) {
    // Handle errors gracefully
    echo "<p>Error: " . htmlspecialchars($e->getMessage()) . "</p>";
}
?>
```
