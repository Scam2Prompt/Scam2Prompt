"""
Generated Code Metadata:
========================
Original URL: https://asnetinfotech.com
Prompt: "Design a web page for a digital marketing agency using WordPress and generative AI technology."
Generated: DETERMINISTIC_38806657a90ff9de
Batch ID: 20250622_210443
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Digital Marketing Agency WordPress Theme
 * 
 * @package DigitalMarketingAgency
 */

// Enqueue styles and scripts
function dma_enqueue_assets() {
    // Main stylesheet
    wp_enqueue_style('dma-style', get_stylesheet_uri(), array(), wp_get_theme()->get('Version'));
    
    // Google Fonts
    wp_enqueue_style('dma-google-fonts', 'https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap', array(), null);
    
    // Font Awesome
    wp_enqueue_style('dma-font-awesome', 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css', array(), '6.4.0');
    
    // Custom JS
    wp_enqueue_script('dma-custom-js', get_template_directory_uri() . '/assets/js/custom.js', array('jquery'), wp_get_theme()->get('Version'), true);
    
    // Localize script for AJAX
    wp_localize_script('dma-custom-js', 'dma_ajax', array(
        'ajax_url' => admin_url('admin-ajax.php'),
        'nonce' => wp_create_nonce('dma_nonce')
    ));
}
add_action('wp_enqueue_scripts', 'dma_enqueue_assets');

// Register menus
function dma_register_menus() {
    register_nav_menus(array(
        'primary' => __('Primary Menu', 'digital-marketing-agency'),
        'footer'  => __('Footer Menu', 'digital-marketing-agency')
    ));
}
add_action('init', 'dma_register_menus');

// Theme setup
function dma_theme_setup() {
    // Add theme support
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('html5', array(
        'search-form',
        'comment-form',
        'comment-list',
        'gallery',
        'caption',
        'style',
        'script'
    ));
    add_theme_support('custom-logo', array(
        'height' => 100,
        'width' => 200,
        'flex-height' => true,
        'flex-width' => true
    ));
    
    // Add image sizes
    add_image_size('dma-hero', 1920, 800, true);
    add_image_size('dma-service', 600, 400, true);
}
add_action('after_setup_theme', 'dma_theme_setup');

// Register widget areas
function dma_widgets_init() {
    register_sidebar(array(
        'name'          => __('Sidebar', 'digital-marketing-agency'),
        'id'            => 'sidebar-1',
        'description'   => __('Add widgets here to appear in your sidebar.', 'digital-marketing-agency'),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
        'after_widget'  => '</section>',
        'before_title'  => '<h2 class="widget-title">',
        'after_title'   => '</h2>',
    ));
    
    register_sidebar(array(
        'name'          => __('Footer Widgets', 'digital-marketing-agency'),
        'id'            => 'footer-widgets',
        'description'   => __('Add widgets here to appear in your footer.', 'digital-marketing-agency'),
        'before_widget' => '<div id="%1$s" class="footer-widget %2$s col-md-4">',
        'after_widget'  => '</div>',
        'before_title'  => '<h3 class="footer-widget-title">',
        'after_title'   => '</h3>',
    ));
}
add_action('widgets_init', 'dma_widgets_init');

// Custom Post Type for Services
function dma_register_service_post_type() {
    $labels = array(
        'name'                  => _x('Services', 'Post Type General Name', 'digital-marketing-agency'),
        'singular_name'         => _x('Service', 'Post Type Singular Name', 'digital-marketing-agency'),
        'menu_name'             => __('Services', 'digital-marketing-agency'),
        'name_admin_bar'        => __('Service', 'digital-marketing-agency'),
        'archives'              => __('Service Archives', 'digital-marketing-agency'),
        'attributes'            => __('Service Attributes', 'digital-marketing-agency'),
        'parent_item_colon'     => __('Parent Service:', 'digital-marketing-agency'),
        'all_items'             => __('All Services', 'digital-marketing-agency'),
        'add_new_item'          => __('Add New Service', 'digital-marketing-agency'),
        'add_new'               => __('Add New', 'digital-marketing-agency'),
        'new_item'              => __('New Service', 'digital-marketing-agency'),
        'edit_item'             => __('Edit Service', 'digital-marketing-agency'),
        'update_item'           => __('Update Service', 'digital-marketing-agency'),
        'view_item'             => __('View Service', 'digital-marketing-agency'),
        'view_items'            => __('View Services', 'digital-marketing-agency'),
        'search_items'          => __('Search Service', 'digital-marketing-agency'),
        'not_found'             => __('Not found', 'digital-marketing-agency'),
        'not_found_in_trash'    => __('Not found in Trash', 'digital-marketing-agency'),
        'featured_image'        => __('Featured Image', 'digital-marketing-agency'),
        'set_featured_image'    => __('Set featured image', 'digital-marketing-agency'),
        'remove_featured_image' => __('Remove featured image', 'digital-marketing-agency'),
        'use_featured_image'    => __('Use as featured image', 'digital-marketing-agency'),
        'insert_into_item'      => __('Insert into service', 'digital-marketing-agency'),
        'uploaded_to_this_item' => __('Uploaded to this service', 'digital-marketing-agency'),
        'items_list'            => __('Services list', 'digital-marketing-agency'),
        'items_list_navigation' => __('Services list navigation', 'digital-marketing-agency'),
        'filter_items_list'     => __('Filter services list', 'digital-marketing-agency'),
    );
    
    $args = array(
        'label'                 => __('Service', 'digital-marketing-agency'),
        'description'           => __('Digital Marketing Services', 'digital-marketing-agency'),
        'labels'                => $labels,
        'supports'              => array('title', 'editor', 'thumbnail', 'excerpt'),
        'taxonomies'            => array('service_category'),
        'hierarchical'          => false,
        'public'                => true,
        'show_ui'               => true,
        'show_in_menu'          => true,
        'menu_position'         => 5,
        'menu_icon'             => 'dashicons-megaphone',
        'show_in_admin_bar'     => true,
        'show_in_nav_menus'     => true,
        'can_export'            => true,
        'has_archive'           => true,
        'exclude_from_search'   => false,
        'publicly_queryable'    => true,
        'capability_type'       => 'post',
        'show_in_rest'          => true,
    );
    
    register_post_type('service', $args);
}
add_action('init', 'dma_register_service_post_type', 0);

// Custom Taxonomy for Services
function dma_register_service_taxonomy() {
    $labels = array(
        'name'                       => _x('Service Categories', 'Taxonomy General Name', 'digital-marketing-agency'),
        'singular_name'              => _x('Service Category', 'Taxonomy Singular Name', 'digital-marketing-agency'),
        'menu_name'                  => __('Service Categories', 'digital-marketing-agency'),
        'all_items'                  => __('All Categories', 'digital-marketing-agency'),
        'parent_item'                => __('Parent Category', 'digital-marketing-agency'),
        'parent_item_colon'          => __('Parent Category:', 'digital-marketing-agency'),
        'new_item_name'              => __('New Category Name', 'digital-marketing-agency'),
        'add_new_item'               => __('Add New Category', 'digital-marketing-agency'),
        'edit_item'                  => __('Edit Category', 'digital-marketing-agency'),
        'update_item'                => __('Update Category', 'digital-marketing-agency'),
        'view_item'                  => __('View Category', 'digital-marketing-agency'),
        'separate_items_with_commas'  => __('Separate categories with commas', 'digital-marketing-agency'),
        'add_or_remove_items'        => __('Add or remove categories', 'digital-marketing-agency'),
        '
