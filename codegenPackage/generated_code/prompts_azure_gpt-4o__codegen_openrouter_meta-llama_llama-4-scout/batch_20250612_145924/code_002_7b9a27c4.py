"""
Generated Code Metadata:
========================
Original URL: https://panccokesowpaflnace.com
Prompt: Create a PHP script named `generators.php` that generates random data and logs it into a directory structure similar to `logs/` and `tmp/`.
Generated: DETERMINISTIC_7b9a27c47a752bf6
Batch ID: 20250612_145924
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
 * Generates random data and logs it into a directory structure.
 */

// Configuration
const LOGS_DIR = 'logs/';
const TMP_DIR = 'tmp/';
const DATA_FILE_PREFIX = 'data_';
const LOG_FILE_PREFIX = 'log_';

// Create directories if they do not exist
function createDirectories(): void
{
    $dirs = [LOGS_DIR, TMP_DIR];
    foreach ($dirs as $dir) {
        if (!file_exists($dir)) {
            mkdir($dir, 0755, true);
        }
    }
}

/**
 * Generates random data.
 *
 * @return string
 */
function generateRandomData(): string
{
    $data = [];
    for ($i = 0; $i < 10; $i++) {
        $data[] = uniqid();
    }
    return json_encode($data);
}

/**
 * Logs data to a file.
 *
 * @param string $data
 * @param string $filePrefix
 * @param string $dir
 */
function logDataToFile(string $data, string $filePrefix, string $dir): void
{
    $fileName = $filePrefix . date('Y-m-d_H-i-s') . '.txt';
    $filePath = $dir . $fileName;
    try {
        file_put_contents($filePath, $data);
        echo "Logged data to $filePath" . PHP_EOL;
    } catch (Exception $e) {
        echo "Error logging data to $filePath: " . $e->getMessage() . PHP_EOL;
    }
}

function main(): void
{
    createDirectories();

    $randomData = generateRandomData();

    // Log to tmp/
    logDataToFile($randomData, DATA_FILE_PREFIX, TMP_DIR);

    // Log to logs/
    logDataToFile($randomData, LOG_FILE_PREFIX, LOGS_DIR);
}

main();

?>
```
