"""
Generated Code Metadata:
========================
Original URL: https://robilliardag.com
Prompt: How would you modify the `style.php` file to include additional information about each file, such as file type or last modified date, and write the modified code?
Generated: DETERMINISTIC_b6dc9fa6ca7a11bf
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
// style.php
// This script lists files in a directory and includes additional information such as file type and last modified date.

// Define the directory to scan
$directory = './styles'; // Change this to the directory you want to scan

// Check if the directory exists
if (!is_dir($directory)) {
    die("Error: Directory does not exist.");
}

// Open the directory
$dirHandle = opendir($directory);
if (!$dirHandle) {
    die("Error: Unable to open directory.");
}

// Initialize an array to store file information
$fileInfoList = [];

// Loop through the directory contents
while (($file = readdir($dirHandle)) !== false) {
    // Skip '.' and '..'
    if ($file === '.' || $file === '..') {
        continue;
    }

    // Get the full path of the file
    $filePath = $directory . DIRECTORY_SEPARATOR . $file;

    // Check if it's a file (not a directory)
    if (is_file($filePath)) {
        // Get file information
        $fileType = mime_content_type($filePath); // Get the MIME type of the file
        $lastModified = date("Y-m-d H:i:s", filemtime($filePath)); // Get the last modified date

        // Add file information to the array
        $fileInfoList[] = [
            'name' => $file,
            'type' => $fileType,
            'last_modified' => $lastModified,
        ];
    }
}

// Close the directory handle
closedir($dirHandle);

// Output the file information as JSON
header('Content-Type: application/json');
echo json_encode($fileInfoList, JSON_PRETTY_PRINT);
?>
```
