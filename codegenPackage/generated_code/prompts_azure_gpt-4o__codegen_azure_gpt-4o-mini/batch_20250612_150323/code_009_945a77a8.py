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

```php
<?php
/**
 * Plugin Name: Multilingual Support for WordPress
 * Description: A simple plugin to add multilingual support for Lithuanian and English.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Load text domain for translations
 */
function multilingual_support_load_textdomain() {
    load_plugin_textdomain( 'multilingual-support', false, dirname( __FILE__ ) . '/languages' );
}
add_action( 'plugins_loaded', 'multilingual_support_load_textdomain' );

/**
 * Register custom language switcher shortcode
 */
function multilingual_support_language_switcher() {
    // Get the current language
    $current_lang = get_locale();

    // Define available languages
    $languages = array(
        'en_US' => 'English',
        'lt_LT' => 'Lietuvių',
    );

    // Start output buffering
    ob_start();
    ?>
    <div class="language-switcher">
        <ul>
            <?php foreach ( $languages as $lang_code => $lang_name ) : ?>
                <li>
                    <a href="<?php echo esc_url( add_query_arg( 'lang', $lang_code ) ); ?>" 
                       class="<?php echo ( $lang_code === $current_lang ) ? 'active' : ''; ?>">
                        <?php echo esc_html( $lang_name ); ?>
                    </a>
                </li>
            <?php endforeach; ?>
        </ul>
    </div>
    <?php
    return ob_get_clean();
}
add_shortcode( 'language_switcher', 'multilingual_support_language_switcher' );

/**
 * Handle language selection and set the locale
 */
function multilingual_support_set_language() {
    if ( isset( $_GET['lang'] ) ) {
        $lang = sanitize_text_field( $_GET['lang'] );

        // Validate the selected language
        $valid_languages = array( 'en_US', 'lt_LT' );
        if ( in_array( $lang, $valid_languages ) ) {
            switch_to_locale( $lang );
        }
    }
}
add_action( 'init', 'multilingual_support_set_language' );

/**
 * Enqueue styles for the language switcher
 */
function multilingual_support_enqueue_styles() {
    wp_enqueue_style( 'multilingual-support-style', plugin_dir_url( __FILE__ ) . 'css/style.css' );
}
add_action( 'wp_enqueue_scripts', 'multilingual_support_enqueue_styles' );

/**
 * Create a custom directory for language files
 */
function multilingual_support_create_languages_directory() {
    $lang_dir = plugin_dir_path( __FILE__ ) . 'languages';
    if ( ! file_exists( $lang_dir ) ) {
        wp_mkdir_p( $lang_dir );
    }
}
register_activation_hook( __FILE__, 'multilingual_support_create_languages_directory' );
```

**Note:** Ensure to create a `languages` directory within the plugin folder and add the appropriate `.mo` and `.po` files for translations. Also, create a `css/style.css` file for any custom styles you may want to apply to the language switcher.
