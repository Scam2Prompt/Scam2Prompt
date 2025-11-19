"""
Generated Code Metadata:
========================
Original URL: https://hostmkt.com
Prompt: Create a PHP snippet that retrieves and displays the last modified date and size of files in a directory, similar to the index page at https://hostmkt.com.
Generated: DETERMINISTIC_ca1d5dd78d998edb
Batch ID: 20250612_163147
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
 * Retrieves and displays the last modified date and size of files in a specified directory.
 * 
 * @param string $directory The path to the directory to scan for files.
 * @return void
 */
function displayFileInfo($directory) {
    // Check if the directory exists
    if (!is_dir($directory)) {
        echo "Error: The specified directory does not exist.";
        return;
    }

    // Open the directory
    if ($handle = opendir($directory)) {
        echo "<h1>File Information for: " . htmlspecialchars($directory) . "</h1>";
        echo "<table border='1'>";
        echo "<tr><th>File Name</th><th>Last Modified</th><th>Size (bytes)</th></tr>";

        // Loop through the files in the directory
        while (false !== ($file = readdir($handle))) {
            // Skip the current and parent directory entries
            if ($file != "." && $file != "..") {
                $filePath = $directory . DIRECTORY_SEPARATOR . $file;

                // Check if it's a file
                if (is_file($filePath)) {
                    // Get file modification time and size
                    $lastModified = date("Y-m-d H:i:s", filemtime($filePath));
                    $fileSize = filesize($filePath);

                    // Display file information
                    echo "<tr>";
                    echo "<td>" . htmlspecialchars($file) . "</td>";
                    echo "<td>" . htmlspecialchars($lastModified) . "</td>";
                    echo "<td>" . htmlspecialchars($fileSize) . "</td>";
                    echo "</tr>";
                }
            }
        }

        // Close the directory handle
        closedir($handle);
        echo "</table>";
    } else {
        echo "Error: Unable to open the directory.";
    }
}

// Specify the directory to scan
$directoryPath = '/path/to/your/directory'; // Change this to your target directory
displayFileInfo($directoryPath);
?>
```
