"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.timeimprint.com
Prompt: Write a PHP script to automate website backups using Plesk's management tools.
Generated: DETERMINISTIC_ef4e145b7472d355
Batch ID: 20250612_151752
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
 * Plesk Website Backup Script
 * 
 * This script automates website backups using Plesk's CLI utility.
 * It creates a backup and stores it in a specified directory.
 * 
 * Ensure that Plesk CLI utilities are accessible and have permissions set correctly.
 */

// Configuration
$pleskCliPath = '/usr/local/psa/bin'; // Path to Plesk CLI utilities
$backupDirectory = '/var/backups/plesk'; // Directory to store backups
$domainName = 'example.com'; // Replace with your domain name
$backupFileName = 'backup_' . date('Y-m-d_H-i-s') . '.tar'; // Backup file name with timestamp

try {
    // Check if the backup directory exists; create it if necessary
    if (!is_dir($backupDirectory)) {
        if (!mkdir($backupDirectory, 0755, true)) {
            throw new Exception("Failed to create backup directory: $backupDirectory");
        }
    }

    // Construct the Plesk CLI backup command
    $backupCommand = sprintf(
        '%s/domain --backup %s --output-file %s/%s',
        escapeshellcmd($pleskCliPath),
        escapeshellarg($domainName),
        escapeshellarg($backupDirectory),
        escapeshellarg($backupFileName)
    );

    // Execute the backup command
    $output = [];
    $returnVar = 0;
    exec($backupCommand, $output, $returnVar);

    if ($returnVar !== 0) {
        throw new Exception("Backup failed. Command: $backupCommand\nOutput: " . implode("\n", $output));
    }

    echo "Backup completed successfully. File saved to $backupDirectory/$backupFileName\n";

} catch (Exception $e) {
    // Handle errors gracefully
    error_log($e->getMessage());
    echo "An error occurred: " . $e->getMessage() . "\n";
    exit(1);
}

?>
```
