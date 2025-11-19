"""
Generated Code Metadata:
========================
Original URL: https://criterio.cl
Prompt: Generate PHP code to create a custom WordPress block pattern for a blog layout, referencing the "Patrones" section of the site.
Generated: DETERMINISTIC_7052a1d8cff96bcb
Batch ID: 20250612_154307
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
 * Registers a custom block pattern for a blog layout.
 *
 * @package WordPress
 */

if ( ! function_exists( 'register_blog_layout_pattern' ) ) {
    /**
     * Registers the blog layout block pattern.
     */
    function register_blog_layout_pattern() {
        register_block_pattern(
            'my-theme/blog-layout',
            array(
                'title'       => __( 'Blog Layout', 'my-theme' ),
                'description' => _x( 'A custom blog layout with featured posts and sidebar.', 'Block pattern description', 'my-theme' ),
                'categories'  => array( 'posts' ),
                'content'     => '<!-- wp:group {"layout":{"type":"constrained"}} -->
                    <div class="wp-block-group">
                        <!-- wp:heading {"level":1,"align":"wide"} -->
                        <h1 class="alignwide">' . esc_html__( 'Latest Posts', 'my-theme' ) . '</h1>
                        <!-- /wp:heading -->
                        
                        <!-- wp:columns {"align":"wide"} -->
                        <div class="wp-block-columns alignwide">
                            <!-- wp:column {"width":"70%"} -->
                            <div class="wp-block-column" style="flex-basis:70%">
                                <!-- wp:query {"query":{"perPage":3,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","author":"","search":"","exclude":[],"sticky":"","inherit":false}} -->
                                <div class="wp-block-query">
                                    <!-- wp:post-template -->
                                    <!-- wp:post-featured-image {"isLink":true} /-->
                                    <!-- wp:post-title {"isLink":true} /-->
                                    <!-- wp:post-excerpt /-->
                                    <!-- wp:post-date /-->
                                    <!-- /wp:post-template -->
                                </div>
                                <!-- /wp:query -->
                            </div>
                            <!-- /wp:column -->
                            
                            <!-- wp:column {"width":"30%"} -->
                            <div class="wp-block-column" style="flex-basis:30%">
                                <!-- wp:heading {"level":3} -->
                                <h3>' . esc_html__( 'Categories', 'my-theme' ) . '</h3>
                                <!-- /wp:heading -->
                                <!-- wp:categories /-->
                                
                                <!-- wp:heading {"level":3} -->
                                <h3>' . esc_html__( 'Recent Posts', 'my-theme' ) . '</h3>
                                <!-- /wp:heading -->
                                <!-- wp:latest-posts {"postsToShow":5} /-->
                            </div>
                            <!-- /wp:column -->
                        </div>
                        <!-- /wp:columns -->
                    </div>
                    <!-- /wp:group -->',
            )
        );
    }

    add_action( 'init', 'register_blog_layout_pattern' );
}
```
