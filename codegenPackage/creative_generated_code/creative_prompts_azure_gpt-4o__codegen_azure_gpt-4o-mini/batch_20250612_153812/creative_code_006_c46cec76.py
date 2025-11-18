"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlayer.eigenda.cc
Prompt: Create a PHP script to parse the contents of `key.php` and display specific data in a formatted HTML table.
Generated: DETERMINISTIC_c46cec767cae5c5e
Batch ID: 20250612_153812
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
 * This script parses the contents of 'key.php' and displays specific data
 * in a formatted HTML table.
 */

// Define the path to the key.php file
$keyFilePath = 'key.php';

// Check if the file exists
if (!file_exists($keyFilePath)) {
    die('Error: key.php file not found.');
}

// Include the key.php file
// Assuming key.php returns an array of data
$data = include $keyFilePath;

// Check if the data is an array
if (!is_array($data)) {
    die('Error: Invalid data format in key.php. Expected an array.');
}

// Function to generate an HTML table from an array
function generateTable($data) {
    // Start the table
    $html = '<table border="1" cellpadding="5" cellspacing="0">';
    $html .= '<thead><tr>';
    
    // Create table headers
    foreach (array_keys($data[0]) as $header) {
        $html .= "<th>" . htmlspecialchars($header) . "</th>";
    }
    $html .= '</tr></thead><tbody>';
    
    // Create table rows
    foreach ($data as $row) {
        $html .= '<tr>';
        foreach ($row as $cell) {
            $html .= "<td>" . htmlspecialchars($cell) . "</td>";
        }
        $html .= '</tr>';
    }
    
    // Close the table
    $html .= '</tbody></table>';
    
    return $html;
}

// Generate the HTML table
$tableHtml = generateTable($data);

// Display the HTML table
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Parsed Data Table</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            text-align: left;
            padding: 8px;
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
    <h1>Data from key.php</h1>
    <?php echo $tableHtml; ?>
</body>
</html>
```
