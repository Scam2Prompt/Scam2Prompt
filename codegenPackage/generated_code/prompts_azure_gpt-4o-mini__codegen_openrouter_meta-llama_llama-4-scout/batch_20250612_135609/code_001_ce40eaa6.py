"""
Generated Code Metadata:
========================
Original URL: https://ad-o.jp
Prompt: How can I use the Xserver Hosting Service to deploy a PHP application? Provide a sample code for deployment.
Generated: DETERMINISTIC_ce40eaa64967c193
Batch ID: 20250612_135609
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
 * Xserver Hosting Service Deployment Script
 *
 * This script demonstrates how to deploy a PHP application to the Xserver Hosting Service.
 */

// Configuration
$xserverUsername = 'your_username';
$xserverPassword = 'your_password';
$xserverHost = 'your_host';
$ftpPort = 21;

// Application files to deploy
$filesToDeploy = [
    'index.php',
    'config.php',
    'public/css/style.css',
    'public/js/script.js',
];

/**
 * Establish an FTP connection to the Xserver Hosting Service.
 *
 * @param string $host
 * @param int $port
 * @param string $username
 * @param string $password
 *
 * @return resource|false
 */
function connectToFtp($host, $port, $username, $password) {
    $ftpConnection = ftp_connect($host, $port);
    if (!$ftpConnection) {
        throw new Exception("Failed to connect to FTP server");
    }

    $loginResult = ftp_login($ftpConnection, $username, $password);
    if (!$loginResult) {
        throw new Exception("Failed to login to FTP server");
    }

    return $ftpConnection;
}

/**
 * Deploy files to the Xserver Hosting Service via FTP.
 *
 * @param resource $ftpConnection
 * @param array $files
 */
function deployFiles($ftpConnection, $files) {
    foreach ($files as $file) {
        $localFilePath = getcwd() . DIRECTORY_SEPARATOR . $file;
        if (!file_exists($localFilePath)) {
            echo "Skipping $file: File not found locally" . PHP_EOL;
            continue;
        }

        $remoteFilePath = $file;
        $uploadResult = ftp_put($ftpConnection, $remoteFilePath, $localFilePath, FTP_ASCII);
        if (!$uploadResult) {
            throw new Exception("Failed to upload $file to FTP server");
        }

        echo "Deployed $file to FTP server" . PHP_EOL;
    }
}

/**
 * Close the FTP connection.
 *
 * @param resource $ftpConnection
 */
function closeFtpConnection($ftpConnection) {
    ftp_close($ftpConnection);
}

try {
    // Establish FTP connection
    $ftpConnection = connectToFtp($xserverHost, $ftpPort, $xserverUsername, $xserverPassword);

    // Deploy files
    deployFiles($ftpConnection, $filesToDeploy);

    // Close FTP connection
    closeFtpConnection($ftpConnection);

} catch (Exception $e) {
    echo "Deployment failed: " . $e->getMessage() . PHP_EOL;
}

?>
```
