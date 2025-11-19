"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vebtec.com
Prompt: Generate a code snippet for a WordPress plugin that allows users to submit book recommendations on a blog.
Generated: DETERMINISTIC_14d2b3eb47d06d20
Batch ID: 20250612_163442
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
 * Plugin Name: Book Recommendation Plugin
 * Description: A simple plugin that allows users to submit book recommendations.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

// Prevent direct access
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Create a custom table for storing book recommendations
 */
function brp_create_table() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'book_recommendations';

    // SQL to create the table
    $sql = "CREATE TABLE $table_name (
        id mediumint(9) NOT NULL AUTO_INCREMENT,
        book_title tinytext NOT NULL,
        author tinytext NOT NULL,
        user_email varchar(100) NOT NULL,
        created_at datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
        PRIMARY KEY  (id)
    );";

    // Include the required files to safely execute SQL
    require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
    dbDelta($sql);
}

// Activate the plugin and create the table
register_activation_hook(__FILE__, 'brp_create_table');

/**
 * Enqueue scripts and styles
 */
function brp_enqueue_scripts() {
    wp_enqueue_style('brp-styles', plugins_url('style.css', __FILE__));
}
add_action('wp_enqueue_scripts', 'brp_enqueue_scripts');

/**
 * Register the shortcode to display the recommendation form
 */
function brp_recommendation_form() {
    ob_start(); ?>
    <form id="book-recommendation-form" method="post">
        <label for="book_title">Book Title:</label>
        <input type="text" name="book_title" required>
        
        <label for="author">Author:</label>
        <input type="text" name="author" required>
        
        <label for="user_email">Your Email:</label>
        <input type="email" name="user_email" required>
        
        <input type="submit" name="submit_recommendation" value="Submit Recommendation">
    </form>
    <?php
    return ob_get_clean();
}
add_shortcode('book_recommendation_form', 'brp_recommendation_form');

/**
 * Handle form submission and save recommendations
 */
function brp_handle_form_submission() {
    if (isset($_POST['submit_recommendation'])) {
        global $wpdb;
        $table_name = $wpdb->prefix . 'book_recommendations';

        // Sanitize user input
        $book_title = sanitize_text_field($_POST['book_title']);
        $author = sanitize_text_field($_POST['author']);
        $user_email = sanitize_email($_POST['user_email']);

        // Prepare data for insertion
        $data = array(
            'book_title' => $book_title,
            'author' => $author,
            'user_email' => $user_email
        );

        // Insert data into the database
        $result = $wpdb->insert($table_name, $data);

        // Check for errors in the insertion
        if ($result === false) {
            // Log the error for debugging
            error_log('Error inserting book recommendation: ' . $wpdb->last_error);
            echo '<p>There was an error submitting your recommendation. Please try again.</p>';
        } else {
            echo '<p>Thank you for your recommendation!</p>';
        }
    }
}
add_action('wp', 'brp_handle_form_submission');
```

Make sure to create a `style.css` file in the plugin directory to style the form as needed.
