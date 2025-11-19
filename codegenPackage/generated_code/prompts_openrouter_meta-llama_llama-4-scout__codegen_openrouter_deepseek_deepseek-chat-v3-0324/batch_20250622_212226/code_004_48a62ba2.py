"""
Generated Code Metadata:
========================
Original URL: https://robilliardag.com
Prompt: Design a simple file explorer interface using PHP and HTML, inspired by the directory listing on Rob Billillard's website.
Generated: DETERMINISTIC_48a62ba289ced801
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
 * Simple File Explorer
 * Inspired by Rob Billillard's directory listing
 */

// Configuration
$baseDir = '.'; // Directory to explore (default: current directory)
$allowedExtensions = ['php', 'html', 'txt', 'md', 'pdf', 'jpg', 'png', 'gif']; // Allowed file extensions
$ignoreFiles = ['.', '..', '.htaccess', '.gitignore']; // Files/directories to ignore

// Security check
if (isset($_GET['dir'])) {
    $requestedDir = realpath($_GET['dir']);
    $basePath = realpath($baseDir);
    
    if (strpos($requestedDir, $basePath) !== 0) {
        die('Access denied: Attempt to access directory outside allowed path');
    }
    $baseDir = $requestedDir;
}

/**
 * Get directory contents
 * @param string $dir Directory path
 * @return array Array of files and directories
 */
function getDirectoryContents($dir) {
    global $ignoreFiles, $allowedExtensions;
    
    $contents = [];
    if (is_dir($dir)) {
        $items = scandir($dir);
        
        foreach ($items as $item) {
            if (in_array($item, $ignoreFiles)) continue;
            
            $path = $dir . DIRECTORY_SEPARATOR . $item;
            $isDir = is_dir($path);
            $extension = pathinfo($item, PATHINFO_EXTENSION);
            
            if (!$isDir && !empty($allowedExtensions) && !in_array(strtolower($extension), $allowedExtensions)) {
                continue;
            }
            
            $contents[] = [
                'name' => $item,
                'path' => $path,
                'is_dir' => $isDir,
                'size' => $isDir ? '' : formatSize(filesize($path)),
                'modified' => date('Y-m-d H:i:s', filemtime($path))
            ];
        }
    }
    return $contents;
}

/**
 * Format file size
 * @param int $bytes File size in bytes
 * @return string Formatted size
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

// Get current directory contents
$contents = getDirectoryContents($baseDir);
$parentDir = dirname($baseDir);

// HTML output
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Explorer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        h1 {
            color: #444;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            padding: 8px 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #f5f5f5;
        }
        tr:hover {
            background-color: #f9f9f9;
        }
        a {
            color: #0066cc;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .dir-icon {
            color: #ff9900;
        }
        .file-icon {
            color: #666;
        }
    </style>
</head>
<body>
    <h1>File Explorer: <?php echo htmlspecialchars($baseDir); ?></h1>
    
    <?php if ($parentDir !== $baseDir): ?>
        <p><a href="?dir=<?php echo urlencode($parentDir); ?>">↑ Parent Directory</a></p>
    <?php endif; ?>
    
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Size</th>
                <th>Modified</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($contents as $item): ?>
                <tr>
                    <td>
                        <?php if ($item['is_dir']): ?>
                            <span class="dir-icon">📁</span>
                            <a href="?dir=<?php echo urlencode($item['path']); ?>"><?php echo htmlspecialchars($item['name']); ?></a>
                        <?php else: ?>
                            <span class="file-icon">📄</span>
                            <a href="<?php echo htmlspecialchars($item['path']); ?>" target="_blank"><?php echo htmlspecialchars($item['name']); ?></a>
                        <?php endif; ?>
                    </td>
                    <td><?php echo $item['size']; ?></td>
                    <td><?php echo $item['modified']; ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```
