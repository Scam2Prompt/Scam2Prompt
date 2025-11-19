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
 * Generates random data and logs it into directory structures.
 * 
 * This script creates 'logs/' and 'tmp/' directories if they don't exist,
 * then generates random data files within them.
 */

// Ensure required directories exist
$directories = ['logs', 'tmp'];
foreach ($directories as $dir) {
    if (!file_exists($dir)) {
        if (!mkdir($dir, 0755, true)) {
            die("Failed to create directory: $dir");
        }
    }
}

/**
 * Generates random string of specified length.
 * 
 * @param int $length Length of the string to generate
 * @return string Randomly generated string
 */
function generateRandomString($length = 10) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, strlen($characters) - 1)];
    }
    return $randomString;
}

/**
 * Generates random log data with timestamp.
 * 
 * @return string Formatted log entry
 */
function generateLogData() {
    $timestamp = date('Y-m-d H:i:s');
    $logLevels = ['INFO', 'WARNING', 'ERROR', 'DEBUG'];
    $logLevel = $logLevels[array_rand($logLevels)];
    $message = generateRandomString(rand(20, 100));
    return "[$timestamp] [$logLevel] $message" . PHP_EOL;
}

/**
 * Generates random temporary data.
 * 
 * @return string Random data for temporary files
 */
function generateTempData() {
    $dataTypes = ['json', 'xml', 'csv'];
    $type = $dataTypes[array_rand($dataTypes)];
    
    switch ($type) {
        case 'json':
            return json_encode([
                'id' => uniqid(),
                'value' => rand(1, 1000),
                'timestamp' => time()
            ]);
        case 'xml':
            return '<?xml version="1.0"?><data><id>' . uniqid() . '</id><value>' . rand(1, 1000) . '</value></data>';
        case 'csv':
            return implode(',', [uniqid(), rand(1, 1000), time()]);
        default:
            return generateRandomString(rand(50, 200));
    }
}

// Generate log files
for ($i = 0; $i < 5; $i++) {
    $filename = 'logs/log_' . date('Ymd_His') . '_' . uniqid() . '.log';
    $content = '';
    for ($j = 0; $j < rand(5, 20); $j++) {
        $content .= generateLogData();
    }
    
    if (file_put_contents($filename, $content) === false) {
        error_log("Failed to write log file: $filename");
    }
}

// Generate temporary files
for ($i = 0; $i < 5; $i++) {
    $filename = 'tmp/temp_' . uniqid() . '.' . ['txt', 'json', 'xml', 'csv'][rand(0, 3)];
    $content = generateTempData();
    
    if (file_put_contents($filename, $content) === false) {
        error_log("Failed to write temp file: $filename");
    }
}

echo "Data generation completed successfully." . PHP_EOL;
?>
```
