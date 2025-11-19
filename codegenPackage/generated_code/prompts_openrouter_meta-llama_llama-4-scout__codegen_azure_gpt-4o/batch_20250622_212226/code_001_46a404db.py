"""
Generated Code Metadata:
========================
Original URL: https://robilliardag.com
Prompt: Write a PHP script that generates an index of files in a directory, similar to the one displayed on Rob Billillard's website.
Generated: DETERMINISTIC_46a404db93e2fa29
Batch ID: 20250622_212226
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
 * File Index Generator
 * 
 * This script generates an index of files in a specified directory.
 * It displays the file name, size, and last modified date in a table format.
 * 
 * Usage: Place this script in the desired directory or modify the $directory variable.
 */

// Set the directory to scan (default is the current directory)
$directory = __DIR__;

// Check if the directory exists
if (!is_dir($directory)) {
    die("Error: The specified directory does not exist.");
}

// Get the list of files in the directory
$files = scandir($directory);

// Filter out '.' and '..' entries
$files = array_filter($files, function ($file) use ($directory) {
    return is_file($directory . DIRECTORY_SEPARATOR . $file);
});

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
            text-align: left;
        }
        th {
            background-color: #f4f4f4;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        tr:hover {
            background-color: #f1f1f1;
        }
    </style>
</head>
<body>
    <h1>File Index</h1>
    <table>
        <thead>
            <tr>
                <th>File Name</th>
                <th>Size (KB)</th>
                <th>Last Modified</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($files as $file): ?>
                <tr>
                    <td>
                        <a href="<?php echo htmlspecialchars($file); ?>" target="_blank">
                            <?php echo htmlspecialchars($file); ?>
                        </a>
                    </td>
                    <td>
                        <?php echo number_format(filesize($directory . DIRECTORY_SEPARATOR . $file) / 1024, 2); ?>
                    </td>
                    <td>
                        <?php echo date("Y-m-d H:i:s", filemtime($directory . DIRECTORY_SEPARATOR . $file)); ?>
                    </td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```
