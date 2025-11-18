"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panccokesowpaflnace.com
Prompt: Create a PHP script named `generators.php` that generates random data and logs it into a directory structure similar to `logs/` and `tmp/`.
Generated: DETERMINISTIC_7b9a27c47a752bf6
Batch ID: 20250612_145924
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
 * generators.php
 *
 * This script generates random data and logs it into a directory structure:
 * - logs/ : Stores persistent logs
 * - tmp/  : Stores temporary logs
 *
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Define directory paths
define('LOGS_DIR', __DIR__ . '/logs/');
define('TMP_DIR', __DIR__ . '/tmp/');

// Ensure required directories exist
createDirectoryIfNotExists(LOGS_DIR);
createDirectoryIfNotExists(TMP_DIR);

/**
 * Main function that generates random data and writes to logs.
 */
function main() {
    // Generate random data
    $randomData = generateRandomData();

    // Log data persistently
    try {
        logData(LOGS_DIR, 'persistent_log.txt', $randomData);
    } catch (Exception $e) {
        error_log('Error writing to persistent log: ' . $e->getMessage());
    }

    // Log data temporarily
    try {
        logData(TMP_DIR, 'temporary_log.txt', $randomData);
    } catch (Exception $e) {
        error_log('Error writing to temporary log: ' . $e->getMessage());
    }
}

/**
 * Generates random data for logging.
 *
 * @return string The random data generated.
 */
function generateRandomData() {
    return json_encode([
        'timestamp' => date('Y-m-d H:i:s'),
        'random_number' => rand(1000, 9999),
        'message' => 'This is a random log entry.'
    ]);
}

/**
 * Writes data to a log file in the specified directory.
 *
 * @param string $directory Directory where the log file is located.
 * @param string $filename Name of the log file.
 * @param string $data Data to write to the log file.
 *
 * @throws Exception If unable to write to the file.
 */
function logData($directory, $filename, $data) {
    $filePath = $directory . $filename;

    // Append data to the file
    if (file_put_contents($filePath, $data . PHP_EOL, FILE_APPEND) === false) {
        throw new Exception('Failed to write to ' . $filePath);
    }
}

/**
 * Ensures a directory exists. If not, attempts to create it.
 *
 * @param string $directory The directory path.
 *
 * @throws Exception If unable to create the directory.
 */
function createDirectoryIfNotExists($directory) {
    if (!is_dir($directory)) {
        if (!mkdir($directory, 0755, true)) {
            throw new Exception('Failed to create directory: ' . $directory);
        }
    }
}

// Execute the script
main();
?>
```
