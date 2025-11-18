"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinmaarokatcap.com
Prompt: Create a PHP script that interacts with files in a directory listing, similar to the one shown on the webpage, to display file metadata (e.g., size, last modified date).
Generated: DETERMINISTIC_d5528e798fb7d68c
Batch ID: 20250612_145923
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
 * File Metadata Display Script
 * 
 * This script scans a specified directory and displays a list of files
 * along with their metadata such as size and last modified date.
 */

// Set the directory to be scanned
$directory = 'path/to/your/directory'; // Update this path to your desired directory

/**
 * Function to get file metadata
 *
 * @param string $filePath The path to the file
 * @return array An associative array containing file metadata
 */
function getFileMetadata($filePath) {
    return [
        'name' => basename($filePath), // Get the file name
        'size' => filesize($filePath), // Get the file size in bytes
        'last_modified' => date("F d Y H:i:s.", filemtime($filePath)) // Get last modified date
    ];
}

// Verify if the directory exists
if (!is_dir($directory)) {
    die("Error: The specified directory does not exist.");
}

// Open the directory
if ($handle = opendir($directory)) {
    echo "<h1>File Metadata List for Directory: $directory</h1>";
    echo "<table border='1'>
            <tr>
                <th>File Name</th>
                <th>File Size (bytes)</th>
                <th>Last Modified</th>
            </tr>";

    // Loop through the directory entries
    while (false !== ($entry = readdir($handle))) {
        // Skip the current and parent directory entries
        if ($entry != "." && $entry != "..") {
            $filePath = $directory . '/' . $entry; // Full path to the file
            if (is_file($filePath)) { // Check if it's a file
                $metadata = getFileMetadata($filePath); // Get file metadata
                echo "<tr>
                        <td>{$metadata['name']}</td>
                        <td>{$metadata['size']}</td>
                        <td>{$metadata['last_modified']}</td>
                      </tr>";
            }
        }
    }
    // Close the directory handle
    closedir($handle);
    echo "</table>";
} else {
    die("Error: Unable to open the directory.");
}
?>
```

Make sure to update the `$directory` variable with the path to the directory you want to scan.
