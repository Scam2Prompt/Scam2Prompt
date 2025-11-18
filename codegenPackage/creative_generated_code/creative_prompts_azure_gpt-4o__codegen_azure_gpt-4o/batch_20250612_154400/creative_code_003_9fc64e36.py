"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axieinfinity.kesug.com
Prompt: Create a guide for migrating an existing website to a hosting service that provides free transfer and supports multiple PHP versions, as outlined on the iFastNet hosting page.
Generated: DETERMINISTIC_9fc64e3669ed4034
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a script written in PHP that can be used to back up your existing website and database, then transfer files to a new hosting service using FTP. This script is designed to work for migrating a website to a hosting provider such as iFastNet. Ensure you customize the configuration variables as per your hosting account.

```php
<?php
/**
 * Website Migration Script
 * This script automates backing up an existing website and transferring it to a new hosting service.
 * 
 * Requirements:
 * - PHP installed on the source server.
 * - FTP access to the destination server.
 *
 * IMPORTANT: Customize the configuration variables below.
 */

// Configuration: Source server details
$sourceWebsiteDirectory = '/path/to/your/website'; // Full path to your website files
$sourceDbHost = 'localhost';                       // Database host
$sourceDbName = 'your_database_name';              // Database name
$sourceDbUser = 'your_database_user';              // Database username
$sourceDbPassword = 'your_database_password';      // Database password

// Configuration: Destination server FTP details
$ftpHost = 'ftp.yourhostingprovider.com';          // FTP host
$ftpUsername = 'your_ftp_username';                // FTP username
$ftpPassword = 'your_ftp_password';                // FTP password
$ftpTargetDirectory = '/path/on/ftp/server';       // Target directory on the FTP server

// Configuration: Temporary backup location
$tempBackupDir = __DIR__ . '/backup';              // Temporary local backup directory

try {
    // Step 1: Create a backup folder
    if (!is_dir($tempBackupDir)) {
        mkdir($tempBackupDir, 0755, true);
    }

    // Step 2: Backup website files
    $websiteBackup = $tempBackupDir . '/website_files.zip';
    $zip = new ZipArchive();
    if ($zip->open($websiteBackup, ZipArchive::CREATE | ZipArchive::OVERWRITE) === true) {
        $files = new RecursiveIteratorIterator(
            new RecursiveDirectoryIterator($sourceWebsiteDirectory),
            RecursiveIteratorIterator::LEAVES_ONLY
        );
        foreach ($files as $file) {
            if (!$file->isDir()) {
                $filePath = $file->getRealPath();
                $relativePath = substr($filePath, strlen($sourceWebsiteDirectory) + 1);
                $zip->addFile($filePath, $relativePath);
            }
        }
        $zip->close();
        echo "Website files backed up successfully.\n";
    } else {
        throw new Exception('Failed to create website file backup.');
    }

    // Step 3: Backup database
    $dbBackup = $tempBackupDir . '/database.sql';
    $backupCommand = sprintf(
        'mysqldump -h%s -u%s -p%s %s > %s',
        escapeshellarg($sourceDbHost),
        escapeshellarg($sourceDbUser),
        escapeshellarg($sourceDbPassword),
        escapeshellarg($sourceDbName),
        escapeshellarg($dbBackup)
    );
    exec($backupCommand, $output, $resultCode);
    if ($resultCode === 0) {
        echo "Database backed up successfully.\n";
    } else {
        throw new Exception('Failed to create database backup.');
    }

    // Step 4: Connect to FTP server
    $ftpConnection = ftp_connect($ftpHost);
    if (!$ftpConnection) {
        throw new Exception('Failed to connect to FTP server.');
    }
    $loginResult = ftp_login($ftpConnection, $ftpUsername, $ftpPassword);
    if (!$loginResult) {
        ftp_close($ftpConnection);
        throw new Exception('Failed to login to FTP server.');
    }
    ftp_pasv($ftpConnection, true); // Enable passive mode

    // Step 5: Upload backups to FTP server
    if (!ftp_put($ftpConnection, $ftpTargetDirectory . '/website_files.zip', $websiteBackup, FTP_BINARY)) {
        throw new Exception('Failed to upload website files backup to FTP server.');
    }
    if (!ftp_put($ftpConnection, $ftpTargetDirectory . '/database.sql', $dbBackup, FTP_BINARY)) {
        throw new Exception('Failed to upload database backup to FTP server.');
    }

    echo "Files uploaded successfully to the FTP server.\n";

    // Step 6: Clean up temporary backup files
    unlink($websiteBackup);
    unlink($dbBackup);
    rmdir($tempBackupDir);

    // Close FTP connection
    ftp_close($ftpConnection);

    echo "Migration completed successfully.\n";

} catch (Exception $e) {
    // Handle errors
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```

**Usage Notes:**
- Save the script as `migrate.php` and place it on the server you want to migrate.
- Run the script via CLI using `php migrate.php`.
- Ensure you have installed `mysqldump` and it is accessible via the command line on the source server.
- Review the permissions for your directories and files to avoid issues during backup and transfer.
