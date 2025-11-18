"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wombatexchange.rf.gd
Prompt: Provide a step-by-step guide to transfer an existing website to a hosting provider like iFastNet, which offers free transfers and supports multiple versions of PHP.
Generated: DETERMINISTIC_518f9bfd0ac451ab
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready PHP script to facilitate transferring a website to a hosting provider like iFastNet. Note that this assumes you have access to the source website files and database, as well as credentials for both the source and target hosting.

```php
<?php
/**
 * Script to automate website file and database transfer to a new hosting provider.
 *
 * Requirements:
 * 1. PHP installed on local environment or old server.
 * 2. Credentials for both source and target hosting providers.
 *
 * Ensure you have enabled necessary permissions on the target hosting environment.
 */

// Configuration - Update these values
$sourceServer = [
    'ftp_host' => 'source-ftp-host.com',
    'ftp_user' => 'source_ftp_username',
    'ftp_pass' => 'source_ftp_password',
    'source_path' => '/path/to/source/files',
];

$targetServer = [
    'ftp_host' => 'target-ftp-host.com',
    'ftp_user' => 'target_ftp_username',
    'ftp_pass' => 'target_ftp_password',
    'target_path' => '/path/to/target/files',
];

$dbConfig = [
    'source_db_host' => 'source-db-host.com',
    'source_db_user' => 'source_db_username',
    'source_db_pass' => 'source_db_password',
    'source_db_name' => 'source_db_name',
    'target_db_host' => 'target-db-host.com',
    'target_db_user' => 'target_db_username',
    'target_db_pass' => 'target_db_password',
    'target_db_name' => 'target_db_name',
];

// Step 1: Backup Source Website Files
function backupSourceFiles($config) {
    $ftp = ftp_connect($config['ftp_host']);
    if (!$ftp) {
        die("Error: Unable to connect to source FTP server.");
    }
    $login = ftp_login($ftp, $config['ftp_user'], $config['ftp_pass']);
    if (!$login) {
        ftp_close($ftp);
        die("Error: Unable to log in to source FTP server.");
    }

    ftp_pasv($ftp, true); // Enable passive mode
    $localBackupDir = __DIR__ . '/backup/';
    if (!is_dir($localBackupDir)) {
        mkdir($localBackupDir, 0777, true);
    }

    ftpRecursiveDownload($ftp, $config['source_path'], $localBackupDir);

    ftp_close($ftp);
    echo "Source website files backed up successfully.\n";
}

// Helper function for recursive FTP download
function ftpRecursiveDownload($ftp, $remoteDir, $localDir) {
    $files = ftp_nlist($ftp, $remoteDir);
    if ($files === false) {
        die("Error: Unable to list files from $remoteDir.");
    }

    foreach ($files as $file) {
        $localPath = $localDir . '/' . basename($file);
        if (ftp_size($ftp, $file) == -1) { // Directory
            mkdir($localPath, 0777, true);
            ftpRecursiveDownload($ftp, $file, $localPath);
        } else { // File
            if (!ftp_get($ftp, $localPath, $file, FTP_BINARY)) {
                die("Error: Unable to download file $file.");
            }
        }
    }
}

// Step 2: Backup Source Database
function backupSourceDatabase($config) {
    $backupFile = __DIR__ . '/backup/source_db.sql';
    $command = sprintf(
        'mysqldump -h%s -u%s -p%s %s > %s',
        $config['source_db_host'],
        $config['source_db_user'],
        $config['source_db_pass'],
        $config['source_db_name'],
        $backupFile
    );

    exec($command, $output, $returnVar);
    if ($returnVar !== 0) {
        die("Error: Failed to back up source database.");
    }

    echo "Source database backed up successfully.\n";
}

// Step 3: Upload Files to Target Server
function uploadFilesToTarget($config) {
    $ftp = ftp_connect($config['ftp_host']);
    if (!$ftp) {
        die("Error: Unable to connect to target FTP server.");
    }
    $login = ftp_login($ftp, $config['ftp_user'], $config['ftp_pass']);
    if (!$login) {
        ftp_close($ftp);
        die("Error: Unable to log in to target FTP server.");
    }

    ftp_pasv($ftp, true); // Enable passive mode
    $localBackupDir = __DIR__ . '/backup/';
    ftpRecursiveUpload($ftp, $localBackupDir, $config['target_path']);

    ftp_close($ftp);
    echo "Files uploaded to target server successfully.\n";
}

// Helper function for recursive FTP upload
function ftpRecursiveUpload($ftp, $localDir, $remoteDir) {
    $files = scandir($localDir);
    if ($files === false) {
        die("Error: Unable to list files from $localDir.");
    }

    foreach ($files as $file) {
        if ($file === '.' || $file === '..') {
            continue;
        }
        $localPath = $localDir . '/' . $file;
        $remotePath = $remoteDir . '/' . $file;

        if (is_dir($localPath)) {
            ftp_mkdir($ftp, $remotePath);
            ftpRecursiveUpload($ftp, $localPath, $remotePath);
        } else {
            if (!ftp_put($ftp, $remotePath, $localPath, FTP_BINARY)) {
                die("Error: Unable to upload file $file.");
            }
        }
    }
}

// Step 4: Restore Database on Target Server
function restoreDatabaseOnTarget($config) {
    $backupFile = __DIR__ . '/backup/source_db.sql';
    $command = sprintf(
        'mysql -h%s -u%s -p%s %s < %s',
        $config['target_db_host'],
        $config['target_db_user'],
        $config['target_db_pass'],
        $config['target_db_name'],
        $backupFile
    );

    exec($command, $output, $returnVar);
    if ($returnVar !== 0) {
        die("Error: Failed to restore database to target server.");
    }

    echo "Database restored to target server successfully.\n";
}

// Execute the steps
echo "Starting website transfer process...\n";

// Step 1: Backup Files
backupSourceFiles($sourceServer);

// Step 2: Backup Database
backupSourceDatabase($dbConfig);

// Step 3: Upload Files
uploadFilesToTarget($targetServer);

// Step 4: Restore Database
restoreDatabaseOnTarget($dbConfig);

echo "Website transfer process completed successfully.\n";
?>
```

**Notes:**
- Replace `sourceServer` and `targetServer` with appropriate FTP credentials.
- Replace `dbConfig` with appropriate database credentials.
- Make sure the necessary tools (e.g., `mysqldump`, `mysql`) are installed on the machine executing the script.
- Ensure proper permissions on the target hosting environment for uploads and database import.
