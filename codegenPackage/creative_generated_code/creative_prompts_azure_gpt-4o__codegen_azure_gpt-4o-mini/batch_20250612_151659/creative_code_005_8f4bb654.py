"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blindarch.cl
Prompt: Generate a PHP script for monitoring server performance metrics on Linux hosting platforms, tailored for hosting providers in Chile.
Generated: DETERMINISTIC_8f4bb654348b7bfb
Batch ID: 20250612_151659
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
 * Server Performance Monitoring Script
 * This script collects and displays various server performance metrics
 * on Linux hosting platforms, tailored for hosting providers in Chile.
 * 
 * Requirements:
 * - PHP version 7.0 or higher
 * - Access to the server via CLI
 */

// Set the timezone for Chile
date_default_timezone_set('America/Santiago');

/**
 * Function to execute shell commands and return the output.
 *
 * @param string $command The command to execute.
 * @return string The output of the command.
 * @throws Exception If the command fails.
 */
function executeCommand($command) {
    // Execute the command and capture the output and return status
    $output = [];
    $returnVar = 0;
    exec($command, $output, $returnVar);
    
    // Check if the command executed successfully
    if ($returnVar !== 0) {
        throw new Exception("Command failed: $command");
    }
    
    // Return the output as a string
    return implode(PHP_EOL, $output);
}

/**
 * Function to collect CPU usage information.
 *
 * @return string CPU usage percentage.
 */
function getCpuUsage() {
    return executeCommand("top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1}'");
}

/**
 * Function to collect memory usage information.
 *
 * @return string Memory usage percentage.
 */
function getMemoryUsage() {
    return executeCommand("free | grep Mem | awk '{print $3/$2 * 100.0}'");
}

/**
 * Function to collect disk usage information.
 *
 * @return string Disk usage percentage for the root partition.
 */
function getDiskUsage() {
    return executeCommand("df -h / | grep / | awk '{ print $5 }'");
}

/**
 * Function to collect and display server performance metrics.
 */
function displayServerMetrics() {
    try {
        // Collect metrics
        $cpuUsage = getCpuUsage();
        $memoryUsage = getMemoryUsage();
        $diskUsage = getDiskUsage();

        // Display metrics
        echo "Server Performance Metrics:\n";
        echo "-----------------------------------\n";
        echo "CPU Usage: $cpuUsage%\n";
        echo "Memory Usage: $memoryUsage%\n";
        echo "Disk Usage: $diskUsage\n";
        echo "Collected on: " . date('Y-m-d H:i:s') . "\n";
        echo "-----------------------------------\n";
    } catch (Exception $e) {
        // Handle errors gracefully
        echo "Error: " . $e->getMessage() . "\n";
    }
}

// Execute the display function
displayServerMetrics();
?>
```
