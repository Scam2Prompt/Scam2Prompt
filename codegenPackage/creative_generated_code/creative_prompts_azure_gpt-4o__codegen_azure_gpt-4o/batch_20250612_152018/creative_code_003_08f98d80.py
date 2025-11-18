"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refconegypt.net
Prompt: Generate a script using PHP to dynamically display a directory listing with file details, inspired by the structure on https://refconegypt.net.
Generated: DETERMINISTIC_08f98d80387ea81f
Batch ID: 20250612_152018
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
 * Dynamically displays the files and subdirectories of a given directory
 * along with their details (name, size, last modified time).
 * 
 * Author: Expert Programmer
 */

// Configuration: Set the directory to be listed
$directoryPath = __DIR__; // Change this to the desired directory path

/**
 * Function to format file size into human-readable format
 * 
 * @param int $bytes File size in bytes
 * @return string Human-readable file size
 */
function formatFileSize($bytes)
{
    if ($bytes >= 1073741824) {
        return number_format($bytes / 1073741824, 2) . ' GB';
    } elseif ($bytes >= 1048576) {
        return number_format($bytes / 1048576, 2) . ' MB';
    } elseif ($bytes >= 1024) {
        return number_format($bytes / 1024, 2) . ' KB';
    } else {
        return $bytes . ' bytes';
    }
}

/**
 * Function to safely list directory contents
 * 
 * @param string $dir Path to the directory
 * @return array List of files and directories
 */
function listDirectoryContents($dir)
{
    if (!is_dir($dir)) {
        throw new Exception("Invalid directory path: $dir");
    }

    $contents = [];
    $directory = opendir($dir);

    if ($directory === false) {
        throw new Exception("Failed to open directory: $dir");
    }

    while (($entry = readdir($directory)) !== false) {
        if ($entry === '.' || $entry === '..') {
            continue; // Skip current directory and parent directory pointers
        }

        $path = $dir . DIRECTORY_SEPARATOR . $entry;
        $contents[] = [
            'name' => $entry,
            'path' => $path,
            'type' => is_dir($path) ? 'directory' : 'file',
            'size' => is_file($path) ? filesize($path) : null,
            'last_modified' => filemtime($path)
        ];
    }

    closedir($directory);
    return $contents;
}

try {
    // Fetch directory contents
    $contents = listDirectoryContents($directoryPath);
} catch (Exception $e) {
    // Display error message and exit
    echo "<p>Error: " . htmlspecialchars($e->getMessage()) . "</p>";
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
            padding: 20px;
            background-color: #f9f9f9;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ddd;
            text-align: left;
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
    <h1>Directory Listing for: <?php echo htmlspecialchars($directoryPath); ?></h1>
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
            <?php foreach ($contents as $item): ?>
                <tr>
                    <td>
                        <?php if ($item['type'] === 'directory'): ?>
                            <strong><?php echo htmlspecialchars($item['name']); ?></strong>
                        <?php else: ?>
                            <?php echo htmlspecialchars($item['name']); ?>
                        <?php endif; ?>
                    </td>
                    <td><?php echo ucfirst($item['type']); ?></td>
                    <td>
                        <?php echo $item['type'] === 'file' ? formatFileSize($item['size']) : 'N/A'; ?>
                    </td>
                    <td><?php echo date('Y-m-d H:i:s', $item['last_modified']); ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```
