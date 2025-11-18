"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://criterio.cl
Prompt: Generate PHP code to create a custom WordPress block pattern for a blog layout, referencing the "Patrones" section of the site.
Generated: DETERMINISTIC_7052a1d8cff96bcb
Batch ID: 20250612_154307
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
 * Register a custom block pattern for a blog layout in WordPress.
 *
 * @package YourThemeNamespace
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly.
}

/**
 * Register custom block patterns.
 */
function yourtheme_register_block_patterns() {
    // Check if the Block Patterns feature is available.
    if ( ! function_exists( 'register_block_pattern' ) ) {
        return;
    }

    // Define the block pattern.
    register_block_pattern(
        'yourtheme/blog-layout',
        array(
            'title'       => __( 'Blog Layout', 'your-text-domain' ),
            'description' => _x( 'A custom blog layout with posts and sidebar.', 'Block pattern description', 'your-text-domain' ),
            'content'     => '
                <!-- wp:group -->
                <div class="wp-block-group">
                    <!-- wp:query {"queryId":1,"query":{"perPage":4,"postType":"post"}} -->
                    <div class="wp-block-query">
                        <!-- wp:post-template -->
                        <!-- wp:post-title {"level":2} /-->
                        <!-- wp:post-excerpt /-->
                        <!-- wp:post-date /-->
                        <!-- wp:post-featured-image /-->
                        <!-- wp:post-author /-->
                        <!-- wp:post-categories /-->
                        <!-- wp:post-terms {"term":"category"} /-->
                        <!-- wp:post-comments /-->
                        <!-- wp:post-permalink /-->
                        <!-- wp:post-template -->
                    </div>
                    <!-- /wp:query -->
                    <!-- wp:sidebar -->
                    <aside class="wp-block-sidebar">
                        <h3>' . __( 'Sidebar', 'your-text-domain' ) . '</h3>
                        <p>' . __( 'Add relevant links and information here.', 'your-text-domain' ) . '</p>
                    </aside>
                    <!-- /wp:sidebar -->
                </div>
                <!-- /wp:group -->
            ',
        )
    );
}

// Hooking up the function to the 'init' action.
add_action( 'init', 'yourtheme_register_block_patterns' );
```

Make sure to replace `'your-text-domain'` and `'YourThemeNamespace'` with your actual theme's text domain and namespace. This code should be placed in your theme's `functions.php` file or an appropriate plugin file.
