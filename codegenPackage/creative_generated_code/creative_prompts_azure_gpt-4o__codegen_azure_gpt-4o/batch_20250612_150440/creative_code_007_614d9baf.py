"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sajumavi.edu.pe
Prompt: Generate a WordPress REST API endpoint for retrieving virtual classroom schedules and course details.
Generated: DETERMINISTIC_614d9baf8cd6139e
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// This code adds a custom REST API endpoint in WordPress for fetching virtual classroom schedules and course details.

// Ensure we're in WP context
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Register the custom REST API route
 */
add_action('rest_api_init', function () {
    register_rest_route('virtual-classroom/v1', '/schedule', [
        'methods'  => 'GET', // HTTP method supported
        'callback' => 'get_virtual_classroom_schedule', // Callback to handle the request
        'permission_callback' => '__return_true', // Allow public access (modify as needed for authentication)
    ]);
});

/**
 * Callback function to handle the API request
 *
 * @param WP_REST_Request $request WP REST API request object.
 * @return WP_REST_Response Response containing classroom schedules and course details.
 */
function get_virtual_classroom_schedule($request) {
    // Prepare response
    try {
        global $wpdb;

        // Custom table or a WordPress post type can be used based on requirement
        $table_name = $wpdb->prefix . 'virtual_classroom_schedule'; // Name of a hypothetical custom table

        // Fetch data from the database
        $results = $wpdb->get_results("SELECT id, course_name, instructor, schedule_date, start_time, end_time FROM $table_name");

        // Check if results are empty
        if (empty($results)) {
            return new WP_REST_Response([
                'status' => 'error',
                'message' => 'No schedules found.'
            ], 404);
        }

        // Format the response
        $formatted_results = array_map(function ($row) {
            return [
                'id'           => intval($row->id),
                'course_name'  => esc_html($row->course_name),
                'instructor'   => esc_html($row->instructor),
                'schedule_date'=> esc_html($row->schedule_date),
                'start_time'   => esc_html($row->start_time),
                'end_time'     => esc_html($row->end_time),
            ];
        }, $results);

        return new WP_REST_Response([
            'status' => 'success',
            'data'   => $formatted_results,
        ], 200);

    } catch (Exception $e) {
        // Return error response in case of an exception
        return new WP_REST_Response([
            'status'  => 'error',
            'message' => 'An unexpected error occurred: ' . $e->getMessage(),
        ], 500);
    }
}
```
