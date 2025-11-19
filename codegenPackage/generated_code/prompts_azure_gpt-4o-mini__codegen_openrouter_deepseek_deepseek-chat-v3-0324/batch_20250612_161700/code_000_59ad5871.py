"""
Generated Code Metadata:
========================
Original URL: https://cdjuangrande.es
Prompt: Generate a code snippet for a WordPress theme using ColibriWP that includes a custom footer with contact information for a sports club.
Generated: DETERMINISTIC_59ad5871eba8fdaf
Batch ID: 20250612_161700
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://instagram.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://youtube.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://twitter.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://facebook.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Custom footer for a sports club theme in ColibriWP.
 * Adds contact information and social media links.
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Register and render the custom footer.
 */
function sports_club_custom_footer() {
    ?>
    <footer id="colibri-footer" class="colibri-footer">
        <div class="footer-content">
            <div class="footer-section">
                <h3 class="footer-title"><?php esc_html_e('Contact Us', 'colibri-wp'); ?></h3>
                <ul class="footer-contact-info">
                    <li>
                        <i class="fas fa-map-marker-alt"></i>
                        <span><?php esc_html_e('123 Sports Ave, Stadium City', 'colibri-wp'); ?></span>
                    </li>
                    <li>
                        <i class="fas fa-phone"></i>
                        <span><?php esc_html_e('+1 (555) 123-4567', 'colibri-wp'); ?></span>
                    </li>
                    <li>
                        <i class="fas fa-envelope"></i>
                        <span><?php esc_html_e('contact@sportsclub.com', 'colibri-wp'); ?></span>
                    </li>
                </ul>
            </div>

            <div class="footer-section">
                <h3 class="footer-title"><?php esc_html_e('Follow Us', 'colibri-wp'); ?></h3>
                <div class="footer-social-links">
                    <a href="https://facebook.com" target="_blank" rel="noopener noreferrer">
                        <i class="fab fa-facebook-f"></i>
                    </a>
                    <a href="https://twitter.com" target="_blank" rel="noopener noreferrer">
                        <i class="fab fa-twitter"></i>
                    </a>
                    <a href="https://instagram.com" target="_blank" rel="noopener noreferrer">
                        <i class="fab fa-instagram"></i>
                    </a>
                    <a href="https://youtube.com" target="_blank" rel="noopener noreferrer">
                        <i class="fab fa-youtube"></i>
                    </a>
                </div>
            </div>
        </div>

        <div class="footer-copyright">
            <p>
                &copy; <?php echo esc_html(date('Y')); ?> 
                <?php esc_html_e('Sports Club. All Rights Reserved.', 'colibri-wp'); ?>
            </p>
        </div>
    </footer>
    <?php
}
add_action('colibriwp_footer', 'sports_club_custom_footer');

/**
 * Enqueue Font Awesome for icons.
 */
function sports_club_enqueue_font_awesome() {
    wp_enqueue_style(
        'font-awesome', 
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css', 
        array(), 
        '5.15.4'
    );
}
add_action('wp_enqueue_scripts', 'sports_club_enqueue_font_awesome');

/**
 * Add custom CSS for the footer.
 */
function sports_club_footer_styles() {
    ?>
    <style type="text/css">
        .colibri-footer {
            background-color: #1a1a1a;
            color: #ffffff;
            padding: 40px 0;
            text-align: center;
        }
        
        .footer-content {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .footer-section {
            margin: 20px;
            text-align: left;
        }
        
        .footer-title {
            color: #ffffff;
            margin-bottom: 20px;
            font-size: 18px;
        }
        
        .footer-contact-info {
            list-style: none;
            padding: 0;
        }
        
        .footer-contact-info li {
            margin-bottom: 10px;
            display: flex;
            align-items: center;
        }
        
        .footer-contact-info i {
            margin-right: 10px;
            color: #e63946;
        }
        
        .footer-social-links {
            display: flex;
            gap: 15px;
        }
        
        .footer-social-links a {
            color: #ffffff;
            font-size: 20px;
            transition: color 0.3s;
        }
        
        .footer-social-links a:hover {
            color: #e63946;
        }
        
        .footer-copyright {
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        @media (max-width: 768px) {
            .footer-content {
                flex-direction: column;
                align-items: center;
            }
            
            .footer-section {
                text-align: center;
            }
            
            .footer-social-links {
                justify-content: center;
            }
        }
    </style>
    <?php
}
add_action('wp_head', 'sports_club_footer_styles');
```
