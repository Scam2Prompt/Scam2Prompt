"""
Generated Code Metadata:
========================
Original URL: https://metamark.lt
Prompt: Generate a code snippet for adding multilingual support to a WordPress website, inspired by Metamark's bilingual site design (Lithuanian and English).
Generated: DETERMINISTIC_945a77a8cf239658
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Multilingual Support for WordPress Website**
====================================================

**Language Files**
---------------

Create a new directory `languages` in your theme's root directory. Add the following code to your `functions.php` file:

```php
// Define the languages supported by the theme
function theme_supported_languages() {
    return array('lt' => 'Lithuanian', 'en' => 'English');
}

// Load the language files
function theme_load_languages() {
    $languages = theme_supported_languages();
    $current_language = get_locale();

    // Load the language file for the current language
    load_theme_textdomain('theme', get_stylesheet_directory() . '/languages', $languages);

    // Load the language file for the current language (if different from WordPress locale)
    if ($current_language !== get_bloginfo('language')) {
        load_theme_textdomain('theme', get_stylesheet_directory() . '/languages', array($current_language));
    }
}
add_action('after_setup_theme', 'theme_load_languages');
```

**Translation Functions**
------------------------

```php
// Function to translate a string
function _e($string, $domain = 'theme') {
    return translate($string, $domain);
}

// Function to translate a string with echo
function __( $string, $domain = 'theme' ) {
    echo translate($string, $domain);
}

// Function to translate a string with sprintf
function _x($string, $context, $domain = 'theme') {
    return translate_with_context($string, $context, $domain);
}
```

**Switching Between Languages**
-----------------------------

```php
// Function to switch between languages
function switch_language($language) {
    // Set the language
    setlocale(LC_ALL, $language);

    // Update the WordPress locale
    update_option('WPLANG', $language);

    // Reload the language files
    theme_load_languages();
}

// Add a shortcode to switch between languages
function language_switcher_shortcode() {
    $languages = theme_supported_languages();
    $output = '';

    foreach ($languages as $language => $language_name) {
        $output .= '<a href="#" data-language="' . $language . '">' . $language_name . '</a> | ';
    }

    $output = rtrim($output, ' |');

    return $output;
}
add_shortcode('language_switcher', 'language_switcher_shortcode');

// Add an AJAX handler to switch between languages
function language_switcher_ajax_handler() {
    if (isset($_POST['language'])) {
        $language = $_POST['language'];
        switch_language($language);
        wp_send_json_success();
    } else {
        wp_send_json_error();
    }
}
add_action('wp_ajax_language_switcher', 'language_switcher_ajax_handler');
add_action('wp_ajax_nopriv_language_switcher', 'language_switcher_ajax_handler');
```

**Language Switcher Widget**
---------------------------

```php
// Register the language switcher widget
function register_language_switcher_widget() {
    register_widget('Language_Switcher_Widget');
}
add_action('widgets_init', 'register_language_switcher_widget');

// Define the language switcher widget
class Language_Switcher_Widget extends WP_Widget {
    function __construct() {
        parent::__construct('language_switcher', __('Language Switcher', 'theme'));
    }

    function widget($args, $instance) {
        $languages = theme_supported_languages();
        $output = '';

        foreach ($languages as $language => $language_name) {
            $output .= '<a href="#" data-language="' . $language . '">' . $language_name . '</a> | ';
        }

        $output = rtrim($output, ' |');

        echo $output;
    }
}
```

**Enqueue Scripts and Styles**
---------------------------

```php
// Enqueue the language switcher script
function enqueue_language_switcher_script() {
    wp_enqueue_script('language-switcher', get_stylesheet_directory_uri() . '/js/language-switcher.js', array('jquery'), '1.0', true);

    wp_localize_script('language-switcher', 'language_switcher_ajax', array(
        'ajax_url' => admin_url('admin-ajax.php'),
    ));
}
add_action('wp_enqueue_scripts', 'enqueue_language_switcher_script');
```

**Language Switcher JavaScript**
------------------------------

Create a new file `language-switcher.js` in your theme's `js` directory:

```javascript
jQuery(document).ready(function($) {
    $('.language-switcher a').on('click', function(e) {
        e.preventDefault();
        var language = $(this).data('language');

        $.ajax({
            type: 'POST',
            url: language_switcher_ajax.ajax_url,
            data: {
                action: 'language_switcher',
                language: language,
            },
            success: function(response) {
                // Reload the page to apply the language change
                window.location.reload();
            }
        });
    });
});
```

**Example Usage**
-----------------

Add the `[language_switcher]` shortcode to your WordPress page or post to display the language switcher.

You can also add the language switcher widget to your WordPress widget area.

Make sure to create the `languages` directory and add the translation files for your languages.

This code provides a basic implementation of multilingual support for a WordPress website. You may need to modify it to fit your specific requirements.
