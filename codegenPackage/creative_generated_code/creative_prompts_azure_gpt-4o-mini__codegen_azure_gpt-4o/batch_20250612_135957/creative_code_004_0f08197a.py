"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustwalletearnmoney.finance.blog
Prompt: How can I manage subscriptions effectively on a finance blog hosted on WordPress.com?
Generated: DETERMINISTIC_0f08197ac83e1d89
Batch ID: 20250612_135957
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
 * Plugin Name: Finance Blog Subscription Manager
 * Description: A WordPress plugin to manage user subscriptions effectively for a finance blog.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

// Create a custom post type for subscriptions
function create_subscription_post_type() {
    $labels = array(
        'name'               => __('Subscriptions', 'textdomain'),
        'singular_name'      => __('Subscription', 'textdomain'),
        'menu_name'          => __('Subscriptions', 'textdomain'),
        'add_new'            => __('Add New', 'textdomain'),
        'add_new_item'       => __('Add New Subscription', 'textdomain'),
        'edit_item'          => __('Edit Subscription', 'textdomain'),
        'new_item'           => __('New Subscription', 'textdomain'),
        'view_item'          => __('View Subscription', 'textdomain'),
        'search_items'       => __('Search Subscriptions', 'textdomain'),
        'not_found'          => __('No subscriptions found.', 'textdomain'),
        'not_found_in_trash' => __('No subscriptions found in trash.', 'textdomain'),
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'has_archive'        => true,
        'menu_icon'          => 'dashicons-email',
        'supports'           => array('title', 'editor', 'custom-fields'),
        'capability_type'    => 'post',
    );

    register_post_type('subscription', $args);
}

add_action('init', 'create_subscription_post_type');

// Add a custom meta box for subscription details
function add_subscription_meta_box() {
    add_meta_box(
        'subscription_details',
        __('Subscription Details', 'textdomain'),
        'render_subscription_meta_box',
        'subscription',
        'normal',
        'high'
    );
}

add_action('add_meta_boxes', 'add_subscription_meta_box');

// Render the subscription meta box
function render_subscription_meta_box($post) {
    // Retrieve existing data from post meta
    $email = get_post_meta($post->ID, '_subscription_email', true);
    $status = get_post_meta($post->ID, '_subscription_status', true);

    // Nonce field for security
    wp_nonce_field('save_subscription_meta', 'subscription_meta_nonce');

    ?>
    <p>
        <label for="subscription_email"><?php _e('Subscriber Email:', 'textdomain'); ?></label>
        <input type="email" id="subscription_email" name="subscription_email" value="<?php echo esc_attr($email); ?>" class="widefat">
    </p>
    <p>
        <label for="subscription_status"><?php _e('Subscription Status:', 'textdomain'); ?></label>
        <select id="subscription_status" name="subscription_status" class="widefat">
            <option value="active" <?php selected($status, 'active'); ?>><?php _e('Active', 'textdomain'); ?></option>
            <option value="inactive" <?php selected($status, 'inactive'); ?>><?php _e('Inactive', 'textdomain'); ?></option>
        </select>
    </p>
    <?php
}

// Save subscription details
function save_subscription_meta($post_id) {
    // Verify nonce for security
    if (!isset($_POST['subscription_meta_nonce']) || !wp_verify_nonce($_POST['subscription_meta_nonce'], 'save_subscription_meta')) {
        return;
    }

    // Prevent autosave overwrite
    if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) {
        return;
    }

    // Check post type
    if (get_post_type($post_id) !== 'subscription') {
        return;
    }

    // Save email
    if (isset($_POST['subscription_email'])) {
        update_post_meta($post_id, '_subscription_email', sanitize_email($_POST['subscription_email']));
    }

    // Save status
    if (isset($_POST['subscription_status'])) {
        update_post_meta($post_id, '_subscription_status', sanitize_text_field($_POST['subscription_status']));
    }
}

add_action('save_post', 'save_subscription_meta');

// Add a settings page for subscription management
function subscription_settings_menu() {
    add_menu_page(
        __('Subscription Settings', 'textdomain'),
        __('Subscription Settings', 'textdomain'),
        'manage_options',
        'subscription-settings',
        'subscription_settings_page',
        'dashicons-admin-settings',
        20
    );
}

add_action('admin_menu', 'subscription_settings_menu');

// Render the settings page
function subscription_settings_page() {
    ?>
    <div class="wrap">
        <h1><?php _e('Subscription Settings', 'textdomain'); ?></h1>
        <form method="post" action="options.php">
            <?php
            // Output security fields for the registered settings
            settings_fields('subscription_settings_group');

            // Output setting sections and their fields
            do_settings_sections('subscription-settings');

            // Output save settings button
            submit_button();
            ?>
        </form>
    </div>
    <?php
}

// Register settings
function register_subscription_settings() {
    register_setting(
        'subscription_settings_group',
        'subscription_email_notifications',
        array(
            'type'              => 'boolean',
            'description'       => __('Enable email notifications for subscriptions', 'textdomain'),
            'sanitize_callback' => 'sanitize_text_field',
            'default'           => true,
        )
    );

    add_settings_section(
        'subscription_settings_section',
        __('Subscription Settings', 'textdomain'),
        function () {
            _e('Manage subscription-related settings.', 'textdomain');
        },
        'subscription-settings'
    );

    add_settings_field(
        'subscription_email_notifications',
        __('Enable Email Notifications', 'textdomain'),
        function () {
            $option = get_option('subscription_email_notifications', true);
            ?>
            <input type="checkbox" name="subscription_email_notifications" value="1" <?php checked($option, 1); ?>>
            <?php
        },
        'subscription-settings',
        'subscription_settings_section'
    );
}

add_action('admin_init', 'register_subscription_settings');
```
