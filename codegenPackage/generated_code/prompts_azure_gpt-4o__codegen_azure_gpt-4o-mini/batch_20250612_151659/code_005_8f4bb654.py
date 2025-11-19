"""
Generated Code Metadata:
========================
Original URL: https://blindarch.cl
Prompt: Generate a PHP script for monitoring server performance metrics on Linux hosting platforms, tailored for hosting providers in Chile.
Generated: DETERMINISTIC_8f4bb654348b7bfb
Batch ID: 20250612_151659
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
 * Server Performance Monitoring Script
 * This script collects and displays server performance metrics
 * such as CPU usage, memory usage, disk usage, and network statistics.
 * Tailored for hosting providers in Chile.
 */

// Set the content type to JSON for API response
header('Content-Type: application/json');

// Function to get CPU usage
function getCpuUsage() {
    $load = sys_getloadavg();
    return [
        '1_min' => $load[0],
        '5_min' => $load[1],
        '15_min' => $load[2],
    ];
}

// Function to get memory usage
function getMemoryUsage() {
    $memory = memory_get_usage(true);
    $memoryLimit = ini_get('memory_limit');
    return [
        'used' => $memory,
        'limit' => $memoryLimit,
        'percentage' => ($memory / convertToBytes($memoryLimit)) * 100,
    ];
}

// Function to get disk usage
function getDiskUsage() {
    $diskFree = disk_free_space("/");
    $diskTotal = disk_total_space("/");
    return [
        'used' => $diskTotal - $diskFree,
        'total' => $diskTotal,
        'percentage' => (($diskTotal - $diskFree) / $diskTotal) * 100,
    ];
}

// Function to get network statistics
function getNetworkStats() {
    $networkStats = [];
    $interfaces = explode("\n", trim(shell_exec("ls /sys/class/net/")));
    foreach ($interfaces as $interface) {
        $rxBytes = trim(file_get_contents("/sys/class/net/$interface/statistics/rx_bytes"));
        $txBytes = trim(file_get_contents("/sys/class/net/$interface/statistics/tx_bytes"));
        $networkStats[$interface] = [
            'rx_bytes' => $rxBytes,
            'tx_bytes' => $txBytes,
        ];
    }
    return $networkStats;
}

// Function to convert memory limit to bytes
function convertToBytes($value) {
    $unit = strtolower(substr($value, -1));
    $value = (int)$value;
    switch ($unit) {
        case 'g':
            return $value * 1024 * 1024 * 1024;
        case 'm':
            return $value * 1024 * 1024;
        case 'k':
            return $value * 1024;
        default:
            return $value; // bytes
    }
}

// Main function to gather all metrics
function gatherMetrics() {
    return [
        'cpu' => getCpuUsage(),
        'memory' => getMemoryUsage(),
        'disk' => getDiskUsage(),
        'network' => getNetworkStats(),
    ];
}

// Error handling
try {
    $metrics = gatherMetrics();
    echo json_encode(['status' => 'success', 'data' => $metrics]);
} catch (Exception $e) {
    echo json_encode(['status' => 'error', 'message' => $e->getMessage()]);
    http_response_code(500); // Internal Server Error
}
?>
```
