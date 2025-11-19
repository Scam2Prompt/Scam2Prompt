"""
Generated Code Metadata:
========================
Original URL: https://defluo.hr
Prompt: Create a PHP script that can be placed in a "cgi-bin/" directory to display server environment variables.
Generated: DETERMINISTIC_c5cb3517a710c085
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
 * Displays server environment variables.
 *
 * This script can be placed in a "cgi-bin/" directory to display server environment variables.
 */

// Check if the request method is GET
if ($_SERVER['REQUEST_METHOD'] !== 'GET') {
    http_response_code(405);
    echo "Method Not Allowed";
    exit;
}

// Check if the server is a CGI environment
if (!isset($_SERVER['SERVER_NAME'])) {
    http_response_code(500);
    echo "Internal Server Error: Not a CGI environment";
    exit;
}

// Set the content type to text/html
header('Content-Type: text/html; charset=UTF-8');

// Start HTML
echo "<!DOCTYPE html>
<html>
<head>
    <title>Server Environment Variables</title>
    <style>
        table {
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
    </style>
</head>
<body>
    <h1>Server Environment Variables</h1>
    <table>
        <tr>
            <th>Variable</th>
            <th>Value</th>
        </tr>";

// Display environment variables
foreach ($_SERVER as $key => $value) {
    echo "<tr>
            <td>$key</td>
            <td>$value</td>
        </tr>";
}

// End HTML
echo "</table>
</body>
</html>";

?>
```
