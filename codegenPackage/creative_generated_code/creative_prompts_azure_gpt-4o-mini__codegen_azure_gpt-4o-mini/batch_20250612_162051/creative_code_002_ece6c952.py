"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cenvirmarketingdigital.com
Prompt: Generate a code snippet that demonstrates how to use the wp-comments-post.php file to handle comment submissions in a WordPress site.
Generated: DETERMINISTIC_ece6c9527846994c
Batch ID: 20250612_162051
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
 * This file handles comment submissions in a WordPress site.
 * It uses wp-comments-post.php to process the comment form.
 * The code snippet below demonstrates how to prepare and submit a comment.
 */

// Check if the comment form has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Include WordPress functions if this is a standalone file
    require_once('wp-load.php');

    // Sanitize and validate input data
    $comment_post_ID = isset($_POST['comment_post_ID']) ? intval($_POST['comment_post_ID']) : 0;
    $comment_author = isset($_POST['author']) ? sanitize_text_field($_POST['author']) : '';
    $comment_author_email = isset($_POST['email']) ? sanitize_email($_POST['email']) : '';
    $comment_content = isset($_POST['comment']) ? wp_kses_post($_POST['comment']) : '';

    // Check for required fields
    if (empty($comment_post_ID) || empty($comment_author) || empty($comment_author_email) || empty($comment_content)) {
        // Return error response for missing fields
        wp_send_json_error('All fields are required.');
    }

    // Prepare the comment data
    $comment_data = array(
        'comment_post_ID' => $comment_post_ID,
        'comment_author' => $comment_author,
        'comment_author_email' => $comment_author_email,
        'comment_content' => $comment_content,
        'comment_type' => '', // Use '' for regular comments
        'comment_parent' => 0, // Use 0 for top-level comments
        'user_id' => get_current_user_id(), // Only if the user is logged in
        'comment_agent' => $_SERVER['HTTP_USER_AGENT'], // Optional user agent
        'comment_date' => current_time('mysql'), // Current date
        'comment_approved' => 1 // Set to 1 to approve the comment by default
    );

    // Insert the comment into the database
    $comment_id = wp_insert_comment($comment_data);

    // Check for errors during insertion
    if (is_wp_error($comment_id)) {
        // Return error response with error message
        wp_send_json_error($comment_id->get_error_message());
    } else {
        // Return success response with comment ID
        wp_send_json_success('Comment submitted successfully.', array('comment_id' => $comment_id));
    }
}
?>
```
