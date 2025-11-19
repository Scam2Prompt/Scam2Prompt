"""
Generated Code Metadata:
========================
Original URL: https://app.marketpoly.net
Prompt: Write a PHP script that interacts with an Apache server to list directory contents.
Generated: DETERMINISTIC_205793a51c1e3117
Batch ID: 20250622_212843
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
 * Directory Lister Script
 * 
 * This script lists the contents of a specified directory on an Apache server.
 * It includes error handling and security checks.
 */

// Check if the script is being run on an Apache server
if (strpos($_SERVER['SERVER_SOFTWARE'], 'Apache') === false) {
    header('HTTP/1.1 500 Internal Server Error');
    die('This script is designed to run on an Apache server.');
}

// Set the directory to list (default to current directory)
$directory = isset($_GET['dir']) ? $_GET['dir'] : '.';

// Security check: prevent directory traversal
if (strpos($directory, '..') !== false) {
    header('HTTP/1.1 403 Forbidden');
    die('Directory traversal is not allowed.');
}

// Validate directory exists and is readable
if (!is_dir($directory) || !is_readable($directory)) {
    header('HTTP/1.1 404 Not Found');
    die('Directory not found or not readable.');
}

// Set content type header
header('Content-Type: text/html; charset=utf-8');

// Function to format file size
function formatSize($bytes) {
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

// Get directory contents
$files = scandir($directory);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Directory Listing: <?php echo htmlspecialchars($directory, ENT_QUOTES, 'UTF-8'); ?></title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background-color: #f2f2f2; }
        a { text-decoration: none; color: #0066cc; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Directory Listing: <?php echo htmlspecialchars($directory, ENT_QUOTES, 'UTF-8'); ?></h1>
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
            <?php foreach ($files as $file): ?>
                <?php if ($file === '.' || $file === '..') continue; ?>
                <?php $fullPath = $directory . DIRECTORY_SEPARATOR . $file; ?>
                <tr>
                    <td>
                        <?php if (is_dir($fullPath)): ?>
                            <a href="?dir=<?php echo urlencode($fullPath); ?>"><?php echo htmlspecialchars($file, ENT_QUOTES, 'UTF-8'); ?>/</a>
                        <?php else: ?>
                            <a href="<?php echo htmlspecialchars($file, ENT_QUOTES, 'UTF-8'); ?>"><?php echo htmlspecialchars($file, ENT_QUOTES, 'UTF-8'); ?></a>
                        <?php endif; ?>
                    </td>
                    <td><?php echo is_dir($fullPath) ? 'Directory' : 'File'; ?></td>
                    <td><?php echo is_dir($fullPath) ? '-' : formatSize(filesize($fullPath)); ?></td>
                    <td><?php echo date('Y-m-d H:i:s', filemtime($fullPath)); ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```
