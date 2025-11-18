"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicbear.com.br
Prompt: Suggest a WordPress plugin for managing bilingual school schedules and provide an example of how to configure it for Magic Bear Canadian School.
Generated: DETERMINISTIC_3a8100f4a4a02a79
Batch ID: 20250612_153224
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
 * Plugin Name: Bilingual School Schedule Manager
 * Description: A WordPress plugin for managing bilingual school schedules.
 * Version: 1.0
 * Author: Your Name
 * License: GPLv2 or later
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Create custom post type for bilingual school schedules
 */
function mbcs_create_schedule_post_type() {
    $labels = array(
        'name'               => __('School Schedules', 'mbcs'),
        'singular_name'      => __('School Schedule', 'mbcs'),
        'menu_name'          => __('School Schedules', 'mbcs'),
        'add_new'            => __('Add New', 'mbcs'),
        'add_new_item'       => __('Add New Schedule', 'mbcs'),
        'edit_item'          => __('Edit Schedule', 'mbcs'),
        'new_item'           => __('New Schedule', 'mbcs'),
        'view_item'          => __('View Schedule', 'mbcs'),
        'search_items'       => __('Search Schedules', 'mbcs'),
        'not_found'          => __('No schedules found', 'mbcs'),
        'not_found_in_trash' => __('No schedules found in trash', 'mbcs'),
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'has_archive'        => true,
        'menu_icon'          => 'dashicons-calendar',
        'supports'           => array('title', 'editor', 'custom-fields'),
        'show_in_rest'       => true, // Enables Gutenberg editor
    );

    register_post_type('mbcs_schedule', $args);
}
add_action('init', 'mbcs_create_schedule_post_type');

/**
 * Add custom meta box for specifying language
 */
function mbcs_add_language_meta_box() {
    add_meta_box(
        'mbcs_language_meta_box',
        __('Schedule Language', 'mbcs'),
        'mbcs_language_meta_box_callback',
        'mbcs_schedule',
        'side',
        'default'
    );
}

add_action('add_meta_boxes', 'mbcs_add_language_meta_box');

/**
 * Meta box callback for language selection
 */
function mbcs_language_meta_box_callback($post) {
    $value = get_post_meta($post->ID, '_mbcs_language', true);
    ?>
    <label for="mbcs_language"><?php _e('Select Schedule Language:', 'mbcs'); ?></label>
    <select name="mbcs_language" id="mbcs_language">
        <option value="english" <?php selected($value, 'english'); ?>><?php _e('English', 'mbcs'); ?></option>
        <option value="french" <?php selected($value, 'french'); ?>><?php _e('French', 'mbcs'); ?></option>
    </select>
    <?php
}

/**
 * Save meta box data
 */
function mbcs_save_language_meta_box_data($post_id) {
    // Check if nonce is set and valid
    if (!isset($_POST['mbcs_language']) || !wp_verify_nonce($_POST['_wpnonce'], 'update-post_' . $post_id)) {
        return;
    }

    // Save/Update meta data
    $language = sanitize_text_field($_POST['mbcs_language']);
    update_post_meta($post_id, '_mbcs_language', $language);
}
add_action('save_post', 'mbcs_save_language_meta_box_data');

/**
 * Enqueue admin scripts and styles
 */
function mbcs_enqueue_admin_scripts($hook) {
    if ('post.php' === $hook || 'post-new.php' === $hook) {
        wp_enqueue_style('mbcs-admin-css', plugins_url('assets/admin.css', __FILE__));
    }
}
add_action('admin_enqueue_scripts', 'mbcs_enqueue_admin_scripts');

/**
 * Shortcode to display schedules
 */
function mbcs_display_schedules_shortcode($atts) {
    $atts = shortcode_atts(
        array(
            'language' => 'english', // Default to English
        ),
        $atts,
        'mbcs_schedules'
    );

    $language = sanitize_text_field($atts['language']);

    $query = new WP_Query(array(
        'post_type'  => 'mbcs_schedule',
        'meta_key'   => '_mbcs_language',
        'meta_value' => $language,
        'posts_per_page' => -1,
    ));

    if ($query->have_posts()) {
        $output = '<ul class="mbcs-schedules">';
        while ($query->have_posts()) {
            $query->the_post();
            $output .= '<li>' . get_the_title() . ' - ' . get_the_content() . '</li>';
        }
        $output .= '</ul>';
        wp_reset_postdata();
        return $output;
    } else {
        return '<p>' . __('No schedules found.', 'mbcs') . '</p>';
    }
}
add_shortcode('mbcs_schedules', 'mbcs_display_schedules_shortcode');
```

### Example of Configuration for Magic Bear Canadian School:

1. Install and activate the plugin in the WordPress admin panel.
2. Go to "School Schedules" and add schedules for both English and French using the custom post type.
3. Use the shortcode `[mbcs_schedules language="english"]` to display English schedules and `[mbcs_schedules language="french"]` to display French schedules on any page or post.
