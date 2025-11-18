"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlayer.eigenda.cc
Prompt: Write a PHP script that dynamically generates a directory listing similar to the one shown at `https://eigenlayer.eigenda.cc`, including file size and last modified date.
Generated: DETERMINISTIC_b8c103335f754307
Batch ID: 20250612_153812
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
 * This script dynamically generates a directory listing, including file sizes 
 * and last modified dates. It is designed to be clean, efficient, and well-documented.
 * 
 * Usage: Place this script in the directory you want to list. Access it via a browser.
 */

// Define the directory to be listed (current directory by default).
$directory = __DIR__;

try {
    // Check if the directory exists and is readable.
    if (!is_dir($directory) || !is_readable($directory)) {
        throw new Exception("Directory not found or not readable.");
    }

    // Open the directory.
    $dirHandle = opendir($directory);
    if (!$dirHandle) {
        throw new Exception("Failed to open directory.");
    }

    // Prepare an array to hold file information.
    $files = [];

    // Loop through the directory entries.
    while (($entry = readdir($dirHandle)) !== false) {
        // Skip the current and parent directory references.
        if ($entry === '.' || $entry === '..') {
            continue;
        }

        // Get the full path of the entry.
        $entryPath = $directory . DIRECTORY_SEPARATOR . $entry;

        // Collect file information.
        $files[] = [
            'name' => $entry,
            'type' => is_dir($entryPath) ? 'Directory' : 'File',
            'size' => is_file($entryPath) ? filesize($entryPath) : '-',
            'last_modified' => date('Y-m-d H:i:s', filemtime($entryPath))
        ];
    }

    // Close the directory handle.
    closedir($dirHandle);

    // Sort files alphabetically by name.
    usort($files, function ($a, $b) {
        return strcasecmp($a['name'], $b['name']);
    });
} catch (Exception $e) {
    // Handle errors gracefully.
    die("Error: " . htmlspecialchars($e->getMessage()));
}

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
            border: 1px solid #ddd;
            padding: 8px;
        }
        th {
            background-color: #f4f4f4;
            text-align: left;
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
                <th>Size (bytes)</th>
                <th>Last Modified</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($files as $file): ?>
                <tr>
                    <td>
                        <?php if ($file['type'] === 'Directory'): ?>
                            <a href="<?= htmlspecialchars($file['name']) ?>/"><?= htmlspecialchars($file['name']) ?></a>
                        <?php else: ?>
                            <a href="<?= htmlspecialchars($file['name']) ?>"><?= htmlspecialchars($file['name']) ?></a>
                        <?php endif; ?>
                    </td>
                    <td><?= htmlspecialchars($file['type']) ?></td>
                    <td><?= htmlspecialchars($file['size']) ?></td>
                    <td><?= htmlspecialchars($file['last_modified']) ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```
