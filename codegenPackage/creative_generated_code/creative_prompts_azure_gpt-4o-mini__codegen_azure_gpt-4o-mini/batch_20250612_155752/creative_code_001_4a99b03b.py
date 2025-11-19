"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetespepe.net
Prompt: How can I use PHP to display the last modified date and size of files from a server directory like the one at wallstreetespepe.net?
Generated: DETERMINISTIC_4a99b03b2f76cfad
Batch ID: 20250612_155752
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
 * Display the last modified date and size of files in a specified directory.
 * 
 * This script reads all files from a given server directory and outputs
 * their last modified date and size in a user-friendly format.
 * 
 * @param string $directory The path to the directory to scan for files.
 * @return void
 */
function displayFileDetails($directory) {
    // Check if the directory exists
    if (!is_dir($directory)) {
        die("Error: The specified directory does not exist.");
    }

    // Open the directory
    if ($handle = opendir($directory)) {
        echo "<h1>Files in Directory: $directory</h1>";
        echo "<table border='1' cellpadding='5'>";
        echo "<tr><th>File Name</th><th>Last Modified</th><th>Size (bytes)</th></tr>";

        // Loop through the directory entries
        while (false !== ($file = readdir($handle))) {
            // Skip the current and parent directory entries
            if ($file != "." && $file != "..") {
                $filePath = $directory . DIRECTORY_SEPARATOR . $file;

                // Only process files (ignore subdirectories)
                if (is_file($filePath)) {
                    $lastModified = date("Y-m-d H:i:s", filemtime($filePath));
                    $fileSize = filesize($filePath);

                    // Output the file details in a table row
                    echo "<tr>
                            <td>{$file}</td>
                            <td>{$lastModified}</td>
                            <td>{$fileSize}</td>
                          </tr>";
                }
            }
        }

        // Close the directory handle
        closedir($handle);
        echo "</table>";
    } else {
        // Handle error opening the directory
        die("Error: Unable to open directory.");
    }
}

// Define the directory path (update this path as needed)
$directoryPath = '/path/to/your/directory';

// Call the function to display file details
displayFileDetails($directoryPath);
?>
```

**Note:** Replace `'/path/to/your/directory'` with the actual path to the directory you want to inspect. Make sure the web server has read permissions for that directory.
