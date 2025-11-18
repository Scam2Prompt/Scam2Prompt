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
 * Custom Index Page Generator for Directory Listing
 * Generates an HTML index page for a directory served by LiteSpeed Web Server.
 * Includes sorting options for file metadata.
 */

// Directory to list files from. Change to the desired directory.
$directory = __DIR__;

// Check if the directory exists and is readable.
if (!is_dir($directory) || !is_readable($directory)) {
    http_response_code(500);
    die("Error: Unable to access directory.");
}

// Fetch sorting options from GET parameters.
$sortBy = $_GET['sort'] ?? 'name'; // Default sorting by name
$order = $_GET['order'] ?? 'asc'; // Default order: ascending

// Validate sorting options.
$validSortOptions = ['name', 'size', 'modified'];
if (!in_array($sortBy, $validSortOptions)) {
    $sortBy = 'name';
}
$order = $order === 'desc' ? 'desc' : 'asc';

// Function to fetch file metadata.
function getFileData($filePath)
{
    return [
        'name' => basename($filePath),
        'size' => filesize($filePath),
        'modified' => filemtime($filePath),
    ];
}

// Get list of files in the directory.
$files = array_filter(scandir($directory), function ($file) use ($directory) {
    $filePath = $directory . DIRECTORY_SEPARATOR . $file;
    return is_file($filePath);
});

// Fetch metadata for each file.
$fileMetadata = array_map(function ($file) use ($directory) {
    $filePath = $directory . DIRECTORY_SEPARATOR . $file;
    return getFileData($filePath);
}, $files);

// Sort the files based on sorting options.
usort($fileMetadata, function ($a, $b) use ($sortBy, $order) {
    if ($a[$sortBy] === $b[$sortBy]) {
        return 0;
    }
    return ($order === 'asc' ? $a[$sortBy] <=> $b[$sortBy] : $b[$sortBy] <=> $a[$sortBy]);
});

// Generate HTML for the index page.
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Index</title>
    <style>
        body { font-family: Arial, sans-serif; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 10px; text-align: left; border: 1px solid #ddd; }
        th { background-color: #f4f4f4; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Directory Index</h1>
    <table>
        <thead>
            <tr>
                <th><a href="?sort=name&order=<?= $sortBy === 'name' && $order === 'asc' ? 'desc' : 'asc' ?>">Name</a></th>
                <th><a href="?sort=size&order=<?= $sortBy === 'size' && $order === 'asc' ? 'desc' : 'asc' ?>">Size</a></th>
                <th><a href="?sort=modified&order=<?= $sortBy === 'modified' && $order === 'asc' ? 'desc' : 'asc' ?>">Last Modified</a></th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($fileMetadata as $file): ?>
                <tr>
                    <td><a href="<?= htmlspecialchars($file['name']) ?>"><?= htmlspecialchars($file['name']) ?></a></td>
                    <td><?= $file['size'] ?> bytes</td>
                    <td><?= date("Y-m-d H:i:s", $file['modified']) ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```
