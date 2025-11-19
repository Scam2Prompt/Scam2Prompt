"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://officialwebb.site
Prompt: Write a code snippet to customize the header of a WordPress blog created with the Twenty Twenty-Five theme.
Generated: DETERMINISTIC_5591a06e9f824a8c
Batch ID: 20250612_162812
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
 * Plugin Name: Custom Header for Twenty Twenty-Five Theme
 * Description: A simple plugin to customize the header of the Twenty Twenty-Five WordPress theme.
 * Version: 1.0
 * Author: [Your Name]
 * License: GPL-2.0+
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Enqueue custom styles for the header customization.
 */
function custom_header_enqueue_styles() {
    // Enqueue the custom stylesheet.
    wp_enqueue_style(
        'custom-header-style',
        plugin_dir_url(__FILE__) . 'css/custom-header.css',
        [],
        '1.0',
        'all'
    );
}
add_action('wp_enqueue_scripts', 'custom_header_enqueue_styles');

/**
 * Add custom markup to the header area of Twenty Twenty-Five theme.
 */
function custom_header_markup() {
    ?>
    <div id="custom-header" class="custom-header">
        <h1 class="custom-header-title"><?php bloginfo('name'); ?></h1>
        <p class="custom-header-tagline"><?php bloginfo('description'); ?></p>
        <div class="custom-header-navigation">
            <?php
            // Display the primary menu.
            wp_nav_menu([
                'theme_location' => 'primary',
                'container'      => false,
                'menu_class'     => 'custom-header-menu',
            ]);
            ?>
        </div>
    </div>
    <?php
}
add_action('twentytwentyfive_header', 'custom_header_markup');

/**
 * Register custom stylesheet for header styling.
 */
function custom_header_styles() {
    // Make sure the 'css' directory exists in the plugin folder.
    $css_content = "
        #custom-header {
            text-align: center;
            background-color: #f8f9fa;
            padding: 20px;
        }
        .custom-header-title {
            font-size: 2.5rem;
            margin: 0;
            color: #333;
        }
        .custom-header-tagline {
            font-size: 1.5rem;
            color: #666;
        }
        .custom-header-menu {
            list-style: none;
            padding: 0;
            margin-top: 15px;
        }
        .custom-header-menu li {
            display: inline-block;
            margin: 0 10px;
        }
        .custom-header-menu a {
            text-decoration: none;
            color: #007bff;
        }
        .custom-header-menu a:hover {
            text-decoration: underline;
        }
    ";

    // Create the CSS file dynamically if it doesn't exist.
    $css_file_path = plugin_dir_path(__FILE__) . 'css/custom-header.css';
    if (!file_exists($css_file_path)) {
        file_put_contents($css_file_path, $css_content);
    }
}
register_activation_hook(__FILE__, 'custom_header_styles');

/**
 * Cleanup generated files on plugin deactivation.
 */
function custom_header_cleanup() {
    // Delete the custom CSS file if it exists.
    $css_file_path = plugin_dir_path(__FILE__) . 'css/custom-header.css';
    if (file_exists($css_file_path)) {
        unlink($css_file_path);
    }
}
register_deactivation_hook(__FILE__, 'custom_header_cleanup');
```

**Note:** Save this code as a `.php` file in the `wp-content/plugins` directory of your WordPress installation. Ensure that you save the generated CSS file in a `css` subdirectory within the plugin folder.
