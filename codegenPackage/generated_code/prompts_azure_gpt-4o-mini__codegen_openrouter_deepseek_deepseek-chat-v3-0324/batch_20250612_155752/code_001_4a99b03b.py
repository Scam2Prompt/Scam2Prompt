"""
Generated Code Metadata:
========================
Original URL: https://wallstreetespepe.net
Prompt: How can I use PHP to display the last modified date and size of files from a server directory like the one at wallstreetespepe.net?
Generated: DETERMINISTIC_4a99b03b2f76cfad
Batch ID: 20250612_155752
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
 * Displays the last modified date and size of files in a directory.
 * 
 * @param string $directory The directory path to scan.
 * @return void
 */
function displayFileInfo($directory) {
    // Check if the directory exists and is readable
    if (!is_dir($directory) || !is_readable($directory)) {
        die("Error: Directory does not exist or is not readable.");
    }

    // Open the directory
    if ($handle = opendir($directory)) {
        echo "<table border='1'>";
        echo "<tr><th>Filename</th><th>Last Modified</th><th>Size</th></tr>";

        // Read each file in the directory
        while (false !== ($file = readdir($handle))) {
            // Skip current and parent directory entries
            if ($file != "." && $file != "..") {
                $filePath = $directory . DIRECTORY_SEPARATOR . $file;
                
                // Check if it's a file (not a directory)
                if (is_file($filePath)) {
                    $lastModified = date("Y-m-d H:i:s", filemtime($filePath));
                    $size = filesize($filePath);
                    
                    // Format size in a human-readable way
                    $formattedSize = formatSizeUnits($size);
                    
                    echo "<tr>";
                    echo "<td>" . htmlspecialchars($file) . "</td>";
                    echo "<td>" . $lastModified . "</td>";
                    echo "<td>" . $formattedSize . "</td>";
                    echo "</tr>";
                }
            }
        }
        echo "</table>";
        closedir($handle);
    } else {
        die("Error: Could not open the directory.");
    }
}

/**
 * Formats file size in human-readable units.
 * 
 * @param int $bytes File size in bytes.
 * @return string Formatted file size.
 */
function formatSizeUnits($bytes) {
    if ($bytes >= 1073741824) {
        $bytes = number_format($bytes / 1073741824, 2) . ' GB';
    } elseif ($bytes >= 1048576) {
        $bytes = number_format($bytes / 1048576, 2) . ' MB';
    } elseif ($bytes >= 1024) {
        $bytes = number_format($bytes / 1024, 2) . ' KB';
    } elseif ($bytes > 1) {
        $bytes = $bytes . ' bytes';
    } elseif ($bytes == 1) {
        $bytes = $bytes . ' byte';
    } else {
        $bytes = '0 bytes';
    }

    return $bytes;
}

// Example usage:
$directoryPath = '/path/to/your/directory'; // Replace with your directory path
displayFileInfo($directoryPath);
?>
```
