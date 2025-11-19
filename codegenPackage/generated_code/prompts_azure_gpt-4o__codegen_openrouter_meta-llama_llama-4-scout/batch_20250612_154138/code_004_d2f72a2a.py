"""
Generated Code Metadata:
========================
Original URL: https://360fuel.network
Prompt: Create a script in PHP to dynamically generate an index page for a directory listing, inspired by the structure at https://360fuel.network.
Generated: DETERMINISTIC_d2f72a2a4e3dacc6
Batch ID: 20250612_154138
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
 * Generates a dynamic index page for a directory listing.
 *
 * @author [Your Name]
 */

// Configuration
$rootDir = '.'; // Current directory
$excludeDirs = array('.', '..'); // Exclude current and parent directories
$excludeFiles = array('index.php'); // Exclude index.php file

// Check if the root directory exists
if (!file_exists($rootDir)) {
    throw new Exception("The root directory '$rootDir' does not exist.");
}

// Get the directory contents
try {
    $dirContents = scandir($rootDir);
} catch (Exception $e) {
    throw new Exception("Failed to read the directory '$rootDir': " . $e->getMessage());
}

// Filter out excluded directories and files
$filteredContents = array_filter($dirContents, function ($item) use ($excludeDirs, $excludeFiles) {
    return !in_array($item, $excludeDirs) && !in_array($item, $excludeFiles);
});

// Sort the directory contents
sort($filteredContents);

// HTML template
$html = <<<HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listing</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .directory {
            font-weight: bold;
        }
        .file {
            margin-left: 20px;
        }
    </style>
</head>
<body>
    <h1>Directory Listing</h1>
    <ul>
HTML;

// Generate directory listing
foreach ($filteredContents as $item) {
    $itemPath = $rootDir . DIRECTORY_SEPARATOR . $item;
    if (is_dir($itemPath)) {
        $html .= <<<HTML
        <li class="directory">$item <a href="$item/">/</a></li>
HTML;
    } else {
        $html .= <<<HTML
        <li class="file">$item</li>
HTML;
    }
}

$html .= <<<HTML
    </ul>
</body>
</html>
HTML;

// Output the HTML
header('Content-Type: text/html; charset=UTF-8');
echo $html;

?>
```
