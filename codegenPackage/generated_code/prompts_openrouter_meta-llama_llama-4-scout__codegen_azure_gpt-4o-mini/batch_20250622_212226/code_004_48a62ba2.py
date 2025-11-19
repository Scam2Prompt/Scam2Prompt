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
// Simple File Explorer Interface in PHP

// Define the root directory to explore
$rootDir = __DIR__; // Current directory
$dir = isset($_GET['dir']) ? $_GET['dir'] : $rootDir;

// Sanitize the directory input to prevent directory traversal attacks
$dir = realpath($dir);
if ($dir === false || strpos($dir, $rootDir) !== 0) {
    die("Invalid directory.");
}

// Function to list files and directories
function listFiles($directory) {
    $files = [];
    if ($handle = opendir($directory)) {
        while (false !== ($entry = readdir($handle))) {
            if ($entry != "." && $entry != "..") {
                $files[] = $entry;
            }
        }
        closedir($handle);
    } else {
        die("Unable to open directory.");
    }
    return $files;
}

// Get the list of files and directories
$files = listFiles($dir);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple File Explorer</title>
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
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        a {
            text-decoration: none;
            color: blue;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

<h1>File Explorer</h1>
<p>Current Directory: <?php echo htmlspecialchars($dir); ?></p>

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Size (bytes)</th>
        </tr>
    </thead>
    <tbody>
        <?php foreach ($files as $file): ?>
            <?php $filePath = $dir . DIRECTORY_SEPARATOR . $file; ?>
            <tr>
                <td>
                    <?php if (is_dir($filePath)): ?>
                        <a href="?dir=<?php echo urlencode($filePath); ?>"><?php echo htmlspecialchars($file); ?></a>
                    <?php else: ?>
                        <?php echo htmlspecialchars($file); ?>
                    <?php endif; ?>
                </td>
                <td><?php echo is_dir($filePath) ? 'Directory' : 'File'; ?></td>
                <td><?php echo is_file($filePath) ? filesize($filePath) : '-'; ?></td>
            </tr>
        <?php endforeach; ?>
    </tbody>
</table>

</body>
</html>
```
