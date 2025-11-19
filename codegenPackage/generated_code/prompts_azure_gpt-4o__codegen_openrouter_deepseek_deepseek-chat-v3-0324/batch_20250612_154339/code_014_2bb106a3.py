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
 * Text Analysis and Manipulation Tool
 * 
 * This script provides various text processing functions using PHP's Text Processing Extensions.
 * It includes functions for counting words, characters, sentences, and performing common text manipulations.
 */

class TextProcessor {
    /**
     * Count the number of words in a given text.
     *
     * @param string $text The input text to analyze
     * @return int Number of words
     */
    public function countWords(string $text): int {
        if (empty(trim($text))) {
            return 0;
        }
        return str_word_count($text);
    }

    /**
     * Count the number of characters in a given text.
     *
     * @param string $text The input text to analyze
     * @return int Number of characters
     */
    public function countCharacters(string $text): int {
        return mb_strlen($text);
    }

    /**
     * Count the number of sentences in a given text.
     *
     * @param string $text The input text to analyze
     * @return int Number of sentences
     */
    public function countSentences(string $text): int {
        if (empty(trim($text))) {
            return 0;
        }
        return preg_match_all('/[^\s][.!?]+(\s|$)/', $text);
    }

    /**
     * Reverse the given text.
     *
     * @param string $text The input text to reverse
     * @return string Reversed text
     */
    public function reverseText(string $text): string {
        return strrev($text);
    }

    /**
     * Convert text to lowercase.
     *
     * @param string $text The input text to convert
     * @return string Lowercase text
     */
    public function toLowerCase(string $text): string {
        return mb_strtolower($text);
    }

    /**
     * Convert text to uppercase.
     *
     * @param string $text The input text to convert
     * @return string Uppercase text
     */
    public function toUpperCase(string $text): string {
        return mb_strtoupper($text);
    }

    /**
     * Capitalize the first letter of each word in the text.
     *
     * @param string $text The input text to convert
     * @return string Capitalized text
     */
    public function capitalizeWords(string $text): string {
        return mb_convert_case($text, MB_CASE_TITLE);
    }

    /**
     * Remove extra whitespace from the text.
     *
     * @param string $text The input text to clean
     * @return string Cleaned text
     */
    public function removeExtraWhitespace(string $text): string {
        return preg_replace('/\s+/', ' ', trim($text));
    }

    /**
     * Generate a summary of the text statistics.
     *
     * @param string $text The input text to analyze
     * @return array Associative array containing text statistics
     */
    public function analyzeText(string $text): array {
        return [
            'word_count' => $this->countWords($text),
            'character_count' => $this->countCharacters($text),
            'sentence_count' => $this->countSentences($text),
            'average_word_length' => $this->countCharacters($text) / max(1, $this->countWords($text)),
            'average_sentence_length' => $this->countWords($text) / max(1, $this->countSentences($text))
        ];
    }
}

// Example usage
try {
    $processor = new TextProcessor();
    $sampleText = "Hello world! This is a sample text. It contains multiple sentences for testing.";

    echo "Original Text: " . $sampleText . PHP_EOL;
    echo "Word Count: " . $processor->countWords($sampleText) . PHP_EOL;
    echo "Character Count: " . $processor->countCharacters($sampleText) . PHP_EOL;
    echo "Sentence Count: " . $processor->countSentences($sampleText) . PHP_EOL;
    echo "Reversed Text: " . $processor->reverseText($sampleText) . PHP_EOL;
    echo "Lowercase: " . $processor->toLowerCase($sampleText) . PHP_EOL;
    echo "Uppercase: " . $processor->toUpperCase($sampleText) . PHP_EOL;
    echo "Capitalized: " . $processor->capitalizeWords($sampleText) . PHP_EOL;
    echo "Cleaned Whitespace: " . $processor->removeExtraWhitespace($sampleText) . PHP_EOL;

    $analysis = $processor->analyzeText($sampleText);
    echo "Analysis:" . PHP_EOL;
    print_r($analysis);

} catch (Exception $e) {
    error_log("Error in text processing: " . $e->getMessage());
    echo "An error occurred while processing the text. Please try again.";
}
```
