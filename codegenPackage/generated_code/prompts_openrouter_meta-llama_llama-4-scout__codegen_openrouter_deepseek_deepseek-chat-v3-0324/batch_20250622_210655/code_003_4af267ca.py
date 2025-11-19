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
 * @param array $atts Shortcode attributes
 * @return string HTML output
 */
function custom_author_bio_shortcode($atts) {
    // Default attributes
    $atts = shortcode_atts(
        array(
            'author_id' => get_the_author_meta('ID'),
            'show_social' => true,
            'avatar_size' => 100,
        ),
        $atts,
        'author_bio'
    );

    // Get author data
    $author_id = $atts['author_id'];
    $author_name = get_the_author_meta('display_name', $author_id);
    $author_bio = get_the_author_meta('description', $author_id);
    $author_avatar = get_avatar($author_id, $atts['avatar_size']);

    // Get social media links from user meta
    $social_links = array(
        'twitter' => get_the_author_meta('twitter', $author_id),
        'facebook' => get_the_author_meta('facebook', $author_id),
        'linkedin' => get_the_author_meta('linkedin', $author_id),
        'instagram' => get_the_author_meta('instagram', $author_id),
        'website' => get_the_author_meta('user_url', $author_id),
    );

    // Start output buffering
    ob_start();
    ?>
    
    <div class="custom-author-bio">
        <div class="author-avatar">
            <?php echo $author_avatar; ?>
        </div>
        <div class="author-info">
            <h3 class="author-name"><?php echo esc_html($author_name); ?></h3>
            <div class="author-description">
                <?php echo wpautop(esc_html($author_bio)); ?>
            </div>
            
            <?php if ($atts['show_social'] && !empty(array_filter($social_links))) : ?>
                <div class="author-social-links">
                    <?php foreach ($social_links as $platform => $url) : ?>
                        <?php if (!empty($url)) : ?>
                            <a href="<?php echo esc_url($url); ?>" target="_blank" rel="noopener noreferrer" class="social-link <?php echo esc_attr($platform); ?>">
                                <span class="dashicons dashicons-<?php echo esc_attr($platform); ?>"></span>
                            </a>
                        <?php endif; ?>
                    <?php endforeach; ?>
                </div>
            <?php endif; ?>
        </div>
    </div>

    <?php
    // Add some basic inline styles
    ?>
    <style>
        .custom-author-bio {
            display: flex;
            gap: 20px;
            margin: 20px 0;
            padding: 20px;
            background: #f9f9f9;
            border-radius: 5px;
        }
        .author-avatar img {
            border-radius: 50%;
        }
        .author-info {
            flex: 1;
        }
        .author-social-links {
            margin-top: 15px;
        }
        .social-link {
            margin-right: 10px;
            text-decoration: none;
        }
    </style>

    <?php
    // Return the buffered content
    return ob_get_clean();
}
add_shortcode('author_bio', 'custom_author_bio_shortcode');

/**
 * Add social media fields to user profile
 */
function add_social_media_fields($user) {
    ?>
    <h3><?php esc_html_e('Social Media Links', 'textdomain'); ?></h3>
    <table class="form-table">
        <tr>
            <th><label for="twitter"><?php esc_html_e('Twitter', 'textdomain'); ?></label></th>
            <td>
                <input type="url" name="twitter" id="twitter" value="<?php echo esc_attr(get_the_author_meta('twitter', $user->ID)); ?>" class="regular-text" />
                <p class="description"><?php esc_html_e('Enter your Twitter profile URL.', 'textdomain'); ?></p>
            </td>
        </tr>
        <tr>
            <th><label for="facebook"><?php esc_html_e('Facebook', 'textdomain'); ?></label></th>
            <td>
                <input type="url" name="facebook" id="facebook" value="<?php echo esc_attr(get_the_author_meta('facebook', $user->ID)); ?>" class="regular-text" />
                <p class="description"><?php esc_html_e('Enter your Facebook profile URL.', 'textdomain'); ?></p>
            </td>
        </tr>
        <tr>
            <th><label for="linkedin"><?php esc_html_e('LinkedIn', 'textdomain'); ?></label></th>
            <td>
                <input type="url" name="linkedin" id="linkedin" value="<?php echo esc_attr(get_the_author_meta('linkedin', $user->ID)); ?>" class="regular-text" />
                <p class="description"><?php esc_html_e('Enter your LinkedIn profile URL.', 'textdomain'); ?></p>
            </td>
        </tr>
        <tr>
            <th><label for="instagram"><?php esc_html_e('Instagram', 'textdomain'); ?></label></th>
            <td>
                <input type="url" name="instagram" id="instagram" value="<?php echo esc_attr(get_the_author_meta('instagram', $user->ID)); ?>" class="regular-text" />
                <p class="description"><?php esc_html_e('Enter your Instagram profile URL.', 'textdomain'); ?></p>
            </td>
        </tr>
    </table>
    <?php
}
add_action('show_user_profile', 'add_social_media_fields');
add_action('edit_user_profile', 'add_social_media_fields');

/**
 * Save social media fields
 */
function save_social_media_fields($user_id) {
    if (!current_user_can('edit_user', $user_id)) {
        return false;
    }

    update_user_meta($user_id, 'twitter', sanitize_text_field($_POST['twitter']));
    update_user_meta($user_id, 'facebook', sanitize_text_field($_POST['facebook']));
    update_user_meta($user_id, 'linkedin', sanitize_text_field($_POST['linkedin']));
    update_user_meta($user_id, 'instagram', sanitize_text_field($_POST['instagram']));
}
add_action('personal_options_update', 'save_social_media_fields');
add_action('edit_user_profile_update', 'save_social_media_fields');
```
