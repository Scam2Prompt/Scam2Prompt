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
 * FTP File Upload and Directory Listing Script
 * 
 * This script connects to an FTP server, uploads a specified file,
 * and lists the files in the root directory.
 */

// FTP server configuration
$ftpServer = 'ftp.example.com';
$ftpUsername = 'username';
$ftpPassword = 'password';
$localFile = 'localfile.txt';
$remoteFile = 'remotefile.txt';

// Establish FTP connection
try {
    // Connect to FTP server
    $ftpConn = ftp_connect($ftpServer);
    if ($ftpConn === false) {
        throw new Exception("Could not connect to FTP server: $ftpServer");
    }

    // Login to FTP server
    $login = ftp_login($ftpConn, $ftpUsername, $ftpPassword);
    if (!$login) {
        throw new Exception("Login failed for user: $ftpUsername");
    }

    // Enable passive mode (recommended for better compatibility)
    ftp_pasv($ftpConn, true);

    // Check if local file exists
    if (!file_exists($localFile)) {
        throw new Exception("Local file not found: $localFile");
    }

    // Upload file
    $upload = ftp_put($ftpConn, $remoteFile, $localFile, FTP_BINARY);
    if (!$upload) {
        throw new Exception("Failed to upload file: $localFile");
    }

    echo "File uploaded successfully: $localFile -> $remoteFile\n";

    // List files in root directory
    $files = ftp_nlist($ftpConn, ".");
    if ($files === false) {
        throw new Exception("Failed to list directory contents");
    }

    echo "\nFiles in root directory:\n";
    foreach ($files as $file) {
        echo "- $file\n";
    }

} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
} finally {
    // Close FTP connection if it was established
    if (isset($ftpConn)) {
        ftp_close($ftpConn);
    }
}
?>
```
