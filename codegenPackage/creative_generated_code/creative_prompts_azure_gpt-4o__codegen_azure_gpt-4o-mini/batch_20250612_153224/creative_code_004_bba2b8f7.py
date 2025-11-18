"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mbandjock.fr
Prompt: Develop a WordPress shortcode to create a search bar styled like the one on the MBANDJOCK homepage.
Generated: DETERMINISTIC_bba2b8f726adea88
Batch ID: 20250612_153224
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
 * Plugin Name: Custom Search Bar Shortcode
 * Description: A shortcode to create a styled search bar similar to the MBANDJOCK homepage.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Enqueue custom styles for the search bar.
 */
function custom_search_bar_styles() {
    wp_enqueue_style( 'custom-search-bar-style', plugin_dir_url( __FILE__ ) . 'css/custom-search-bar.css' );
}
add_action( 'wp_enqueue_scripts', 'custom_search_bar_styles' );

/**
 * Shortcode function to display the search bar.
 *
 * @param array $atts Shortcode attributes.
 * @return string HTML output of the search bar.
 */
function custom_search_bar_shortcode( $atts ) {
    // Shortcode attributes with default values
    $atts = shortcode_atts(
        array(
            'placeholder' => 'Search...',
        ),
        $atts,
        'custom_search_bar'
    );

    // Escape output for security
    $placeholder = esc_attr( $atts['placeholder'] );

    // Output HTML for the search bar
    ob_start(); ?>
    <form role="search" method="get" class="custom-search-form" action="<?php echo esc_url( home_url( '/' ) ); ?>">
        <label for="search-bar" class="screen-reader-text"><?php _e( 'Search for:', 'textdomain' ); ?></label>
        <input type="search" id="search-bar" class="search-field" placeholder="<?php echo $placeholder; ?>" value="<?php echo get_search_query(); ?>" name="s" />
        <button type="submit" class="search-submit"><?php _e( 'Search', 'textdomain' ); ?></button>
    </form>
    <?php
    return ob_get_clean();
}
add_shortcode( 'custom_search_bar', 'custom_search_bar_shortcode' );

/**
 * Activate the shortcode on WordPress.
 */
function custom_search_bar_activate() {
    // Placeholder for potential future activation tasks
}
register_activation_hook( __FILE__, 'custom_search_bar_activate' );
```

**CSS (custom-search-bar.css)**

```css
/* Custom Search Bar Styles */
.custom-search-form {
    display: flex;
    align-items: center;
    margin: 20px 0;
}

.search-field {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    width: 100%;
    max-width: 300px; /* Adjust max-width as needed */
}

.search-submit {
    background-color: #0073aa; /* Adjust button color */
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-left: 10px; /* Space between input and button */
}

.search-submit:hover {
    background-color: #005177; /* Darker shade on hover */
}
```

**Usage**
To use the shortcode in your WordPress posts or pages, simply add `[custom_search_bar placeholder="Your Search..."]` to the content.
