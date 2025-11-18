"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morpheus-labs.net
Prompt: Generate a PHP script to upload website files to a Hostinger server and verify successful deployment.
Generated: DETERMINISTIC_e41c0ca1fc39e39c
Batch ID: 20250612_152920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Upload and deploy website files to a Hostinger server
// Configuration
$host = 'ftp.example.com'; // Replace with your Hostinger FTP server address
$username = 'your_username'; // Replace with your Hostinger FTP username
$password = 'your_password'; // Replace with your Hostinger FTP password
$localDirectory = '/path/to/local/files'; // Replace with the path to local files
$remoteDirectory = '/path/to/remote/directory'; // Replace with the path on the server

/**
 * Uploads a file to the remote FTP server.
 * 
 * @param resource $ftpConnection The FTP connection resource.
 * @param string $localFile The path to the local file.
 * @param string $remoteFile The path to the remote file.
 * @return bool True if upload was successful, false otherwise.
 */
function uploadFile($ftpConnection, $localFile, $remoteFile)
{
    // Upload the file using FTP and binary mode
    $uploadStatus = ftp_put($ftpConnection, $remoteFile, $localFile, FTP_BINARY);
    if (!$uploadStatus) {
        throw new Exception("Failed to upload $localFile to $remoteFile.");
    }
    return $uploadStatus;
}

/**
 * Recursively uploads all files in a local directory to a remote FTP directory.
 * 
 * @param resource $ftpConnection The FTP connection resource.
 * @param string $localDir The path to the local directory.
 * @param string $remoteDir The path to the remote directory.
 */
function uploadDirectory($ftpConnection, $localDir, $remoteDir)
{
    // Ensure the remote directory exists
    if (!ftp_chdir($ftpConnection, $remoteDir)) {
        ftp_mkdir($ftpConnection, $remoteDir);
    }

    $localFiles = scandir($localDir);
    foreach ($localFiles as $file) {
        if ($file === '.' || $file === '..') {
            continue; // Skip these special directory entries
        }

        $localPath = $localDir . DIRECTORY_SEPARATOR . $file;
        $remotePath = $remoteDir . '/' . $file;

        if (is_dir($localPath)) {
            // Recursively upload subdirectories
            uploadDirectory($ftpConnection, $localPath, $remotePath);
        } else {
            // Upload individual files
            uploadFile($ftpConnection, $localPath, $remotePath);
        }
    }
}

/**
 * Main function to handle file upload and deployment
 */
function deployFiles($host, $username, $password, $localDirectory, $remoteDirectory)
{
    try {
        // Establish FTP connection
        $ftpConnection = ftp_connect($host);
        if (!$ftpConnection) {
            throw new Exception("Could not connect to FTP server: $host");
        }

        // Login to FTP server
        $loginStatus = ftp_login($ftpConnection, $username, $password);
        if (!$loginStatus) {
            throw new Exception("FTP login failed for user: $username");
        }

        // Enable passive mode for better compatibility
        ftp_pasv($ftpConnection, true);

        // Upload files
        uploadDirectory($ftpConnection, $localDirectory, $remoteDirectory);

        // Close the FTP connection
        ftp_close($ftpConnection);

        echo "Deployment to Hostinger server was successful.\n";
    } catch (Exception $e) {
        // Handle errors gracefully
        echo "Error: " . $e->getMessage() . "\n";
    }
}

// Execute the deployment
deployFiles($host, $username, $password, $localDirectory, $remoteDirectory);
?>
```
