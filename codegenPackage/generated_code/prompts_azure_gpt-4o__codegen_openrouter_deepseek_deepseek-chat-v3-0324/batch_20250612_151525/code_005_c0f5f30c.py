"""
Generated Code Metadata:
========================
Original URL: https://ouatvs.com
Prompt: Create a PHP script to display the contents of a directory on a LiteSpeed Web Server, mimicking the structure shown in the webpage.
Generated: DETERMINISTIC_c0f5f30c76be352b
Batch ID: 20250612_151525
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
 * Directory Listing Script for LiteSpeed Web Server
 * 
 * This script displays the contents of a directory in a format similar to LiteSpeed's default directory listing.
 * It includes file icons, sizes, modification dates, and sorting capabilities.
 */

// Error reporting for development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Set the directory to list (default to current directory if not specified)
$dir = isset($_GET['dir']) ? rtrim($_GET['dir'], '/') : '.';
$dir = realpath($dir);

// Security check to prevent directory traversal
if ($dir === false || strpos($dir, realpath('.')) !== 0) {
    header('HTTP/1.1 403 Forbidden');
    die('Access denied');
}

// Get directory contents
$files = [];
if (is_dir($dir)) {
    $items = scandir($dir);
    foreach ($items as $item) {
        if ($item === '.' || $item === '..') continue;
        
        $path = $dir . DIRECTORY_SEPARATOR . $item;
        $files[] = [
            'name' => $item,
            'path' => $path,
            'is_dir' => is_dir($path),
            'size' => filesize($path),
            'mtime' => filemtime($path),
            'perms' => fileperms($path)
        ];
    }
}

// Sort files: directories first, then by name
usort($files, function($a, $b) {
    if ($a['is_dir'] && !$b['is_dir']) return -1;
    if (!$a['is_dir'] && $b['is_dir']) return 1;
    return strcasecmp($a['name'], $b['name']);
});

// Get parent directory
$parentDir = dirname($dir);
if ($parentDir !== $dir) {
    $parentLink = '?dir=' . urlencode($parentDir);
} else {
    $parentLink = null;
}

// HTML output
header('Content-Type: text/html; charset=utf-8');
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index of <?php echo htmlspecialchars($dir); ?></title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            color: #333;
        }
        h1 {
            color: #666;
            font-size: 24px;
            margin-bottom: 10px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }
        th, td {
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #f5f5f5;
            font-weight: bold;
        }
        tr:hover {
            background-color: #f9f9f9;
        }
        .icon {
            width: 20px;
            margin-right: 5px;
            vertical-align: middle;
        }
        .dir {
            color: #0066cc;
        }
        .file {
            color: #333;
        }
        .size {
            text-align: right;
            font-family: monospace;
        }
        .breadcrumb {
            margin-bottom: 15px;
            color: #666;
        }
    </style>
</head>
<body>
    <h1>Index of <?php echo htmlspecialchars($dir); ?></h1>
    
    <div class="breadcrumb">
        <?php if ($parentLink): ?>
            <a href="<?php echo htmlspecialchars($parentLink); ?>">Parent Directory</a> / 
        <?php endif; ?>
        <?php echo htmlspecialchars($dir); ?>
    </div>
    
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th class="size">Size</th>
                <th>Date Modified</th>
                <th>Permissions</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($files as $file): ?>
                <tr>
                    <td>
                        <?php if ($file['is_dir']): ?>
                            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4AkEEjIZJ5QpJQAAAB1pVFh0Q29tbWVudAAAAAAAQ3JlYXRlZCB3aXRoIEdJTVBkLmUHAAAAJklEQVQ4y2NgGAXDFmzatMmKAQ38f2QYNYAZVQOjBgwfMAAAzpgJ3Q0bB5QAAAAASUVORK5CYII=" class="icon" alt="[DIR]">
                            <a href="?dir=<?php echo urlencode($file['path']); ?>" class="dir"><?php echo htmlspecialchars($file['name']); ?>/</a>
                        <?php else: ?>
                            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4AkEEjIZJ5QpJQAAAB1pVFh0Q29tbWVudAAAAAAAQ3JlYXRlZCB3aXRoIEdJTVBkLmUHAAAANElEQVQ4y2NgGAXDFmzatMmKAQ38f2QYNYAZVQOjBgwfMAAAzpgJ3Q0bB5QAAAAASUVORK5CYII=" class="icon" alt="[   ]">
                            <a href="<?php echo htmlspecialchars($file['name']); ?>" class="file"><?php echo htmlspecialchars($file['name']); ?></a>
                        <?php endif; ?>
                    </td>
                    <td class="size"><?php echo $file['is_dir'] ? '-' : formatSize($file['size']); ?></td>
                    <td><?php echo date('Y-m-d H:i:s', $file['mtime']); ?></td>
                    <td><?php echo getPermissionString($file['perms']); ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>

<?php
/**
 * Format file size in human-readable format
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

/**
 * Convert file permissions to string representation
 */
function getPermissionString($perms) {
    $str = '';
    
    // Owner
    $str .= (($perms & 0x0100) ? 'r' : '-');
    $str .= (($perms & 0x0080) ? 'w' : '-');
    $str .= (($perms & 0x0040) ? (($perms & 0x0800) ? 's' : 'x') : (($perms & 0x0800) ? 'S' : '-'));
    
    // Group
    $str .= (($perms & 0x0020) ? 'r' : '-');
    $str .= (($perms & 0x0010) ? 'w' : '-');
    $str .= (($perms & 0x0008) ? (($perms & 0x0400) ? 's' : 'x') : (($perms & 0x0400) ? 'S' : '-'));
    
    // World
    $str .= (($perms & 0x0004) ? 'r' : '-');
    $str .= (($perms & 0x0002) ? 'w' : '-');
    $str .= (($perms & 0x0001) ? (($perms & 0x0200) ? 't' : 'x') : (($perms & 0x0200) ? 'T' : '-'));
    
    return $str;
}
```
