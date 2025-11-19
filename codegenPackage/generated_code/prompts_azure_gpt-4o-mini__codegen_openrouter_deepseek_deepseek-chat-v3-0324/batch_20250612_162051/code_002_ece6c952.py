"""
Generated Code Metadata:
========================
Original URL: https://www.cenvirmarketingdigital.com
Prompt: Generate a code snippet that demonstrates how to use the wp-comments-post.php file to handle comment submissions in a WordPress site.
Generated: DETERMINISTIC_ece6c9527846994c
Batch ID: 20250612_162051
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
 * Handles comment submissions in WordPress via wp-comments-post.php
 * 
 * This code demonstrates how to properly handle comment submissions
 * while ensuring security and validation.
 */

// Check if the request method is POST
if ('POST' === $_SERVER['REQUEST_METHOD']) {
    // Verify nonce for security (if using in a custom form)
    // $nonce = isset($_POST['_wpnonce']) ? $_POST['_wpnonce'] : '';
    // if (!wp_verify_nonce($nonce, 'comment_nonce_action')) {
    //     wp_die('Security check failed');
    // }

    // Check if comment is coming from the correct screen
    if (!isset($_POST['comment_post_ID'])) {
        wp_die('Invalid comment submission');
    }

    // Get the post ID
    $post_id = absint($_POST['comment_post_ID']);

    // Verify the post exists and is open for comments
    $post = get_post($post_id);
    if (!$post || 'open' !== $post->comment_status) {
        wp_die('Comments are closed for this post');
    }

    // Get the current user (if logged in)
    $user = wp_get_current_user();
    $user_identity = $user->exists() ? $user->display_name : '';

    // Prepare comment data
    $comment_data = array(
        'comment_post_ID'      => $post_id,
        'comment_author'       => isset($_POST['author']) ? trim(strip_tags($_POST['author'])) : '',
        'comment_author_email' => isset($_POST['email']) ? trim($_POST['email']) : '',
        'comment_author_url'   => isset($_POST['url']) ? trim($_POST['url']) : '',
        'comment_content'      => isset($_POST['comment']) ? trim($_POST['comment']) : '',
        'comment_type'         => '',
        'comment_parent'       => isset($_POST['comment_parent']) ? absint($_POST['comment_parent']) : 0,
        'user_id'              => $user->ID,
    );

    // Validate the comment data
    if ('' === $comment_data['comment_content']) {
        wp_die('Error: Please type a comment');
    }

    // Check if user is logged in
    if ($user->exists()) {
        $comment_data['comment_author'] = $user->display_name;
        $comment_data['comment_author_email'] = $user->user_email;
        $comment_data['comment_author_url'] = $user->user_url;
    } else {
        // Validate guest comment fields
        if (get_option('require_name_email') && !$user->exists()) {
            if ('' === $comment_data['comment_author_email'] || '' === $comment_data['comment_author']) {
                wp_die('Error: Please fill the required fields (name, email)');
            }
            if (!is_email($comment_data['comment_author_email'])) {
                wp_die('Error: Please enter a valid email address');
            }
        }
    }

    // Insert the comment
    $comment_id = wp_new_comment(wp_slash($comment_data), true);

    // Handle comment insertion errors
    if (is_wp_error($comment_id)) {
        wp_die($comment_id->get_error_message());
    }

    // Set cookies if user is not logged in
    if (!$user->exists()) {
        do_action('set_comment_cookies', get_comment($comment_id), $user);
    }

    // Redirect back to the post
    $redirect_to = get_permalink($post_id) . '#comment-' . $comment_id;
    wp_safe_redirect($redirect_to);
    exit;
} else {
    // If not a POST request, redirect to homepage
    wp_safe_redirect(home_url());
    exit;
}
```
