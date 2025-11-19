"""
Generated Code Metadata:
========================
Original URL: https://mail.cornucopiastrategy.com
Prompt: Generate a PHP script to test multiple MailerLite API connections, using the methods from `test2_mailerlite_connection.php` through `test5_mailerlite_connection.php`.
Generated: DETERMINISTIC_d0d676acb0d70fc6
Batch ID: 20250612_155057
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
 * MailerLite API Connection Tester
 * 
 * This script tests multiple MailerLite API connections by including and executing
 * test scripts from test2_mailerlite_connection.php through test5_mailerlite_connection.php.
 * It aggregates and displays the results of all tests.
 */

require_once __DIR__ . '/vendor/autoload.php';

// Configuration for error reporting
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Define test files to include
$testFiles = [
    'test2_mailerlite_connection.php',
    'test3_mailerlite_connection.php',
    'test4_mailerlite_connection.php',
    'test5_mailerlite_connection.php'
];

// Initialize results array
$testResults = [];

/**
 * Run individual test file and capture results
 * 
 * @param string $filename The test file to include
 * @return array Test results including status and message
 */
function runTest($filename) {
    try {
        if (!file_exists(__DIR__ . '/' . $filename)) {
            throw new Exception("Test file not found: $filename");
        }

        // Start output buffering to capture test output
        ob_start();
        include __DIR__ . '/' . $filename;
        $output = ob_get_clean();

        return [
            'status' => 'success',
            'message' => $output,
            'filename' => $filename
        ];
    } catch (Exception $e) {
        return [
            'status' => 'error',
            'message' => $e->getMessage(),
            'filename' => $filename
        ];
    }
}

// Execute all tests
foreach ($testFiles as $testFile) {
    $testResults[] = runTest($testFile);
}

// Display results
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MailerLite API Connection Tests</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
        .test-container { margin-bottom: 30px; }
        .test-header { font-weight: bold; font-size: 1.2em; margin-bottom: 10px; }
        .success { color: green; }
        .error { color: red; }
        pre { background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }
    </style>
</head>
<body>
    <h1>MailerLite API Connection Test Results</h1>
    
    <?php foreach ($testResults as $result): ?>
    <div class="test-container">
        <div class="test-header">
            Test: <?php echo htmlspecialchars($result['filename']); ?> - 
            <span class="<?php echo $result['status']; ?>">
                <?php echo strtoupper($result['status']); ?>
            </span>
        </div>
        <div class="test-output">
            <pre><?php echo htmlspecialchars($result['message']); ?></pre>
        </div>
    </div>
    <?php endforeach; ?>
    
    <h2>Summary</h2>
    <p>Total tests: <?php echo count($testResults); ?></p>
    <p>Successful: <?php echo count(array_filter($testResults, fn($r) => $r['status'] === 'success')); ?></p>
    <p>Failed: <?php echo count(array_filter($testResults, fn($r) => $r['status'] === 'error')); ?></p>
</body>
</html>
```
