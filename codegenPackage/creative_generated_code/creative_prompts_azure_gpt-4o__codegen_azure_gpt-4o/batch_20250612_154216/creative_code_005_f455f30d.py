"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perurest.com
Prompt: Write a PHP script to dynamically display directory contents served by LiteSpeed Web Server in a user-friendly format.
Generated: DETERMINISTIC_f455f30dc6e35bca
Batch ID: 20250612_154216
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
 * Dynamic Directory Listing Script for LiteSpeed Web Server
 * 
 * This script lists the contents of a directory in a user-friendly format,
 * including files and subdirectories, with proper error handling.
 *
 * Requirements:
 * - PHP enabled on LiteSpeed Web Server.
 *
 * Author: Professional Software Developer
 * License: MIT
 */

declare(strict_types=1);

// Configuration
$directory = __DIR__; // Current directory; change this to target another directory

/**
 * Function to escape HTML entities for safe output
 * 
 * @param string $string
 * @return string
 */
function escapeHtml(string $string): string
{
    return htmlspecialchars($string, ENT_QUOTES | ENT_HTML5, 'UTF-8');
}

try {
    // Ensure the directory exists and is readable
    if (!is_dir($directory)) {
        throw new RuntimeException("Directory not found: {$directory}");
    }

    if (!is_readable($directory)) {
        throw new RuntimeException("Directory is not readable: {$directory}");
    }

    // Open the directory handle
    $dirHandle = opendir($directory);
    if (!$dirHandle) {
        throw new RuntimeException("Failed to open directory: {$directory}");
    }

    // Generate the directory listing
    $entries = [];
    while (($entry = readdir($dirHandle)) !== false) {
        if ($entry === '.' || $entry === '..') {
            continue; // Skip current and parent directory references
        }

        $entryPath = $directory . DIRECTORY_SEPARATOR . $entry;
        $entries[] = [
            'name' => $entry,
            'is_dir' => is_dir($entryPath),
            'size' => is_file($entryPath) ? filesize($entryPath) : null,
            'last_modified' => filemtime($entryPath),
        ];
    }

    closedir($dirHandle);

    // Sort entries alphabetically (directories first, then files)
    usort($entries, function ($a, $b) {
        if ($a['is_dir'] === $b['is_dir']) {
            return strcasecmp($a['name'], $b['name']);
        }
        return $a['is_dir'] ? -1 : 1;
    });

} catch (Exception $e) {
    // Display error message
    http_response_code(500);
    echo "<h1>Error</h1>";
    echo "<p>" . escapeHtml($e->getMessage()) . "</p>";
    exit;
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
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ddd;
            text-align: left;
        }
        th {
            background-color: #f4f4f4;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
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
    <h1>Directory Listing for: <?= escapeHtml(basename($directory)) ?></h1>
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
            <?php foreach ($entries as $entry): ?>
                <tr>
                    <td>
                        <?php if ($entry['is_dir']): ?>
                            <a href="<?= escapeHtml($entry['name']) ?>/"><?= escapeHtml($entry['name']) ?></a>
                        <?php else: ?>
                            <a href="<?= escapeHtml($entry['name']) ?>"><?= escapeHtml($entry['name']) ?></a>
                        <?php endif; ?>
                    </td>
                    <td><?= $entry['is_dir'] ? 'Directory' : 'File' ?></td>
                    <td><?= $entry['size'] !== null ? number_format($entry['size']) . ' bytes' : '-' ?></td>
                    <td><?= date('Y-m-d H:i:s', $entry['last_modified']) ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```
