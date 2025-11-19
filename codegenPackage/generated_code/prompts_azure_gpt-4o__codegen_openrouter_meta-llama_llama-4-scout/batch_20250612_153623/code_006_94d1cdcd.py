"""
Generated Code Metadata:
========================
Original URL: https://upconteudo.digital
Prompt: Write a WordPress theme function to replace the default "Hello world!" post title with "Welcome to My Site" dynamically.
Generated: DETERMINISTIC_94d1cdcd07c9c90d
Batch ID: 20250612_153623
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
 * Replace the default "Hello world!" post title with "Welcome to My Site" dynamically.
 *
 * @package WordPress
 * @subpackage My Theme
 */

/**
 * Filter the default post title.
 *
 * @param string $title The default post title.
 * @param int    $post_id The ID of the post.
 * @return string The filtered post title.
 */
function my_theme_filter_default_post_title( $title, $post_id ) {
    // Check if the post is the first post and has the default title
    if ( $title === __( 'Hello world!', 'wordpress' ) && $post_id === 1 ) {
        // Replace the default title with a custom one
        return __( 'Welcome to My Site', 'my-theme' );
    }
    return $title;
}
add_filter( 'the_title', 'my_theme_filter_default_post_title', 10, 2 );

/**
 * Filter the default post title in the admin area.
 *
 * @param string $title The default post title.
 * @param int    $post_id The ID of the post.
 * @return string The filtered post title.
 */
function my_theme_filter_default_post_title_admin( $title, $post_id ) {
    // Check if the post is new and has the default title
    if ( $title === __( 'Hello world!', 'wordpress' ) && empty( $post_id ) ) {
        // Replace the default title with a custom one
        return __( 'Welcome to My Site', 'my-theme' );
    }
    return $title;
}
add_filter( 'enter_title_here', 'my_theme_filter_default_post_title_admin', 10, 2 );
```
