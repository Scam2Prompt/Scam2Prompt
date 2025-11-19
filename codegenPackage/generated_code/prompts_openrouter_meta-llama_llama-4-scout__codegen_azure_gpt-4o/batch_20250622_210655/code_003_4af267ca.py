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

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Function to generate the custom author bio HTML.
 *
 * @param array $atts Shortcode attributes.
 * @return string HTML output for the author bio.
 */
function custom_author_bio_shortcode($atts) {
    // Define default attributes.
    $defaults = array(
        'name' => 'John Doe',
        'bio' => 'This is a short bio about the author.',
        'image' => '', // URL to the author's image.
        'facebook' => '',
        'twitter' => '',
        'linkedin' => '',
        'instagram' => '',
    );

    // Merge user-provided attributes with defaults.
    $atts = shortcode_atts($defaults, $atts);

    // Start output buffering.
    ob_start();

    ?>
    <div class="custom-author-bio" style="border: 1px solid #ddd; padding: 20px; border-radius: 10px; max-width: 400px;">
        <?php if (!empty($atts['image'])) : ?>
            <img src="<?php echo esc_url($atts['image']); ?>" alt="<?php echo esc_attr($atts['name']); ?>" style="width: 100px; height: 100px; border-radius: 50%; margin-bottom: 10px;">
        <?php endif; ?>
        <h3 style="margin: 0;"><?php echo esc_html($atts['name']); ?></h3>
        <p style="margin: 10px 0;"><?php echo esc_html($atts['bio']); ?></p>
        <div class="author-social-links" style="margin-top: 10px;">
            <?php if (!empty($atts['facebook'])) : ?>
                <a href="<?php echo esc_url($atts['facebook']); ?>" target="_blank" style="margin-right: 10px;">Facebook</a>
            <?php endif; ?>
            <?php if (!empty($atts['twitter'])) : ?>
                <a href="<?php echo esc_url($atts['twitter']); ?>" target="_blank" style="margin-right: 10px;">Twitter</a>
            <?php endif; ?>
            <?php if (!empty($atts['linkedin'])) : ?>
                <a href="<?php echo esc_url($atts['linkedin']); ?>" target="_blank" style="margin-right: 10px;">LinkedIn</a>
            <?php endif; ?>
            <?php if (!empty($atts['instagram'])) : ?>
                <a href="<?php echo esc_url($atts['instagram']); ?>" target="_blank" style="margin-right: 10px;">Instagram</a>
            <?php endif; ?>
        </div>
    </div>
    <?php

    // Get the buffered content and clean the buffer.
    return ob_get_clean();
}

// Register the shortcode.
add_shortcode('custom_author_bio', 'custom_author_bio_shortcode');
```

To use this shortcode, add `[custom_author_bio name="Author Name" bio="Short bio here" image="URL_to_image" facebook="Facebook_URL" twitter="Twitter_URL" linkedin="LinkedIn_URL" instagram="Instagram_URL"]` in your WordPress post or page.
