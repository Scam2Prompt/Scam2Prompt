"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ouatvs.com
Prompt: Provide an example of configuring a LiteSpeed Web Server to display directory listings with custom formatting, including file metadata such as size and modification date.
Generated: DETERMINISTIC_39759df04c01530d
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of configuring LiteSpeed Web Server to display custom directory listings with specific formatting. This involves using a custom PHP script for formatting the file metadata:

```php
<?php
/**
 * Directory Listing Script for LiteSpeed Web Server
 * This script creates custom directory listings with file metadata such as size and modification date.
 * Save this file as index.php in the directory you want to list.
 */

// Error reporting for development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Get the directory to list
$directory = __DIR__;

// Open the directory
if (!is_dir($directory) || !($handle = opendir($directory))) {
    die("Failed to open directory.");
}

// Create an array to store file information
$fileList = [];

// Read files and directories
while (($entry = readdir($handle)) !== false) {
    // Skip '.' and '..'
    if ($entry === '.' || $entry === '..') {
        continue;
    }

    // Get full path
    $fullPath = $directory . DIRECTORY_SEPARATOR . $entry;

    // Gather file metadata
    $fileInfo = [
        'name' => $entry,
        'size' => is_file($fullPath) ? filesize($fullPath) : '-',
        'modified' => date('Y-m-d H:i:s', filemtime($fullPath)),
        'type' => is_file($fullPath) ? 'File' : 'Directory',
    ];

    // Add file metadata to the list
    $fileList[] = $fileInfo;
}

// Close the directory handle
closedir($handle);

// Sort files alphabetically
usort($fileList, fn($a, $b) => strcmp($a['name'], $b['name']));

// HTML output begins
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
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #f4f4f4;
        }
        tr:hover {
            background-color: #f1f1f1;
        }
    </style>
</head>
<body>
    <h1>Directory Listing</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Type</th>
                <th>Size</th>
                <th>Last Modified</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($fileList as $file): ?>
                <tr>
                    <td>
                        <?php if ($file['type'] === 'Directory'): ?>
                            <a href="<?= htmlspecialchars($file['name']) ?>"><?= htmlspecialchars($file['name']) ?></a>
                        <?php else: ?>
                            <?= htmlspecialchars($file['name']) ?>
                        <?php endif; ?>
                    </td>
                    <td><?= htmlspecialchars($file['type']) ?></td>
                    <td><?= htmlspecialchars($file['size']) ?></td>
                    <td><?= htmlspecialchars($file['modified']) ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```

### How to Use
1. Save this script as `index.php` in the directory you want to list.
2. Ensure LiteSpeed Web Server is configured to allow `index.php` as a directory index file:
   - Go to your LiteSpeed Web Server configuration and ensure `index.php` is included in the list of index files.
3. Access the directory in your browser. The custom directory listing with file metadata will be displayed.

### Notes:
- For production, disable error reporting (`error_reporting(0)`).
- Ensure proper permissions for the script to access the directory contents.
