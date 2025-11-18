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
/**
 * Directory File Display
 * This script dynamically displays files and their metadata (name, size, last modified date)
 * from a specific directory on the web server.
 */

define('DIRECTORY_PATH', 'path/to/your/directory'); // Set the path to your directory

// Function to get files and their metadata
function getFilesMetadata($directory) {
    // Check if the directory exists
    if (!is_dir($directory)) {
        throw new InvalidArgumentException("Directory does not exist: $directory");
    }

    // Initialize an array to hold file metadata
    $filesMetadata = [];

    // Open the directory
    if ($handle = opendir($directory)) {
        // Loop through the directory contents
        while (false !== ($file = readdir($handle))) {
            // Skip the current and parent directory links
            if ($file !== '.' && $file !== '..') {
                // Get full path of the file
                $filePath = $directory . DIRECTORY_SEPARATOR . $file;
                
                // Check if it is a file
                if (is_file($filePath)) {
                    // Get file metadata
                    $filesMetadata[] = [
                        'name' => $file,
                        'size' => filesize($filePath), // Size in bytes
                        'last_modified' => date("F d Y H:i:s.", filemtime($filePath)) // Last modified date
                    ];
                }
            }
        }
        // Close the directory handle
        closedir($handle);
    } else {
        throw new RuntimeException("Failed to open directory: $directory");
    }

    return $filesMetadata;
}

// Error handling
try {
    // Retrieve file metadata
    $files = getFilesMetadata(DIRECTORY_PATH);

    // Display the files and their metadata in an HTML table
    echo "<table border='1'>";
    echo "<tr><th>File Name</th><th>Size (bytes)</th><th>Last Modified</th></tr>";

    foreach ($files as $file) {
        echo "<tr>";
        echo "<td>" . htmlspecialchars($file['name']) . "</td>";
        echo "<td>" . htmlspecialchars($file['size']) . "</td>";
        echo "<td>" . htmlspecialchars($file['last_modified']) . "</td>";
        echo "</tr>";
    }

    echo "</table>";
} catch (Exception $e) {
    // Handle exceptions and display error messages
    echo "Error: " . htmlspecialchars($e->getMessage());
}
?>
```
