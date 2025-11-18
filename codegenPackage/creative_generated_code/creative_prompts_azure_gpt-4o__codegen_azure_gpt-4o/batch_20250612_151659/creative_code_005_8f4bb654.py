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
 * This script monitors key server performance metrics for Linux hosting platforms.
 * Designed for hosting providers in Chile.
 * 
 * Metrics Monitored:
 * - CPU usage
 * - Memory usage
 * - Disk usage
 * - Network activity
 * 
 * Outputs JSON data for easy integration with monitoring dashboards.
 */

// Set the timezone to Santiago, Chile
date_default_timezone_set('America/Santiago');

/**
 * Get CPU usage percentage.
 */
function getCpuUsage()
{
    try {
        $load = sys_getloadavg(); // Get system load averages
        return $load[0]; // Return 1-minute load average
    } catch (Exception $e) {
        return "Error retrieving CPU usage: " . $e->getMessage();
    }
}

/**
 * Get memory usage stats.
 */
function getMemoryUsage()
{
    try {
        $data = file_get_contents("/proc/meminfo");
        $lines = explode("\n", $data);

        $memoryInfo = [];
        foreach ($lines as $line) {
            if (preg_match('/^(\w+):\s+(\d+)/', $line, $matches)) {
                $memoryInfo[$matches[1]] = (int)$matches[2]; // Extract key-value pairs
            }
        }

        // Calculate usage percentage
        if (isset($memoryInfo['MemTotal'], $memoryInfo['MemAvailable'])) {
            $usedMemory = $memoryInfo['MemTotal'] - $memoryInfo['MemAvailable'];
            $usagePercentage = ($usedMemory / $memoryInfo['MemTotal']) * 100;
            return round($usagePercentage, 2);
        }

        throw new Exception("Missing memory data fields.");
    } catch (Exception $e) {
        return "Error retrieving memory usage: " . $e->getMessage();
    }
}

/**
 * Get disk usage stats.
 */
function getDiskUsage()
{
    try {
        $diskTotal = disk_total_space("/");
        $diskFree = disk_free_space("/");
        if ($diskTotal && $diskFree) {
            $diskUsed = $diskTotal - $diskFree;
            $usagePercentage = ($diskUsed / $diskTotal) * 100;
            return round($usagePercentage, 2);
        }

        throw new Exception("Disk space data unavailable.");
    } catch (Exception $e) {
        return "Error retrieving disk usage: " . $e->getMessage();
    }
}

/**
 * Get network activity stats.
 */
function getNetworkActivity()
{
    try {
        $data = @file_get_contents("/proc/net/dev");
        if ($data === false) {
            throw new Exception("Unable to read network data.");
        }

        $lines = explode("\n", $data);
        $networkStats = [];

        foreach ($lines as $line) {
            if (preg_match('/^\s*(\w+):\s+([\d\s]+)/', $line, $matches)) {
                $interface = $matches[1];
                $stats = preg_split('/\s+/', trim($matches[2]));

                // Extract received and sent bytes for each interface
                $networkStats[$interface] = [
                    'received_bytes' => (int)$stats[0],
                    'sent_bytes' => (int)$stats[8],
                ];
            }
        }

        return $networkStats;
    } catch (Exception $e) {
        return "Error retrieving network activity: " . $e->getMessage();
    }
}

/**
 * Main function to gather server metrics.
 */
function getServerMetrics()
{
    return [
        'timestamp' => date('Y-m-d H:i:s'), // Current timestamp
        'cpu_usage_percentage' => getCpuUsage(),
        'memory_usage_percentage' => getMemoryUsage(),
        'disk_usage_percentage' => getDiskUsage(),
        'network_activity' => getNetworkActivity(),
    ];
}

// Execute the monitoring function
$metrics = getServerMetrics();

// Output metrics as JSON
header('Content-Type: application/json');
echo json_encode($metrics, JSON_PRETTY_PRINT);
```
