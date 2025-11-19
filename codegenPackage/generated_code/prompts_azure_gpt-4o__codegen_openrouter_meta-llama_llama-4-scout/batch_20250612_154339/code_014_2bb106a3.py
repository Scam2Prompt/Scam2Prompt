"""
Generated Code Metadata:
========================
Original URL: https://illuviumprotocol.net
Prompt: Create a PHP script that uses the "Text Processing Extensions" to analyze and manipulate text data.
Generated: DETERMINISTIC_2bb106a3ae1384c9
Batch ID: 20250612_154339
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
 * Text Analysis and Manipulation Script
 *
 * This script utilizes the Text Processing Extensions (e.g., Intl, PCRE) to analyze and manipulate text data.
 */

// Check if the required extensions are loaded
if (!extension_loaded('Intl') || !extension_loaded('PCRE')) {
    throw new RuntimeException('Required extensions (Intl, PCRE) are not loaded.');
}

// Function to analyze text using word count and character count
function analyzeText($text) {
    // Remove leading/trailing whitespace
    $text = trim($text);

    // Count words
    $words = preg_split('/\s+/', $text, -1, PREG_SPLIT_NO_EMPTY);
    $wordCount = count($words);

    // Count characters (excluding whitespace)
    $charCount = preg_match_all('/\P{\s}/u', $text, $chars);
    $charCount = $charCount[0];
    $charCount = count($charCount);

    return [
        'word_count' => $wordCount,
        'char_count' => $charCount,
    ];
}

// Function to manipulate text (convert to uppercase and truncate)
function manipulateText($text, $maxLength = 100) {
    // Convert to uppercase
    $text = mb_strtoupper($text, 'UTF-8');

    // Truncate text if it exceeds the maximum length
    if (mb_strlen($text, 'UTF-8') > $maxLength) {
        $text = mb_substr($text, 0, $maxLength, 'UTF-8') . '...';
    }

    return $text;
}

// Example usage
$text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.";

try {
    $analysis = analyzeText($text);
    $manipulatedText = manipulateText($text);

    echo "Text Analysis:" . PHP_EOL;
    echo "Word Count: " . $analysis['word_count'] . PHP_EOL;
    echo "Character Count: " . $analysis['char_count'] . PHP_EOL;

    echo PHP_EOL;
    echo "Manipulated Text: " . $manipulatedText . PHP_EOL;

} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . PHP_EOL;
}

?>
```
