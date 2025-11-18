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
 * Directory Scanner Script
 *
 * This script scans a specified directory and outputs file metadata
 * such as name, size, and last modified date in a formatted manner.
 * 
 * Usage: Modify the $directory variable to the path you want to scan.
 */

// Set the directory to scan
$directory = '/path/to/your/directory'; // Change this to your target directory

/**
 * Function to scan the directory and retrieve file metadata
 *
 * @param string $dir The directory path to scan
 * @return array An array of file metadata
 */
function scanDirectory($dir) {
    // Initialize an array to hold file metadata
    $fileData = [];

    // Check if the directory exists
    if (!is_dir($dir)) {
        throw new InvalidArgumentException("The provided path is not a valid directory: $dir");
    }

    // Use DirectoryIterator to iterate through files in the directory
    $iterator = new DirectoryIterator($dir);
    foreach ($iterator as $fileInfo) {
        // Skip '.' and '..' directories
        if ($fileInfo->isDot()) {
            continue;
        }

        // Collect metadata for each file
        $fileData[] = [
            'name' => $fileInfo->getFilename(),
            'size' => $fileInfo->getSize(), // Size in bytes
            'last_modified' => date('Y-m-d H:i:s', $fileInfo->getMTime()), // Formatted last modified date
        ];
    }

    return $fileData;
}

/**
 * Function to display file metadata in a formatted way
 *
 * @param array $fileData The array of file metadata
 * @return void
 */
function displayFileMetadata($fileData) {
    // Output header
    echo "<h1>File Metadata</h1>";
    echo "<table border='1'>
            <tr>
                <th>File Name</th>
                <th>Size (bytes)</th>
                <th>Last Modified</th>
            </tr>";

    // Output each file's metadata
    foreach ($fileData as $file) {
        echo "<tr>
                <td>{$file['name']}</td>
                <td>{$file['size']}</td>
                <td>{$file['last_modified']}</td>
              </tr>";
    }

    echo "</table>";
}

try {
    // Scan the directory and get the file metadata
    $fileData = scanDirectory($directory);
    
    // Display the file metadata
    displayFileMetadata($fileData);
} catch (Exception $e) {
    // Handle exceptions that may arise and display an error message
    echo "<p>Error: {$e->getMessage()}</p>";
}
?>
```

Make sure to replace `'/path/to/your/directory'` with the actual path of the directory you want to scan before running the script.
