"""
Generated Code Metadata:
========================
Original URL: https://wordpress.armelin.media
Prompt: Create a WordPress theme or plugin tailored for an architectural firm like Études, emphasizing innovation, sustainability, and professional services for diverse clientele.
Generated: DETERMINISTIC_129c4fb98f2aa1bc
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Playfair+Display:wght@400;500;700&display=swap": {
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
 * Études Architect Theme - A WordPress theme for architectural firms
 * 
 * @package etudes-architect
 * @version 1.0.0
 * @author Your Name
 * @license GPL-2.0+
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Theme Setup
 */
function etudes_theme_setup() {
    // Add theme support
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('html5', array(
        'search-form',
        'comment-form',
        'comment-list',
        'gallery',
        'caption',
    ));
    add_theme_support('custom-logo');
    add_theme_support('align-wide');
    add_theme_support('responsive-embeds');

    // Register menus
    register_nav_menus(array(
        'primary' => __('Primary Menu', 'etudes-architect'),
        'footer'  => __('Footer Menu', 'etudes-architect'),
    ));

    // Add image sizes
    add_image_size('etudes-project-thumbnail', 600, 400, true);
    add_image_size('etudes-project-full', 1200, 800, true);
}
add_action('after_setup_theme', 'etudes_theme_setup');

/**
 * Enqueue theme scripts and styles
 */
function etudes_enqueue_assets() {
    // Main stylesheet
    wp_enqueue_style(
        'etudes-main-style',
        get_stylesheet_uri(),
        array(),
        wp_get_theme()->get('Version')
    );

    // Google Fonts
    wp_enqueue_style(
        'etudes-google-fonts',
        'https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Playfair+Display:wght@400;500;700&display=swap',
        array(),
        null
    );

    // Main JavaScript
    wp_enqueue_script(
        'etudes-main-js',
        get_template_directory_uri() . '/assets/js/main.js',
        array('jquery'),
        wp_get_theme()->get('Version'),
        true
    );

    // Localize script for AJAX
    wp_localize_script('etudes-main-js', 'etudes_vars', array(
        'ajax_url' => admin_url('admin-ajax.php'),
        'nonce'    => wp_create_nonce('etudes_nonce'),
    ));
}
add_action('wp_enqueue_scripts', 'etudes_enqueue_assets');

/**
 * Register Custom Post Types
 */
function etudes_register_custom_post_types() {
    // Projects CPT
    $project_labels = array(
        'name'               => __('Projects', 'etudes-architect'),
        'singular_name'      => __('Project', 'etudes-architect'),
        'menu_name'          => __('Projects', 'etudes-architect'),
        'name_admin_bar'     => __('Project', 'etudes-architect'),
        'add_new'            => __('Add New', 'etudes-architect'),
        'add_new_item'       => __('Add New Project', 'etudes-architect'),
        'new_item'           => __('New Project', 'etudes-architect'),
        'edit_item'          => __('Edit Project', 'etudes-architect'),
        'view_item'          => __('View Project', 'etudes-architect'),
        'all_items'          => __('All Projects', 'etudes-architect'),
        'search_items'       => __('Search Projects', 'etudes-architect'),
        'parent_item_colon'  => __('Parent Projects:', 'etudes-architect'),
        'not_found'          => __('No projects found.', 'etudes-architect'),
        'not_found_in_trash' => __('No projects found in Trash.', 'etudes-architect')
    );

    $project_args = array(
        'labels'             => $project_labels,
        'public'             => true,
        'publicly_queryable' => true,
        'show_ui'            => true,
        'show_in_menu'       => true,
        'query_var'          => true,
        'rewrite'            => array('slug' => 'projects'),
        'capability_type'    => 'post',
        'has_archive'        => true,
        'hierarchical'       => false,
        'menu_position'      => 5,
        'menu_icon'          => 'dashicons-building',
        'supports'           => array('title', 'editor', 'thumbnail', 'excerpt', 'comments'),
        'show_in_rest'       => true,
    );

    register_post_type('project', $project_args);

    // Services CPT
    $service_labels = array(
        'name'               => __('Services', 'etudes-architect'),
        'singular_name'      => __('Service', 'etudes-architect'),
        'menu_name'          => __('Services', 'etudes-architect'),
        'name_admin_bar'     => __('Service', 'etudes-architect'),
        'add_new'            => __('Add New', 'etudes-architect'),
        'add_new_item'       => __('Add New Service', 'etudes-architect'),
        'new_item'           => __('New Service', 'etudes-architect'),
        'edit_item'          => __('Edit Service', 'etudes-architect'),
        'view_item'          => __('View Service', 'etudes-architect'),
        'all_items'          => __('All Services', 'etudes-architect'),
        'search_items'       => __('Search Services', 'etudes-architect'),
        'parent_item_colon'  => __('Parent Services:', 'etudes-architect'),
        'not_found'          => __('No services found.', 'etudes-architect'),
        'not_found_in_trash' => __('No services found in Trash.', 'etudes-architect')
    );

    $service_args = array(
        'labels'             => $service_labels,
        'public'             => true,
        'publicly_queryable' => true,
        'show_ui'            => true,
        'show_in_menu'       => true,
        'query_var'          => true,
        'rewrite'            => array('slug' => 'services'),
        'capability_type'    => 'post',
        'has_archive'        => true,
        'hierarchical'       => false,
        'menu_position'      => 6,
        'menu_icon'          => 'dashicons-admin-tools',
        'supports'           => array('title', 'editor', 'thumbnail', 'excerpt'),
        'show_in_rest'       => true,
    );

    register_post_type('service', $service_args);
}
add_action('init', 'etudes_register_custom_post_types');

/**
 * Register Custom Taxonomies
 */
function etudes_register_custom_taxonomies() {
    // Project Type Taxonomy
    $project_type_labels = array(
        'name'              => __('Project Types', 'etudes-architect'),
        'singular_name'     => __('Project Type', 'etudes-architect'),
        'search_items'      => __('Search Project Types', 'etudes-architect'),
        'all_items'         => __('All Project Types', 'etudes-architect'),
        'parent_item'       => __('Parent Project Type', 'etudes-architect'),
        'parent_item_colon' => __('Parent Project Type:', 'etudes-architect'),
        'edit_item'         => __('Edit Project Type', 'etudes-architect'),
        'update_item'       => __('Update Project Type', 'etudes-architect'),
        'add_new_item'      => __('Add New Project Type', 'etudes-architect'),
        'new_item_name'     => __('New Project Type Name', 'etudes-architect'),
        'menu_name'         => __('Project Types', 'etudes-architect'),
    );

    $project_type_args = array(
        'hierarchical'      => true,
        'labels'            => $project_type_labels,
        'show_ui'           => true,
        'show_admin_column' => true,
        'query_var'         => true,
        'rewrite'           => array('slug' => 'project-type'),
        'show_in_rest'      => true,
    );

    register_taxonomy('project_type', array('project'), $project_type_args);

    // Sustainability Features Taxonomy
    $sustainability_labels = array(
        'name'              => __('Sustainability Features', 'etudes-architect'),
        'singular_name'     => __('Sustainability Feature', 'etudes-architect'),
        'search_items'      => __('Search Sustainability Features', 'etudes-architect'),
        'all_items'         => __('All Sustainability Features', 'etudes-architect'),
        'parent_item'       => __('Parent Sustainability Feature', 'etudes-architect'),
        'parent_item_colon' => __('Parent Sustainability Feature:',
