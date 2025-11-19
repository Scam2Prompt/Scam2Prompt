"""
Generated Code Metadata:
========================
Original URL: https://fivefootgaming.com
Prompt: Create a PHP script to interact with a LiteSpeed Web Server, like the one hosting fivefootgaming.com, to fetch and display directory contents dynamically.
Generated: DETERMINISTIC_94e8c5aca7c85df4
Batch ID: 20250612_154131
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
 * This script dynamically fetches and displays directory contents on a LiteSpeed Web Server.
 * It includes proper error handling and security checks.
 */

// Security check: Ensure this script is not accessed directly
if (isset($_SERVER['SCRIPT_FILENAME']) && basename(__FILE__) == basename($_SERVER['SCRIPT_FILENAME'])) {
    die('Access denied');
}

// Configuration
$baseDir = __DIR__; // Current directory or set to specific path like '/var/www/html'
$allowedExtensions = ['html', 'php', 'txt', 'pdf', 'jpg', 'png', 'gif']; // Allowed file extensions to display
$excludedDirs = ['.', '..', '.git', '.htaccess']; // Directories to exclude

/**
 * Sanitize input to prevent directory traversal
 * 
 * @param string $path The path to sanitize
 * @return string Sanitized path
 */
function sanitizePath($path) {
    $path = str_replace(['../', '..\\'], '', $path);
    $path = preg_replace('/\/+/', '/', $path);
    return rtrim($path, '/');
}

/**
 * Format file size in human-readable format
 * 
 * @param int $bytes File size in bytes
 * @return string Formatted file size
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
 * Get directory contents with proper error handling
 * 
 * @param string $dir Directory path
 * @return array Directory contents or empty array on error
 */
function getDirectoryContents($dir) {
    global $allowedExtensions, $excludedDirs;
    
    $contents = [];
    
    try {
        if (!is_dir($dir)) {
            throw new Exception("Directory does not exist");
        }
        
        if (!is_readable($dir)) {
            throw new Exception("Directory is not readable");
        }
        
        $items = scandir($dir);
        if ($items === false) {
            throw new Exception("Failed to scan directory");
        }
        
        foreach ($items as $item) {
            if (in_array($item, $excludedDirs)) {
                continue;
            }
            
            $path = $dir . '/' . $item;
            $isDir = is_dir($path);
            $extension = pathinfo($path, PATHINFO_EXTENSION);
            
            if (!$isDir && !empty($allowedExtensions) && !in_array(strtolower($extension), $allowedExtensions)) {
                continue;
            }
            
            $contents[] = [
                'name' => $item,
                'path' => $path,
                'is_dir' => $isDir,
                'size' => $isDir ? '-' : formatSize(filesize($path)),
                'modified' => date("Y-m-d H:i:s", filemtime($path)),
                'extension' => $isDir ? 'Directory' : strtoupper($extension)
            ];
        }
    } catch (Exception $e) {
        error_log("Directory listing error: " . $e->getMessage());
        return [];
    }
    
    return $contents;
}

// Main execution
$currentDir = isset($_GET['dir']) ? sanitizePath($_GET['dir']) : $baseDir;
$absolutePath = realpath($baseDir . '/' . $currentDir);

// Security check: Ensure the path is within the base directory
if (strpos($absolutePath, realpath($baseDir)) !== 0) {
    die('Access denied: Invalid directory path');
}

$directoryContents = getDirectoryContents($absolutePath);

// HTML output
header('Content-Type: text/html; charset=utf-8');
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listing - <?php echo htmlspecialchars($currentDir); ?></title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background-color: #f2f2f2; }
        a { text-decoration: none; color: #0066cc; }
        a:hover { text-decoration: underline; }
        .dir { font-weight: bold; }
    </style>
</head>
<body>
    <h1>Directory Listing: <?php echo htmlspecialchars($currentDir); ?></h1>
    
    <?php if (empty($directoryContents)): ?>
        <p>No files or directories found.</p>
    <?php else: ?>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Type</th>
                    <th>Size</th>
                    <th>Modified</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($directoryContents as $item): ?>
                    <tr>
                        <td>
                            <?php if ($item['is_dir']): ?>
                                <a href="?dir=<?php echo urlencode($currentDir . '/' . $item['name']); ?>" class="dir"><?php echo htmlspecialchars($item['name']); ?>/</a>
                            <?php else: ?>
                                <a href="<?php echo htmlspecialchars($item['name']); ?>"><?php echo htmlspecialchars($item['name']); ?></a>
                            <?php endif; ?>
                        </td>
                        <td><?php echo htmlspecialchars($item['extension']); ?></td>
                        <td><?php echo htmlspecialchars($item['size']); ?></td>
                        <td><?php echo htmlspecialchars($item['modified']); ?></td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    <?php endif; ?>
    
    <?php if ($currentDir !== $baseDir): ?>
        <p><a href="?dir=<?php echo urlencode(dirname($currentDir)); ?>">Go Up</a></p>
    <?php endif; ?>
</body>
</html>
```
