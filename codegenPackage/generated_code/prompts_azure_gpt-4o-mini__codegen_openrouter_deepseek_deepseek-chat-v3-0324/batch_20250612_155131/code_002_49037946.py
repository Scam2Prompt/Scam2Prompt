"""
Generated Code Metadata:
========================
Original URL: https://sayacosmetics.com
Prompt: Write a function in PHP that modifies the default WordPress post to include a custom message for new users, inspired by the content on Saya Cosmetics.
Generated: DETERMINISTIC_490379463fa6887b
Batch ID: 20250612_155131
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
 * Adds a custom welcome message to WordPress posts for new users.
 * Inspired by Saya Cosmetics' content style.
 *
 * @param string $content The original post content.
 * @return string Modified content with welcome message.
 */
function saya_custom_welcome_message($content) {
    // Check if user is logged in and is a new user (registered within last 30 days)
    if (is_user_logged_in()) {
        $user_id = get_current_user_id();
        $user_data = get_userdata($user_id);
        $registered_date = $user_data->user_registered;
        $current_date = current_time('mysql');
        
        $days_since_registration = round((strtotime($current_date) - strtotime($registered_date)) / (60 * 60 * 24));
        
        if ($days_since_registration <= 30) {
            $welcome_message = '<div class="saya-welcome-message" style="background-color: #f8f3f0; padding: 20px; margin: 20px 0; border-radius: 5px; border-left: 4px solid #d4a5a5;">';
            $welcome_message .= '<h3 style="color: #8b5a5a; margin-top: 0;">Welcome to Our Community!</h3>';
            $welcome_message .= '<p>Thank you for joining us! As a new member, we\'d love to share our passion for natural beauty and self-care, inspired by Saya Cosmetics\' philosophy.</p>';
            $welcome_message .= '<p>Explore our content and discover tips for radiant skin and holistic wellness. Don\'t hesitate to engage with our community!</p>';
            $welcome_message .= '</div>';
            
            // Prepend the welcome message to the content
            $content = $welcome_message . $content;
        }
    }
    
    return $content;
}

// Hook the function to the_content filter with appropriate priority
add_filter('the_content', 'saya_custom_welcome_message', 10);
```
