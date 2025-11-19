"""
Generated Code Metadata:
========================
Original URL: https://36destinations.com
Prompt: Create a WordPress shortcode to add a "Scroll to Top" button for a site using the Astra theme.
Generated: DETERMINISTIC_4058c9427990e3e0
Batch ID: 20250612_153246
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
 * Adds a "Scroll to Top" button to the site.
 *
 * @package Astra
 */

/**
 * Register the shortcode.
 */
function astra_scroll_to_top_shortcode() {
    // Check if Astra theme is active
    if ( function_exists( 'astra' ) ) {
        // Add shortcode
        add_shortcode( 'scroll_to_top', 'astra_scroll_to_top_callback' );
    } else {
        // Log error or display notice
        error_log( 'Astra theme is not active.' );
    }
}
add_action( 'init', 'astra_scroll_to_top_shortcode' );

/**
 * Callback function for the shortcode.
 *
 * @return string
 */
function astra_scroll_to_top_callback() {
    // Get the button text
    $button_text = __( 'Scroll to Top', 'astra' );

    // Get the button classes
    $button_classes = 'scroll-to-top-btn astra-button';

    // Return the button HTML
    return '<button class="' . esc_attr( $button_classes ) . '">' . esc_html( $button_text ) . '</button>';
}

/**
 * Enqueue the required scripts and styles.
 */
function astra_scroll_to_top_scripts() {
    // Check if Astra theme is active
    if ( function_exists( 'astra' ) ) {
        // Enqueue script
        wp_enqueue_script(
            'astra-scroll-to-top',
            plugins_url( 'js/scroll-to-top.js', __FILE__ ),
            array( 'jquery' ),
            '1.0',
            true
        );

        // Enqueue style
        wp_enqueue_style(
            'astra-scroll-to-top',
            plugins_url( 'css/scroll-to-top.css', __FILE__ ),
            array(),
            '1.0'
        );
    }
}
add_action( 'wp_enqueue_scripts', 'astra_scroll_to_top_scripts' );
```

```javascript
// scroll-to-top.js

jQuery( document ).ready( function( $ ) {
    // Get the button
    var $scrollToTopBtn = $( '.scroll-to-top-btn' );

    // Show the button on scroll
    $( window ).scroll( function() {
        if ( $( this ).scrollTop() > 100 ) {
            $scrollToTopBtn.fadeIn();
        } else {
            $scrollToTopBtn.fadeOut();
        }
    } );

    // Scroll to top on click
    $scrollToTopBtn.on( 'click', function( e ) {
        e.preventDefault();
        $( 'html, body' ).animate( { scrollTop: 0 }, 'slow' );
    } );
} );
```

```css
/* scroll-to-top.css */

.scroll-to-top-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

.scroll-to-top-btn:hover {
    background-color: #444;
}
```
