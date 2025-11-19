"""
Generated Code Metadata:
========================
Original URL: https://digihimanshu.in
Prompt: Generate a code snippet for a WordPress theme using Astra that includes a custom header and footer.
Generated: DETERMINISTIC_30b5a594144c2c5d
Batch ID: 20250612_162050
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
 * Astra Child Theme functions.php
 * 
 * This file is used to customize the Astra theme by adding a custom header and footer.
 * 
 * @package AstraChild
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Enqueue parent theme styles.
 */
function astra_child_enqueue_styles() {
    // Enqueue the parent theme stylesheet.
    wp_enqueue_style( 'astra-parent-style', get_template_directory_uri() . '/style.css' );
}
add_action( 'wp_enqueue_scripts', 'astra_child_enqueue_styles' );

/**
 * Custom Header Function
 */
function astra_child_custom_header() {
    ?>
    <header class="custom-header">
        <div class="header-content">
            <h1><?php bloginfo( 'name' ); ?></h1>
            <p><?php bloginfo( 'description' ); ?></p>
        </div>
    </header>
    <?php
}

/**
 * Custom Footer Function
 */
function astra_child_custom_footer() {
    ?>
    <footer class="custom-footer">
        <div class="footer-content">
            <p>&copy; <?php echo date( 'Y' ); ?> <?php bloginfo( 'name' ); ?>. All rights reserved.</p>
        </div>
    </footer>
    <?php
}

/**
 * Hook the custom header and footer into the theme.
 */
function astra_child_add_custom_header_footer() {
    // Output the custom header.
    astra_child_custom_header();

    // Output the main content area.
    if ( have_posts() ) {
        while ( have_posts() ) {
            the_post();
            the_content();
        }
    }

    // Output the custom footer.
    astra_child_custom_footer();
}
add_action( 'astra_header', 'astra_child_add_custom_header_footer' );
add_action( 'astra_footer', 'astra_child_add_custom_header_footer' );
```

Make sure to create a `style.css` file in your child theme directory to style the custom header and footer as needed.
