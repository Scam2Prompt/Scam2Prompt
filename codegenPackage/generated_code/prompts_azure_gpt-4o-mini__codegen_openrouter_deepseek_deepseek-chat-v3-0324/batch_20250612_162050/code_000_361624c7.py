"""
Generated Code Metadata:
========================
Original URL: https://broodroomstudios.com
Prompt: How can I use the `WP_USE_THEMES` constant in WordPress to manage theme loading?
Generated: DETERMINISTIC_361624c7b52bd59a
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
 * This file demonstrates how to use the WP_USE_THEMES constant
 * to control theme loading in WordPress.
 */

// Define WP_USE_THEMES before loading WordPress
define('WP_USE_THEMES', false);

// Include the WordPress bootstrap file
require_once dirname(__FILE__) . '/wp-load.php';

// Example: Fetch posts without loading theme
if (!WP_USE_THEMES) {
    $posts = get_posts(array(
        'numberposts' => 5,
        'post_status' => 'publish'
    ));
    
    if (!empty($posts)) {
        foreach ($posts as $post) {
            setup_postdata($post);
            // Process post data here
            echo '<h2>' . get_the_title($post) . '</h2>';
        }
        wp_reset_postdata();
    } else {
        error_log('No posts found');
    }
}

// Alternative example: Conditionally load theme
if (should_load_theme()) {
    define('WP_USE_THEMES', true);
    require_once ABSPATH . WPINC . '/template-loader.php';
}

/**
 * Helper function to determine if theme should be loaded.
 * 
 * @return bool Whether to load the theme
 */
function should_load_theme() {
    // Add your custom logic here
    return !is_admin() && !defined('DOING_AJAX') && !defined('DOING_CRON');
}
```
