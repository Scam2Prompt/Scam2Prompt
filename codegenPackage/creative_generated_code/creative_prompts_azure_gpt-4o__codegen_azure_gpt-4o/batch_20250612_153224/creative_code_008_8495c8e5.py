"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rupakparajuli.com.np
Prompt: Suggest a method to integrate social media sharing buttons for blog posts on a WordPress site using a plugin or custom code.
Generated: DETERMINISTIC_8495c8e5e7cbb402
Batch ID: 20250612_153224
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://twitter.com/intent/tweet?url=": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.facebook.com/sharer/sharer.php?u=": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.linkedin.com/sharing/share-offsite/?url=": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.facebook.com/sharer/sharer.php?u=' . $url . ": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.linkedin.com/sharing/share-offsite/?url=' . $url . ": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://twitter.com/intent/tweet?url=' . $url . '&text=' . $title . ": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/*
Plugin Name: Social Media Sharing Buttons
Description: Adds social media sharing buttons to blog posts.
Version: 1.0
Author: Your Name
License: GPL2
*/

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

// Enqueue necessary styles and scripts
function smsb_enqueue_scripts() {
    // Add CSS for styling buttons (optional, customize as needed)
    wp_enqueue_style('smsb-style', plugins_url('css/smsb-style.css', __FILE__));
}
add_action('wp_enqueue_scripts', 'smsb_enqueue_scripts');

// Function to generate sharing buttons HTML
function smsb_generate_buttons($content) {
    // Only add buttons on single blog posts
    if (is_single() && is_main_query()) {
        $url = urlencode(get_permalink());
        $title = urlencode(get_the_title());
        $buttons = '';

        // Facebook
        $buttons .= '<a href="https://www.facebook.com/sharer/sharer.php?u=' . $url . '" target="_blank" rel="noopener noreferrer" class="smsb-button smsb-facebook">Share on Facebook</a>';
        
        // Twitter
        $buttons .= '<a href="https://twitter.com/intent/tweet?url=' . $url . '&text=' . $title . '" target="_blank" rel="noopener noreferrer" class="smsb-button smsb-twitter">Share on Twitter</a>';
        
        // LinkedIn
        $buttons .= '<a href="https://www.linkedin.com/sharing/share-offsite/?url=' . $url . '" target="_blank" rel="noopener noreferrer" class="smsb-button smsb-linkedin">Share on LinkedIn</a>';

        // Append buttons to the content
        $content .= '<div class="smsb-buttons">' . $buttons . '</div>';
    }
    return $content;
}
add_filter('the_content', 'smsb_generate_buttons');

// Activation hook
function smsb_activate_plugin() {
    // Perform tasks on plugin activation, if needed
}
register_activation_hook(__FILE__, 'smsb_activate_plugin');

// Deactivation hook
function smsb_deactivate_plugin() {
    // Perform cleanup tasks on plugin deactivation, if needed
}
register_deactivation_hook(__FILE__, 'smsb_deactivate_plugin');
```

**CSS Example (`css/smsb-style.css`):**
```css
.smsb-buttons {
    margin-top: 20px;
}

.smsb-button {
    display: inline-block;
    margin-right: 10px;
    padding: 10px 15px;
    color: #fff;
    text-decoration: none;
    border-radius: 5px;
    font-size: 14px;
}

.smsb-facebook {
    background-color: #3b5998;
}

.smsb-twitter {
    background-color: #1da1f2;
}

.smsb-linkedin {
    background-color: #0077b5;
}
```

This code can be saved as a WordPress plugin (`social-media-sharing-buttons.php`) and activated like any other plugin.
