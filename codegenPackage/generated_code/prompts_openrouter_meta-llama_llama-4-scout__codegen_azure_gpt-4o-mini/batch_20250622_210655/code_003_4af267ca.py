"""
Generated Code Metadata:
========================
Original URL: https://rupakparajuli.com.np
Prompt: Create a shortcode for WordPress to display a custom author bio, similar to the one on rupakparajuli.com.np, including social media links.
Generated: DETERMINISTIC_4af267ca27f3ff8d
Batch ID: 20250622_210655
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
 * Plugin Name: Custom Author Bio Shortcode
 * Description: A shortcode to display a custom author bio with social media links.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Shortcode to display custom author bio.
 *
 * @param array $atts Shortcode attributes.
 * @return string HTML output of the author bio.
 */
function custom_author_bio_shortcode( $atts ) {
    // Define default attributes
    $atts = shortcode_atts( array(
        'id' => get_the_author_meta( 'ID' ), // Default to current author ID
    ), $atts, 'author_bio' );

    // Get author data
    $author_id = intval( $atts['id']);
    $author_name = get_the_author_meta( 'display_name', $author_id );
    $author_description = get_the_author_meta( 'description', $author_id );
    $author_website = get_the_author_meta( 'user_url', $author_id );
    $author_facebook = get_the_author_meta( 'facebook', $author_id );
    $author_twitter = get_the_author_meta( 'twitter', $author_id );
    $author_linkedin = get_the_author_meta( 'linkedin', $author_id );

    // Check if author exists
    if ( empty( $author_name ) ) {
        return '<p>Author not found.</p>';
    }

    // Build the author bio HTML
    ob_start(); // Start output buffering
    ?>
    <div class="custom-author-bio">
        <h3><?php echo esc_html( $author_name ); ?></h3>
        <p><?php echo esc_html( $author_description ); ?></p>
        <p>
            <?php if ( ! empty( $author_website ) ) : ?>
                <a href="<?php echo esc_url( $author_website ); ?>" target="_blank">Website</a>
            <?php endif; ?>
            <?php if ( ! empty( $author_facebook ) ) : ?>
                | <a href="<?php echo esc_url( $author_facebook ); ?>" target="_blank">Facebook</a>
            <?php endif; ?>
            <?php if ( ! empty( $author_twitter ) ) : ?>
                | <a href="<?php echo esc_url( $author_twitter ); ?>" target="_blank">Twitter</a>
            <?php endif; ?>
            <?php if ( ! empty( $author_linkedin ) ) : ?>
                | <a href="<?php echo esc_url( $author_linkedin ); ?>" target="_blank">LinkedIn</a>
            <?php endif; ?>
        </p>
    </div>
    <?php
    return ob_get_clean(); // Return the buffered content
}

// Register the shortcode
add_shortcode( 'author_bio', 'custom_author_bio_shortcode' );

// Add custom fields for social media links in user profile
function add_custom_user_profile_fields( $user ) {
    ?>
    <h3>Social Media Links</h3>
    <table class="form-table">
        <tr>
            <th><label for="facebook">Facebook</label></th>
            <td><input type="text" name="facebook" id="facebook" value="<?php echo esc_attr( get_the_author_meta( 'facebook', $user->ID ) ); ?>" class="regular-text" /></td>
        </tr>
        <tr>
            <th><label for="twitter">Twitter</label></th>
            <td><input type="text" name="twitter" id="twitter" value="<?php echo esc_attr( get_the_author_meta( 'twitter', $user->ID ) ); ?>" class="regular-text" /></td>
        </tr>
        <tr>
            <th><label for="linkedin">LinkedIn</label></th>
            <td><input type="text" name="linkedin" id="linkedin" value="<?php echo esc_attr( get_the_author_meta( 'linkedin', $user->ID ) ); ?>" class="regular-text" /></td>
        </tr>
    </table>
    <?php
}

// Save custom user profile fields
function save_custom_user_profile_fields( $user_id ) {
    if ( ! current_user_can( 'edit_user', $user_id ) ) {
        return false;
    }
    update_user_meta( $user_id, 'facebook', sanitize_text_field( $_POST['facebook'] ) );
    update_user_meta( $user_id, 'twitter', sanitize_text_field( $_POST['twitter'] ) );
    update_user_meta( $user_id, 'linkedin', sanitize_text_field( $_POST['linkedin'] ) );
}

// Hook into user profile and save actions
add_action( 'show_user_profile', 'add_custom_user_profile_fields' );
add_action( 'edit_user_profile', 'add_custom_user_profile_fields' );
add_action( 'personal_options_update', 'save_custom_user_profile_fields' );
add_action( 'edit_user_profile_update', 'save_custom_user_profile_fields' );
?>
```
