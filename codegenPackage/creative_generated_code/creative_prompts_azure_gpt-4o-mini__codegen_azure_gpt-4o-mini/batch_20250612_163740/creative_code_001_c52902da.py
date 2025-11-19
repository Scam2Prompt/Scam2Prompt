"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strive.serwerdwg.pl
Prompt: What are the best practices for loading translations in WordPress to avoid early loading issues?
Generated: DETERMINISTIC_c52902da99bcb468
Batch ID: 20250612_163740
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
 * Plugin Name: Translation Loader
 * Description: A simple plugin to load translations correctly in WordPress.
 * Version: 1.0
 * Author: Your Name
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Class TranslationLoader
 * Handles the loading of translation files for the plugin.
 */
class TranslationLoader {
    
    /**
     * Constructor to set up the hooks.
     */
    public function __construct() {
        add_action( 'plugins_loaded', [ $this, 'load_translations' ] );
    }

    /**
     * Load translations for the plugin.
     *
     * This method checks for the presence of the translation files and loads them
     * in the appropriate language based on the site language setting.
     *
     * @return void
     */
    public function load_translations() {
        // Load the text domain for translations
        $plugin_locale = apply_filters( 'plugin_locale', get_locale(), 'translation-loader' );
        $mofile = 'translation-loader-' . $plugin_locale . '.mo';
        $mofile_path = plugin_dir_path( __FILE__ ) . 'languages/' . $mofile;

        // Check if the translation file exists before loading
        if ( file_exists( $mofile_path ) ) {
            load_textdomain( 'translation-loader', $mofile_path );
        } else {
            error_log( 'Translation file not found: ' . $mofile_path );
        }
    }
}

// Initialize the TranslationLoader class
new TranslationLoader();
```

**Note:** Place your translation files in the `languages` directory inside your plugin folder named as `translation-loader-{locale}.mo`.
