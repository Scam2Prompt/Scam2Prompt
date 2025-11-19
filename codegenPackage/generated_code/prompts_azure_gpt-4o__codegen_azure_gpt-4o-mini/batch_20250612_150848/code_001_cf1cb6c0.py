"""
Generated Code Metadata:
========================
Original URL: https://phpm.ru
Prompt: Generate a PHP script to create typographically correct text using the typographic tool described on phpm.ru.
Generated: DETERMINISTIC_cf1cb6c00cf466c7
Batch ID: 20250612_150848
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
 * Typographic Tool for PHP
 * This script takes a string input and applies typographic corrections
 * according to the rules defined on phpm.ru.
 * 
 * Usage: Call the `typographic` function with a string to get the corrected output.
 */

/**
 * Applies typographic corrections to the given text.
 *
 * @param string $text The input text to be corrected.
 * @return string The corrected text with proper typography.
 * @throws InvalidArgumentException If the input is not a string.
 */
function typographic($text) {
    // Validate input
    if (!is_string($text)) {
        throw new InvalidArgumentException('Input must be a string.');
    }

    // Define typographic replacements
    $replacements = [
        '/\s*([,.!?;:])/' => '$1', // Remove spaces before punctuation
        '/([,.!?;:])\s*/' => '$1 ', // Ensure space after punctuation
        '/\s{2,}/' => ' ', // Replace multiple spaces with a single space
        '/\s*-\s*/' => ' — ', // Replace hyphen with em dash
        '/\s*—\s*/' => ' — ', // Ensure proper spacing around em dash
        '/\s*“\s*/' => ' “', // Ensure proper spacing before opening quotes
        '/\s*”\s*/' => '” ', // Ensure proper spacing after closing quotes
        '/\s*‘\s*/' => ' ‘', // Ensure proper spacing before opening single quotes
        '/\s*’\s*/' => '’ ', // Ensure proper spacing after closing single quotes
    ];

    // Apply replacements
    $correctedText = preg_replace(array_keys($replacements), array_values($replacements), $text);

    // Return the corrected text
    return trim($correctedText);
}

// Example usage
try {
    $inputText = "  This is an example text  ,  with some typographic   errors!  ";
    $correctedText = typographic($inputText);
    echo $correctedText; // Output the corrected text
} catch (InvalidArgumentException $e) {
    // Handle invalid input
    echo 'Error: ' . $e->getMessage();
}
?>
```
