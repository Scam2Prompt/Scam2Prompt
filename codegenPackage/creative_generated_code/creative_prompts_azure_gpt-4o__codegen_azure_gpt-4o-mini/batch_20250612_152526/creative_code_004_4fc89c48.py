"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shib-airdrop.x10.bz
Prompt: Create a PHP script to display the contents of the `public_html` directory on a webpage.
Generated: DETERMINISTIC_4fc89c48ef4d9af4
Batch ID: 20250612_152526
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
 * PHP Script to display the contents of the public_html directory.
 * 
 * This script scans the specified directory and displays the files and folders in an HTML table format.
 * It includes error handling to manage directory access issues.
 */

// Define the directory to be scanned
$directory = 'public_html';

// Function to check if the directory exists and is readable
function isDirectoryReadable($dir) {
    return is_dir($dir) && is_readable($dir);
}

// Function to get the contents of the directory
function getDirectoryContents($dir) {
    return scandir($dir);
}

// Start HTML output
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Contents</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>

<h1>Contents of <?php echo htmlspecialchars($directory); ?></h1>

<?php
if (isDirectoryReadable($directory)) {
    // Get directory contents
    $contents = getDirectoryContents($directory);
    
    // Filter out the current (.) and parent (..) directory entries
    $contents = array_diff($contents, array('.', '..'));

    // Display contents in a table
    if (empty($contents)) {
        echo "<p>No files or directories found.</p>";
    } else {
        echo "<table>";
        echo "<tr><th>Name</th><th>Type</th></tr>";
        foreach ($contents as $item) {
            $type = is_dir($directory . '/' . $item) ? 'Directory' : 'File';
            echo "<tr><td>" . htmlspecialchars($item) . "</td><td>" . htmlspecialchars($type) . "</td></tr>";
        }
        echo "</table>";
    }
} else {
    // Error handling: directory does not exist or is not readable
    echo "<p>Error: Unable to access the directory <strong>" . htmlspecialchars($directory) . "</strong>. Please check permissions.</p>";
}
?>

</body>
</html>
```
