"""
Generated Code Metadata:
========================
Original URL: https://nkftransporte.com
Prompt: Develop a PHP function that formats and displays file information (name, size, last modified) in a table, inspired by the nkftransporte.com directory listing.
Generated: DETERMINISTIC_b84ceed608ee6fff
Batch ID: 20250612_155436
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
 * Formats and displays file information in a table
 * 
 * @param string $directory Path to the directory to scan
 * @param array $excludedFiles Array of filenames to exclude from listing
 * @return void Outputs HTML table with file information
 * @throws Exception If directory cannot be opened
 */
function displayFileTable($directory, $excludedFiles = ['.', '..', '.htaccess']) {
    // Validate directory exists and is readable
    if (!is_dir($directory) || !is_readable($directory)) {
        throw new Exception("Directory '$directory' does not exist or is not readable");
    }

    // Open directory handle
    if (!($handle = opendir($directory))) {
        throw new Exception("Could not open directory '$directory'");
    }

    // Start HTML table
    echo '<table class="file-table">';
    echo '<thead><tr>';
    echo '<th>Name</th>';
    echo '<th>Size</th>';
    echo '<th>Last Modified</th>';
    echo '</tr></thead>';
    echo '<tbody>';

    // Read directory contents
    while (false !== ($file = readdir($handle))) {
        // Skip excluded files
        if (in_array($file, $excludedFiles)) {
            continue;
        }

        $filePath = $directory . DIRECTORY_SEPARATOR . $file;
        
        // Skip if not a file
        if (!is_file($filePath)) {
            continue;
        }

        // Get file info
        $fileSize = filesize($filePath);
        $lastModified = filemtime($filePath);

        // Format file size
        $formattedSize = formatFileSize($fileSize);

        // Format date
        $formattedDate = date('Y-m-d H:i:s', $lastModified);

        // Output table row
        echo '<tr>';
        echo '<td><a href="' . htmlspecialchars($file) . '">' . htmlspecialchars($file) . '</a></td>';
        echo '<td>' . htmlspecialchars($formattedSize) . '</td>';
        echo '<td>' . htmlspecialchars($formattedDate) . '</td>';
        echo '</tr>';
    }

    // Close table and directory handle
    echo '</tbody></table>';
    closedir($handle);
}

/**
 * Formats file size in human-readable format
 * 
 * @param int $bytes File size in bytes
 * @return string Formatted file size with appropriate unit
 */
function formatFileSize($bytes) {
    if ($bytes >= 1073741824) {
        return number_format($bytes / 1073741824, 2) . ' GB';
    } elseif ($bytes >= 1048576) {
        return number_format($bytes / 1048576, 2) . ' MB';
    } elseif ($bytes >= 1024) {
        return number_format($bytes / 1024, 2) . ' KB';
    } elseif ($bytes > 1) {
        return $bytes . ' bytes';
    } elseif ($bytes == 1) {
        return '1 byte';
    } else {
        return '0 bytes';
    }
}

// Example usage:
// try {
//     displayFileTable(__DIR__);
// } catch (Exception $e) {
//     echo 'Error: ' . $e->getMessage();
// }
?>
```
