"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robilliardag.com
Prompt: How can I implement a file index page in PHP that mimics the directory listing format of robilliardag.com?
Generated: DETERMINISTIC_b1fee573b2957111
Batch ID: 20250612_161209
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
 * File Index Page
 * This script generates an index page that lists files in a specified directory
 * in a format similar to robilliardag.com.
 */

// Set the desired directory to list files from
$directory = './files'; // Change this to your desired directory

// Function to generate the file index page
function generateFileIndex($dir) {
    // Check if the directory exists
    if (!is_dir($dir)) {
        die('Error: Directory does not exist.');
    }

    // Open the directory
    if ($handle = opendir($dir)) {
        // Initialize an array to hold file information
        $files = [];

        // Loop through the directory entries
        while (false !== ($entry = readdir($handle))) {
            // Skip the current and parent directory entries
            if ($entry != '.' && $entry != '..') {
                // Get file path
                $filePath = $dir . '/' . $entry;
                
                // Store file information in the array
                $files[] = [
                    'name' => $entry,
                    'size' => filesize($filePath),
                    'modified' => date("F d Y H:i:s.", filemtime($filePath)),
                    'isDir' => is_dir($filePath)
                ];
            }
        }

        // Close the directory handle
        closedir($handle);
        
        // Sort files by name
        usort($files, function($a, $b) {
            return strcmp($a['name'], $b['name']);
        });

        return $files;
    } else {
        die('Error: Unable to open directory.');
    }
}

// Generate the file list
$fileList = generateFileIndex($directory);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Index</title>
    <style>
        body { font-family: Arial, sans-serif; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        th, td { border: 1px solid #ddd; padding: 8px; }
        th { background-color: #f2f2f2; }
        tr:hover { background-color: #f1f1f1; }
    </style>
</head>
<body>

<h1>File Index</h1>

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Size (bytes)</th>
            <th>Last Modified</th>
            <th>Type</th>
        </tr>
    </thead>
    <tbody>
        <?php foreach ($fileList as $file): ?>
            <tr>
                <td>
                    <?php if ($file['isDir']): ?>
                        <strong><?php echo htmlspecialchars($file['name']); ?></strong>
                    <?php else: ?>
                        <a href="<?php echo htmlspecialchars($directory . '/' . $file['name']); ?>">
                            <?php echo htmlspecialchars($file['name']); ?>
                        </a>
                    <?php endif; ?>
                </td>
                <td><?php echo $file['size']; ?></td>
                <td><?php echo $file['modified']; ?></td>
                <td><?php echo $file['isDir'] ? 'Directory' : 'File'; ?></td>
            </tr>
        <?php endforeach; ?>
    </tbody>
</table>

</body>
</html>
```
