"""
Generated Code Metadata:
========================
Original URL: https://binance2.epizy.com
Prompt: Provide a step-by-step guide to transfer an existing website to a hosting service that supports multiple PHP versions and offers free transfers, referencing iFastNet's hosting options.
Generated: DETERMINISTIC_8bfd739d1ad6ae38
Batch ID: 20250612_151446
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
 * Transfer an existing website to iFastNet hosting service.
 *
 * This script provides a step-by-step guide to transfer an existing website to iFastNet hosting service,
 * which supports multiple PHP versions and offers free transfers.
 */

// Configuration
$ifastnet_ftp_host = 'ftp.ifastnet.com';
$ifastnet_ftp_username = 'your_ifastnet_ftp_username';
$ifastnet_ftp_password = 'your_ifastnet_ftp_password';
$ifastnet_ftp_port = 21;

// Website configuration
$website_directory = '/path/to/your/website';
$php_version = '7.4'; // Specify the desired PHP version

// Function to connect to iFastNet FTP server
function connect_to_ifastnet_ftp($host, $username, $password, $port) {
    $ftp_connection = ftp_connect($host, $port);
    if (!$ftp_connection) {
        throw new Exception("Failed to connect to iFastNet FTP server");
    }

    $login = ftp_login($ftp_connection, $username, $password);
    if (!$login) {
        throw new Exception("Failed to login to iFastNet FTP server");
    }

    return $ftp_connection;
}

// Function to transfer website to iFastNet hosting
function transfer_website_to_ifastnet($ftp_connection, $website_directory, $php_version) {
    try {
        // Create a new directory for the website on iFastNet FTP server
        $ftp_directory = 'public_html';
        if (!ftp_chdir($ftp_connection, $ftp_directory)) {
            ftp_mkdir($ftp_connection, $ftp_directory);
            ftp_chdir($ftp_connection, $ftp_directory);
        }

        // Transfer website files to iFastNet FTP server
        $files = scandir($website_directory);
        foreach ($files as $file) {
            if ($file !== '.' && $file !== '..') {
                $file_path = $website_directory . '/' . $file;
                if (is_file($file_path)) {
                    $ftp_file_path = $ftp_directory . '/' . $file;
                    ftp_put($ftp_connection, $ftp_file_path, $file_path);
                } elseif (is_dir($file_path)) {
                    transfer_directory($ftp_connection, $file_path, $ftp_directory . '/' . $file);
                }
            }
        }

        // Set PHP version
        // Note: This step may vary depending on iFastNet's control panel and API
        // For demonstration purposes, assume a .user.ini file is used to set PHP version
        $php_ini_content = "phpversion=$php_version";
        $ftp_php_ini_path = $ftp_directory . '/.user.ini';
        ftp_put($ftp_connection, $ftp_php_ini_path, $php_ini_content);

    } catch (Exception $e) {
        echo "Error transferring website: " . $e->getMessage() . "\n";
    }
}

// Function to transfer a directory recursively
function transfer_directory($ftp_connection, $local_directory, $remote_directory) {
    $files = scandir($local_directory);
    foreach ($files as $file) {
        if ($file !== '.' && $file !== '..') {
            $file_path = $local_directory . '/' . $file;
            $remote_file_path = $remote_directory . '/' . $file;
            if (is_file($file_path)) {
                ftp_put($ftp_connection, $remote_file_path, $file_path);
            } elseif (is_dir($file_path)) {
                if (!ftp_chdir($ftp_connection, $remote_directory)) {
                    ftp_mkdir($ftp_connection, $remote_directory);
                    ftp_chdir($ftp_connection, $remote_directory);
                }
                transfer_directory($ftp_connection, $file_path, $remote_file_path);
            }
        }
    }
}

// Main function
function main() {
    try {
        // Connect to iFastNet FTP server
        $ftp_connection = connect_to_ifastnet_ftp($GLOBALS['ifastnet_ftp_host'], $GLOBALS['ifastnet_ftp_username'], $GLOBALS['ifastnet_ftp_password'], $GLOBALS['ifastnet_ftp_port']);

        // Transfer website to iFastNet hosting
        transfer_website_to_ifastnet($ftp_connection, $GLOBALS['website_directory'], $GLOBALS['php_version']);

        // Close FTP connection
        ftp_close($ftp_connection);

    } catch (Exception $e) {
        echo "Error: " . $e->getMessage() . "\n";
    }
}

main();

?>
```
