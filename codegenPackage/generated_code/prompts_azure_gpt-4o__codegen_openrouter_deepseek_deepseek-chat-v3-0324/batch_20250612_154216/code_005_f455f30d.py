"""
Generated Code Metadata:
========================
Original URL: https://perurest.com
Prompt: Write a PHP script to dynamically display directory contents served by LiteSpeed Web Server in a user-friendly format.
Generated: DETERMINISTIC_f455f30dc6e35bca
Batch ID: 20250612_154216
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
 * Directory Lister for LiteSpeed Web Server
 * 
 * This script dynamically displays the contents of a directory in a user-friendly format.
 * It includes file icons, sizes, last modified dates, and provides navigation.
 */

// Configuration
$baseDir = __DIR__; // Current directory or set to specific path like '/var/www/html'
$allowedExtensions = ['php', 'html', 'css', 'js', 'jpg', 'png', 'gif', 'pdf', 'txt', 'zip'];
$excludedFiles = ['.', '..', '.htaccess', '.gitignore'];
$title = 'Directory Listing';

// Security check - ensure we're only serving allowed directories
if (!is_dir($baseDir)) {
    die('Error: Invalid directory specified');
}

// Get directory contents
try {
    $files = scandir($baseDir);
    if ($files === false) {
        throw new Exception('Unable to scan directory');
    }
    
    $fileList = [];
    foreach ($files as $file) {
        if (!in_array($file, $excludedFiles)) {
            $filePath = $baseDir . DIRECTORY_SEPARATOR . $file;
            $fileList[] = [
                'name' => $file,
                'path' => $filePath,
                'is_dir' => is_dir($filePath),
                'size' => filesize($filePath),
                'modified' => filemtime($filePath),
                'extension' => pathinfo($file, PATHINFO_EXTENSION)
            ];
        }
    }
    
    // Sort directories first, then files
    usort($fileList, function($a, $b) {
        if ($a['is_dir'] === $b['is_dir']) {
            return strcasecmp($a['name'], $b['name']);
        }
        return $a['is_dir'] ? -1 : 1;
    });

} catch (Exception $e) {
    die('Error: ' . $e->getMessage());
}

// Function to get icon for file type
function getFileIcon($file) {
    $extension = strtolower($file['extension']);
    
    $iconMap = [
        'dir' => '📁',
        'php' => '🐘',
        'html' => '🌐',
        'css' => '🎨',
        'js' => '📜',
        'jpg' => '🖼️',
        'png' => '🖼️',
        'gif' => '🖼️',
        'pdf' => '📄',
        'txt' => '📝',
        'zip' => '🗜️'
    ];
    
    return $file['is_dir'] ? $iconMap['dir'] : ($iconMap[$extension] ?? '📄');
}

// Function to format file size
function formatSize($bytes) {
    if ($bytes < 1024) return $bytes . ' B';
    elseif ($bytes < 1048576) return round($bytes / 1024, 2) . ' KB';
    elseif ($bytes < 1073741824) return round($bytes / 1048576, 2) . ' MB';
    else return round($bytes / 1073741824, 2) . ' GB';
}

// HTML Output
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo htmlspecialchars($title); ?></title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            margin-top: 0;
            color: #333;
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
            background-color: #f2f2f2;
        }
        tr:hover {
            background-color: #f9f9f9;
        }
        .icon {
            font-size: 1.2em;
            margin-right: 5px;
        }
        .dir {
            font-weight: bold;
        }
        .breadcrumb {
            margin-bottom: 20px;
            padding: 10px;
            background: #f2f2f2;
            border-radius: 3px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1><?php echo htmlspecialchars($title); ?></h1>
        
        <div class="breadcrumb">
            <?php echo htmlspecialchars($baseDir); ?>
        </div>
        
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Size</th>
                    <th>Modified</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($fileList as $file): ?>
                <tr>
                    <td>
                        <span class="icon"><?php echo getFileIcon($file); ?></span>
                        <?php if ($file['is_dir']): ?>
                            <a href="<?php echo htmlspecialchars($file['name']); ?>/" class="dir"><?php echo htmlspecialchars($file['name']); ?></a>
                        <?php else: ?>
                            <a href="<?php echo htmlspecialchars($file['name']); ?>"><?php echo htmlspecialchars($file['name']); ?></a>
                        <?php endif; ?>
                    </td>
                    <td><?php echo $file['is_dir'] ? '-' : formatSize($file['size']); ?></td>
                    <td><?php echo date('Y-m-d H:i:s', $file['modified']); ?></td>
                </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>
</body>
</html>
```
