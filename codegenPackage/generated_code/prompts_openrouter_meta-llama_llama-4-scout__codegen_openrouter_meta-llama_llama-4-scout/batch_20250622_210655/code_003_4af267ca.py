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
 * Custom Author Bio Shortcode
 *
 * Displays a custom author bio with social media links.
 *
 * @package WordPress
 * @subpackage Custom Shortcodes
 */

// Define the shortcode function
function custom_author_bio_shortcode() {
    // Get the current author object
    $author = get_user_by( 'id', get_the_author_meta( 'ID' ) );

    // Check if author object exists
    if ( ! $author ) {
        return __( 'Author not found.', 'text-domain' );
    }

    // Get author bio and social media links from database
    $author_bio = get_the_author_meta( 'description' );
    $facebook_url = get_the_author_meta( 'facebook_url', $author->ID );
    $twitter_url = get_the_author_meta( 'twitter_url', $author->ID );
    $linkedin_url = get_the_author_meta( 'linkedin_url', $author->ID );
    $github_url = get_the_author_meta( 'github_url', $author->ID );

    // Shortcode output
    $output = '<div class="author-bio">';

    // Author image
    $author_image_id = get_avatar( $author->ID, 100 );
    $output .= '<div class="author-image">' . $author_image_id . '</div>';

    // Author bio
    $output .= '<div class="author-info">';
    $output .= '<h4 class="author-name">' . $author->display_name . '</h4>';
    $output .= '<p class="author-description">' . wp_kses_post( $author_bio ) . '</p>';

    // Social media links
    $output .= '<ul class="social-media-links">';
    if ( $facebook_url ) {
        $output .= '<li><a href="' . esc_url( $facebook_url ) . '" target="_blank" rel="noopener noreferrer"><i class="fab fa-facebook-f"></i></a></li>';
    }
    if ( $twitter_url ) {
        $output .= '<li><a href="' . esc_url( $twitter_url ) . '" target="_blank" rel="noopener noreferrer"><i class="fab fa-twitter"></i></a></li>';
    }
    if ( $linkedin_url ) {
        $output .= '<li><a href="' . esc_url( $linkedin_url ) . '" target="_blank" rel="noopener noreferrer"><i class="fab fa-linkedin-in"></i></a></li>';
    }
    if ( $github_url ) {
        $output .= '<li><a href="' . esc_url( $github_url ) . '" target="_blank" rel="noopener noreferrer"><i class="fab fa-github"></i></a></li>';
    }
    $output .= '</ul>';

    $output .= '</div></div>';

    return $output;
}
add_shortcode( 'custom_author_bio', 'custom_author_bio_shortcode' );

// Add custom user fields for social media links
function custom_user_fields( $user ) {
    ?>
    <h3>Social Media Links</h3>
    <table class="form-table">
        <tr>
            <th><label for="facebook_url">Facebook URL</label></th>
            <td><input type="text" name="facebook_url" id="facebook_url" value="<?php echo esc_attr( get_the_author_meta( 'facebook_url', $user->ID ) ); ?>" /></td>
        </tr>
        <tr>
            <th><label for="twitter_url">Twitter URL</label></th>
            <td><input type="text" name="twitter_url" id="twitter_url" value="<?php echo esc_attr( get_the_author_meta( 'twitter_url', $user->ID ) ); ?>" /></td>
        </tr>
        <tr>
            <th><label for="linkedin_url">LinkedIn URL</label></th>
            <td><input type="text" name="linkedin_url" id="linkedin_url" value="<?php echo esc_attr( get_the_author_meta( 'linkedin_url', $user->ID ) ); ?>" /></td>
        </tr>
        <tr>
            <th><label for="github_url">GitHub URL</label></th>
            <td><input type="text" name="github_url" id="github_url" value="<?php echo esc_attr( get_the_author_meta( 'github_url', $user->ID ) ); ?>" /></td>
        </tr>
    </table>
    <?php
}
add_action( 'show_user_profile', 'custom_user_fields' );
add_action( 'edit_user_profile', 'custom_user_fields' );

// Save custom user fields
function save_custom_user_fields( $user_id ) {
    if ( ! current_user_can( 'edit_user', $user_id ) ) {
        return false;
    }

    update_user_meta( $user_id, 'facebook_url', $_POST['facebook_url'] );
    update_user_meta( $user_id, 'twitter_url', $_POST['twitter_url'] );
    update_user_meta( $user_id, 'linkedin_url', $_POST['linkedin_url'] );
    update_user_meta( $user_id, 'github_url', $_POST['github_url'] );
}
add_action( 'personal_options_update', 'save_custom_user_fields' );
add_action( 'edit_user_profile_update', 'save_custom_user_fields' );
```
