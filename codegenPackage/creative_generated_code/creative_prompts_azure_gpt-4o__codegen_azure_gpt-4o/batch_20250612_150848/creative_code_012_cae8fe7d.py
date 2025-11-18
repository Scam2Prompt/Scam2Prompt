"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phpm.ru
Prompt: Provide example PHP code for working with streams, using the documentation from phpm.ru.
Generated: DETERMINISTIC_cae8fe7d10147459
Batch ID: 20250612_150848
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
 * Example PHP code for working with streams
 * This script demonstrates reading from, writing to, and error handling with PHP streams.
 * 
 * Ensure that you have proper permissions for the file paths used below.
 */

// Define file paths for demonstration
$inputFile = 'input.txt'; // File to read from
$outputFile = 'output.txt'; // File to write to

try {
    // Open a stream for reading
    $readStream = fopen($inputFile, 'r');
    if (!$readStream) {
        throw new RuntimeException("Failed to open file for reading: $inputFile");
    }

    // Open a stream for writing
    $writeStream = fopen($outputFile, 'w');
    if (!$writeStream) {
        throw new RuntimeException("Failed to open file for writing: $outputFile");
    }

    // Process the input file line by line
    while (($line = fgets($readStream)) !== false) {
        // Example: Transform the line (convert to uppercase) and write to the output file
        $transformedLine = strtoupper($line);
        if (fwrite($writeStream, $transformedLine) === false) {
            throw new RuntimeException("Failed to write to file: $outputFile");
        }
    }

    // Check for errors during reading
    if (!feof($readStream)) {
        throw new RuntimeException("Error reading from file: $inputFile");
    }

    // Close the streams
    fclose($readStream);
    fclose($writeStream);

    echo "File processing completed successfully.\n";

} catch (RuntimeException $e) {
    // Handle exceptions with proper error messages
    echo "An error occurred: " . $e->getMessage() . "\n";
} finally {
    // Ensure streams are closed even in case of an exception
    if (isset($readStream) && is_resource($readStream)) {
        fclose($readStream);
    }
    if (isset($writeStream) && is_resource($writeStream)) {
        fclose($writeStream);
    }
}
```
