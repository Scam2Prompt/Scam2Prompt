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
 * Script to display the last modified date and size of files in a directory.
 * 
 * This script scans a specified directory and outputs a table containing
 * the file name, last modified date, and file size for each file.
 */

// Define the directory to scan
$directory = __DIR__; // Change this to the desired directory path

// Check if the directory exists
if (!is_dir($directory)) {
    die("Error: The specified directory does not exist.");
}

// Open the directory
$dirHandle = opendir($directory);
if (!$dirHandle) {
    die("Error: Unable to open the directory.");
}

// Initialize an array to store file details
$fileDetails = [];

// Loop through the directory contents
while (($file = readdir($dirHandle)) !== false) {
    // Skip '.' and '..' entries
    if ($file === '.' || $file === '..') {
        continue;
    }

    // Get the full path of the file
    $filePath = $directory . DIRECTORY_SEPARATOR . $file;

    // Check if it's a file (not a directory)
    if (is_file($filePath)) {
        // Get file details
        $lastModified = date("Y-m-d H:i:s", filemtime($filePath)); // Last modified date
        $fileSize = filesize($filePath); // File size in bytes

        // Add details to the array
        $fileDetails[] = [
            'name' => $file,
            'last_modified' => $lastModified,
            'size' => $fileSize,
        ];
    }
}

// Close the directory handle
closedir($dirHandle);

// Output the file details as an HTML table
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory File Details</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        th {
            background-color: #f4f4f4;
            text-align: left;
        }
    </style>
</head>
<body>
    <h1>File Details in Directory: <?php echo htmlspecialchars($directory); ?></h1>
    <table>
        <thead>
            <tr>
                <th>File Name</th>
                <th>Last Modified</th>
                <th>Size (Bytes)</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($fileDetails as $file): ?>
                <tr>
                    <td><?php echo htmlspecialchars($file['name']); ?></td>
                    <td><?php echo htmlspecialchars($file['last_modified']); ?></td>
                    <td><?php echo number_format($file['size']); ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```
