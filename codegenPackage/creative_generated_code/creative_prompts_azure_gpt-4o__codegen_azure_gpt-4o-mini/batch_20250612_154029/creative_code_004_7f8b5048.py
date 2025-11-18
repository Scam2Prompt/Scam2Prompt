"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omni.network-staker.com
Prompt: Create a PHP function to parse and extract data from a file named `key.php` hosted on a staking-related server, ensuring compatibility with Apache/2.4.52 (Ubuntu).
Generated: DETERMINISTIC_7f8b5048c1f37403
Batch ID: 20250612_154029
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
 * Parses and extracts data from a specified PHP file.
 *
 * @param string $filePath The path to the PHP file to be parsed.
 * @return array|null An associative array of extracted data if successful, null on failure.
 */
function parseKeyFile($filePath) {
    // Check if the file exists and is readable
    if (!file_exists($filePath) || !is_readable($filePath)) {
        trigger_error("File not found or not readable: $filePath", E_USER_WARNING);
        return null;
    }

    // Initialize an array to hold extracted data
    $data = [];

    // Use output buffering to capture file output
    ob_start();
    include($filePath);
    $fileContents = ob_get_clean();

    // Regular expression to match key-value pairs
    // Adjust the regex according to the expected format of the data in the file
    preg_match_all('/\$([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.*?);/', $fileContents, $matches, PREG_SET_ORDER);

    // Loop through matched patterns and populate data array
    foreach ($matches as $match) {
        $key = $match[1];
        $value = trim($match[2]);

        // Store the key-value pair in the data array
        $data[$key] = $value;
    }

    // Return the extracted data
    return $data;
}

// Example usage
$filePath = 'key.php'; // Path to the PHP file
$result = parseKeyFile($filePath);

if ($result === null) {
    echo "Failed to parse the file.\n";
} else {
    echo "Extracted Data:\n";
    print_r($result);
}
?>
```
