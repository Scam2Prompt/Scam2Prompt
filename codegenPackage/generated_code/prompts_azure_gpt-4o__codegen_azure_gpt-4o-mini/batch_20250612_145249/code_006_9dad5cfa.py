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
 * Directory Index Generator
 * This script generates a dynamic index page for a directory listing.
 * It displays files and subdirectories in a user-friendly format.
 */

// Set the directory to be listed
$directory = '.';

// Check if the directory exists
if (!is_dir($directory)) {
    die("Error: The specified directory does not exist.");
}

// Get the list of files and directories
$items = scandir($directory);

// Filter out the current and parent directory entries
$items = array_diff($items, array('.', '..'));

// Sort items by name
sort($items);

// Start HTML output
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Index of <?php echo htmlspecialchars($directory); ?></title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        tr:hover {
            background-color: #f1f1f1;
        }
        a {
            text-decoration: none;
            color: #007BFF;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

<h1>Directory Index of <?php echo htmlspecialchars($directory); ?></h1>
<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Size</th>
        <th>Last Modified</th>
    </tr>
    <?php foreach ($items as $item): ?>
        <tr>
            <td>
                <?php
                // Check if the item is a directory
                if (is_dir($item)) {
                    echo '<a href="' . htmlspecialchars($item) . '/">' . htmlspecialchars($item) . '</a>';
                } else {
                    echo '<a href="' . htmlspecialchars($item) . '">' . htmlspecialchars($item) . '</a>';
                }
                ?>
            </td>
            <td><?php echo is_dir($item) ? 'Directory' : 'File'; ?></td>
            <td><?php echo is_dir($item) ? '-' : formatSize(filesize($item)); ?></td>
            <td><?php echo date('Y-m-d H:i:s', filemtime($item)); ?></td>
        </tr>
    <?php endforeach; ?>
</table>

<?php
/**
 * Format file size into human-readable format
 *
 * @param int $bytes Size in bytes
 * @return string Formatted size
 */
function formatSize($bytes) {
    $units = ['B', 'KB', 'MB', 'GB', 'TB'];
    $factor = floor((strlen($bytes) - 1) / 3);
    return sprintf("%.2f", $bytes / pow(1024, $factor)) . ' ' . $units[$factor];
}
?>

</body>
</html>
```
