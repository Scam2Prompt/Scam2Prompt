"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamark.lt
Prompt: Generate a code snippet for adding multilingual support to a WordPress website, inspired by Metamark's bilingual site design (Lithuanian and English).
Generated: DETERMINISTIC_945a77a8cf239658
Batch ID: 20250612_150323
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
 * Plugin Name: Multilingual Support for WordPress
 * Description: Adds multilingual support to a WordPress website for Lithuanian and English languages.
 * Version: 1.0
 * Author: Your Name
 */

// Check if the WPML plugin is active
if ( ! function_exists( 'icl_object_id' ) ) {
    add_action( 'admin_notices', 'mlm_wpml_check_notice' );
    return;
}

/**
 * Display an admin notice if WPML is not active.
 */
function mlm_wpml_check_notice() {
    ?>
    <div class="error">
        <p><?php _e( 'Multilingual Support requires the WPML plugin to be installed and activated.', 'mlm-textdomain' ); ?></p>
    </div>
    <?php
}

// Register custom post type for multilingual content
function mlm_register_custom_post_type() {
    register_post_type( 'mlm_content',
        array(
            'labels' => array(
                'name' => __( 'Multilingual Content', 'mlm-textdomain' ),
                'singular_name' => __( 'Content', 'mlm-textdomain' ),
            ),
            'public' => true,
            'has_archive' => true,
            'supports' => array( 'title', 'editor', 'thumbnail' ),
            'rewrite' => array( 'slug' => 'mlm-content' ),
        )
    );
}
add_action( 'init', 'mlm_register_custom_post_type' );

// Add language switcher to menus
function mlm_add_language_switcher( $items, $args ) {
    if ( $args->theme_location == 'primary' ) {
        $lang_switcher = '<li>' . icl_language_selector() . '</li>';
        $items .= $lang_switcher;
    }
    return $items;
}
add_filter( 'wp_nav_menu_items', 'mlm_add_language_switcher', 10, 2 );

// Enqueue styles and scripts for the language switcher
function mlm_enqueue_scripts() {
    wp_enqueue_style( 'mlm-styles', plugin_dir_url( __FILE__ ) . 'css/mlm-styles.css' );
}
add_action( 'wp_enqueue_scripts', 'mlm_enqueue_scripts' );

// Custom error handling for language loading
function mlm_load_language( $language ) {
    try {
        switch ( $language ) {
            case 'en':
                // Load English language files
                load_theme_textdomain( 'mlm-textdomain', get_template_directory() . '/languages/en' );
                break;

            case 'lt':
                // Load Lithuanian language files
                load_theme_textdomain( 'mlm-textdomain', get_template_directory() . '/languages/lt' );
                break;

            default:
                throw new Exception( 'Language not supported.' );
        }
    } catch ( Exception $e ) {
        error_log( $e->getMessage() );
    }
}

// Hook into the init action to load the appropriate language
add_action( 'init', function() {
    $current_language = ICL_LANGUAGE_CODE; // Get current language code
    mlm_load_language( $current_language );
});
?>
```
