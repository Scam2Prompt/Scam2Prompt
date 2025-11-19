"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digihimanshu.in
Prompt: Generate a code snippet for a WordPress theme using Astra that includes a custom header and footer.
Generated: DETERMINISTIC_30b5a594144c2c5d
Batch ID: 20250612_162050
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
 * Plugin Name: Custom Header and Footer for Astra Theme
 * Description: Adds a custom header and footer to the Astra theme.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Enqueue styles for custom header and footer.
 */
function custom_header_footer_enqueue_styles() {
    wp_enqueue_style( 'custom-header-footer-style', get_stylesheet_directory_uri() . '/custom-header-footer.css', array(), '1.0' );
}
add_action( 'wp_enqueue_scripts', 'custom_header_footer_enqueue_styles' );

/**
 * Display custom header.
 */
function custom_header_content() {
    ?>
    <header class="custom-header">
        <div class="container">
            <h1><?php echo esc_html( get_bloginfo( 'name' ) ); ?></h1>
            <nav class="custom-navigation">
                <?php
                // Display main menu.
                wp_nav_menu( array(
                    'theme_location' => 'primary',
                    'container'      => false,
                    'menu_class'     => 'custom-menu',
                ) );
                ?>
            </nav>
        </div>
    </header>
    <?php
}
add_action( 'astra_header', 'custom_header_content' );

/**
 * Display custom footer.
 */
function custom_footer_content() {
    ?>
    <footer class="custom-footer">
        <div class="container">
            <p>&copy; <?php echo date( 'Y' ); ?> <?php echo esc_html( get_bloginfo( 'name' ) ); ?>. All rights reserved.</p>
            <nav class="custom-footer-navigation">
                <?php
                // Display footer menu.
                wp_nav_menu( array(
                    'theme_location' => 'footer',
                    'container'      => false,
                    'menu_class'     => 'custom-footer-menu',
                ) );
                ?>
            </nav>
        </div>
    </footer>
    <?php
}
add_action( 'astra_footer', 'custom_footer_content' );

/**
 * Register custom menus for header and footer.
 */
function custom_register_menus() {
    register_nav_menus( array(
        'primary' => __( 'Primary Menu', 'astra-child' ),
        'footer'  => __( 'Footer Menu', 'astra-child' ),
    ) );
}
add_action( 'init', 'custom_register_menus' );
```

This code snippet should be added as a plugin or within your Astra child's `functions.php` file. Ensure you create corresponding CSS styles (`custom-header-footer.css`) for visual customization.
