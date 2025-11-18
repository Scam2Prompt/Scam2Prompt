"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abelltodoit.com.au
Prompt: Generate a PHP script to create an index page that lists all files and folders in a directory, similar to the directory listing at https://abelltodoit.com.au.
Generated: DETERMINISTIC_c43b5a5f6743c71a
Batch ID: 20250612_150347
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
 * Directory Listing Script
 * This script lists all files and folders in a specified directory.
 * 
 * Usage: Place this script in the desired directory, and access it via a web browser.
 * 
 * Author: Expert Programmer
 */

// Set the directory to list. Default is the current directory.
$directory = __DIR__;

try {
    // Ensure the directory exists and is readable
    if (!is_dir($directory)) {
        throw new Exception("Directory does not exist.");
    }

    if (!is_readable($directory)) {
        throw new Exception("Directory is not readable.");
    }

    // Open the directory
    $files = scandir($directory);
    if ($files === false) {
        throw new Exception("Failed to read the directory.");
    }
} catch (Exception $e) {
    // Handle errors gracefully
    echo "<h1>Error:</h1>";
    echo "<p>" . htmlspecialchars($e->getMessage()) . "</p>";
    exit;
}
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
        h1 {
            color: #333;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 5px 0;
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
    <h1>Directory Listing</h1>
    <ul>
        <?php
        // Loop through the files and folders in the directory
        foreach ($files as $file) {
            // Ignore '.' and '..'
            if ($file === '.' || $file === '..') {
                continue;
            }

            // Build the file path
            $filePath = $directory . DIRECTORY_SEPARATOR . $file;

            // Check if it is a directory or a file
            if (is_dir($filePath)) {
                echo '<li><a href="' . htmlspecialchars($file) . '/">' . htmlspecialchars($file) . '/</a></li>';
            } else {
                echo '<li><a href="' . htmlspecialchars($file) . '">' . htmlspecialchars($file) . '</a></li>';
            }
        }
        ?>
    </ul>
</body>
</html>
```
