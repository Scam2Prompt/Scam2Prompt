"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robilliardag.com
Prompt: Generate a PHP script that retrieves and displays the contents of a directory similar to the index found on robilliardag.com.
Generated: DETERMINISTIC_cf2280f8475eea3c
Batch ID: 20250612_161209
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
 * Directory Listing Script
 * 
 * This script retrieves the contents of a directory and displays them in a user-friendly format.
 * It includes file names, sizes, and modification dates.
 * 
 * Usage: Place this script in the directory you want to list or modify the $directory variable below.
 */

// Set the directory to be listed (current directory by default)
$directory = __DIR__;

try {
    // Ensure the directory exists
    if (!is_dir($directory)) {
        throw new Exception("The specified directory does not exist.");
    }

    // Open the directory
    $dirHandle = opendir($directory);
    if (!$dirHandle) {
        throw new Exception("Failed to open the directory.");
    }

    // Prepare to store directory contents
    $files = [];

    // Read each entry in the directory
    while (($entry = readdir($dirHandle)) !== false) {
        // Skip current and parent directory references
        if ($entry === '.' || $entry === '..') {
            continue;
        }

        // Get full path of the entry
        $filePath = $directory . DIRECTORY_SEPARATOR . $entry;

        // Gather file details
        $files[] = [
            'name' => $entry,
            'type' => is_dir($filePath) ? 'Directory' : 'File',
            'size' => is_file($filePath) ? filesize($filePath) : null,
            'modified' => date('Y-m-d H:i:s', filemtime($filePath))
        ];
    }

    // Close the directory handle
    closedir($dirHandle);

    // Sort files alphabetically by name
    usort($files, function ($a, $b) {
        return strcmp($a['name'], $b['name']);
    });

    // Display directory contents as an HTML table
    echo "<!DOCTYPE html>";
    echo "<html lang='en'>";
    echo "<head>";
    echo "<meta charset='UTF-8'>";
    echo "<meta name='viewport' content='width=device-width, initial-scale=1.0'>";
    echo "<title>Directory Listing</title>";
    echo "<style>";
    echo "body { font-family: Arial, sans-serif; margin: 20px; }";
    echo "table { width: 100%; border-collapse: collapse; }";
    echo "th, td { padding: 10px; border: 1px solid #ddd; text-align: left; }";
    echo "th { background-color: #f4f4f4; }";
    echo "</style>";
    echo "</head>";
    echo "<body>";
    echo "<h1>Directory Listing</h1>";
    echo "<table>";
    echo "<thead>";
    echo "<tr>";
    echo "<th>Name</th>";
    echo "<th>Type</th>";
    echo "<th>Size (bytes)</th>";
    echo "<th>Last Modified</th>";
    echo "</tr>";
    echo "</thead>";
    echo "<tbody>";

    foreach ($files as $file) {
        echo "<tr>";
        echo "<td>" . htmlspecialchars($file['name']) . "</td>";
        echo "<td>" . $file['type'] . "</td>";
        echo "<td>" . ($file['size'] !== null ? $file['size'] : 'N/A') . "</td>";
        echo "<td>" . $file['modified'] . "</td>";
        echo "</tr>";
    }

    echo "</tbody>";
    echo "</table>";
    echo "</body>";
    echo "</html>";

} catch (Exception $e) {
    // Handle errors gracefully
    echo "<p>Error: " . htmlspecialchars($e->getMessage()) . "</p>";
}
?>
```
