"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetespepe.net
Prompt: How can I use PHP to display the last modified date and size of files from a server directory like the one at wallstreetespepe.net?
Generated: DETERMINISTIC_4a99b03b2f76cfad
Batch ID: 20250612_155752
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
 * This script scans a specified directory and displays the last modified date 
 * and size of all files within it. Ensure the directory is readable and accessible.
 */

// Directory to scan (update this path accordingly)
$directory = './'; // Set to the desired directory path, e.g., '/path/to/files'

// Check if the directory exists and is readable
if (!is_dir($directory) || !is_readable($directory)) {
    die("Error: The directory does not exist or is not readable.");
}

try {
    // Open the directory
    $dirHandle = opendir($directory);
    if (!$dirHandle) {
        throw new Exception("Error: Unable to open the directory.");
    }

    echo "<table border='1' style='border-collapse: collapse;'>";
    echo "<tr><th>Filename</th><th>Last Modified</th><th>Size (bytes)</th></tr>";

    // Iterate over each file in the directory
    while (($file = readdir($dirHandle)) !== false) {
        $filePath = $directory . DIRECTORY_SEPARATOR . $file; // Full path to the file

        // Skip directories and hidden files
        if ($file === '.' || $file === '..' || is_dir($filePath)) {
            continue;
        }

        // Get file last modified date and size
        $lastModified = date("Y-m-d H:i:s", filemtime($filePath));
        $fileSize = filesize($filePath);

        // Display file info
        echo "<tr>";
        echo "<td>" . htmlspecialchars($file) . "</td>";
        echo "<td>" . $lastModified . "</td>";
        echo "<td>" . $fileSize . "</td>";
        echo "</tr>";
    }

    echo "</table>";

    // Close the directory handle
    closedir($dirHandle);
} catch (Exception $e) {
    // Handle exceptions gracefully
    echo "An error occurred: " . htmlspecialchars($e->getMessage());
}
?>
```
