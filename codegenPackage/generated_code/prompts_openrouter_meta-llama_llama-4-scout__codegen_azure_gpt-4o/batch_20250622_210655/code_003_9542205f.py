"""
Generated Code Metadata:
========================
Original URL: https://wordpress.armelin.media
Prompt: Design a WordPress theme for an architecture company that highlights their portfolio, services, and news, incorporating a newsletter signup feature like the Études Newsletter.
Generated: DETERMINISTIC_9542205fbf6c2fad
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
 * Architecture Company Theme - functions.php
 * A WordPress theme for showcasing portfolio, services, news, and a newsletter signup feature.
 * 
 * @package ArchitectureCompanyTheme
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Theme setup function.
 */
function architecture_theme_setup() {
    // Add theme support for title tag.
    add_theme_support('title-tag');

    // Add theme support for post thumbnails.
    add_theme_support('post-thumbnails');

    // Register navigation menus.
    register_nav_menus(array(
        'primary' => __('Primary Menu', 'architecture-theme'),
        'footer' => __('Footer Menu', 'architecture-theme'),
    ));
}
add_action('after_setup_theme', 'architecture_theme_setup');

/**
 * Enqueue theme styles and scripts.
 */
function architecture_theme_enqueue_scripts() {
    // Enqueue main stylesheet.
    wp_enqueue_style('architecture-theme-style', get_stylesheet_uri());

    // Enqueue custom JavaScript file.
    wp_enqueue_script('architecture-theme-script', get_template_directory_uri() . '/js/main.js', array('jquery'), null, true);
}
add_action('wp_enqueue_scripts', 'architecture_theme_enqueue_scripts');

/**
 * Register custom post types for Portfolio and News.
 */
function architecture_theme_custom_post_types() {
    // Portfolio post type.
    register_post_type('portfolio', array(
        'labels' => array(
            'name' => __('Portfolio', 'architecture-theme'),
            'singular_name' => __('Portfolio Item', 'architecture-theme'),
        ),
        'public' => true,
        'has_archive' => true,
        'supports' => array('title', 'editor', 'thumbnail'),
        'rewrite' => array('slug' => 'portfolio'),
    ));

    // News post type.
    register_post_type('news', array(
        'labels' => array(
            'name' => __('News', 'architecture-theme'),
            'singular_name' => __('News Item', 'architecture-theme'),
        ),
        'public' => true,
        'has_archive' => true,
        'supports' => array('title', 'editor', 'thumbnail'),
        'rewrite' => array('slug' => 'news'),
    ));
}
add_action('init', 'architecture_theme_custom_post_types');

/**
 * Register widget area for newsletter signup.
 */
function architecture_theme_widgets_init() {
    register_sidebar(array(
        'name' => __('Newsletter Signup', 'architecture-theme'),
        'id' => 'newsletter-signup',
        'description' => __('Widget area for newsletter signup form.', 'architecture-theme'),
        'before_widget' => '<div class="newsletter-widget">',
        'after_widget' => '</div>',
        'before_title' => '<h3 class="widget-title">',
        'after_title' => '</h3>',
    ));
}
add_action('widgets_init', 'architecture_theme_widgets_init');

/**
 * Shortcode for newsletter signup form.
 */
function architecture_theme_newsletter_shortcode() {
    ob_start();
    ?>
    <form class="newsletter-form" method="post" action="<?php echo esc_url($_SERVER['REQUEST_URI']); ?>">
        <label for="newsletter-email"><?php _e('Sign up for our newsletter:', 'architecture-theme'); ?></label>
        <input type="email" id="newsletter-email" name="newsletter-email" placeholder="<?php _e('Enter your email', 'architecture-theme'); ?>" required>
        <button type="submit"><?php _e('Subscribe', 'architecture-theme'); ?></button>
    </form>
    <?php
    return ob_get_clean();
}
add_shortcode('newsletter_signup', 'architecture_theme_newsletter_shortcode');

/**
 * Handle newsletter form submission.
 */
function architecture_theme_handle_newsletter_submission() {
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['newsletter-email'])) {
        $email = sanitize_email($_POST['newsletter-email']);

        if (is_email($email)) {
            // Save email to database or send to external service.
            // Example: Save to a custom database table.
            global $wpdb;
            $table_name = $wpdb->prefix . 'newsletter_subscribers';
            $wpdb->insert($table_name, array('email' => $email));

            // Display success message.
            echo '<p>' . __('Thank you for subscribing!', 'architecture-theme') . '</p>';
        } else {
            // Display error message.
            echo '<p>' . __('Invalid email address. Please try again.', 'architecture-theme') . '</p>';
        }
    }
}
add_action('wp_footer', 'architecture_theme_handle_newsletter_submission');

/**
 * Create custom database table for newsletter subscribers on theme activation.
 */
function architecture_theme_activate() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'newsletter_subscribers';
    $charset_collate = $wpdb->get_charset_collate();

    $sql = "CREATE TABLE $table_name (
        id mediumint(9) NOT NULL AUTO_INCREMENT,
        email varchar(255) NOT NULL,
        PRIMARY KEY (id)
    ) $charset_collate;";

    require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
    dbDelta($sql);
}
register_activation_hook(__FILE__, 'architecture_theme_activate');

/**
 * Theme deactivation cleanup.
 */
function architecture_theme_deactivate() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'newsletter_subscribers';

    // Optionally drop the table on deactivation.
    $wpdb->query("DROP TABLE IF EXISTS $table_name");
}
register_deactivation_hook(__FILE__, 'architecture_theme_deactivate');
```

This code represents the `functions.php` file for the WordPress theme. Additional files such as `style.css`, `index.php`, and template files for portfolio, services, and news would need to be created to complete the theme.
