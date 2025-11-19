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
 * Server Performance Monitor
 *
 * This script collects and displays server performance metrics on Linux hosting platforms.
 *
 * @author [Your Name]
 */

// Configuration
$config = [
    'updateInterval' => 60, // seconds
    'metrics' => [
        'cpuUsage' => true,
        'memoryUsage' => true,
        'diskUsage' => true,
        'networkTraffic' => true,
    ],
];

// Function to get CPU usage
function getCpuUsage() {
    $cpuUsage = shell_exec('top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/"');
    return (float) $cpuUsage;
}

// Function to get memory usage
function getMemoryUsage() {
    $memoryUsage = shell_exec('free -m | awk "NR==2{print \$3/\$2 * 100}"');
    return (float) $memoryUsage;
}

// Function to get disk usage
function getDiskUsage() {
    $diskUsage = shell_exec('df -h / | awk "NR==2{print \$5}"');
    $diskUsage = str_replace('%', '', $diskUsage);
    return (float) $diskUsage;
}

// Function to get network traffic
function getNetworkTraffic() {
    $networkTraffic = shell_exec('cat /proc/net/dev | grep -v "lo" | awk \'{print $2}\'');
    $networkTraffic = explode("\n", $networkTraffic);
    $networkTraffic = array_sum(array_map('intval', $networkTraffic));
    return $networkTraffic;
}

// Main function
function monitorServerPerformance($config) {
    $metrics = [];

    if ($config['metrics']['cpuUsage']) {
        $metrics['cpuUsage'] = getCpuUsage();
    }

    if ($config['metrics']['memoryUsage']) {
        $metrics['memoryUsage'] = getMemoryUsage();
    }

    if ($config['metrics']['diskUsage']) {
        $metrics['diskUsage'] = getDiskUsage();
    }

    if ($config['metrics']['networkTraffic']) {
        $metrics['networkTraffic'] = getNetworkTraffic();
    }

    return $metrics;
}

// Error handling
function handleError($error) {
    error_log($error, 0);
    http_response_code(500);
    echo "Internal Server Error";
    exit;
}

// Main execution
try {
    $metrics = monitorServerPerformance($config);
    header('Content-Type: application/json');
    echo json_encode($metrics, JSON_PRETTY_PRINT);
} catch (Exception $e) {
    handleError($e->getMessage());
}

?>
```
