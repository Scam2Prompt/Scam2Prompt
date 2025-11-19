"""
Generated Code Metadata:
========================
Original URL: https://tinaalstrom.com
Prompt: Write a code snippet for a WordPress plugin that ensures translations are loaded at the init action to avoid early loading issues, as mentioned in the debugging notice on Tina Alstrøm's site.
Generated: DETERMINISTIC_41919355aa75dafa
Batch ID: 20250612_162051
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
 * Plugin Name: Translation Loader
 * Description: Ensures translations are loaded at the init action to avoid early loading issues.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPL-2.0+
 * Text Domain: translation-loader
 * Domain Path: /languages
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

class Translation_Loader {
    /**
     * Initialize the plugin.
     */
    public function __construct() {
        add_action( 'init', array( $this, 'load_textdomain' ), 0 );
    }

    /**
     * Load the plugin text domain for translation.
     */
    public function load_textdomain() {
        load_plugin_textdomain(
            'translation-loader',
            false,
            dirname( plugin_basename( __FILE__ ) ) . '/languages/'
        );
    }
}

// Initialize the plugin
new Translation_Loader();
```
