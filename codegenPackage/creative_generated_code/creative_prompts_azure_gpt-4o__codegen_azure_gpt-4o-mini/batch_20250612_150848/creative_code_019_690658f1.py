"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phpm.ru
Prompt: Recommend a PHP library for working with XML and generate example code, based on the phpm.ru documentation.
Generated: DETERMINISTIC_690658f1104b0fe4
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
 * Example code demonstrating the usage of the SimpleXML library in PHP 
 * for working with XML data.
 */

// Ensure error reporting is enabled for debugging during development
error_reporting(E_ALL);
ini_set('display_errors', 1);

/**
 * Function to load and parse XML data from a given file.
 *
 * @param string $filePath Path to the XML file.
 * @return SimpleXMLElement|null Returns a SimpleXMLElement on success, null on failure.
 */
function loadXML($filePath) {
    // Check if the file exists
    if (!file_exists($filePath)) {
        throw new RuntimeException("File not found: $filePath");
    }

    // Load the XML file and handle possible errors
    libxml_use_internal_errors(true); // Suppress XML errors for custom handling
    $xml = simplexml_load_file($filePath);

    if ($xml === false) {
        // Collect errors and prepare a user-friendly message
        $errors = libxml_get_errors();
        libxml_clear_errors();
        $errorMessage = "Failed loading XML: ";
        foreach ($errors as $error) {
            $errorMessage .= "\n - " . $error->message;
        }
        throw new RuntimeException($errorMessage);
    }

    return $xml;
}

/**
 * Function to display XML data in a readable format.
 *
 * @param SimpleXMLElement $xml The SimpleXMLElement object to display.
 */
function displayXML(SimpleXMLElement $xml) {
    // Convert XML object to string and format for readability
    echo $xml->asXML() . PHP_EOL;
}

// Example usage
try {
    // Load the XML data from a file
    $xmlData = loadXML('example.xml');

    // Display the loaded XML data
    displayXML($xmlData);
} catch (RuntimeException $e) {
    // Handle exceptions gracefully
    echo "An error occurred: " . $e->getMessage() . PHP_EOL;
}
?>
```

This code demonstrates how to work with XML in PHP using the SimpleXML library, including error handling and documentation. Adjust the file path in the `loadXML` function call to point to your actual XML file.
