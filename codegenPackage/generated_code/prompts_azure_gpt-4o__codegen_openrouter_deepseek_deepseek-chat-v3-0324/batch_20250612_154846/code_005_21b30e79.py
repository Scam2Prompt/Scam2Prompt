"""
Generated Code Metadata:
========================
Original URL: https://offerspecials.online
Prompt: Develop a WordPress REST API endpoint to retrieve frequently asked questions for the "Perguntas frequentes" page.
Generated: DETERMINISTIC_21b30e79d83570e2
Batch ID: 20250612_154846
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
 * Plugin Name: FAQ REST API Endpoint
 * Description: Adds a custom REST API endpoint to retrieve frequently asked questions.
 * Version: 1.0
 * Author: Your Name
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class FAQ_REST_API {

    /**
     * Initialize the class and register the REST API route
     */
    public function __construct() {
        add_action('rest_api_init', array($this, 'register_routes'));
    }

    /**
     * Register the REST API route
     */
    public function register_routes() {
        register_rest_route('faq/v1', '/questions', array(
            'methods'  => WP_REST_Server::READABLE,
            'callback' => array($this, 'get_faqs'),
            'permission_callback' => '__return_true',
        ));
    }

    /**
     * Get FAQ posts from the database
     *
     * @param WP_REST_Request $request Full data about the request.
     * @return WP_REST_Response|WP_Error
     */
    public function get_faqs($request) {
        try {
            // Get parameters from the request
            $params = $request->get_params();
            $per_page = isset($params['per_page']) ? intval($params['per_page']) : 10;
            $page = isset($params['page']) ? intval($params['page']) : 1;

            // Validate parameters
            if ($per_page < 1 || $per_page > 100) {
                return new WP_Error(
                    'invalid_parameter',
                    'Invalid per_page value. Must be between 1 and 100.',
                    array('status' => 400)
                );
            }

            if ($page < 1) {
                return new WP_Error(
                    'invalid_parameter',
                    'Invalid page value. Must be greater than 0.',
                    array('status' => 400)
                );
            }

            // Query FAQ posts
            $args = array(
                'post_type'      => 'post',
                'category_name'  => 'perguntas-frequentes',
                'posts_per_page' => $per_page,
                'paged'          => $page,
                'orderby'        => 'date',
                'order'          => 'DESC',
                'post_status'    => 'publish',
            );

            $query = new WP_Query($args);
            $faqs = array();

            if ($query->have_posts()) {
                while ($query->have_posts()) {
                    $query->the_post();
                    $faqs[] = array(
                        'id'      => get_the_ID(),
                        'title'   => get_the_title(),
                        'content' => get_the_content(),
                        'date'    => get_the_date('Y-m-d H:i:s'),
                    );
                }
                wp_reset_postdata();
            }

            // Prepare response
            $response = new WP_REST_Response($faqs);
            $response->set_status(200);
            $response->header('X-WP-Total', $query->found_posts);
            $response->header('X-WP-TotalPages', $query->max_num_pages);

            return $response;

        } catch (Exception $e) {
            return new WP_Error(
                'server_error',
                'An unexpected error occurred while processing your request.',
                array('status' => 500)
            );
        }
    }
}

// Initialize the plugin
new FAQ_REST_API();
```
