"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiregotrack.info
Prompt: How can I use PHP to list files from a directory on a web server similar to the structure found at wiregotrack.info?
Generated: DETERMINISTIC_f7831c941d96c131
Batch ID: 20250612_160102
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
 * File Listing Script
 * This script lists all files and directories within a specified directory on the server
 * similar to the structure found at wiregotrack.info. It includes error handling 
 * and follows best practices to ensure a clean and secure implementation.
 */

// Define the target directory to scan
$targetDirectory = __DIR__; // Default to the current directory

// Function to safely list files and directories
function listFilesFromDirectory($directory) {
    // Check if the directory exists
    if (!is_dir($directory)) {
        die("Error: The specified directory does not exist.");
    }

    // Attempt to open the directory
    $dirHandle = opendir($directory);
    if ($dirHandle === false) {
        die("Error: Unable to open the directory.");
    }

    // Initialize an array to store file and directory names
    $fileList = [];

    // Read through the directory contents
    while (($entry = readdir($dirHandle)) !== false) {
        // Filter out the current and parent directory references
        if ($entry !== "." && $entry !== "..") {
            $fileList[] = $entry;
        }
    }

    // Close the directory handle
    closedir($dirHandle);

    // Sort the file list for consistency
    sort($fileList);

    return $fileList;
}

// Get the list of files and directories
$fileList = listFilesFromDirectory($targetDirectory);

// Display the files and directories as HTML
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listing</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .file-list {
            list-style-type: none;
            padding: 0;
        }
        .file-list li {
            padding: 5px;
            border: 1px solid #ddd;
            margin: 5px 0;
            border-radius: 3px;
        }
        .file-list li a {
            text-decoration: none;
            color: #007BFF;
        }
        .file-list li a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Directory Listing</h1>
    <ul class="file-list">
        <?php foreach ($fileList as $file): ?>
            <li>
                <?php
                // Check if the entry is a directory or file and generate appropriate link
                $filePath = $targetDirectory . DIRECTORY_SEPARATOR . $file;
                if (is_dir($filePath)) {
                    echo '<a href="?dir=' . urlencode($file) . '">' . htmlspecialchars($file) . ' (Directory)</a>';
                } else {
                    echo '<a href="' . htmlspecialchars($file) . '">' . htmlspecialchars($file) . '</a>';
                }
                ?>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```
