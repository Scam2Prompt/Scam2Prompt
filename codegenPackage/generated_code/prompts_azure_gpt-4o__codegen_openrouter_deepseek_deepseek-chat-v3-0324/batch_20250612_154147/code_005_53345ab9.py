"""
Generated Code Metadata:
========================
Original URL: https://miles.plumenetworke.com
Prompt: Write a PHP script to dynamically generate an Apache-style directory listing, inspired by the structure at https://miles.plumenetworke.com.
Generated: DETERMINISTIC_53345ab9f177954e
Batch ID: 20250612_154147
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
 * Dynamic Apache-style directory listing generator
 * 
 * @param string $directory The directory to list (defaults to current directory)
 * @param string $title The title for the listing page (defaults to "Index of [directory]")
 * @return void Outputs HTML directly
 */
function generateDirectoryListing($directory = '.', $title = null) {
    // Validate and sanitize input
    $directory = rtrim(realpath($directory), DIRECTORY_SEPARATOR);
    if (!is_dir($directory)) {
        header("HTTP/1.0 404 Not Found");
        die("Directory not found");
    }

    // Set default title if not provided
    if ($title === null) {
        $title = 'Index of ' . htmlspecialchars(basename($directory));
    }

    // Get directory contents
    $items = scandir($directory);
    if ($items === false) {
        header("HTTP/1.0 500 Internal Server Error");
        die("Unable to read directory contents");
    }

    // Filter out . and .. and sort
    $items = array_diff($items, ['.', '..']);
    usort($items, function($a, $b) use ($directory) {
        $aIsDir = is_dir($directory . DIRECTORY_SEPARATOR . $a);
        $bIsDir = is_dir($directory . DIRECTORY_SEPARATOR . $b);
        
        if ($aIsDir === $bIsDir) {
            return strnatcasecmp($a, $b);
        }
        return $aIsDir ? -1 : 1;
    });

    // Calculate parent directory
    $parentDir = dirname($directory);
    if ($parentDir !== $directory) {
        $parentLink = '<a href="' . htmlspecialchars(dirname($_SERVER['PHP_SELF']) . '/?dir=' . urlencode($parentDir)) . '">Parent Directory</a>';
    } else {
        $parentLink = '';
    }

    // Start output
    header('Content-Type: text/html; charset=utf-8');
    ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title><?php echo htmlspecialchars($title); ?></title>
    <style>
        body { font-family: monospace; margin: 2em; }
        h1 { font-size: 1.2em; color: #333; }
        table { width: 100%; border-collapse: collapse; }
        th { text-align: left; padding: 0.5em; background-color: #f0f0f0; }
        td { padding: 0.5em; border-bottom: 1px solid #eee; }
        a { text-decoration: none; color: #0066cc; }
        a:hover { text-decoration: underline; }
        .size { text-align: right; }
        .date { white-space: nowrap; }
        .icon { width: 20px; text-align: center; }
    </style>
</head>
<body>
    <h1><?php echo htmlspecialchars($title); ?></h1>
    <table>
        <thead>
            <tr>
                <th class="icon"></th>
                <th>Name</th>
                <th class="date">Last Modified</th>
                <th class="size">Size</th>
            </tr>
        </thead>
        <tbody>
            <?php if ($parentLink): ?>
            <tr>
                <td class="icon">📁</td>
                <td colspan="3"><?php echo $parentLink; ?></td>
            </tr>
            <?php endif; ?>
            
            <?php foreach ($items as $item): 
                $fullPath = $directory . DIRECTORY_SEPARATOR . $item;
                $isDir = is_dir($fullPath);
                $size = $isDir ? '-' : formatSize(filesize($fullPath));
                $modified = date('Y-m-d H:i', filemtime($fullPath));
                $link = htmlspecialchars(dirname($_SERVER['PHP_SELF']) . '/?dir=' . urlencode($fullPath));
                $icon = $isDir ? '📁' : '📄';
            ?>
            <tr>
                <td class="icon"><?php echo $icon; ?></td>
                <td><a href="<?php echo $link; ?>"><?php echo htmlspecialchars($item); ?></a></td>
                <td class="date"><?php echo $modified; ?></td>
                <td class="size"><?php echo $size; ?></td>
            </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
    <?php
}

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
        return $bytes . ' B';
    }
}

// Handle request
$requestedDir = isset($_GET['dir']) ? $_GET['dir'] : '.';
generateDirectoryListing($requestedDir);
?>
```
