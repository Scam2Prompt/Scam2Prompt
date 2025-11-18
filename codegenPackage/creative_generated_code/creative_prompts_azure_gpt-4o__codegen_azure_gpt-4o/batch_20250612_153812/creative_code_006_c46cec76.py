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
 * Parse the contents of key.php and display specific data in a formatted HTML table.
 * 
 * Assumptions:
 * - `key.php` contains PHP code that defines an array or dataset to be parsed.
 * - The script safely includes the file and extracts relevant data.
 */

// Define the path to the file to be parsed
$keyFile = 'key.php';

try {
    // Validate that the file exists
    if (!file_exists($keyFile)) {
        throw new Exception("The file 'key.php' does not exist.");
    }

    // Safely include the file
    // Suppress any output using output buffering
    ob_start();
    include $keyFile;
    ob_end_clean();

    // Ensure the expected variable or data is loaded
    if (!isset($data) || !is_array($data)) {
        throw new Exception("The included file does not define a valid data array.");
    }

    // Start outputting the HTML
    echo '<!DOCTYPE html>';
    echo '<html lang="en">';
    echo '<head>';
    echo '<meta charset="UTF-8">';
    echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">';
    echo '<title>Data Table</title>';
    echo '<style>
            table {
                border-collapse: collapse;
                width: 100%;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
          </style>';
    echo '</head>';
    echo '<body>';

    echo '<h1>Data Table</h1>';
    echo '<table>';
    echo '<thead>';
    echo '<tr>';
    echo '<th>Key</th>';
    echo '<th>Value</th>';
    echo '</tr>';
    echo '</thead>';
    echo '<tbody>';

    // Loop through the data array and populate the table
    foreach ($data as $key => $value) {
        echo '<tr>';
        echo '<td>' . htmlspecialchars($key) . '</td>';
        echo '<td>' . htmlspecialchars($value) . '</td>';
        echo '</tr>';
    }

    echo '</tbody>';
    echo '</table>';

    echo '</body>';
    echo '</html>';

} catch (Exception $e) {
    // Handle errors gracefully
    http_response_code(500);
    echo '<!DOCTYPE html>';
    echo '<html lang="en">';
    echo '<head>';
    echo '<meta charset="UTF-8">';
    echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">';
    echo '<title>Error</title>';
    echo '</head>';
    echo '<body>';
    echo '<h1>An error occurred</h1>';
    echo '<p>' . htmlspecialchars($e->getMessage()) . '</p>';
    echo '</body>';
    echo '</html>';
}
?>
```

**Note**: Ensure the `key.php` file defines a `$data` variable that is an associative array, e.g., `$data = ['Name' => 'John', 'Age' => 30];`. This script assumes such a structure.
