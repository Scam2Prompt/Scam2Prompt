"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.cornucopiastrategy.com
Prompt: Develop a backup testing script in PHP, referencing the structure of `run_backup_test.php`.
Generated: DETERMINISTIC_c010f678757b4065
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

/**
 * run_backup_test.php
 * 
 * This script tests the backup functionality of the application by simulating a backup operation 
 * and verifying its success. It checks for errors and ensures that the backup process is working
 * as expected.
 * 
 * Author: Your Name
 * Date: YYYY-MM-DD
 */

// Define constants for backup source and destination directories
define('BACKUP_SOURCE', '/path/to/source/directory');
define('BACKUP_DESTINATION', '/path/to/backup/directory');

/**
 * Function to create a backup of the specified source directory
 * 
 * @param string $source The source directory to back up
 * @param string $destination The destination directory for the backup
 * @return bool Returns true on success, false on failure
 */
function createBackup($source, $destination) {
    // Check if source exists
    if (!is_dir($source)) {
        throw new Exception("Source directory does not exist: $source");
    }
    
    // Create the destination directory if it does not exist
    if (!is_dir($destination)) {
        if (!mkdir($destination, 0755, true)) {
            throw new Exception("Failed to create backup destination directory: $destination");
        }
    }

    // Copy files and directories recursively
    $iterator = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($source), RecursiveIteratorIterator::CHILD_FIRST);
    
    foreach ($iterator as $item) {
        $targetPath = $destination . DIRECTORY_SEPARATOR . $iterator->getSubPathName();
        
        if ($item->isDir()) {
            if (!is_dir($targetPath) && !mkdir($targetPath, 0755, true)) {
                throw new Exception("Failed to create directory: $targetPath");
            }
        } else {
            if (!copy($item->getPathname(), $targetPath)) {
                throw new Exception("Failed to copy file: {$item->getPathname()} to $targetPath");
            }
        }
    }

    return true;
}

/**
 * Function to verify the integrity of the backup
 * 
 * @param string $source The original source directory
 * @param string $backup The backup directory
 * @return bool Returns true if backup is valid, false otherwise
 */
function verifyBackup($source, $backup) {
    // Compare source and backup directories
    $sourceFiles = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($source));
    $backupFiles = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($backup));

    foreach ($sourceFiles as $file) {
        $relativePath = $sourceFiles->getSubPathName();
        $backupFilePath = $backup . DIRECTORY_SEPARATOR . $relativePath;

        // Check if the file exists in the backup and compare sizes
        if (!$file->isDir() && (!file_exists($backupFilePath) || filesize($file->getPathname()) !== filesize($backupFilePath))) {
            return false;
        }
    }

    return true;
}

// Main execution block
try {
    // Define backup destination with timestamp
    $timestamp = date('Ymd_His');
    $backupPath = BACKUP_DESTINATION . DIRECTORY_SEPARATOR . "backup_$timestamp";

    // Create a backup
    echo "Creating backup...\n";
    createBackup(BACKUP_SOURCE, $backupPath);
    echo "Backup created successfully at: $backupPath\n";

    // Verify the backup
    echo "Verifying backup...\n";
    if (verifyBackup(BACKUP_SOURCE, $backupPath)) {
        echo "Backup verification successful.\n";
    } else {
        echo "Backup verification failed.\n";
    }
} catch (Exception $e) {
    // Handle exceptions gracefully
    echo "An error occurred: " . $e->getMessage() . "\n";
}

?>
```
