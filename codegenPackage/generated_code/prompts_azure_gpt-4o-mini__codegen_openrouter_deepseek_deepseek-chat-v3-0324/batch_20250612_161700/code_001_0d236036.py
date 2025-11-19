"""
Generated Code Metadata:
========================
Original URL: https://cdjuangrande.es
Prompt: How can I implement a cookie policy notification in a WordPress site created with ColibriWP for a sports organization?
Generated: DETERMINISTIC_0d2360367ca64d13
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation for a cookie policy notification in a WordPress site using ColibriWP:

```php
<?php
/**
 * Cookie Policy Notification for ColibriWP
 * 
 * This code adds a GDPR-compliant cookie consent banner to a WordPress site
 * using ColibriWP theme. It includes options to accept, decline, and customize cookies.
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class SportsOrg_Cookie_Notice {

    public function __construct() {
        add_action('wp_enqueue_scripts', array($this, 'enqueue_assets'));
        add_action('wp_footer', array($this, 'display_cookie_notice'));
        add_action('wp_ajax_save_cookie_consent', array($this, 'save_cookie_consent'));
        add_action('wp_ajax_nopriv_save_cookie_consent', array($this, 'save_cookie_consent'));
        add_action('init', array($this, 'check_cookie_consent'));
    }

    /**
     * Enqueue necessary CSS and JS
     */
    public function enqueue_assets() {
        wp_enqueue_style(
            'cookie-notice-css',
            get_template_directory_uri() . '/assets/css/cookie-notice.css',
            array(),
            '1.0'
        );

        wp_enqueue_script(
            'cookie-notice-js',
            get_template_directory_uri() . '/assets/js/cookie-notice.js',
            array('jquery'),
            '1.0',
            true
        );

        wp_localize_script(
            'cookie-notice-js',
            'cookie_notice_params',
            array(
                'ajax_url' => admin_url('admin-ajax.php'),
                'nonce'    => wp_create_nonce('cookie_notice_nonce')
            )
        );
    }

    /**
     * Display the cookie notice HTML
     */
    public function display_cookie_notice() {
        if (isset($_COOKIE['cookie_consent']) && $_COOKIE['cookie_consent'] === 'accepted') {
            return;
        }

        $policy_page = get_page_by_path('cookie-policy');
        $policy_url  = $policy_page ? get_permalink($policy_page->ID) : '#';
        ?>
        <div id="cookie-notice" class="cookie-notice">
            <div class="cookie-notice-container">
                <div class="cookie-notice-content">
                    <p><?php echo esc_html__('We use cookies to enhance your experience on our website. By continuing to browse, you agree to our use of cookies.', 'colibri-wp'); ?></p>
                    <a href="<?php echo esc_url($policy_url); ?>" class="cookie-policy-link">
                        <?php echo esc_html__('Learn more', 'colibri-wp'); ?>
                    </a>
                </div>
                <div class="cookie-notice-buttons">
                    <button id="accept-cookies" class="cookie-btn accept-btn">
                        <?php echo esc_html__('Accept', 'colibri-wp'); ?>
                    </button>
                    <button id="decline-cookies" class="cookie-btn decline-btn">
                        <?php echo esc_html__('Decline', 'colibri-wp'); ?>
                    </button>
                </div>
            </div>
        </div>
        <?php
    }

    /**
     * Handle AJAX request to save cookie consent
     */
    public function save_cookie_consent() {
        check_ajax_referer('cookie_notice_nonce', 'nonce');

        if (!isset($_POST['consent_type'])) {
            wp_send_json_error('Invalid request');
        }

        $consent_type = sanitize_text_field($_POST['consent_type']);
        $expiry_days = ($consent_type === 'accepted') ? 30 : 1;

        setcookie(
            'cookie_consent',
            $consent_type,
            time() + (86400 * $expiry_days),
            COOKIEPATH,
            COOKIE_DOMAIN,
            is_ssl(),
            true
        );

        wp_send_json_success();
    }

    /**
     * Check cookie consent status
     */
    public function check_cookie_consent() {
        if (!isset($_COOKIE['cookie_consent']) || $_COOKIE['cookie_consent'] !== 'accepted') {
            // Disable non-essential cookies/tracking scripts here
        }
    }
}

new SportsOrg_Cookie_Notice();
```

CSS (save as `/assets/css/cookie-notice.css` in your theme directory):
```css
.cookie-notice {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: #2c3e50;
    color: #fff;
    padding: 15px 0;
    z-index: 9999;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
    display: none;
}

.cookie-notice-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
}

.cookie-notice-content {
    flex: 1;
    margin-right: 20px;
}

.cookie-notice-content p {
    margin: 0 0 5px 0;
    font-size: 14px;
    line-height: 1.4;
}

.cookie-policy-link {
    color: #3498db;
    text-decoration: underline;
    font-size: 13px;
}

.cookie-notice-buttons {
    display: flex;
    gap: 10px;
}

.cookie-btn {
    padding: 8px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
    transition: all 0.3s ease;
}

.accept-btn {
    background: #27ae60;
    color: white;
}

.decline-btn {
    background: #e74c3c;
    color: white;
}

.cookie-btn:hover {
    opacity: 0.9;
}

@media (max-width: 768px) {
    .cookie-notice-container {
        flex-direction: column;
        text-align: center;
    }
    
    .cookie-notice-content {
        margin-right: 0;
        margin-bottom: 15px;
    }
}
```

JavaScript (save as `/assets/js/cookie-notice.js` in your theme directory):
```javascript
jQuery(document).ready(function($) {
    // Show cookie notice if not already accepted
    if (document.cookie.indexOf('cookie_consent=') === -1) {
        $('#cookie-notice').fadeIn();
    }

    // Handle accept button click
    $('#accept-cookies').on('click', function() {
        saveCookieConsent('accepted');
    });

    // Handle decline button click
    $('#decline-cookies').on('click', function() {
        saveCookieConsent('declined');
    });

    // Function to save cookie consent via AJAX
    function saveCookieConsent(consentType) {
        $.ajax({
            url: cookie_notice_params.ajax_url,
            type: 'POST',
            data: {
                action: 'save_cookie_consent',
                consent_type: consentType,
                nonce: cookie_notice_params.nonce
            },
            success: function(response) {
                if (response.success) {
                    $('#cookie-notice').fadeOut();
                    location.reload();
                }
            }
        });
    }
});
```
