"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wombatexchange.rf.gd
Prompt: Write a PHP script to monitor daily process usage on a hosting service that advertises no daily process limits, such as iFastNet.
Generated: DETERMINISTIC_f8b26f5cd661160d
Batch ID: 20250612_154239
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
 * monitor_process_usage.php
 *
 * This script monitors daily process usage on a hosting service.
 * It logs the process usage statistics to a file.
 * 
 * Requirements:
 * - PHP CLI (Command Line Interface)
 * - Proper permissions for reading system process info and writing logs
 *
 * Usage:
 * Run this script via the command line: `php monitor_process_usage.php`
 */

// Configuration
$logFile = __DIR__ . '/process_usage_log.txt'; // Log file location
$monitorInterval = 60; // Time interval in seconds between checks

/**
 * Get the current system process usage.
 *
 * @return array Returns an associative array with process usage statistics.
 */
function getProcessUsage()
{
    $usageData = [
        'timestamp' => date('Y-m-d H:i:s'),
        'process_count' => 0,
        'error' => null,
    ];

    try {
        // Execute shell command to get process count (works on Linux-based systems)
        $processCount = shell_exec("ps aux | wc -l");

        if ($processCount === null) {
            throw new Exception("Failed to retrieve process count.");
        }

        // Clean up and parse output
        $usageData['process_count'] = intval(trim($processCount));
    } catch (Exception $e) {
        // Capture error message
        $usageData['error'] = $e->getMessage();
    }

    return $usageData;
}

/**
 * Log process usage data to a file.
 *
 * @param array $data Associative array containing process usage information.
 * @param string $filePath Path to the log file.
 * @return void
 */
function logProcessUsage(array $data, string $filePath)
{
    $logEntry = sprintf(
        "[%s] Process Count: %d %s\n",
        $data['timestamp'],
        $data['process_count'],
        $data['error'] ? "| Error: " . $data['error'] : ""
    );

    try {
        if (!file_put_contents($filePath, $logEntry, FILE_APPEND)) {
            throw new Exception("Failed to write to log file.");
        }
    } catch (Exception $e) {
        // Print error to console (or handle appropriately for production)
        echo "Logging Error: " . $e->getMessage() . PHP_EOL;
    }
}

// Main Execution Loop
echo "Monitoring process usage. Press Ctrl+C to stop.\n";

while (true) {
    // Fetch usage data
    $usageData = getProcessUsage();

    // Log usage data to file
    logProcessUsage($usageData, $logFile);

    // Print status to the console
    if ($usageData['error']) {
        echo "Error: " . $usageData['error'] . PHP_EOL;
    } else {
        echo "[" . $usageData['timestamp'] . "] Process Count: " . $usageData['process_count'] . "\n";
    }

    // Wait for the next interval
    sleep($monitorInterval);
}
```
