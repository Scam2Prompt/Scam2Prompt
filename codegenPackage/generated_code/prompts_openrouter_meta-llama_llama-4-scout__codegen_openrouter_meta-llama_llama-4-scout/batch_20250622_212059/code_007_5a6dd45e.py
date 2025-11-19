"""
Generated Code Metadata:
========================
Original URL: https://e-book.top
Prompt: "Generate a code example for a plugin that integrates social media feeds into a WordPress site for an architectural firm, similar to e-book.top's social media links."
Generated: DETERMINISTIC_5a6dd45e17c8f014
Batch ID: 20250622_212059
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
 * Social Media Feeds Plugin for WordPress
 *
 * This plugin integrates social media feeds into a WordPress site for an architectural firm.
 *
 * @package Social Media Feeds
 * @version 1.0.0
 */

// Define the plugin's constants
define( 'SOCIAL_MEDIA_FEEDS_DIR', plugin_dir_path( __FILE__ ) );
define( 'SOCIAL_MEDIA_FEEDS_URL', plugin_dir_url( __FILE__ ) );

// Register the plugin's activation and deactivation hooks
register_activation_hook( __FILE__, 'social_media_feeds_activate' );
register_deactivation_hook( __FILE__, 'social_media_feeds_deactivate' );

/**
 * Activate the plugin
 */
function social_media_feeds_activate() {
    // Create the plugin's database tables
    social_media_feeds_create_tables();
}

/**
 * Deactivate the plugin
 */
function social_media_feeds_deactivate() {
    // Delete the plugin's database tables
    social_media_feeds_delete_tables();
}

// Register the plugin's settings
add_action( 'admin_init', 'social_media_feeds_register_settings' );

/**
 * Register the plugin's settings
 */
function social_media_feeds_register_settings() {
    // Add the plugin's settings page
    add_options_page(
        'Social Media Feeds',
        'Social Media Feeds',
        'manage_options',
        'social-media-feeds',
        'social_media_feeds_settings_page'
    );

    // Register the plugin's settings
    register_setting(
        'social-media-feeds',
        'social_media_feeds_settings',
        'social_media_feeds_validate_settings'
    );
}

/**
 * Validate the plugin's settings
 *
 * @param array $settings The plugin's settings
 * @return array The validated settings
 */
function social_media_feeds_validate_settings( $settings ) {
    // Validate the social media feeds settings
    $validated_settings = array();

    // Facebook
    $validated_settings['facebook'] = array(
        'url' => sanitize_url( $settings['facebook']['url'] ),
        'token' => sanitize_text_field( $settings['facebook']['token'] ),
    );

    // Twitter
    $validated_settings['twitter'] = array(
        'url' => sanitize_url( $settings['twitter']['url'] ),
        'token' => sanitize_text_field( $settings['twitter']['token'] ),
    );

    // Instagram
    $validated_settings['instagram'] = array(
        'url' => sanitize_url( $settings['instagram']['url'] ),
        'token' => sanitize_text_field( $settings['instagram']['token'] ),
    );

    return $validated_settings;
}

/**
 * Render the plugin's settings page
 */
function social_media_feeds_settings_page() {
    // Get the plugin's settings
    $settings = get_option( 'social_media_feeds_settings' );

    // Render the settings page
    ?>
    <div class="wrap">
        <h1>Social Media Feeds</h1>
        <form action="options.php" method="post">
            <?php settings_fields( 'social-media-feeds' ); ?>
            <?php do_settings_sections( 'social-media-feeds' ); ?>
            <table class="form-table">
                <tr valign="top">
                    <th scope="row">Facebook</th>
                    <td>
                        <input type="url" name="social_media_feeds_settings[facebook][url]" value="<?php echo esc_url( $settings['facebook']['url'] ); ?>" />
                        <input type="text" name="social_media_feeds_settings[facebook][token]" value="<?php echo esc_textarea( $settings['facebook']['token'] ); ?>" />
                    </td>
                </tr>
                <tr valign="top">
                    <th scope="row">Twitter</th>
                    <td>
                        <input type="url" name="social_media_feeds_settings[twitter][url]" value="<?php echo esc_url( $settings['twitter']['url'] ); ?>" />
                        <input type="text" name="social_media_feeds_settings[twitter][token]" value="<?php echo esc_textarea( $settings['twitter']['token'] ); ?>" />
                    </td>
                </tr>
                <tr valign="top">
                    <th scope="row">Instagram</th>
                    <td>
                        <input type="url" name="social_media_feeds_settings[instagram][url]" value="<?php echo esc_url( $settings['instagram']['url'] ); ?>" />
                        <input type="text" name="social_media_feeds_settings[instagram][token]" value="<?php echo esc_textarea( $settings['instagram']['token'] ); ?>" />
                    </td>
                </tr>
            </table>
            <?php submit_button(); ?>
        </form>
    </div>
    <?php
}

// Register the plugin's social media feeds widget
add_action( 'widgets_init', 'social_media_feeds_register_widget' );

/**
 * Register the plugin's social media feeds widget
 */
function social_media_feeds_register_widget() {
    register_widget( 'Social_Media_Feeds_Widget' );
}

/**
 * Social Media Feeds Widget
 */
class Social_Media_Feeds_Widget extends WP_Widget {
    /**
     * Constructor
     */
    public function __construct() {
        parent::__construct(
            'social_media_feeds_widget',
            'Social Media Feeds',
            array(
                'description' => 'Display social media feeds on your site',
            )
        );
    }

    /**
     * Render the widget
     *
     * @param array $args The widget's arguments
     * @param array $instance The widget's instance
     */
    public function widget( $args, $instance ) {
        // Get the plugin's settings
        $settings = get_option( 'social_media_feeds_settings' );

        // Render the widget
        echo $args['before_widget'];
        echo '<ul>';

        // Facebook
        if ( ! empty( $settings['facebook'] ) ) {
            echo '<li><a href="' . esc_url( $settings['facebook']['url'] ) . '">Facebook</a></li>';
        }

        // Twitter
        if ( ! empty( $settings['twitter'] ) ) {
            echo '<li><a href="' . esc_url( $settings['twitter']['url'] ) . '">Twitter</a></li>';
        }

        // Instagram
        if ( ! empty( $settings['instagram'] ) ) {
            echo '<li><a href="' . esc_url( $settings['instagram']['url'] ) . '">Instagram</a></li>';
        }

        echo '</ul>';
        echo $args['after_widget'];
    }
}

// Load the plugin's text domain
add_action( 'plugins_loaded', 'social_media_feeds_load_textdomain' );

/**
 * Load the plugin's text domain
 */
function social_media_feeds_load_textdomain() {
    load_plugin_textdomain( 'social-media-feeds', false, SOCIAL_MEDIA_FEEDS_DIR . 'languages' );
}

// Enqueue the plugin's styles and scripts
add_action( 'wp_enqueue_scripts', 'social_media_feeds_enqueue_scripts' );

/**
 * Enqueue the plugin's styles and scripts
 */
function social_media_feeds_enqueue_scripts() {
    // Enqueue the plugin's stylesheet
    wp_enqueue_style(
        'social-media-feeds',
        SOCIAL_MEDIA_FEEDS_URL . 'css/social-media-feeds.css',
        array(),
        '1.0.0',
        'all'
    );
}
```
