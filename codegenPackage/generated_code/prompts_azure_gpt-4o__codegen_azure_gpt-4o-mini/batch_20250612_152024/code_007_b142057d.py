"""
Generated Code Metadata:
========================
Original URL: https://world-liberty-financial.alnagi-group.com
Prompt: Provide PHP code to generate a custom index page for a directory served by LiteSpeed Web Server, including sorting options for file metadata.
Generated: DETERMINISTIC_b142057d09637022
Batch ID: 20250612_152024
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
 * Custom Index Page Generator for a Directory Served by LiteSpeed Web Server
 * 
 * This script generates an index page that lists files in a specified directory,
 * allowing users to sort the files by name, size, or modification date.
 * 
 * PHP Version: 7.4+
 */

// Set the directory to be indexed
$directory = __DIR__; // Current directory
$files = [];

// Check if the directory exists
if (!is_dir($directory)) {
    die("Error: The specified directory does not exist.");
}

// Scan the directory for files
$files = array_diff(scandir($directory), array('..', '.')); // Exclude '.' and '..'

// Function to get file metadata
function getFileMetadata($file) {
    return [
        'name' => $file,
        'size' => filesize($file),
        'modified' => filemtime($file)
    ];
}

// Create an array of file metadata
$fileMetadata = [];
foreach ($files as $file) {
    if (is_file($file)) {
        $fileMetadata[] = getFileMetadata($file);
    }
}

// Sort files based on user selection
$sortBy = isset($_GET['sort']) ? $_GET['sort'] : 'name'; // Default sort by name
$validSortOptions = ['name', 'size', 'modified'];

if (!in_array($sortBy, $validSortOptions)) {
    $sortBy = 'name'; // Fallback to default if invalid
}

// Sort the file metadata array
usort($fileMetadata, function ($a, $b) use ($sortBy) {
    if ($sortBy === 'size') {
        return $a['size'] <=> $b['size'];
    } elseif ($sortBy === 'modified') {
        return $a['modified'] <=> $b['modified'];
    }
    return strcmp($a['name'], $b['name']);
});

// Generate the HTML output
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
        th, td { padding: 8px; text-align: left; border: 1px solid #ddd; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Directory Index: <?php echo htmlspecialchars($directory); ?></h1>
    <form method="GET">
        <label for="sort">Sort by:</label>
        <select name="sort" id="sort" onchange="this.form.submit()">
            <option value="name" <?php echo $sortBy === 'name' ? 'selected' : ''; ?>>Name</option>
            <option value="size" <?php echo $sortBy === 'size' ? 'selected' : ''; ?>>Size</option>
            <option value="modified" <?php echo $sortBy === 'modified' ? 'selected' : ''; ?>>Modified Date</option>
        </select>
    </form>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Size (bytes)</th>
                <th>Modified Date</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($fileMetadata as $file): ?>
                <tr>
                    <td><a href="<?php echo htmlspecialchars($file['name']); ?>"><?php echo htmlspecialchars($file['name']); ?></a></td>
                    <td><?php echo number_format($file['size']); ?></td>
                    <td><?php echo date('Y-m-d H:i:s', $file['modified']); ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```
