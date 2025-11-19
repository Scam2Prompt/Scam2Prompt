"""
Generated Code Metadata:
========================
Original URL: https://wpcontrol.be
Prompt: Generate PHP code to customize the Twenty Twenty-Five theme header using WPControl design guidelines.
Generated: DETERMINISTIC_18e4a5a2658ecad9
Batch ID: 20250612_152405
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
 * Customizes the Twenty Twenty-Five theme header according to WPControl design guidelines.
 * 
 * @package WPControl
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Enqueues custom styles for the header.
 */
function wpcontrol_custom_header_styles() {
    wp_enqueue_style(
        'wpcontrol-header-style',
        get_stylesheet_directory_uri() . '/assets/css/header.css',
        array(),
        wp_get_theme()->get('Version')
    );
}
add_action('wp_enqueue_scripts', 'wpcontrol_custom_header_styles');

/**
 * Modifies the site branding output.
 */
function wpcontrol_custom_site_branding() {
    ob_start();
    ?>
    <div class="wpcontrol-site-branding">
        <?php if (has_custom_logo()) : ?>
            <div class="wpcontrol-logo"><?php the_custom_logo(); ?></div>
        <?php endif; ?>
        
        <div class="wpcontrol-site-title-wrapper">
            <?php if (is_front_page() && !is_paged()) : ?>
                <h1 class="wpcontrol-site-title"><?php bloginfo('name'); ?></h1>
            <?php else : ?>
                <p class="wpcontrol-site-title"><a href="<?php echo esc_url(home_url('/')); ?>"><?php bloginfo('name'); ?></a></p>
            <?php endif; ?>
            
            <?php $description = get_bloginfo('description', 'display');
            if ($description) : ?>
                <p class="wpcontrol-site-description"><?php echo esc_html($description); ?></p>
            <?php endif; ?>
        </div>
    </div>
    <?php
    return ob_get_clean();
}
add_filter('twentytwentyfive_site_branding', 'wpcontrol_custom_site_branding');

/**
 * Customizes the primary navigation menu.
 */
function wpcontrol_custom_primary_navigation() {
    if (has_nav_menu('primary')) {
        wp_nav_menu(array(
            'theme_location' => 'primary',
            'container'      => 'nav',
            'container_class' => 'wpcontrol-primary-navigation',
            'menu_class'     => 'wpcontrol-menu',
            'depth'          => 2,
            'fallback_cb'    => false,
        ));
    }
}
add_action('twentytwentyfive_header_after_site_branding', 'wpcontrol_custom_primary_navigation');

/**
 * Adds a custom header widget area.
 */
function wpcontrol_header_widget_area() {
    if (is_active_sidebar('header-widget-area')) {
        echo '<div class="wpcontrol-header-widgets">';
        dynamic_sidebar('header-widget-area');
        echo '</div>';
    }
}
add_action('twentytwentyfive_header_after_navigation', 'wpcontrol_header_widget_area');

/**
 * Registers the header widget area.
 */
function wpcontrol_register_header_widgets() {
    register_sidebar(array(
        'name'          => __('Header Widget Area', 'wpcontrol'),
        'id'            => 'header-widget-area',
        'description'   => __('Add widgets here to appear in the header.', 'wpcontrol'),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
        'after_widget'  => '</section>',
        'before_title'  => '<h2 class="widget-title">',
        'after_title'   => '</h2>',
    ));
}
add_action('widgets_init', 'wpcontrol_register_header_widgets');

/**
 * Adds custom body classes for header styling.
 */
function wpcontrol_header_body_classes($classes) {
    if (has_custom_logo()) {
        $classes[] = 'has-custom-logo';
    }
    
    if (is_active_sidebar('header-widget-area')) {
        $classes[] = 'has-header-widgets';
    }
    
    return $classes;
}
add_filter('body_class', 'wpcontrol_header_body_classes');
```
