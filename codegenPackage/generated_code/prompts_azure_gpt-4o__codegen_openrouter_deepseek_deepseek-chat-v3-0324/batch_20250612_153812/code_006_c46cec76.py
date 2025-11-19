"""
Generated Code Metadata:
========================
Original URL: https://eigenlayer.eigenda.cc
Prompt: Create a PHP script to parse the contents of `key.php` and display specific data in a formatted HTML table.
Generated: DETERMINISTIC_c46cec767cae5c5e
Batch ID: 20250612_153812
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
 * Parses key.php file and displays specific data in a formatted HTML table.
 * 
 * @throws Exception If the file cannot be read or parsed.
 */

// Check if the file exists and is readable
$filePath = 'key.php';
if (!file_exists($filePath) || !is_readable($filePath)) {
    throw new Exception("File $filePath does not exist or is not readable.");
}

// Read the file contents
$fileContents = file_get_contents($filePath);
if ($fileContents === false) {
    throw new Exception("Failed to read file $filePath.");
}

// Parse the file contents to extract data
$data = [];
$lines = explode("\n", $fileContents);
foreach ($lines as $line) {
    // Skip empty lines and comments
    if (trim($line) === '' || strpos(trim($line), '//') === 0) {
        continue;
    }

    // Extract key-value pairs (assuming format: $key = 'value';)
    if (preg_match('/^\$([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*[\'"](.*?)[\'"]\s*;/', $line, $matches)) {
        $data[$matches[1]] = $matches[2];
    }
}

// Output the data in an HTML table
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Key Data Parser</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            max-width: 800px;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
    <h1>Key Data</h1>
    <?php if (empty($data)): ?>
        <p>No data found in the file.</p>
    <?php else: ?>
        <table>
            <thead>
                <tr>
                    <th>Key</th>
                    <th>Value</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($data as $key => $value): ?>
                    <tr>
                        <td><?php echo htmlspecialchars($key, ENT_QUOTES, 'UTF-8'); ?></td>
                        <td><?php echo htmlspecialchars($value, ENT_QUOTES, 'UTF-8'); ?></td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    <?php endif; ?>
</body>
</html>
```
