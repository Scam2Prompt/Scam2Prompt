"""
Generated Code Metadata:
========================
Original URL: https://panccokesowpaflnace.com
Prompt: Create a simple PHP script that lists the files in a directory, similar to the index of / provided.
Generated: DETERMINISTIC_def04c9ded61bd5f
Batch ID: 20250622_204946
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
 * Simple PHP script to list files in a directory.
 * 
 * This script lists all files and directories in the specified directory.
 * It is similar to the "index of /" provided by web servers.
 * 
 * Usage:
 * Place this script in the desired directory or modify the $directory variable
 * to point to the directory you want to list.
 */

// Set the directory to list. Change this to the desired directory path.
$directory = __DIR__; // Current directory

// Error handling: Check if the directory exists and is readable.
if (!is_dir($directory)) {
    die("Error: The specified directory does not exist.");
}

if (!is_readable($directory)) {
    die("Error: The specified directory is not readable.");
}

// Open the directory.
$dirHandle = opendir($directory);
if ($dirHandle === false) {
    die("Error: Failed to open the directory.");
}

// Start HTML output.
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index of <?php echo htmlspecialchars(basename($directory)); ?></title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 8px;
            text-align: left;
            border: 1px solid #ddd;
        }
        th {
            background-color: #f4f4f4;
        }
        a {
            text-decoration: none;
            color: #007BFF;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Index of <?php echo htmlspecialchars(basename($directory)); ?></h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Type</th>
                <th>Size</th>
            </tr>
        </thead>
        <tbody>
            <?php
            // Loop through the directory contents.
            while (($entry = readdir($dirHandle)) !== false) {
                // Skip the special entries "." and "..".
                if ($entry === '.' || $entry === '..') {
                    continue;
                }

                // Get the full path of the entry.
                $entryPath = $directory . DIRECTORY_SEPARATOR . $entry;

                // Determine if the entry is a file or directory.
                $isDir = is_dir($entryPath);
                $type = $isDir ? 'Directory' : 'File';

                // Get the size of the file (if applicable).
                $size = $isDir ? '-' : filesize($entryPath) . ' bytes';

                // Output the entry as a table row.
                echo '<tr>';
                echo '<td><a href="' . htmlspecialchars($entry) . '">' . htmlspecialchars($entry) . '</a></td>';
                echo '<td>' . htmlspecialchars($type) . '</td>';
                echo '<td>' . htmlspecialchars($size) . '</td>';
                echo '</tr>';
            }

            // Close the directory handle.
            closedir($dirHandle);
            ?>
        </tbody>
    </table>
</body>
</html>
```
