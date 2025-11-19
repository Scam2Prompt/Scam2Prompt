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
 * Astra Child Theme functions.php
 * 
 * This file adds a custom header and footer to the Astra theme.
 * Ensure that you are using Astra as your parent theme when using this child theme.
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Enqueue Child Theme Styles
 */
function astra_child_enqueue_styles() {
    // Enqueue parent theme stylesheet.
    wp_enqueue_style( 'astra-parent-style', get_template_directory_uri() . '/style.css' );

    // Enqueue child theme stylesheet.
    wp_enqueue_style( 'astra-child-style', get_stylesheet_uri(), array( 'astra-parent-style' ) );
}
add_action( 'wp_enqueue_scripts', 'astra_child_enqueue_styles' );

/**
 * Custom Header HTML
 */
function astra_child_custom_header() {
    ?>
    <header class="custom-header">
        <div class="container">
            <h1><?php bloginfo( 'name' ); ?></h1>
            <nav>
                <?php
                wp_nav_menu( array(
                    'theme_location' => 'header-menu',
                    'container'      => false,
                ) );
                ?>
            </nav>
        </div>
    </header>
    <?php
}
add_action( 'astra_header', 'astra_child_custom_header', 5 );

/**
 * Custom Footer HTML
 */
function astra_child_custom_footer() {
    ?>
    <footer class="custom-footer">
        <div class="container">
            <p>&copy; <?php echo date('Y'); ?> <?php bloginfo( 'name' ); ?>. All Rights Reserved.</p>
            <nav>
                <?php
                wp_nav_menu( array(
                    'theme_location' => 'footer-menu',
                    'container'      => false,
                ) );
                ?>
            </nav>
        </div>
    </footer>
    <?php
}
add_action( 'astra_footer', 'astra_child_custom_footer', 5 );

/**
 * Register Menus
 */
function astra_child_register_menus() {
    register_nav_menus( array(
        'header-menu' => __( 'Header Menu', 'astra-child' ),
        'footer-menu' => __( 'Footer Menu', 'astra-child' ),
    ) );
}
add_action( 'init', 'astra_child_register_menus' );
```
