"""
Generated Code Metadata:
========================
Original URL: https://www.cenvirmarketingdigital.com
Prompt: "Generate code to monitor and alert on changes in WordPress core files, plugins, or themes using PHP and server logs."
Generated: DETERMINISTIC_fd3c118e8fc8f7f5
Batch ID: 20250622_210655
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
 * WordPress File Change Monitor
 * 
 * This script monitors changes in WordPress core files, plugins, and themes.
 * It logs changes and sends alerts when modifications are detected.
 * 
 * Requirements:
 * - PHP 7.4 or higher
 * - Proper permissions to access WordPress directories
 * - Mail server configured for sending alerts
 */

// Configuration
define('WP_ROOT', '/path/to/wordpress'); // Update with the path to your WordPress installation
define('LOG_FILE', '/path/to/log/file.log'); // Path to the log file
define('ALERT_EMAIL', 'admin@example.com'); // Email to send alerts
define('HASH_FILE', '/path/to/hash/file.json'); // File to store hashes of monitored files

/**
 * Recursively scan a directory and generate a hash map of files.
 *
 * @param string $directory Path to the directory to scan.
 * @return array Associative array of file paths and their hashes.
 */
function generateFileHashes($directory) {
    $hashes = [];
    $iterator = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($directory));
    foreach ($iterator as $file) {
        if ($file->isFile()) {
            $filePath = $file->getRealPath();
            $hashes[$filePath] = hash_file('sha256', $filePath);
        }
    }
    return $hashes;
}

/**
 * Load existing file hashes from the hash file.
 *
 * @return array|null Associative array of file hashes or null if file does not exist.
 */
function loadExistingHashes() {
    if (file_exists(HASH_FILE)) {
        $data = file_get_contents(HASH_FILE);
        return json_decode($data, true);
    }
    return null;
}

/**
 * Save file hashes to the hash file.
 *
 * @param array $hashes Associative array of file hashes.
 * @return void
 */
function saveHashes($hashes) {
    file_put_contents(HASH_FILE, json_encode($hashes, JSON_PRETTY_PRINT));
}

/**
 * Log a message to the log file.
 *
 * @param string $message Message to log.
 * @return void
 */
function logMessage($message) {
    $timestamp = date('Y-m-d H:i:s');
    file_put_contents(LOG_FILE, "[$timestamp] $message\n", FILE_APPEND);
}

/**
 * Send an alert email.
 *
 * @param string $subject Email subject.
 * @param string $message Email body.
 * @return void
 */
function sendAlert($subject, $message) {
    mail(ALERT_EMAIL, $subject, $message);
}

/**
 * Monitor files for changes and alert if modifications are detected.
 *
 * @return void
 */
function monitorFiles() {
    $currentHashes = generateFileHashes(WP_ROOT);
    $existingHashes = loadExistingHashes();

    if ($existingHashes === null) {
        // First run: Save hashes and exit
        saveHashes($currentHashes);
        logMessage('Initial file hashes saved.');
        return;
    }

    $changesDetected = false;
    $alertMessage = "Changes detected in WordPress files:\n\n";

    foreach ($currentHashes as $file => $hash) {
        if (!isset($existingHashes[$file])) {
            $changesDetected = true;
            $alertMessage .= "New file added: $file\n";
            logMessage("New file added: $file");
        } elseif ($existingHashes[$file] !== $hash) {
            $changesDetected = true;
            $alertMessage .= "File modified: $file\n";
            logMessage("File modified: $file");
        }
    }

    foreach ($existingHashes as $file => $hash) {
        if (!isset($currentHashes[$file])) {
            $changesDetected = true;
            $alertMessage .= "File deleted: $file\n";
            logMessage("File deleted: $file");
        }
    }

    if ($changesDetected) {
        sendAlert('WordPress File Change Alert', $alertMessage);
    }

    // Update hashes
    saveHashes($currentHashes);
}

// Run the file monitoring function
monitorFiles();
?>
```
