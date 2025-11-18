"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Create a PHP script that uses the "Text Processing Extensions" to analyze and manipulate text data.
Generated: DETERMINISTIC_2bb106a3ae1384c9
Batch ID: 20250612_154339
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
 * Text Analysis and Manipulation Script
 * This script utilizes PHP's Text Processing Extensions to analyze and manipulate text.
 * It counts words, sentences, and characters in the input text and provides a summary.
 * 
 * PHP version: 8.0+
 */

// Check if the required PHP extensions are loaded
if (!extension_loaded('mbstring') || !extension_loaded('intl')) {
    die('Required PHP extensions (mbstring, intl) are not loaded. Please enable them in your PHP installation.');
}

/**
 * Function to perform text analysis
 * @param string $text The input text to analyze
 * @return array An associative array containing word count, sentence count, and character count
 */
function analyzeText(string $text): array {
    // Trim any whitespace from the beginning and end of the text
    $trimmedText = trim($text);
    
    // Count words using str_word_count
    $wordCount = str_word_count($trimmedText);
    
    // Count sentences using preg_match_all
    $sentenceCount = preg_match_all('/[.!?]+/', $trimmedText);
    
    // Count characters (including spaces) using mb_strlen
    $characterCount = mb_strlen($trimmedText);
    
    return [
        'word_count' => $wordCount,
        'sentence_count' => $sentenceCount,
        'character_count' => $characterCount
    ];
}

/**
 * Function to manipulate text by converting it to uppercase
 * @param string $text The input text to manipulate
 * @return string The manipulated text in uppercase
 */
function manipulateText(string $text): string {
    return mb_strtoupper($text);
}

// Input text (could be from user input, file, etc.)
$inputText = "Hello world! Let's analyze this text. It's a simple example.";

// Analyze the input text
try {
    $analysisResult = analyzeText($inputText);
    echo "Text Analysis:\n";
    echo "Word Count: {$analysisResult['word_count']}\n";
    echo "Sentence Count: {$analysisResult['sentence_count']}\n";
    echo "Character Count: {$analysisResult['character_count']}\n";

    // Manipulate the text
    $manipulatedText = manipulateText($inputText);
    echo "\nManipulated Text:\n";
    echo $manipulatedText . "\n";

} catch (Exception $e) {
    // Handle any exceptions that may occur
    echo "An error occurred during text processing: " . $e->getMessage();
}
?>
```
