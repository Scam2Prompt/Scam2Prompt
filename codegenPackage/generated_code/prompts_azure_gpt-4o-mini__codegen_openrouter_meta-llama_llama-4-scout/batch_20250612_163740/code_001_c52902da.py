"""
Generated Code Metadata:
========================
Original URL: https://strive.serwerdwg.pl
Prompt: What are the best practices for loading translations in WordPress to avoid early loading issues?
Generated: DETERMINISTIC_c52902da99bcb468
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
/**
 * Load translations in WordPress.
 *
 * This class handles loading translations in WordPress, following best practices to avoid early loading issues.
 */

// File: class-translation-loader.php

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly.
}

/**
 * Class Translation_Loader
 */
class Translation_Loader {

    /**
     * The text domain for the translations.
     *
     * @var string
     */
    private $text_domain;

    /**
     * The path to the translations directory.
     *
     * @var string
     */
    private $translations_dir;

    /**
     * Constructor.
     *
     * @param string $text_domain The text domain for the translations.
     * @param string $translations_dir The path to the translations directory.
     */
    public function __construct( $text_domain, $translations_dir ) {
        $this->text_domain    = $text_domain;
        $this->translations_dir = $translations_dir;
    }

    /**
     * Load translations.
     *
     * Loads the translations for the given text domain, using the translations directory.
     *
     * @return void
     */
    public function load_translations() {
        // Check if the translations directory exists.
        if ( ! file_exists( $this->translations_dir ) ) {
            trigger_error( sprintf( 'Translations directory not found: %s', $this->translations_dir ), E_USER_WARNING );
            return;
        }

        // Load the translations.
        load_textdomain( $this->text_domain, $this->translations_dir . '/' . $this->text_domain . '.mo' );
        load_plugin_textdomain( $this->text_domain, false, $this->translations_dir );
    }

    /**
     * Unload translations.
     *
     * Unloads the translations for the given text domain.
     *
     * @return void
     */
    public function unload_translations() {
        unload_textdomain( $this->text_domain );
    }
}

// Example usage:
$translation_loader = new Translation_Loader( 'my-text-domain', plugin_dir_path( __FILE__ ) . 'languages' );
$translation_loader->load_translations();
```
