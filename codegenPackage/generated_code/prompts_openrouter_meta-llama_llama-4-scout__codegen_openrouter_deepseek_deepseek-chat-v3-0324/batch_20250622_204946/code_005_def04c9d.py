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
 * Simple directory listing script
 * 
 * Lists files and directories in the current directory with basic information
 * similar to Apache's directory index.
 */

// Set the directory to list (defaults to current directory)
$directory = isset($_GET['dir']) ? $_GET['dir'] : '.';

// Security check: prevent directory traversal
$directory = realpath($directory);
if ($directory === false || strpos($directory, realpath('.')) !== 0) {
    header('HTTP/1.1 403 Forbidden');
    die('Access denied');
}

// Check if the path is a directory
if (!is_dir($directory)) {
    header('HTTP/1.1 404 Not Found');
    die('Directory not found');
}

// Get directory contents
$files = scandir($directory);
if ($files === false) {
    header('HTTP/1.1 500 Internal Server Error');
    die('Unable to read directory');
}

// Filter out . and .. entries
$files = array_diff($files, array('.', '..'));

// Sort files alphabetically
sort($files);

// Set content type and charset
header('Content-Type: text/html; charset=utf-8');

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Index of <?php echo htmlspecialchars($directory); ?></title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background-color: #f2f2f2; }
        tr:hover { background-color: #f5f5f5; }
        a { text-decoration: none; color: #0066cc; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Index of <?php echo htmlspecialchars($directory); ?></h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Last Modified</th>
                <th>Size</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($files as $file): ?>
                <?php
                $filePath = $directory . DIRECTORY_SEPARATOR . $file;
                $isDir = is_dir($filePath);
                $lastModified = date('Y-m-d H:i:s', filemtime($filePath));
                $size = $isDir ? '-' : filesize($filePath);
                $sizeFormatted = $isDir ? '-' : formatSize($size);
                ?>
                <tr>
                    <td>
                        <a href="<?php echo htmlspecialchars($file . ($isDir ? '/' : '')); ?>">
                            <?php echo htmlspecialchars($file); ?>
                            <?php if ($isDir): ?>/<?php endif; ?>
                        </a>
                    </td>
                    <td><?php echo $lastModified; ?></td>
                    <td><?php echo $sizeFormatted; ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>

<?php
/**
 * Format file size in human-readable format
 *
 * @param int $bytes File size in bytes
 * @return string Formatted size with appropriate unit
 */
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
?>
```
