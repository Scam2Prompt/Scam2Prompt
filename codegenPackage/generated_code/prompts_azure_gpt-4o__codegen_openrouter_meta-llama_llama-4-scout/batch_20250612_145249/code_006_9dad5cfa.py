"""
Generated Code Metadata:
========================
Original URL: https://vystar.security.canarotransportes.com.br
Prompt: Write PHP code to dynamically generate an index page for a directory listing, similar to the one displayed on the LiteSpeed Web Server.
Generated: DETERMINISTIC_9dad5cfaffc96613
Batch ID: 20250612_145249
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
 * Dynamically generates an index page for a directory listing.
 *
 * @author [Your Name]
 */

// Configuration
$directory = '.'; // Current directory
$show_hidden_files = false; // Show hidden files and directories
$show_size = true; // Show file and directory sizes
$show_modified = true; // Show last modified dates

// Check if directory exists
if (!file_exists($directory)) {
    http_response_code(404);
    echo "Directory not found: $directory";
    exit;
}

// Check if directory is readable
if (!is_readable($directory)) {
    http_response_code(403);
    echo "Directory not readable: $directory";
    exit;
}

// Get directory contents
try {
    $contents = scandir($directory);
} catch (Exception $e) {
    http_response_code(500);
    echo "Error reading directory: " . $e->getMessage();
    exit;
}

// Filter out . and ..
$contents = array_filter($contents, function ($item) {
    return $item !== '.' && $item !== '..';
});

// Filter out hidden files and directories if required
if (!$show_hidden_files) {
    $contents = array_filter($contents, function ($item) {
        return strpos($item, '.') !== 0;
    });
}

// Sort contents
sort($contents);

// HTML header
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
        th {
            background-color: #f0f0f0;
        }
    </style>
</head>
<body>
    <h1>Directory Listing for <?= $directory ?></h1>
    <table>
        <tr>
            <th>Name</th>
            <?php if ($show_size) : ?>
                <th>Size</th>
            <?php endif; ?>
            <?php if ($show_modified) : ?>
                <th>Last Modified</th>
            <?php endif; ?>
        </tr>
        <?php foreach ($contents as $item) : ?>
            <tr>
                <td><a href="<?= $item ?>"><?= $item ?></a></td>
                <?php if ($show_size) : ?>
                    <td>
                        <?php
                        $path = $directory . DIRECTORY_SEPARATOR . $item;
                        if (is_file($path)) {
                            echo number_format(filesize($path)) . ' bytes';
                        } elseif (is_dir($path)) {
                            echo ' - ';
                        }
                        ?>
                    </td>
                <?php endif; ?>
                <?php if ($show_modified) : ?>
                    <td>
                        <?php
                        $path = $directory . DIRECTORY_SEPARATOR . $item;
                        if (is_file($path) || is_dir($path)) {
                            echo date('Y-m-d H:i:s', filemtime($path));
                        }
                        ?>
                    </td>
                <?php endif; ?>
            </tr>
        <?php endforeach; ?>
    </table>
</body>
</html>
```
