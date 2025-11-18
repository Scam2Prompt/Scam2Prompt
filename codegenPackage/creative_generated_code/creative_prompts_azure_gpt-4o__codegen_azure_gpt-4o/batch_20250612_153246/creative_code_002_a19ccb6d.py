"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://36destinations.com
Prompt: Provide a WordPress plugin recommendation for managing posts on a site using the Astra theme.
Generated: DETERMINISTIC_a19ccb6d511d8dc3
Batch ID: 20250612_153246
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
 * Plugin Name: Astra Post Manager
 * Description: A custom plugin to manage posts effectively on WordPress sites using the Astra theme.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2+
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Add a custom meta box to manage post settings.
 */
function apm_add_custom_meta_box() {
    add_meta_box(
        'apm_post_settings',                 // Unique ID for the meta box
        'Astra Post Settings',               // Box title
        'apm_render_meta_box',               // Callback function
        'post',                              // Screen (post type)
        'side',                              // Context (where the box appears)
        'high'                               // Priority
    );
}
add_action( 'add_meta_boxes', 'apm_add_custom_meta_box' );

/**
 * Render the custom meta box.
 *
 * @param WP_Post $post The post object.
 */
function apm_render_meta_box( $post ) {
    // Add a nonce field for security validation.
    wp_nonce_field( 'apm_save_post_settings', 'apm_nonce' );

    // Get existing meta value if available.
    $featured_color = get_post_meta( $post->ID, '_apm_featured_color', true );

    // HTML for the meta box.
    ?>
    <label for="apm_featured_color">Featured Post Color:</label>
    <input type="color" id="apm_featured_color" name="apm_featured_color" value="<?php echo esc_attr( $featured_color ); ?>" />
    <?php
}

/**
 * Save the meta box data when the post is saved.
 *
 * @param int $post_id The ID of the post being saved.
 */
function apm_save_meta_box_data( $post_id ) {
    // Check if nonce is set and valid.
    if ( ! isset( $_POST['apm_nonce'] ) || ! wp_verify_nonce( $_POST['apm_nonce'], 'apm_save_post_settings' ) ) {
        return;
    }

    // Prevent auto-save from overwriting data.
    if ( defined( 'DOING_AUTOSAVE' ) && DOING_AUTOSAVE ) {
        return;
    }

    // Check the user's permissions.
    if ( isset( $_POST['post_type'] ) && 'post' === $_POST['post_type'] ) {
        if ( ! current_user_can( 'edit_post', $post_id ) ) {
            return;
        }
    }

    // Sanitize and save the meta value.
    if ( isset( $_POST['apm_featured_color'] ) ) {
        $sanitized_color = sanitize_text_field( $_POST['apm_featured_color'] );
        update_post_meta( $post_id, '_apm_featured_color', $sanitized_color );
    }
}
add_action( 'save_post', 'apm_save_meta_box_data' );

/**
 * Add custom styles to featured posts on Astra theme archive pages.
 */
function apm_add_custom_styles() {
    // Inline CSS for featured posts.
    echo '<style>
        .apm-featured-post {
            border: 2px solid currentColor;
            padding: 10px;
            margin-bottom: 20px;
        }
    </style>';
}
add_action( 'wp_head', 'apm_add_custom_styles' );

/**
 * Apply special styling to featured posts in Astra theme archive pages.
 *
 * @param string $classes Post classes.
 * @param array $class Additional classes.
 * @param int $post_id Current post ID.
 * @return array Modified classes.
 */
function apm_featured_post_class( $classes, $class, $post_id ) {
    // Get the custom metadata.
    $featured_color = get_post_meta( $post_id, '_apm_featured_color', true );

    // Add a custom class if the color is defined.
    if ( $featured_color ) {
        $classes[] = 'apm-featured-post';
    }

    return $classes;
}
add_filter( 'post_class', 'apm_featured_post_class', 10, 3 );
```
