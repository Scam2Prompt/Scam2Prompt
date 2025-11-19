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
 * Directory Listing Script
 * This script dynamically displays the contents of a specified directory
 * in a user-friendly format. It is designed to run on a LiteSpeed Web Server.
 */

// Set the directory to be listed
$directory = isset($_GET['dir']) ? $_GET['dir'] : '.';

// Sanitize the directory input to prevent directory traversal attacks
$directory = realpath($directory);
$baseDir = realpath('.'); // Get the base directory

if ($directory === false || strpos($directory, $baseDir) !== 0) {
    // If the directory is invalid or outside the base directory, show an error
    die("Invalid directory specified.");
}

// Get the contents of the directory
$files = scandir($directory);

// Check for errors while scanning the directory
if ($files === false) {
    die("Error reading directory.");
}

// Filter out the current and parent directory references
$files = array_diff($files, array('.', '..'));

// Function to generate a user-friendly link for each file/directory
function generateLink($file) {
    return htmlspecialchars($file);
}

// Start HTML output
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listing</title>
    <style>
        body { font-family: Arial, sans-serif; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background-color: #f2f2f2; }
        a { text-decoration: none; color: #007BFF; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Directory Listing for: <?php echo generateLink($directory); ?></h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Type</th>
                <th>Size (bytes)</th>
                <th>Last Modified</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($files as $file): ?>
                <?php
                $filePath = $directory . DIRECTORY_SEPARATOR . $file;
                $isDir = is_dir($filePath);
                $size = $isDir ? '-' : filesize($filePath);
                $lastModified = date("Y-m-d H:i:s", filemtime($filePath));
                ?>
                <tr>
                    <td>
                        <a href="<?php echo generateLink($filePath); ?>">
                            <?php echo generateLink($file); ?>
                        </a>
                    </td>
                    <td><?php echo $isDir ? 'Directory' : 'File'; ?></td>
                    <td><?php echo $size; ?></td>
                    <td><?php echo $lastModified; ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```
