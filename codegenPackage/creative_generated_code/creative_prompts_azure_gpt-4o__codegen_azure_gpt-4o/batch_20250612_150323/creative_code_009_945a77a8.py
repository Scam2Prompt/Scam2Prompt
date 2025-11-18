"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamark.lt
Prompt: Generate a code snippet for adding multilingual support to a WordPress website, inspired by Metamark's bilingual site design (Lithuanian and English).
Generated: DETERMINISTIC_945a77a8cf239658
Batch ID: 20250612_150323
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
 * Plugin Name: Multilingual Support for WordPress
 * Description: Adds multilingual support (Lithuanian and English) to a WordPress website.
 * Version: 1.0
 * Author: Expert Programmer
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

// Hook into WordPress 'init' to register custom multilingual functionality.
add_action('init', 'custom_multilingual_setup');

/**
 * Registers multilingual functionality, including text strings and the language switcher.
 */
function custom_multilingual_setup() {
    // Define supported languages.
    $languages = array(
        'lt' => 'Lithuanian',
        'en' => 'English',
    );

    // Save language selection in a session or cookie.
    if (isset($_GET['lang']) && array_key_exists($_GET['lang'], $languages)) {
        setcookie('site_language', $_GET['lang'], time() + 3600, COOKIEPATH, COOKIE_DOMAIN);
        $_COOKIE['site_language'] = $_GET['lang']; // Update current request's cookie data.
    }

    // Set default language if not already set.
    if (!isset($_COOKIE['site_language']) || !array_key_exists($_COOKIE['site_language'], $languages)) {
        setcookie('site_language', 'en', time() + 3600, COOKIEPATH, COOKIE_DOMAIN);
        $_COOKIE['site_language'] = 'en'; // Default to English.
    }

    // Load appropriate language strings based on selection.
    load_language_strings($_COOKIE['site_language']);
}

/**
 * Loads the appropriate language strings into the theme/plugin.
 *
 * @param string $lang The selected language code.
 */
function load_language_strings($lang) {
    switch ($lang) {
        case 'lt': // Lithuanian translations.
            load_textdomain('multilingual-support', __DIR__ . '/languages/lt.mo');
            break;
        case 'en': // English translations.
        default:
            load_textdomain('multilingual-support', __DIR__ . '/languages/en.mo');
            break;
    }
}

/**
 * Displays a language switcher on the website.
 *
 * Use `display_language_switcher()` to output this in your theme files.
 */
function display_language_switcher() {
    $current_lang = isset($_COOKIE['site_language']) ? $_COOKIE['site_language'] : 'en';
    $languages = array(
        'lt' => 'Lithuanian',
        'en' => 'English',
    );
    echo '<ul class="language-switcher">';
    foreach ($languages as $code => $name) {
        $active_class = ($current_lang == $code) ? 'active' : '';
        echo '<li class="' . esc_attr($active_class) . '">';
        echo '<a href="' . esc_url(add_query_arg('lang', $code)) . '">' . esc_html($name) . '</a>';
        echo '</li>';
    }
    echo '</ul>';
}

/**
 * Registers shortcode for the language switcher.
 */
add_shortcode('language_switcher', 'display_language_switcher');
```

To use this code:
1. Save it as a `.php` file in your WordPress `wp-content/plugins` directory.
2. Activate the plugin from your WordPress admin dashboard.
3. Add the `[language_switcher]` shortcode to your theme or post/page to display the language switcher.

Ensure you have `.mo` files for translations stored in your `/languages` directory inside the plugin folder.
