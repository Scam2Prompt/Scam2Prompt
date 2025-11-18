"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://world-liberty-financial.alnagi-group.com
Prompt: Provide PHP code to generate a custom index page for a directory served by LiteSpeed Web Server, including sorting options for file metadata.
Generated: DETERMINISTIC_b142057d09637022
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Custom Index Page Generator for a Directory
 * This script generates an HTML index page for a specified directory,
 * displaying files and directories with sorting options for file metadata.
 */

// Set the directory to be indexed
$directory = '.'; // Change to the desired directory path

// Check if the directory exists
if (!is_dir($directory)) {
    die("Error: The specified directory does not exist.");
}

// Get sorting options from query parameters
$sort = isset($_GET['sort']) ? $_GET['sort'] : 'name'; // Default sort by name
$order = isset($_GET['order']) && strtolower($_GET['order']) === 'desc' ? SORT_DESC : SORT_ASC;

// Validate sorting options
$validSortOptions = ['name', 'size', 'date'];
if (!in_array($sort, $validSortOptions)) {
    die("Error: Invalid sorting option.");
}

// Initialize an array to hold file information
$files = [];

// Open the directory and read its contents
if ($handle = opendir($directory)) {
    while (false !== ($entry = readdir($handle))) {
        // Skip current and parent directory references
        if ($entry == '.' || $entry == '..') {
            continue;
        }

        // Get file path
        $filePath = $directory . DIRECTORY_SEPARATOR . $entry;
        $files[] = [
            'name' => $entry,
            'size' => filesize($filePath),
            'date' => filemtime($filePath),
            'is_dir' => is_dir($filePath),
        ];
    }
    closedir($handle);
} else {
    die("Error: Unable to open the directory.");
}

// Sorting function based on selected option
usort($files, function ($a, $b) use ($sort, $order) {
    if ($sort === 'name') {
        return ($order === SORT_DESC) ? strcmp($b['name'], $a['name']) : strcmp($a['name'], $b['name']);
    } elseif ($sort === 'size') {
        return ($order === SORT_DESC) ? $b['size'] - $a['size'] : $a['size'] - $b['size'];
    } elseif ($sort === 'date') {
        return ($order === SORT_DESC) ? $b['date'] - $a['date'] : $a['date'] - $b['date'];
    }
    return 0; // Fallback
});

// Generate HTML output
header('Content-Type: text/html; charset=utf-8');
echo '<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Index</title>
    <style>
        body { font-family: Arial, sans-serif; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 8px; border: 1px solid #ccc; }
        th { background-color: #f4f4f4; }
        a { text-decoration: none; }
    </style>
</head>
<body>
    <h1>Index of ' . htmlspecialchars($directory) . '</h1>
    <table>
        <thead>
            <tr>
                <th><a href="?sort=name&order=' . (($sort === 'name' && $order === SORT_ASC) ? 'desc' : 'asc') . '">Name</a></th>
                <th><a href="?sort=size&order=' . (($sort === 'size' && $order === SORT_ASC) ? 'desc' : 'asc') . '">Size (bytes)</a></th>
                <th><a href="?sort=date&order=' . (($sort === 'date' && $order === SORT_ASC) ? 'desc' : 'asc') . '">Last Modified</a></th>
            </tr>
        </thead>
        <tbody>';

foreach ($files as $file) {
    echo '<tr>
            <td><a href="' . htmlspecialchars($file['name']) . '">' . htmlspecialchars($file['name']) . '</a></td>
            <td>' . ($file['is_dir'] ? '-' : $file['size']) . '</td>
            <td>' . date('Y-m-d H:i:s', $file['date']) . '</td>
          </tr>';
}

echo '    </tbody>
    </table>
</body>
</html>';
?>
```
