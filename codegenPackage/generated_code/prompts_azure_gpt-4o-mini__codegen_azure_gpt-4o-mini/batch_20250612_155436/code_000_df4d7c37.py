"""
Generated Code Metadata:
========================
Original URL: https://nkftransporte.com
Prompt: Generate a PHP script that retrieves the last modified date of a file from a web server, similar to how it's displayed in the index of nkftransporte.com.
Generated: DETERMINISTIC_df4d7c3796164358
Batch ID: 20250612_155436
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
 * Retrieves the last modified date of a specified file from a web server.
 * 
 * This script uses the `get_headers` function to fetch the headers of the file
 * and extracts the 'Last-Modified' header to display the last modified date.
 * 
 * Usage: php get_last_modified.php <url>
 */

// Check if the URL is provided as a command line argument
if ($argc !== 2) {
    echo "Usage: php get_last_modified.php <url>\n";
    exit(1);
}

// Get the URL from the command line argument
$url = $argv[1];

// Validate the URL
if (!filter_var($url, FILTER_VALIDATE_URL)) {
    echo "Error: Invalid URL provided.\n";
    exit(1);
}

// Function to retrieve the last modified date of a file
function getLastModifiedDate($url) {
    // Fetch the headers of the URL
    $headers = @get_headers($url, 1);

    // Check if the headers were retrieved successfully
    if ($headers === false) {
        echo "Error: Unable to retrieve headers for the URL: $url\n";
        return null;
    }

    // Check if the 'Last-Modified' header exists
    if (isset($headers['Last-Modified'])) {
        return $headers['Last-Modified'];
    } else {
        echo "Warning: 'Last-Modified' header not found for the URL: $url\n";
        return null;
    }
}

// Retrieve the last modified date
$lastModified = getLastModifiedDate($url);

// Display the result
if ($lastModified !== null) {
    echo "Last Modified Date: $lastModified\n";
} else {
    echo "Could not retrieve the last modified date.\n";
}
?>
```
