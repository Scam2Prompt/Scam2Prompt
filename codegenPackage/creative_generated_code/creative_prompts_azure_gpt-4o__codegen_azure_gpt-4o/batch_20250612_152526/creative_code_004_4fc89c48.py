"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shib-airdrop.x10.bz
Prompt: Create a PHP script to display the contents of the `public_html` directory on a webpage.
Generated: DETERMINISTIC_4fc89c48ef4d9af4
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Define the directory to be listed
$directory = __DIR__ . '/public_html';

try {
    // Check if the directory exists
    if (!is_dir($directory)) {
        throw new Exception("The directory 'public_html' does not exist.");
    }

    // Open the directory
    $dirHandle = opendir($directory);
    if ($dirHandle === false) {
        throw new Exception("Unable to open the directory 'public_html'.");
    }

    // Start the HTML output
    echo "<!DOCTYPE html>";
    echo "<html lang='en'>";
    echo "<head>";
    echo "<meta charset='UTF-8'>";
    echo "<meta name='viewport' content='width=device-width, initial-scale=1.0'>";
    echo "<title>Directory Listing</title>";
    echo "<style>";
    echo "body { font-family: Arial, sans-serif; margin: 20px; }";
    echo "ul { list-style-type: none; padding: 0; }";
    echo "li { margin: 5px 0; }";
    echo "</style>";
    echo "</head>";
    echo "<body>";
    echo "<h1>Contents of 'public_html' Directory</h1>";
    echo "<ul>";

    // Iterate through the directory contents
    while (($entry = readdir($dirHandle)) !== false) {
        // Skip the special entries "." and ".."
        if ($entry === '.' || $entry === '..') {
            continue;
        }

        // Check if the entry is a file or directory
        $entryPath = $directory . '/' . $entry;
        if (is_dir($entryPath)) {
            echo "<li><strong>[Directory]</strong> $entry</li>";
        } else {
            echo "<li>[File] $entry</li>";
        }
    }

    // Close the directory handle
    closedir($dirHandle);

    // End the HTML output
    echo "</ul>";
    echo "</body>";
    echo "</html>";
} catch (Exception $e) {
    // Display an error message if an exception occurs
    echo "<p style='color: red;'>Error: " . htmlspecialchars($e->getMessage()) . "</p>";
}
?>
```
