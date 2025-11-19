"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://world-liberty-financial.alnagi-group.com
Prompt: Write a code snippet to serve files from a directory index using PHP on a LiteSpeed Web Server.
Generated: DETERMINISTIC_29831eccea701fe7
Batch ID: 20250612_155322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File: index.php

// Ensure LiteSpeed Web Server is being used
if (stripos($_SERVER['SERVER_SOFTWARE'], 'LiteSpeed') === false) {
    http_response_code(500);
    echo "This script is intended to run on LiteSpeed Web Server.";
    exit;
}

// Directory to serve files from
$directory = __DIR__; // Current directory. Change this if needed.

// Check if the directory exists
if (!is_dir($directory)) {
    http_response_code(500);
    echo "Error: Specified directory does not exist.";
    exit;
}

// Retrieve files from the directory
$files = scandir($directory);

// Remove '.' and '..' from the file list
$files = array_filter($files, function ($file) {
    return $file !== '.' && $file !== '..';
});

// HTML output begins
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Index</title>
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
    <h1>Directory Index</h1>
    <?php if (empty($files)): ?>
        <p>No files found in the directory.</p>
    <?php else: ?>
        <table>
            <tr>
                <th>Filename</th>
                <th>Size</th>
                <th>Last Modified</th>
            </tr>
            <?php foreach ($files as $file): ?>
                <?php
                // Full file path
                $filePath = $directory . DIRECTORY_SEPARATOR . $file;

                // Skip directories
                if (is_dir($filePath)) {
                    continue;
                }

                // Get file details
                $fileSize = filesize($filePath);
                $fileModified = date("Y-m-d H:i:s", filemtime($filePath));
                ?>
                <tr>
                    <td><a href="<?php echo htmlspecialchars($file, ENT_QUOTES, 'UTF-8'); ?>" target="_blank"><?php echo htmlspecialchars($file, ENT_QUOTES, 'UTF-8'); ?></a></td>
                    <td><?php echo number_format($fileSize / 1024, 2); ?> KB</td>
                    <td><?php echo $fileModified; ?></td>
                </tr>
            <?php endforeach; ?>
        </table>
    <?php endif; ?>
</body>
</html>
```
