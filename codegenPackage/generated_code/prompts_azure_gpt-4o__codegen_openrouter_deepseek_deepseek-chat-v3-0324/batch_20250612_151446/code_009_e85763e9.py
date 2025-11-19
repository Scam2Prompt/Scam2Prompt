"""
Generated Code Metadata:
========================
Original URL: https://kinglol.42web.io
Prompt: Create a PHP script to monitor bandwidth usage on a hosting service with unlimited bandwidth and modern cPanel, as described by iFastNet.
Generated: DETERMINISTIC_e85763e91481a098
Batch ID: 20250612_151446
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
 * Bandwidth Monitor for cPanel Hosting
 * 
 * This script monitors bandwidth usage on a cPanel hosting account with unlimited bandwidth.
 * It uses cPanel's UAPI to fetch bandwidth statistics and logs the data for monitoring.
 * 
 * @author Your Name
 * @version 1.0
 */

// Ensure script is run via CLI or web with proper authentication
if (php_sapi_name() !== 'cli' && !isset($_SERVER['HTTP_AUTHORIZATION'])) {
    header('HTTP/1.1 403 Forbidden');
    exit('Access denied. This script must be run via command line or with proper authentication.');
}

// Configuration
define('LOG_FILE', '/home/' . getenv('USER') . '/bandwidth_monitor.log');
define('MAX_LOG_SIZE', 1048576); // 1MB in bytes
define('ALERT_THRESHOLD', 90); // Percentage threshold for alerts
define('ALERT_EMAIL', 'admin@example.com');

// Main execution
try {
    $bandwidthData = getBandwidthUsage();
    logBandwidthData($bandwidthData);
    
    if (shouldSendAlert($bandwidthData)) {
        sendAlertEmail($bandwidthData);
    }
    
    echo "Bandwidth monitoring completed successfully.\n";
} catch (Exception $e) {
    error_log('Bandwidth Monitor Error: ' . $e->getMessage());
    exit('Error: ' . $e->getMessage());
}

/**
 * Fetches bandwidth usage data from cPanel UAPI
 * 
 * @return array Bandwidth usage data
 * @throws Exception If unable to fetch data
 */
function getBandwidthUsage(): array {
    $uapiCommand = '/usr/local/cpanel/bin/uapi --output=json StatsBar get_bandwidth_data';
    $output = shell_exec($uapiCommand);
    
    if (!$output) {
        throw new Exception('Failed to execute UAPI command');
    }
    
    $data = json_decode($output, true);
    
    if (json_last_error() !== JSON_ERROR_NONE || !isset($data['result']['data'])) {
        throw new Exception('Invalid or incomplete bandwidth data received');
    }
    
    return [
        'timestamp' => time(),
        'total' => $data['result']['data']['total'],
        'used' => $data['result']['data']['used'],
        'free' => $data['result']['data']['free'],
        'percent_used' => $data['result']['data']['percent_used']
    ];
}

/**
 * Logs bandwidth data to file with rotation
 * 
 * @param array $data Bandwidth data to log
 * @throws Exception If unable to write to log file
 */
function logBandwidthData(array $data): void {
    $logEntry = sprintf(
        "[%s] Used: %s/%s (%.2f%%)",
        date('Y-m-d H:i:s', $data['timestamp']),
        formatBytes($data['used']),
        formatBytes($data['total']),
        $data['percent_used']
    ) . PHP_EOL;
    
    // Rotate log if it's too large
    if (file_exists(LOG_FILE) && filesize(LOG_FILE) > MAX_LOG_SIZE) {
        $backupFile = LOG_FILE . '.' . time();
        if (!rename(LOG_FILE, $backupFile)) {
            throw new Exception('Failed to rotate log file');
        }
    }
    
    if (file_put_contents(LOG_FILE, $logEntry, FILE_APPEND | LOCK_EX) === false) {
        throw new Exception('Failed to write to log file');
    }
}

/**
 * Checks if an alert should be sent based on usage threshold
 * 
 * @param array $data Bandwidth data
 * @return bool True if alert should be sent
 */
function shouldSendAlert(array $data): bool {
    return $data['percent_used'] >= ALERT_THRESHOLD;
}

/**
 * Sends an alert email about high bandwidth usage
 * 
 * @param array $data Bandwidth data
 * @throws Exception If email fails to send
 */
function sendAlertEmail(array $data): void {
    $subject = 'Bandwidth Usage Alert: ' . $data['percent_used'] . '% Used';
    $message = sprintf(
        "Bandwidth usage alert!\n\n" .
        "Current Usage: %s/%s (%.2f%%)\n" .
        "Threshold: %d%%\n\n" .
        "This is an automated alert from your bandwidth monitoring system.",
        formatBytes($data['used']),
        formatBytes($data['total']),
        $data['percent_used'],
        ALERT_THRESHOLD
    );
    
    $headers = 'From: bandwidth-monitor@' . gethostname() . "\r\n";
    
    if (!mail(ALERT_EMAIL, $subject, $message, $headers)) {
        throw new Exception('Failed to send alert email');
    }
}

/**
 * Formats bytes to human-readable format
 * 
 * @param int $bytes Bytes to format
 * @param int $precision Decimal precision
 * @return string Formatted string
 */
function formatBytes(int $bytes, int $precision = 2): string {
    $units = ['B', 'KB', 'MB', 'GB', 'TB'];
    
    $bytes = max($bytes, 0);
    $pow = floor(($bytes ? log($bytes) : 0) / log(1024));
    $pow = min($pow, count($units) - 1);
    
    $bytes /= (1 << (10 * $pow));
    
    return round($bytes, $precision) . ' ' . $units[$pow];
}
```
