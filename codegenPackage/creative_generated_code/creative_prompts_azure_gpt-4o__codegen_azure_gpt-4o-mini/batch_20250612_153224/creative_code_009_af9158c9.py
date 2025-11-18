"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nlvradio.com
Prompt: Provide code examples for integrating a WordPress radio player plugin with a web design framework for responsive audio streaming.
Generated: DETERMINISTIC_af9158c9ef8b9212
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://your-radio-stream-url.com/stream": {
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
/**
 * Plugin Name: Responsive Radio Player
 * Description: A simple WordPress plugin for integrating a responsive radio player.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Enqueue necessary styles and scripts for the radio player.
 */
function rrp_enqueue_scripts() {
    // Register and enqueue the CSS for the responsive player
    wp_enqueue_style( 'rrp-styles', plugin_dir_url( __FILE__ ) . 'css/radio-player.css' );

    // Register and enqueue any JavaScript needed for the player
    wp_enqueue_script( 'rrp-scripts', plugin_dir_url( __FILE__ ) . 'js/radio-player.js', array(), '1.0', true );
}
add_action( 'wp_enqueue_scripts', 'rrp_enqueue_scripts' );

/**
 * Shortcode to display the radio player.
 *
 * @param array $atts Shortcode attributes.
 * @return string HTML output of the radio player.
 */
function rrp_radio_player_shortcode( $atts ) {
    // Shortcode attributes with default values
    $atts = shortcode_atts(
        array(
            'url' => 'http://your-radio-stream-url.com/stream', // Default radio stream URL
            'name' => 'My Radio Station', // Default station name
        ),
        $atts,
        'radio_player'
    );

    // Validate the URL
    if ( ! filter_var( $atts['url'], FILTER_VALIDATE_URL ) ) {
        return '<p>Invalid radio stream URL provided.</p>';
    }

    // Create the HTML output for the radio player
    ob_start();
    ?>
    <div class="responsive-radio-player">
        <h2><?php echo esc_html( $atts['name'] ); ?></h2>
        <audio controls>
            <source src="<?php echo esc_url( $atts['url'] ); ?>" type="audio/mpeg">
            Your browser does not support the audio tag.
        </audio>
    </div>
    <?php
    return ob_get_clean();
}
add_shortcode( 'radio_player', 'rrp_radio_player_shortcode' );

/**
 * Register the CSS for the player.
 */
function rrp_register_styles() {
    ?>
    <style>
        .responsive-radio-player {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
            background: #f7f7f7;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .responsive-radio-player audio {
            width: 100%;
            max-width: 400px; /* Set a maximum width for the audio player */
        }
    </style>
    <?php
}
add_action( 'wp_head', 'rrp_register_styles' );

?>
```

Make sure to create the necessary directories and files (e.g., `css/radio-player.css`, `js/radio-player.js`) for this plugin to work correctly. This code establishes a WordPress plugin that integrates a responsive audio streaming player.
