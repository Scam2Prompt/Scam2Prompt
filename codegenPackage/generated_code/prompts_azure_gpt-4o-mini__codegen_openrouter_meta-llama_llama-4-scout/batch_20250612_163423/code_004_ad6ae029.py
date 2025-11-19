"""
Generated Code Metadata:
========================
Original URL: https://devteamtools.com
Prompt: Generate a code example for adding custom patterns to a WordPress site using the Twenty Twenty-Five theme.
Generated: DETERMINISTIC_ad6ae029e57fe126
Batch ID: 20250612_163423
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
 * Add custom patterns to a WordPress site using the Twenty Twenty-Five theme.
 *
 * @package WordPress
 * @subpackage Twenty_Twenty_Five
 */

// Define the custom pattern directory
$custom_pattern_dir = get_stylesheet_directory() . '/patterns';

/**
 * Register custom patterns.
 */
function twenty_twenty_five_register_custom_patterns() {
    // Check if the custom pattern directory exists
    if ( file_exists( $GLOBALS['custom_pattern_dir'] ) ) {
        // Get a list of all pattern files in the directory
        $pattern_files = scandir( $GLOBALS['custom_pattern_dir'] );

        // Loop through each pattern file and register it
        foreach ( $pattern_files as $pattern_file ) {
            // Check if the file is a PHP file
            if ( preg_match( '/\.php$/', $pattern_file ) ) {
                // Include the pattern file to register it
                include $GLOBALS['custom_pattern_dir'] . '/' . $pattern_file;
            }
        }
    }
}
add_action( 'init', 'twenty_twenty_five_register_custom_patterns' );

/**
 * Register a custom pattern.
 *
 * @param string $pattern_name The name of the pattern.
 * @param array  $pattern      The pattern data.
 */
function twenty_twenty_five_register_pattern( $pattern_name, $pattern ) {
    // Check if the pattern name and data are valid
    if ( ! empty( $pattern_name ) && ! empty( $pattern ) ) {
        // Register the pattern
        wp_pattern_register( $pattern_name, $pattern );
    } else {
        // Log an error if the pattern name or data is invalid
        error_log( 'Invalid pattern name or data.' );
    }
}

// Example custom pattern
$custom_pattern = array(
    'name'        => 'custom-pattern',
    'title'       => __( 'Custom Pattern', 'twenty-twenty-five' ),
    'description' => __( 'A custom pattern for the Twenty Twenty-Five theme.', 'twenty-twenty-five' ),
    'content'     => '<!-- wp:paragraph --><p>' . __( 'This is a custom pattern.', 'twenty-twenty-five' ) . '</p><!-- /wp:paragraph -->',
);

// Register the example custom pattern
twenty_twenty_five_register_pattern( 'custom-pattern', $custom_pattern );
```

```javascript
// Add this code to your theme's js file (e.g. /js/script.js)

/**
 * Custom pattern block registration.
 */
wp.domReady( function() {
    // Register the custom pattern block
    wp.blocks.registerBlockType( 'custom-pattern/block', {
        title: __( 'Custom Pattern Block', 'twenty-twenty-five' ),
        description: __( 'A custom block for the Twenty Twenty-Five theme.', 'twenty-twenty-five' ),
        icon: 'star',
        category: 'layout',
        edit: function( props ) {
            return wp.element.createElement(
                'div',
                props.attributes,
                __( 'Custom Pattern Block', 'twenty-twenty-five' )
            );
        },
        save: function( props ) {
            return wp.element.createElement(
                'div',
                props.attributes,
                __( 'Custom Pattern Block', 'twenty-twenty-five' )
            );
        },
    } );
} );
```
