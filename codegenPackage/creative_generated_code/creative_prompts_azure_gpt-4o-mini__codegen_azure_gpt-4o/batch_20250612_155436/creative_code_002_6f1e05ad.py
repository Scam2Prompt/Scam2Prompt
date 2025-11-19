"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nkftransporte.com
Prompt: Create an API endpoint in PHP that serves a directory index, similar to the one on nkftransporte.com, including file size and last modified date.
Generated: DETERMINISTIC_6f1e05ad67cdaa0a
Batch ID: 20250612_155436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Filename: directoryIndexAPI.php

// Enable strict error reporting for development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Set appropriate headers for the API
header('Content-Type: application/json');

// Function to format file size in a human-readable format
function formatFileSize($bytes) {
    if ($bytes < 1024) return $bytes . ' B';
    if ($bytes < 1048576) return round($bytes / 1024, 2) . ' KB';
    if ($bytes < 1073741824) return round($bytes / 1048576, 2) . ' MB';
    return round($bytes / 1073741824, 2) . ' GB';
}

// Function to create the directory index
function getDirectoryIndex($dirPath) {
    // Ensure the directory exists
    if (!is_dir($dirPath)) {
        http_response_code(404);
        return ['error' => 'Directory not found'];
    }

    // Open the directory and read its contents
    $files = scandir($dirPath);
    if ($files === false) {
        http_response_code(500);
        return ['error' => 'Failed to read the directory'];
    }

    // Prepare the response data
    $directoryIndex = [];
    foreach ($files as $file) {
        // Ignore current and parent directory entries
        if ($file === '.' || $file === '..') continue;

        $filePath = $dirPath . DIRECTORY_SEPARATOR . $file;

        // Get file details
        $fileInfo = [
            'name' => $file,
            'size' => is_file($filePath) ? formatFileSize(filesize($filePath)) : 'N/A',
            'last_modified' => date('Y-m-d H:i:s', filemtime($filePath)),
            'type' => is_dir($filePath) ? 'directory' : 'file'
        ];

        $directoryIndex[] = $fileInfo;
    }

    return $directoryIndex;
}

// Main script logic
$requestedDir = isset($_GET['dir']) ? $_GET['dir'] : '.';
$realPath = realpath($requestedDir);

// Ensure the requested path is within the allowed directory
$baseDir = realpath(__DIR__);
if (strpos($realPath, $baseDir) !== 0) {
    http_response_code(403);
    echo json_encode(['error' => 'Access denied']);
    exit;
}

// Generate and return the directory index
$response = getDirectoryIndex($realPath);
echo json_encode($response, JSON_PRETTY_PRINT);
?>
```

### How to use:
1. Place this script in your web server's root directory or a subdirectory.
2. Access the endpoint by navigating to `/directoryIndexAPI.php?dir=<desired_directory>` in your browser or using an HTTP client.
3. Replace `<desired_directory>` with the relative path of the directory you want to index. If omitted, it defaults to the current directory.
