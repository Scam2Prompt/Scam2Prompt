"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omni.newtork.cc
Prompt: Generate a PHP script that retrieves and displays the index of files from a specified directory on an Apache server.
Generated: DETERMINISTIC_57c104a61914cade
Batch ID: 20250612_163231
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
 * File Indexer Script
 * 
 * This script retrieves and displays a list of files in the specified directory.
 * It is designed to run on an Apache server.
 * 
 * Usage:
 * 1. Place this script in your desired location on the server.
 * 2. Modify the `$directoryPath` variable to point to the target directory.
 * 3. Ensure appropriate permissions are set for the directory.
 */

// Configuration: Specify the directory to scan
$directoryPath = __DIR__; // Change this to the desired directory path, e.g., '/var/www/html/files'

// Error handling: Check if the directory exists and is readable
if (!is_dir($directoryPath)) {
    http_response_code(400); // Bad request
    die("Error: The specified directory does not exist.");
}

if (!is_readable($directoryPath)) {
    http_response_code(403); // Forbidden
    die("Error: The specified directory is not readable.");
}

// Retrieve the list of files in the directory
$fileList = scandir($directoryPath);

// Error handling: Check if scandir succeeded
if ($fileList === false) {
    http_response_code(500); // Internal Server Error
    die("Error: Failed to retrieve the file list.");
}

// Output the file index
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Index</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
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
    <h1>File Index for Directory: <?php echo htmlspecialchars($directoryPath); ?></h1>
    <table>
        <thead>
            <tr>
                <th>#</th>
                <th>File Name</th>
            </tr>
        </thead>
        <tbody>
            <?php
            // Iterate through the file list and display each file
            $index = 1;
            foreach ($fileList as $file) {
                // Skip '.' and '..'
                if ($file === '.' || $file === '..') {
                    continue;
                }
                echo '<tr>';
                echo '<td>' . $index++ . '</td>';
                echo '<td>' . htmlspecialchars($file) . '</td>';
                echo '</tr>';
            }
            ?>
        </tbody>
    </table>
</body>
</html>
```
