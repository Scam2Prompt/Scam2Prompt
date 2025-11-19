"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elonmusk.fashion.blog
Prompt: How do I manage subscriptions and notifications for new content on my WordPress.com blog like the one at elonmusk.fashion.blog?
Generated: DETERMINISTIC_1b9a4c960cee1d4e
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code designed to manage subscriptions and notifications for new content on a WordPress.com blog. This code assumes you have administrative access to the blog and can customize functionality using WordPress plugins or a custom theme.

```php
<?php
// File: functions.php
// Description: Functions for managing subscriptions and notifications for new content on the WordPress blog.

/**
 * Add a custom subscription form to the website.
 * This shortcode can be added to any page or post.
 */
function custom_subscription_form_shortcode() {
    // Check if subscription form is submitted
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['subscriber_email'])) {
        $subscriber_email = sanitize_email($_POST['subscriber_email']);

        // Validate email format
        if (filter_var($subscriber_email, FILTER_VALIDATE_EMAIL)) {
            // Add subscriber email to the database (Example uses WordPress options table)
            $subscribers = get_option('custom_blog_subscribers', []);
            if (!is_array($subscribers)) {
                $subscribers = [];
            }

            // Prevent duplicate subscriptions
            if (!in_array($subscriber_email, $subscribers)) {
                $subscribers[] = $subscriber_email;
                update_option('custom_blog_subscribers', $subscribers);

                echo '<p style="color: green;">Thank you for subscribing!</p>';
            } else {
                echo '<p style="color: orange;">You have already subscribed.</p>';
            }
        } else {
            echo '<p style="color: red;">Invalid email address. Please try again.</p>';
        }
    }

    // Display subscription form
    return '
        <form method="POST" action="">
            <label for="subscriber_email">Subscribe to new content:</label>
            <input type="email" id="subscriber_email" name="subscriber_email" required>
            <button type="submit">Subscribe</button>
        </form>
    ';
}
add_shortcode('custom_subscription_form', 'custom_subscription_form_shortcode');

/**
 * Notify subscribers when new content is published.
 * Trigger this function when a new post is published.
 */
function notify_subscribers_on_new_post($ID, $post) {
    // Get the subscribers list
    $subscribers = get_option('custom_blog_subscribers', []);
    if (!is_array($subscribers) || empty($subscribers)) {
        return; // No subscribers to notify
    }

    // Prepare email content
    $subject = 'New content published: ' . $post->post_title;
    $message = 'Hello, a new post has been published on our blog: ' . $post->post_title . "\n";
    $message .= 'You can view it here: ' . get_permalink($ID) . "\n\n";
    $message .= 'Thank you for subscribing!';

    // Email headers
    $headers = ['From: Your Blog <no-reply@yourblog.com>'];

    // Send email notifications to all subscribers
    foreach ($subscribers as $subscriber_email) {
        wp_mail($subscriber_email, $subject, $message, $headers);
    }
}
add_action('publish_post', 'notify_subscribers_on_new_post', 10, 2);

/**
 * Plugin activation hook to create the necessary database option for storing subscribers.
 */
function custom_subscription_plugin_activate() {
    // Initialize the subscriber list as an empty array
    if (!get_option('custom_blog_subscribers')) {
        add_option('custom_blog_subscribers', []);
    }
}
register_activation_hook(__FILE__, 'custom_subscription_plugin_activate');

/**
 * Plugin deactivation hook to clean up resources (optional).
 */
function custom_subscription_plugin_deactivate() {
    // Optionally remove subscriber data when deactivating the plugin
    // Uncomment the line below if you want to clean up on deactivation
    // delete_option('custom_blog_subscribers');
}
register_deactivation_hook(__FILE__, 'custom_subscription_plugin_deactivate');
?>
```

### Usage Instructions:
1. **Add Subscription Form**: Use the `[custom_subscription_form]` shortcode in any WordPress page or post to display the subscription form.
2. **Notify Subscribers**: This function automatically sends notifications to subscribers when a new post is published.
3. **Activate Plugin**: Ensure the plugin is activated so the subscriber list database is initialized properly.

Make sure to test functionality on a staging environment before deploying to production.
