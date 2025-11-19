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
 * Typographizer class.
 *
 * This class provides methods for typographic corrections of the text.
 */
class Typographizer
{
    /**
     * Corrects the given text by replacing multiple spaces with a single space.
     *
     * @param string $text The text to correct.
     *
     * @return string The corrected text.
     */
    public function correctMultipleSpaces(string $text): string
    {
        return preg_replace('/\s+/', ' ', $text);
    }

    /**
     * Replaces straight quotes with curly quotes.
     *
     * @param string $text The text to correct.
     *
     * @return string The corrected text.
     */
    public function correctQuotes(string $text): string
    {
        $text = str_replace(['"', '"'], ['“', '”'], $text);
        $text = str_replace(["\n\""], ["\n“"], $text);
        $text = str_replace(['\'', '\''], ['‘', '’'], $text);
        return $text;
    }

    /**
     * Replaces three dots with an ellipsis.
     *
     * @param string $text The text to correct.
     *
     * @return string The corrected text.
     */
    public function correctEllipsis(string $text): string
    {
        return str_replace(['...', '. . .'], ['…', '…'], $text);
    }

    /**
     * Replaces dashes with typographic dashes.
     *
     * @param string $text The text to correct.
     *
     * @return string The corrected text.
     */
    public function correctDashes(string $text): string
    {
        $text = str_replace('-', '–', $text);
        $text = str_replace(['--', '---'], ['—', '—'], $text);
        return $text;
    }

    /**
     * Typographically corrects the given text.
     *
     * @param string $text The text to correct.
     *
     * @return string The corrected text.
     */
    public function typographize(string $text): string
    {
        try {
            $text = $this->correctMultipleSpaces($text);
            $text = $this->correctQuotes($text);
            $text = $this->correctEllipsis($text);
            $text = $this->correctDashes($text);
            return $text;
        } catch (\Exception $e) {
            throw new \RuntimeException('Failed to typographize text: ' . $e->getMessage());
        }
    }
}

// Example usage:
$typographizer = new Typographizer();
$text = 'This   is  a sample text. It has "quotes" and \'single quotes\'.
The text also has ... and -- dashes.';
echo $typographizer->typographize($text);

```
