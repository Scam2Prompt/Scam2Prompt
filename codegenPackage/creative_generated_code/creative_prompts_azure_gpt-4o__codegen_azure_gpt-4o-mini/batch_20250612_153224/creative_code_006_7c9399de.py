"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicbear.com.br
Prompt: Provide an example of integrating a bilingual education API into a WordPress theme, such as the one used by Magic Bear Canadian School.
Generated: DETERMINISTIC_7c9399deee215678
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bilingual-education.com/translate": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Bilingual Education API Integration for Magic Bear Canadian School Theme
 *
 * This code snippet demonstrates how to integrate a bilingual education API 
 * into a WordPress theme. It fetches translations and displays them in a 
 * user-friendly format.
 */

// Define the API endpoint and your API key
define('API_ENDPOINT', 'https://api.bilingual-education.com/translate');
define('API_KEY', 'YOUR_API_KEY_HERE');

/**
 * Fetches translation from the Bilingual Education API.
 *
 * @param string $text The text to be translated.
 * @param string $target_language The target language code (e.g., 'fr' for French).
 * @return string Translated text or an error message.
 */
function fetch_translation($text, $target_language) {
    // Prepare the request arguments
    $args = array(
        'body' => json_encode(array('text' => $text, 'target_lang' => $target_language)),
        'headers' => array(
            'Content-Type' => 'application/json',
            'Authorization' => 'Bearer ' . API_KEY
        ),
        'timeout' => 15
    );

    // Make the API request
    $response = wp_remote_post(API_ENDPOINT, $args);

    // Check for errors
    if (is_wp_error($response)) {
        return 'Error fetching translation: ' . $response->get_error_message();
    }

    // Decode the response
    $body = wp_remote_retrieve_body($response);
    $data = json_decode($body, true);
    
    // Check if the API response contains a valid translation
    if (isset($data['translated_text'])) {
        return $data['translated_text'];
    } else {
        return 'Translation not available.';
    }
}

/**
 * Shortcode to display translations on a WordPress page.
 *
 * Usage: [bilingual_translate text="Hello" target_language="fr"]
 *
 * @param array $atts Shortcode attributes.
 * @return string HTML output with translation.
 */
function bilingual_translate_shortcode($atts) {
    // Define default attributes
    $atts = shortcode_atts(array(
        'text' => 'Hello',
        'target_language' => 'fr'
    ), $atts);

    // Fetch the translated text
    $translated_text = fetch_translation($atts['text'], $atts['target_language']);

    // Return the translation in a formatted output
    return '<div class="bilingual-translation">
                <p><strong>Original:</strong> ' . esc_html($atts['text']) . '</p>
                <p><strong>Translation:</strong> ' . esc_html($translated_text) . '</p>
            </div>';
}

// Register the shortcode with WordPress
add_shortcode('bilingual_translate', 'bilingual_translate_shortcode');

// Enqueue necessary styles for the translation display
function bilingual_translation_styles() {
    wp_enqueue_style('bilingual-translation-style', get_template_directory_uri() . '/css/bilingual-translation.css');
}
add_action('wp_enqueue_scripts', 'bilingual_translation_styles');

?>
```
