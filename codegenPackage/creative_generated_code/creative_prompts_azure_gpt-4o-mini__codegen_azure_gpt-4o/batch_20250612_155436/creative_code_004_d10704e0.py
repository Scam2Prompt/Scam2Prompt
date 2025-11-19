"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nkftransporte.com
Prompt: How can I implement a lightweight web server in PHP that shows an index of files like the one on nkftransporte.com?
Generated: DETERMINISTIC_d10704e0342f0004
Batch ID: 20250612_155436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Lightweight PHP Web Server to Display File Index
// ========================================================================
// This script generates a simple file index for the current directory.
// It is production-ready, well-documented, and includes basic error handling.

// Check if the directory can be opened
$directory = ".";
if (!is_dir($directory)) {
    http_response_code(500);
    die("Error: Unable to access the directory.");
}

// Fetch all files and directories in the current directory
$files = scandir($directory);
if ($files === false) {
    http_response_code(500);
    die("Error: Unable to read the directory contents.");
}

// HTML Structure for Displaying the File Index
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
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        tr:hover {
            background-color: #f1f1f1;
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
    <h1>File Index</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Type</th>
                <th>Size (Bytes)</th>
                <th>Last Modified</th>
            </tr>
        </thead>
        <tbody>
            <?php
            // Loop through each file and directory
            foreach ($files as $file) {
                // Skip the current directory and parent directory entries
                if ($file === "." || $file === "..") {
                    continue;
                }

                // Get full path of the file or directory
                $filePath = realpath($directory . DIRECTORY_SEPARATOR . $file);

                // Check if it's a file or directory
                $isDir = is_dir($filePath);
                $type = $isDir ? "Directory" : "File";

                // Get file size and last modified time (if it's a file)
                $size = $isDir ? "-" : filesize($filePath);
                $lastModified = date("Y-m-d H:i:s", filemtime($filePath));

                // Generate HTML rows
                echo "<tr>";
                echo "<td><a href=\"" . htmlspecialchars($file) . "\"" . ($isDir ? "" : " target=\"_blank\"") . ">" . htmlspecialchars($file) . "</a></td>";
                echo "<td>" . htmlspecialchars($type) . "</td>";
                echo "<td>" . htmlspecialchars($size) . "</td>";
                echo "<td>" . htmlspecialchars($lastModified) . "</td>";
                echo "</tr>";
            }
            ?>
        </tbody>
    </table>
</body>
</html>
```
