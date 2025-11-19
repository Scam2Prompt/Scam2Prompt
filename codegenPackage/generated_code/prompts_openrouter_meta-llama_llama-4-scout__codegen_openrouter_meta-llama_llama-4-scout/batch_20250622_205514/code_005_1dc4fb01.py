"""
Generated Code Metadata:
========================
Original URL: https://hhyp.shop
Prompt: Create a simple PHP script that connects to an FTP server, uploads a file, and then lists the files in the root directory.
Generated: DETERMINISTIC_1dc4fb016fb2424e
Batch ID: 20250622_205514
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
 * FTP Client Script
 * 
 * This script connects to an FTP server, uploads a file, and lists the files in the root directory.
 */

// Configuration
$ftpHost = 'ftp.example.com';
$ftpUsername = 'username';
$ftpPassword = 'password';
$localFilePath = '/path/to/local/file.txt';
$remoteFileName = 'file.txt';

/**
 * Establish a connection to the FTP server
 * 
 * @param string $ftpHost
 * @param string $ftpUsername
 * @param string $ftpPassword
 * 
 * @return resource|false
 */
function connectToFtp($ftpHost, $ftpUsername, $ftpPassword) {
    $ftpConnection = ftp_connect($ftpHost);
    if (!$ftpConnection) {
        throw new Exception("Failed to connect to FTP server");
    }

    $login = ftp_login($ftpConnection, $ftpUsername, $ftpPassword);
    if (!$login) {
        throw new Exception("Failed to login to FTP server");
    }

    return $ftpConnection;
}

/**
 * Upload a file to the FTP server
 * 
 * @param resource $ftpConnection
 * @param string $localFilePath
 * @param string $remoteFileName
 * 
 * @return bool
 */
function uploadFile($ftpConnection, $localFilePath, $remoteFileName) {
    $upload = ftp_put($ftpConnection, $remoteFileName, $localFilePath, FTP_ASCII);
    if (!$upload) {
        throw new Exception("Failed to upload file to FTP server");
    }

    return $upload;
}

/**
 * List files in the root directory of the FTP server
 * 
 * @param resource $ftpConnection
 * 
 * @return array
 */
function listFiles($ftpConnection) {
    $files = ftp_nlist($ftpConnection, '.');
    if ($files === false) {
        throw new Exception("Failed to list files in FTP server");
    }

    return $files;
}

try {
    // Connect to FTP server
    $ftpConnection = connectToFtp($ftpHost, $ftpUsername, $ftpPassword);

    // Upload file
    uploadFile($ftpConnection, $localFilePath, $remoteFileName);

    // List files
    $files = listFiles($ftpConnection);

    // Print files
    echo "Files in the root directory:\n";
    foreach ($files as $file) {
        echo "$file\n";
    }

    // Close FTP connection
    ftp_close($ftpConnection);

} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

?>
```
