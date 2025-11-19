"""
Generated Code Metadata:
========================
Original URL: https://bpearlegy.com
Prompt: Create a simple CGI script in PHP to display the current server time and environment variables.
Generated: DETERMINISTIC_550567040bf7a69d
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Set the content type to HTML
header('Content-Type: text/html; charset=utf-8');

// Function to safely display environment variables
function safeDisplay($value) {
    return htmlspecialchars($value, ENT_QUOTES, 'UTF-8');
}

// Get current server time
$currentTime = date('Y-m-d H:i:s');

// Get environment variables
$envVars = $_SERVER;
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Server Information</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            color: #333;
        }
        h1 {
            color: #2c3e50;
        }
        .time {
            font-size: 1.2em;
            margin-bottom: 20px;
            padding: 10px;
            background-color: #f8f9fa;
            border-radius: 4px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #f2f2f2;
        }
        tr:hover {
            background-color: #f5f5f5;
        }
    </style>
</head>
<body>
    <h1>Server Information</h1>
    
    <div class="time">
        <strong>Current Server Time:</strong> <?php echo safeDisplay($currentTime); ?>
    </div>
    
    <h2>Environment Variables</h2>
    <table>
        <thead>
            <tr>
                <th>Variable</th>
                <th>Value</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($envVars as $key => $value): ?>
                <tr>
                    <td><?php echo safeDisplay($key); ?></td>
                    <td><?php echo safeDisplay($value); ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```
