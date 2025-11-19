"""
Generated Code Metadata:
========================
Original URL: https://ouvaton.link
Prompt: How can YOURLS be customized to include branding for Ouvaton.coop when shortening links?
Generated: DETERMINISTIC_df06c18c33a2c0ed
Batch ID: 20250612_150426
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
 * Custom YOURLS Plugin for Branding Shortened Links with Ouvaton.coop
 *
 * This plugin customizes the YOURLS link shortening service to include
 * branding for Ouvaton.coop in the shortened URLs.
 *
 * @package OuvatonBranding
 * @version 1.0
 * @author Your Name
 * @license MIT
 */

// Prevent direct access to the file
if ( ! defined( 'YOURLS_ABSPATH' ) ) {
    die( 'No direct access allowed.' );
}

/**
 * Add a custom filter to modify the shortened URL
 *
 * @param string $shorturl The original shortened URL
 * @param string $url The original URL being shortened
 * @param string $title The title of the URL
 * @return string The modified shortened URL
 */
function ouvaton_branding_shorturl( $shorturl, $url, $title ) {
    // Define the custom domain for Ouvaton.coop
    $custom_domain = 'ouvaton.coop';

    // Check if the short URL already contains the custom domain
    if ( strpos( $shorturl, $custom_domain ) === false ) {
        // Replace the default YOURLS domain with the custom domain
        $shorturl = str_replace( YOURLS_SITE, $custom_domain, $shorturl );
    }

    return $shorturl;
}

// Hook the function into the YOURLS filter for short URLs
yourls_add_filter( 'get_shortlink', 'ouvaton_branding_shorturl', 10, 3 );

/**
 * Activate the plugin
 */
function ouvaton_branding_activate() {
    // Perform any necessary setup when the plugin is activated
    // For example, you could log the activation or set default options
    yourls_log( 'Ouvaton Branding Plugin activated.' );
}

// Hook the activation function
yourls_add_action( 'plugin_activation', 'ouvaton_branding_activate' );

/**
 * Deactivate the plugin
 */
function ouvaton_branding_deactivate() {
    // Perform any necessary cleanup when the plugin is deactivated
    yourls_log( 'Ouvaton Branding Plugin deactivated.' );
}

// Hook the deactivation function
yourls_add_action( 'plugin_deactivation', 'ouvaton_branding_deactivate' );

?>
```
