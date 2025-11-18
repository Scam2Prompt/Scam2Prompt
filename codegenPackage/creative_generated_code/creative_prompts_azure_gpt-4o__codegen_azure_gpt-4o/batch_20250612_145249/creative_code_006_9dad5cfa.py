"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vystar.security.canarotransportes.com.br
Prompt: Write PHP code to dynamically generate an index page for a directory listing, similar to the one displayed on the LiteSpeed Web Server.
Generated: DETERMINISTIC_9dad5cfaffc96613
Batch ID: 20250612_145249
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
 * Directory Index Page Generator
 * Dynamically generates an index page for a directory listing.
 *
 * PHP Version: 7.4+
 * Author: Professional Software Developer
 */

// Define the directory to list files from. Default to the current directory.
$directoryPath = '.';

// Error handling: Check if the directory exists and is readable.
if (!is_dir($directoryPath) || !is_readable($directoryPath)) {
    http_response_code(500);
    die("Error: Unable to access the directory.");
}

// Fetch the list of files and directories.
$items = scandir($directoryPath);

// Filter out '.' and '..' from the directory listing.
$items = array_filter($items, function ($item) use ($directoryPath) {
    return $item !== '.' && $item !== '..' && is_readable($directoryPath . DIRECTORY_SEPARATOR . $item);
});
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Index</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
            text-align: left;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        tr:hover {
            background-color: #ddd;
        }
        a {
            color: #007BFF;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Directory Listing</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Type</th>
                <th>Size</th>
                <th>Last Modified</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($items as $item): ?>
                <?php
                // Full path to the item.
                $itemPath = $directoryPath . DIRECTORY_SEPARATOR . $item;

                // Determine the item's type (file or directory).
                $itemType = is_dir($itemPath) ? 'Directory' : 'File';

                // Get the item's size (if it's a file).
                $itemSize = is_file($itemPath) ? filesize($itemPath) : '-';

                // Get the item's last modification time.
                $itemModified = date('Y-m-d H:i:s', filemtime($itemPath));
                ?>
                <tr>
                    <td>
                        <a href="<?php echo htmlspecialchars($item, ENT_QUOTES, 'UTF-8'); ?>">
                            <?php echo htmlspecialchars($item, ENT_QUOTES, 'UTF-8'); ?>
                        </a>
                    </td>
                    <td><?php echo $itemType; ?></td>
                    <td><?php echo $itemSize; ?></td>
                    <td><?php echo $itemModified; ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```
