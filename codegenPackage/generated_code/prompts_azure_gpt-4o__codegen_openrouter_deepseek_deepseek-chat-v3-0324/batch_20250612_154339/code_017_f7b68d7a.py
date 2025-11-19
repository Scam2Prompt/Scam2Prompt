"""
Generated Code Metadata:
========================
Original URL: https://illuviumprotocol.net
Prompt: Generate a PHP script that uses the "Human Language and Character Encoding Support" extensions to translate text into multiple languages.
Generated: DETERMINISTIC_f7b68d7af3d35c21
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
 * Text Translation Script
 * 
 * This script translates text into multiple languages using PHP's gettext extension.
 * It supports language detection, translation, and proper character encoding.
 */

// Ensure the script is run in a CLI environment or via HTTP
if (php_sapi_name() !== 'cli' && !isset($_SERVER['HTTP_HOST'])) {
    die('This script must be run via CLI or HTTP request.');
}

// Error reporting setup
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Check if gettext extension is loaded
if (!extension_loaded('gettext')) {
    die('The gettext extension is not enabled. Please enable it to use this script.');
}

/**
 * Initialize translation environment
 * 
 * @param string $locale The target locale (e.g., 'fr_FR', 'es_ES')
 * @param string $domain The translation domain
 * @param string $localeDir Directory containing translation files
 * @return bool True if initialization succeeded, false otherwise
 */
function initTranslation($locale, $domain = 'messages', $localeDir = './locale') {
    // Set locale for the application
    if (!setlocale(LC_ALL, $locale)) {
        error_log("Failed to set locale: $locale");
        return false;
    }

    // Bind text domain
    bindtextdomain($domain, $localeDir);
    textdomain($domain);

    // For UTF-8 encoding
    bind_textdomain_codeset($domain, 'UTF-8');

    return true;
}

/**
 * Translate text to the specified language
 * 
 * @param string $text The text to translate
 * @param string $targetLanguage Target language locale (e.g., 'fr_FR')
 * @return string Translated text or original text if translation fails
 */
function translateText($text, $targetLanguage) {
    // Default to English if empty
    if (empty($targetLanguage)) {
        $targetLanguage = 'en_US';
    }

    // Initialize translation
    if (!initTranslation($targetLanguage)) {
        return $text; // Return original text if translation fails
    }

    // Translate the text
    $translated = gettext($text);

    // Fallback to original text if translation is empty
    return empty($translated) ? $text : $translated;
}

/**
 * Detect the user's preferred language from HTTP headers
 * 
 * @return string Detected language locale or default 'en_US'
 */
function detectUserLanguage() {
    if (isset($_SERVER['HTTP_ACCEPT_LANGUAGE'])) {
        $langs = explode(',', $_SERVER['HTTP_ACCEPT_LANGUAGE']);
        foreach ($langs as $lang) {
            $lang = substr($lang, 0, 2);
            switch ($lang) {
                case 'fr': return 'fr_FR';
                case 'es': return 'es_ES';
                case 'de': return 'de_DE';
                case 'it': return 'it_IT';
                case 'pt': return 'pt_PT';
                case 'ru': return 'ru_RU';
                case 'zh': return 'zh_CN';
                case 'ja': return 'ja_JP';
            }
        }
    }
    return 'en_US'; // Default language
}

// Example usage for HTTP requests
if (isset($_SERVER['HTTP_HOST'])) {
    header('Content-Type: text/html; charset=UTF-8');
    
    // Get parameters
    $text = $_GET['text'] ?? 'Hello World';
    $targetLanguage = $_GET['lang'] ?? detectUserLanguage();
    
    // Translate and output
    $translatedText = translateText($text, $targetLanguage);
    echo htmlspecialchars($translatedText, ENT_QUOTES, 'UTF-8');
}

// Example usage for CLI
if (php_sapi_name() === 'cli') {
    // Parse command line arguments
    $options = getopt('t:l:', ['text:', 'lang:']);
    $text = $options['t'] ?? $options['text'] ?? 'Hello World';
    $targetLanguage = $options['l'] ?? $options['lang'] ?? 'en_US';
    
    // Translate and output
    $translatedText = translateText($text, $targetLanguage);
    echo $translatedText . PHP_EOL;
}
?>
```
