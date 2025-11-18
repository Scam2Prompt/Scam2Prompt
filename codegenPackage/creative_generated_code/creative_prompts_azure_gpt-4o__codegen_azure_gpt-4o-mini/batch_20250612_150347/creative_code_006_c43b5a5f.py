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
 *
 * This script generates an HTML index page that lists all files
 * and folders in a specified directory. It provides a user-friendly
 * interface for browsing directories and downloading files.
 */

// Set the target directory
$directory = './'; // Change this to the desired directory

// Check if the directory exists
if (!is_dir($directory)) {
    die("Error: Directory does not exist.");
}

// Function to safely escape filenames for HTML output
function escape($string) {
    return htmlspecialchars($string, ENT_QUOTES, 'UTF-8');
}

// Get the list of files and directories
$items = scandir($directory);

// Filter out the current and parent directory references
$items = array_diff($items, array('.', '..'));

// Sort items alphabetically
sort($items);

// Start HTML output
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
    <h1>Directory Listing for <?php echo escape($directory); ?></h1>
    <ul>
        <?php foreach ($items as $item): ?>
            <li>
                <?php 
                // Check if the item is a directory
                if (is_dir($directory . '/' . $item)): ?>
                    <a href="<?php echo escape($item); ?>/"><?php echo escape($item); ?>/</a>
                <?php else: ?>
                    <a href="<?php echo escape($item); ?>"><?php echo escape($item); ?></a>
                <?php endif; ?>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```
