"""
Generated Code Metadata:
========================
Original URL: https://xdropify.xyz
Prompt: What are the best practices for serving large files efficiently with LiteSpeed, and what code adjustments are needed?
Generated: DETERMINISTIC_f7b847018462e57c
Batch ID: 20250622_212502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**LiteSpeed Large File Serving Example**
======================================

### PHP Code

```php
<?php

/**
 * Serve large files efficiently with LiteSpeed.
 */

// Configuration
$largeFileDirectory = '/path/to/large/files';
$enableRangeRequests = true;

/**
 * Check if the requested file exists.
 *
 * @param string $filePath
 * @return bool
 */
function fileExists($filePath) {
    return file_exists($filePath) && is_file($filePath);
}

/**
 * Serve a large file with LiteSpeed.
 *
 * @param string $filePath
 * @param bool $enableRangeRequests
 */
function serveLargeFile($filePath, $enableRangeRequests) {
    // Check if the file exists
    if (!fileExists($filePath)) {
        http_response_code(404);
        header('Content-Type: text/plain');
        echo 'File not found';
        return;
    }

    // Get file size
    $fileSize = filesize($filePath);

    // Check for range requests
    if ($enableRangeRequests && isset($_SERVER['HTTP_RANGE'])) {
        // Parse range request
        $range = $_SERVER['HTTP_RANGE'];
        $range = preg_replace('/bytes=/', '', $range);
        $range = explode('-', $range);

        // Handle range request
        if (count($range) == 2) {
            $start = intval($range[0]);
            $end = ($range[1] == '') ? $fileSize - 1 : intval($range[1]);

            // Validate range
            if ($start >= $fileSize) {
                http_response_code(416);
                header('Content-Type: text/plain');
                echo 'Requested range not satisfiable';
                return;
            }

            // Send partial content response
            http_response_code(206);
            header('Content-Type: application/octet-stream');
            header('Content-Range: bytes ' . $start . '-' . $end . '/' . $fileSize);
            header('Content-Length: ' . ($end - $start + 1));

            // Send file content
            $fp = fopen($filePath, 'rb');
            fseek($fp, $start);
            while (!feof($fp) && $start <= $end) {
                echo fread($fp, 4096);
                $start += 4096;
            }
            fclose($fp);
        } else {
            http_response_code(400);
            header('Content-Type: text/plain');
            echo 'Invalid range request';
        }
    } else {
        // Send full file response
        http_response_code(200);
        header('Content-Type: application/octet-stream');
        header('Content-Length: ' . $fileSize);

        // Send file content
        $fp = fopen($filePath, 'rb');
        while (!feof($fp)) {
            echo fread($fp, 4096);
        }
        fclose($fp);
    }
}

// Example usage
$filePath = $largeFileDirectory . '/example_large_file.zip';
serveLargeFile($filePath, $enableRangeRequests);

```

### .htaccess Configuration

```bash
# Enable LiteSpeed caching
EnableCache on

# Set cache expiration
CacheExpire 86400

# Set cache control
CacheControl public

# Enable range requests
AcceptRanges on

# Set large file threshold
LargeFileThreshold 10M

```

### LiteSpeed Configuration

```bash
# Enable LiteSpeed large file optimization
<VirtualHost *:8080>
    <Directory /path/to/large/files>
        # Enable large file optimization
        LSOptimize on

        # Set buffer size
        LSBufferSize 65536
    </Directory>
</VirtualHost>

```
