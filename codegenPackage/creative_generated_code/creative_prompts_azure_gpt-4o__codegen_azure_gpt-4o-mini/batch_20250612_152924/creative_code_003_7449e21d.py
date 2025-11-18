"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asnetinfotech.com
Prompt: Create a WordPress plugin for managing client portfolios, inspired by the portfolio management features highlighted on Asnet Infotech's website.
Generated: DETERMINISTIC_7449e21d724265d2
Batch ID: 20250612_152924
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
 * Plugin Name: Client Portfolio Manager
 * Description: A WordPress plugin for managing client portfolios with features inspired by Asnet Infotech.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPL2
 */

// Prevent direct access to the file
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Class ClientPortfolioManager
 * Handles the creation and management of client portfolios.
 */
class ClientPortfolioManager {

    public function __construct() {
        // Hook to initialize the plugin
        add_action('init', [$this, 'create_portfolio_post_type']);
        add_action('add_meta_boxes', [$this, 'add_portfolio_meta_boxes']);
        add_action('save_post', [$this, 'save_portfolio_meta'], 10, 2);
        add_shortcode('client_portfolio', [$this, 'render_portfolio_shortcode']);
    }

    /**
     * Registers the custom post type for portfolios.
     */
    public function create_portfolio_post_type() {
        $labels = [
            'name' => __('Portfolios', 'textdomain'),
            'singular_name' => __('Portfolio', 'textdomain'),
        ];

        $args = [
            'label' => __('Portfolios', 'textdomain'),
            'labels' => $labels,
            'public' => true,
            'has_archive' => true,
            'supports' => ['title', 'editor', 'thumbnail'],
            'rewrite' => ['slug' => 'portfolios'],
        ];

        register_post_type('portfolio', $args);
    }

    /**
     * Adds meta boxes for the portfolio post type.
     */
    public function add_portfolio_meta_boxes() {
        add_meta_box('portfolio_details', __('Portfolio Details', 'textdomain'), [$this, 'render_portfolio_meta_box'], 'portfolio', 'normal', 'high');
    }

    /**
     * Renders the meta box for portfolio details.
     * 
     * @param WP_Post $post The current post object.
     */
    public function render_portfolio_meta_box($post) {
        // Security nonce for saving data
        wp_nonce_field(basename(__FILE__), 'portfolio_nonce');

        // Retrieve current meta values
        $client_name = get_post_meta($post->ID, '_client_name', true);
        $project_link = get_post_meta($post->ID, '_project_link', true);

        // Render form fields
        echo '<label for="client_name">' . __('Client Name', 'textdomain') . '</label>';
        echo '<input type="text" id="client_name" name="client_name" value="' . esc_attr($client_name) . '" />';
        
        echo '<label for="project_link">' . __('Project Link', 'textdomain') . '</label>';
        echo '<input type="url" id="project_link" name="project_link" value="' . esc_url($project_link) . '" />';
    }

    /**
     * Saves the portfolio meta data.
     * 
     * @param int $post_id The ID of the post.
     * @param WP_Post $post The post object.
     */
    public function save_portfolio_meta($post_id, $post) {
        // Verify nonce
        if (!isset($_POST['portfolio_nonce']) || !wp_verify_nonce($_POST['portfolio_nonce'], basename(__FILE__))) {
            return;
        }

        // Check the user permissions
        if (!current_user_can('edit_post', $post_id)) {
            return;
        }

        // Save client name
        if (isset($_POST['client_name'])) {
            update_post_meta($post_id, '_client_name', sanitize_text_field($_POST['client_name']));
        }

        // Save project link
        if (isset($_POST['project_link'])) {
            update_post_meta($post_id, '_project_link', esc_url_raw($_POST['project_link']));
        }
    }

    /**
     * Renders the client portfolio shortcode.
     * 
     * @param array $atts Shortcode attributes.
     * @return string Rendered output.
     */
    public function render_portfolio_shortcode($atts) {
        $args = [
            'post_type' => 'portfolio',
            'posts_per_page' => -1,
        ];

        $query = new WP_Query($args);
        $output = '<div class="client-portfolios">';

        // Loop through the portfolios
        if ($query->have_posts()) {
            while ($query->have_posts()) {
                $query->the_post();
                
                $client_name = get_post_meta(get_the_ID(), '_client_name', true);
                $project_link = get_post_meta(get_the_ID(), '_project_link', true);
                
                $output .= '<div class="portfolio-item">';
                $output .= '<h2>' . get_the_title() . '</h2>';
                $output .= '<p><strong>Client:</strong> ' . esc_html($client_name) . '</p>';
                $output .= '<p><strong>Project Link:</strong> <a href="' . esc_url($project_link) . '" target="_blank">' . esc_url($project_link) . '</a></p>';
                $output .= get_the_post_thumbnail(get_the_ID(), 'thumbnail');
                $output .= '</div>';
            }
        } else {
            $output .= '<p>' . __('No portfolios found.', 'textdomain') . '</p>';
        }

        wp_reset_postdata();
        $output .= '</div>';

        return $output;
    }
}

// Initialize the plugin
new ClientPortfolioManager();
```
