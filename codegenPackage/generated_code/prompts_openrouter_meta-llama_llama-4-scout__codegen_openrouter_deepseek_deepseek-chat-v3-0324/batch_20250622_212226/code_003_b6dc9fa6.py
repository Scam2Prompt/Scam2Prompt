"""
Generated Code Metadata:
========================
Original URL: https://robilliardag.com
Prompt: How would you modify the `style.php` file to include additional information about each file, such as file type or last modified date, and write the modified code?
Generated: DETERMINISTIC_b6dc9fa6ca7a11bf
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
 * style.php - Displays directory contents with enhanced file information
 */

// Check if directory path is provided
if (!isset($_GET['dir'])) {
    die("Error: No directory specified.");
}

$dir = $_GET['dir'];

// Sanitize directory path
$dir = rtrim($dir, '/');
$dir = str_replace('..', '', $dir);

// Check if directory exists and is readable
if (!is_dir($dir) || !is_readable($dir)) {
    die("Error: Directory does not exist or is not readable.");
}

// Get directory contents
$files = scandir($dir);
if ($files === false) {
    die("Error: Could not read directory contents.");
}

// Filter out . and .. entries
$files = array_diff($files, array('.', '..'));

// Function to get file type
function getFileType($file) {
    if (is_dir($file)) {
        return 'Directory';
    } elseif (is_link($file)) {
        return 'Symlink';
    } else {
        $ext = pathinfo($file, PATHINFO_EXTENSION);
        return $ext ? strtoupper($ext) . ' File' : 'File';
    }
}

// Function to format file size
function formatSize($bytes) {
    if ($bytes < 1024) {
        return $bytes . ' B';
    } elseif ($bytes < 1048576) {
        return round($bytes / 1024, 2) . ' KB';
    } else {
        return round($bytes / 1048576, 2) . ' MB';
    }
}

// Output HTML
?>
<!DOCTYPE html>
<html>
<head>
    <title>Directory Listing: <?php echo htmlspecialchars($dir); ?></title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background-color: #f2f2f2; }
        tr:hover { background-color: #f5f5f5; }
    </style>
</head>
<body>
    <h1>Directory Listing: <?php echo htmlspecialchars($dir); ?></h1>
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
                <?php
                $filepath = $dir . '/' . $file;
                $filetype = getFileType($filepath);
                $filesize = is_dir($filepath) ? '-' : formatSize(filesize($filepath));
                $lastmod = date("Y-m-d H:i:s", filemtime($filepath));
                ?>
                <tr>
                    <td>
                        <?php if (is_dir($filepath)): ?>
                            <a href="?dir=<?php echo urlencode($filepath); ?>"><?php echo htmlspecialchars($file); ?>/</a>
                        <?php else: ?>
                            <a href="<?php echo htmlspecialchars($filepath); ?>"><?php echo htmlspecialchars($file); ?></a>
                        <?php endif; ?>
                    </td>
                    <td><?php echo htmlspecialchars($filetype); ?></td>
                    <td><?php echo htmlspecialchars($filesize); ?></td>
                    <td><?php echo htmlspecialchars($lastmod); ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```
