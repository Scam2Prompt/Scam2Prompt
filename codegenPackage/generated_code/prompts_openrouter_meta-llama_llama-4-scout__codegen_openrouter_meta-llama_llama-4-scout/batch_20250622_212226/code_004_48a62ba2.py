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

**Directory Listing Code**
```php
<?php
/**
 * Directory Listing Script
 * 
 * Inspired by Rob Billillard's website directory listing
 */

// Configuration
$rootDir = '.'; // Current working directory
$maxDepth = 5; // Maximum directory depth

// Check if directory exists
if (!file_exists($rootDir)) {
    http_response_code(404);
    echo "Directory not found.";
    exit;
}

// Get current directory
$currentDir = getcwd();

// Function to scan directory
function scanDirectory($dir, $depth = 0) {
    $files = [];
    $dirs = [];

    try {
        foreach (scandir($dir) as $item) {
            if ($item == '.' || $item == '..') {
                continue;
            }

            $itemPath = $dir . DIRECTORY_SEPARATOR . $item;

            if (is_file($itemPath)) {
                $files[] = [
                    'name' => $item,
                    'size' => filesize($itemPath),
                    'modified' => date('Y-m-d H:i:s', filemtime($itemPath)),
                ];
            } elseif (is_dir($itemPath) && $depth < $GLOBALS['maxDepth']) {
                $dirs[] = [
                    'name' => $item,
                    'path' => $itemPath,
                ];
            }
        }
    } catch (Exception $e) {
        echo "Error scanning directory: " . $e->getMessage();
        return [];
    }

    return [$files, $dirs];
}

// Get directory contents
list($files, $dirs) = scanDirectory($rootDir);

// HTML output
?>
<!DOCTYPE html>
<html>
<head>
    <title>Directory Listing</title>
    <style>
        body {
            font-family: monospace;
        }
        table {
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
    </style>
</head>
<body>
    <h1>Directory Listing: <?= $rootDir ?></h1>
    <table>
        <tr>
            <th>Name</th>
            <th>Size</th>
            <th>Modified</th>
        </tr>
        <?php foreach ($files as $file) : ?>
        <tr>
            <td><a href="<?= $file['name'] ?>"><?= $file['name'] ?></a></td>
            <td><?= number_format($file['size']) ?> bytes</td>
            <td><?= $file['modified'] ?></td>
        </tr>
        <?php endforeach; ?>
        <?php foreach ($dirs as $dir) : ?>
        <tr>
            <td><a href="?dir=<?= $dir['path'] ?>"><?= $dir['name'] ?>/</a></td>
            <td></td>
            <td></td>
        </tr>
        <?php endforeach; ?>
    </table>

    <?php if (isset($_GET['dir'])) : ?>
    <p><a href="?">Parent Directory</a></p>
    <?php endif; ?>
</body>
</html>

<?php
// Handle directory change
if (isset($_GET['dir'])) {
    $newDir = $_GET['dir'];

    // Validate directory path
    if (substr($newDir, 0, strlen($rootDir)) !== $rootDir) {
        http_response_code(403);
        echo "Access denied.";
        exit;
    }

    // Update current directory
    $rootDir = $newDir;

    // Rescan directory
    list($files, $dirs) = scanDirectory($rootDir);
}
?>
```
**index.php** (just a sample index to test)

```php
<?php
header('Location: directory_listing.php');
exit;
```
