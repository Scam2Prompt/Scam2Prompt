"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://world-liberty-financial.alnagi-group.com
Prompt: Write PHP code to create a directory listing similar to the one displayed on a LiteSpeed Web Server, including file names, last modified dates, and sizes.
Generated: DETERMINISTIC_7fde7e1e5ffb4221
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
 * Directory Listing Script
 * Generates a directory listing with file names, last modified dates, and sizes
 * Similar to LiteSpeed Web Server
 */

// Define the directory to list. Change to desired directory path.
$directoryPath = __DIR__; // Current directory

// Error handling: Check if directory exists
if (!is_dir($directoryPath)) {
    die("Error: Specified directory does not exist.");
}

// Function to format file size into a human-readable format
function formatFileSize($bytes) {
    $units = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    $power = $bytes > 0 ? floor(log($bytes, 1024)) : 0;
    return number_format($bytes / pow(1024, $power), 2) . ' ' . $units[$power];
}

// Get list of files and directories
$items = scandir($directoryPath);

// Error handling: Check if directory can be read
if ($items === false) {
    die("Error: Unable to read the directory.");
}

// Output HTML structure for directory listing
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listing</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 10px;
            text-align: left;
            border: 1px solid #ccc;
        }
        th {
            background-color: #f4f4f4;
        }
        tr:hover {
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
    <h1>Directory Listing</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Last Modified</th>
                <th>Size</th>
            </tr>
        </thead>
        <tbody>
            <?php
            foreach ($items as $item) {
                // Skip "." and ".." entries
                if ($item === '.' || $item === '..') {
                    continue;
                }

                $itemPath = $directoryPath . DIRECTORY_SEPARATOR . $item;
                $isDirectory = is_dir($itemPath);

                // Get file info
                $lastModified = date("Y-m-d H:i:s", filemtime($itemPath));
                $size = $isDirectory ? '-' : formatFileSize(filesize($itemPath));

                // Output table row
                echo "<tr>";
                echo "<td>" . ($isDirectory ? "<strong>$item/</strong>" : $item) . "</td>";
                echo "<td>$lastModified</td>";
                echo "<td>$size</td>";
                echo "</tr>";
            }
            ?>
        </tbody>
    </table>
</body>
</html>
```
