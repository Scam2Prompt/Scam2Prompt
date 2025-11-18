"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meezaninteriorsolutions.com
Prompt: Create a WordPress plugin to manage and display a portfolio of completed projects, including details like project name, year, and awards received, inspired by Meezan Interior Solutions' "Recent Award Winning Projects."
Generated: DETERMINISTIC_2364729ffc8ac064
Batch ID: 20250612_154226
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
 * Plugin Name: Portfolio Manager Plugin
 * Description: A WordPress plugin to manage and display a portfolio of completed projects with details like project name, year, and awards received.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

// Create Custom Post Type for Portfolio Projects
function portfolio_manager_register_post_type() {
    $labels = array(
        'name'               => __('Projects', 'portfolio-manager'),
        'singular_name'      => __('Project', 'portfolio-manager'),
        'menu_name'          => __('Portfolio Manager', 'portfolio-manager'),
        'add_new'            => __('Add New Project', 'portfolio-manager'),
        'add_new_item'       => __('Add New Project', 'portfolio-manager'),
        'edit_item'          => __('Edit Project', 'portfolio-manager'),
        'new_item'           => __('New Project', 'portfolio-manager'),
        'view_item'          => __('View Project', 'portfolio-manager'),
        'search_items'       => __('Search Projects', 'portfolio-manager'),
        'not_found'          => __('No projects found', 'portfolio-manager'),
        'not_found_in_trash' => __('No projects found in Trash', 'portfolio-manager'),
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'has_archive'        => true,
        'rewrite'            => array('slug' => 'projects'),
        'supports'           => array('title', 'editor', 'thumbnail'),
        'show_in_rest'       => true,
        'menu_icon'          => 'dashicons-awards',
    );

    register_post_type('portfolio_project', $args);
}
add_action('init', 'portfolio_manager_register_post_type');

// Register Custom Meta Boxes
function portfolio_manager_meta_boxes() {
    add_meta_box(
        'portfolio_project_details',
        __('Project Details', 'portfolio-manager'),
        'portfolio_manager_meta_box_callback',
        'portfolio_project',
        'normal',
        'high'
    );
}
add_action('add_meta_boxes', 'portfolio_manager_meta_boxes');

// Meta Box Callback
function portfolio_manager_meta_box_callback($post) {
    // Retrieve existing values
    $project_year = get_post_meta($post->ID, '_project_year', true);
    $project_awards = get_post_meta($post->ID, '_project_awards', true);

    wp_nonce_field('portfolio_manager_save_meta_box', 'portfolio_manager_meta_box_nonce');

    ?>
    <p>
        <label for="project_year"><?php _e('Year Completed:', 'portfolio-manager'); ?></label>
        <input type="number" id="project_year" name="project_year" value="<?php echo esc_attr($project_year); ?>" />
    </p>
    <p>
        <label for="project_awards"><?php _e('Awards Received:', 'portfolio-manager'); ?></label>
        <input type="text" id="project_awards" name="project_awards" value="<?php echo esc_attr($project_awards); ?>" />
    </p>
    <?php
}

// Save Meta Box Data
function portfolio_manager_save_meta_box($post_id) {
    // Check nonce
    if (!isset($_POST['portfolio_manager_meta_box_nonce']) || !wp_verify_nonce($_POST['portfolio_manager_meta_box_nonce'], 'portfolio_manager_save_meta_box')) {
        return;
    }

    // Check autosave
    if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) {
        return;
    }

    // Check user permissions
    if (!current_user_can('edit_post', $post_id)) {
        return;
    }

    // Save Year Completed
    if (isset($_POST['project_year'])) {
        update_post_meta($post_id, '_project_year', sanitize_text_field($_POST['project_year']));
    }

    // Save Awards Received
    if (isset($_POST['project_awards'])) {
        update_post_meta($post_id, '_project_awards', sanitize_text_field($_POST['project_awards']));
    }
}
add_action('save_post', 'portfolio_manager_save_meta_box');

// Shortcode to Display Projects
function portfolio_manager_shortcode($atts) {
    $atts = shortcode_atts(array(
        'limit' => 5, // Default limit
    ), $atts, 'portfolio_projects');

    $args = array(
        'post_type'      => 'portfolio_project',
        'posts_per_page' => intval($atts['limit']),
    );

    $query = new WP_Query($args);

    ob_start();

    if ($query->have_posts()) {
        echo '<div class="portfolio-projects">';
        while ($query->have_posts()) {
            $query->the_post();

            $project_year = get_post_meta(get_the_ID(), '_project_year', true);
            $project_awards = get_post_meta(get_the_ID(), '_project_awards', true);

            ?>
            <div class="portfolio-project">
                <h2><?php the_title(); ?></h2>
                <p><?php the_content(); ?></p>
                <p><strong><?php _e('Year Completed:', 'portfolio-manager'); ?></strong> <?php echo esc_html($project_year); ?></p>
                <p><strong><?php _e('Awards Received:', 'portfolio-manager'); ?></strong> <?php echo esc_html($project_awards); ?></p>
            </div>
            <?php
        }
        echo '</div>';
    } else {
        _e('No projects found.', 'portfolio-manager');
    }

    wp_reset_postdata();

    return ob_get_clean();
}
add_shortcode('portfolio_projects', 'portfolio_manager_shortcode');

// Enqueue Styles
function portfolio_manager_enqueue_styles() {
    wp_enqueue_style('portfolio-manager-styles', plugins_url('style.css', __FILE__));
}
add_action('wp_enqueue_scripts', 'portfolio_manager_enqueue_styles');
```

Note: For production use, ensure you create a separate `style.css` file for custom styling. This plugin meets the requirements for managing and displaying portfolio projects. It includes error handling, clean code, and follows WordPress coding standards.
