"""
Generated Code Metadata:
========================
Original URL: https://robilliardag.com
Prompt: Write a PHP script that generates an index of files in a directory, similar to the one displayed on Rob Billillard's website.
Generated: DETERMINISTIC_46a404db93e2fa29
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
/**
 * Generates an index of files in a specified directory.
 * 
 * This script scans a directory for files and generates an HTML index
 * listing the files with links to download them. It also handles errors
 * gracefully and ensures that only valid files are displayed.
 * 
 * @param string $directory The path to the directory to scan.
 * @return void
 */
function generateFileIndex($directory) {
    // Check if the directory exists
    if (!is_dir($directory)) {
        http_response_code(404);
        die("Error: Directory not found.");
    }

    // Open the directory
    $files = scandir($directory);
    if ($files === false) {
        http_response_code(500);
        die("Error: Unable to read directory.");
    }

    // Filter out the current and parent directory references
    $files = array_diff($files, array('.', '..'));

    // Start generating the HTML output
    echo "<!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>File Index</title>
        <style>
            body { font-family: Arial, sans-serif; }
            table { width: 100%; border-collapse: collapse; }
            th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h1>File Index for ' . htmlspecialchars($directory) . '</h1>
        <table>
            <tr>
                <th>File Name</th>
                <th>Size (bytes)</th>
                <th>Last Modified</th>
            </tr>";

    // Loop through the files and create a table row for each
    foreach ($files as $file) {
        $filePath = $directory . DIRECTORY_SEPARATOR . $file;

        // Only include files (ignore directories)
        if (is_file($filePath)) {
            $fileSize = filesize($filePath);
            $fileModified = date("Y-m-d H:i:s", filemtime($filePath));

            echo "<tr>
                    <td><a href='" . htmlspecialchars($filePath) . "'>" . htmlspecialchars($file) . "</a></td>
                    <td>" . htmlspecialchars($fileSize) . "</td>
                    <td>" . htmlspecialchars($fileModified) . "</td>
                  </tr>";
        }
    }

    echo "</table>
    </body>
    </html>";
}

// Specify the directory to index
$directoryToIndex = 'path/to/your/directory'; // Change this to your target directory
generateFileIndex($directoryToIndex);
?>
```
