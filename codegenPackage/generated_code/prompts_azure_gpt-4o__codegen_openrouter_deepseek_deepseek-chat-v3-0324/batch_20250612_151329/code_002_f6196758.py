"""
Generated Code Metadata:
========================
Original URL: https://strive.serwerdwg.pl
Prompt: Generate PHP code for loading translations in WordPress plugins during the `init` action, specifically addressing the error "_load_textdomain_just_in_time was called incorrectly."
Generated: DETERMINISTIC_f6196758644e1cd1
Batch ID: 20250612_151329
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
 * Load plugin textdomain during 'init' action to avoid "just in time" loading error.
 *
 * @package MyPlugin
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Load plugin textdomain.
 *
 * @return void
 */
function myplugin_load_textdomain() {
    $domain = 'my-plugin-textdomain';
    $locale = apply_filters( 'plugin_locale', determine_locale(), $domain );

    // Path to the plugin's languages directory.
    $plugin_lang_dir = dirname( plugin_basename( __FILE__ ) ) . '/languages/';

    // Traditional WordPress plugin locale filter.
    $mofile = sprintf( '%1$s-%2$s.mo', $domain, $locale );

    // Setup paths to current locale file.
    $mofile_local  = $plugin_lang_dir . $mofile;
    $mofile_global = WP_LANG_DIR . '/plugins/' . $mofile;

    // Load global first (for network admin translations).
    if ( file_exists( $mofile_global ) ) {
        load_textdomain( $domain, $mofile_global );
    } 
    // Fallback to local if global doesn't exist.
    elseif ( file_exists( $mofile_local ) ) {
        load_textdomain( $domain, $mofile_local );
    } 
    // If no translation file found, load the default textdomain.
    else {
        load_plugin_textdomain( $domain, false, $plugin_lang_dir );
    }
}
add_action( 'init', 'myplugin_load_textdomain' );
```
