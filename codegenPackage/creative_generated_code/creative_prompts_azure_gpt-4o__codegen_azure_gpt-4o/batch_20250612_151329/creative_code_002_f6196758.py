"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strive.serwerdwg.pl
Prompt: Generate PHP code for loading translations in WordPress plugins during the `init` action, specifically addressing the error "_load_textdomain_just_in_time was called incorrectly."
Generated: DETERMINISTIC_f6196758644e1cd1
Batch ID: 20250612_151329
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
 * Plugin Name: Translation Loader Example
 * Description: Properly loads translations for a WordPress plugin to avoid "_load_textdomain_just_in_time was called incorrectly" error.
 * Version: 1.0
 * Author: Expert Programmer
 */

// Define the text domain for the plugin.
define( 'TRANSLATION_LOADER_TEXTDOMAIN', 'translation-loader-example' );

/**
 * Load the plugin's translations during the `init` action.
 */
function translation_loader_load_textdomain() {
    // Path to the translation files, usually inside the plugin's "languages" directory.
    $lang_dir = plugin_dir_path( __FILE__ ) . 'languages/';
    
    // Load the translations from the specified directory.
    $loaded = load_plugin_textdomain( TRANSLATION_LOADER_TEXTDOMAIN, false, $lang_dir );

    // Check if the translation files were successfully loaded.
    if ( ! $loaded ) {
        error_log( sprintf( 'Failed to load textdomain %s from directory %s', TRANSLATION_LOADER_TEXTDOMAIN, $lang_dir ) );
    }
}

// Hook into the `init` action to load translations.
add_action( 'init', 'translation_loader_load_textdomain' );

/**
 * Example usage of a translatable string in the plugin.
 */
function translation_loader_example_function() {
    // Display a string that can be translated using the text domain.
    echo esc_html__( 'Hello, World!', TRANSLATION_LOADER_TEXTDOMAIN );
}

// Example usage when the plugin is loaded (optional).
add_action( 'wp_footer', 'translation_loader_example_function' );
```
