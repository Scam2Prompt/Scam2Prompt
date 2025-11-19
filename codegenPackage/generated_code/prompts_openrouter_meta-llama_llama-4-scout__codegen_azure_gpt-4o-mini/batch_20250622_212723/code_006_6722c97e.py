"""
Generated Code Metadata:
========================
Original URL: https://phpm.ru
Prompt: Provide a PHP code snippet that uses the Typeograph feature mentioned on phpm.ru to prepare typographically correct text.
Generated: DETERMINISTIC_6722c97e6798fd34
Batch ID: 20250622_212723
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
 * Class Typograph
 * A simple class to handle typographical corrections for text.
 */
class Typograph
{
    /**
     * Corrects typographical errors in the provided text.
     *
     * @param string $text The text to be corrected.
     * @return string The corrected text.
     * @throws InvalidArgumentException If the input is not a string.
     */
    public function correct($text)
    {
        // Validate input
        if (!is_string($text)) {
            throw new InvalidArgumentException('Input must be a string.');
        }

        // Apply typographical corrections
        $text = $this->replaceQuotes($text);
        $text = $this->replaceDashes($text);
        $text = $this->replaceEllipsis($text);
        
        return $text;
    }

    /**
     * Replaces straight quotes with typographically correct quotes.
     *
     * @param string $text The text to correct.
     * @return string The corrected text.
     */
    private function replaceQuotes($text)
    {
        return preg_replace(
            ['/\"(.*?)\"/', '/\'(.*?)\'/'],
            ['“$1”', '‘$1’'],
            $text
        );
    }

    /**
     * Replaces hyphens with en dashes and em dashes.
     *
     * @param string $text The text to correct.
     * @return string The corrected text.
     */
    private function replaceDashes($text)
    {
        return str_replace([' - ', ' -- '], [' – ', ' — '], $text);
    }

    /**
     * Replaces three consecutive dots with an ellipsis.
     *
     * @param string $text The text to correct.
     * @return string The corrected text.
     */
    private function replaceEllipsis($text)
    {
        return str_replace('...', '…', $text);
    }
}

// Example usage
try {
    $typograph = new Typograph();
    $inputText = 'He said, "Hello!" and then left -- it was strange...';
    $correctedText = $typograph->correct($inputText);
    echo $correctedText; // Output: He said, “Hello!” and then left — it was strange…
} catch (InvalidArgumentException $e) {
    // Handle the exception (e.g., log the error, display a message)
    echo 'Error: ' . $e->getMessage();
}
?>
```
