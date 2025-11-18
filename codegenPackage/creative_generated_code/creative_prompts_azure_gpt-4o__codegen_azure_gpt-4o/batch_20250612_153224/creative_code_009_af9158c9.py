"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nlvradio.com
Prompt: Provide code examples for integrating a WordPress radio player plugin with a web design framework for responsive audio streaming.
Generated: DETERMINISTIC_af9158c9ef8b9212
Batch ID: 20250612_153224
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
 * Plugin Name: Custom Radio Player Integration
 * Description: Integrates a responsive radio player into a WordPress site.
 * Version: 1.0
 * Author: Your Name
 */

// Enqueue necessary scripts and styles for the radio player
add_action('wp_enqueue_scripts', 'enqueue_radio_player_assets');
function enqueue_radio_player_assets() {
    // Load the radio player plugin's CSS
    wp_enqueue_style('radio-player-style', plugin_dir_url(__FILE__) . 'assets/css/radio-player.css');

    // Load the radio player plugin's JavaScript
    wp_enqueue_script('radio-player-script', plugin_dir_url(__FILE__) . 'assets/js/radio-player.js', ['jquery'], null, true);
}

// Shortcode to render the radio player
add_shortcode('radio_player', 'render_radio_player');
function render_radio_player($atts) {
    $atts = shortcode_atts(
        [
            'stream_url' => '', // The URL of the radio stream
            'player_title' => 'Live Radio', // Default player title
        ],
        $atts,
        'radio_player'
    );

    if (empty($atts['stream_url'])) {
        return '<p>Error: Stream URL is missing.</p>';
    }

    ob_start();
    ?>
    <div class="radio-player-wrapper">
        <h3 class="radio-player-title"><?php echo esc_html($atts['player_title']); ?></h3>
        <audio id="radio-player" controls preload="none">
            <source src="<?php echo esc_url($atts['stream_url']); ?>" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
    </div>
    <?php
    return ob_get_clean();
}

// Add a settings page to configure default stream URL
add_action('admin_menu', 'radio_player_settings_page');
function radio_player_settings_page() {
    add_options_page(
        'Radio Player Settings',
        'Radio Player',
        'manage_options',
        'radio-player-settings',
        'radio_player_settings_page_html'
    );
}

function radio_player_settings_page_html() {
    // Check user permissions
    if (!current_user_can('manage_options')) {
        return;
    }

    // Save settings
    if (isset($_POST['radio_player_stream_url'])) {
        update_option('radio_player_stream_url', sanitize_text_field($_POST['radio_player_stream_url']));
    }

    // Fetch current setting
    $stream_url = get_option('radio_player_stream_url', '');
    ?>
    <div class="wrap">
        <h1>Radio Player Settings</h1>
        <form method="POST" action="">
            <label for="radio_player_stream_url">Default Stream URL:</label>
            <input type="text" id="radio_player_stream_url" name="radio_player_stream_url" value="<?php echo esc_attr($stream_url); ?>" style="width: 100%">
            <input type="submit" value="Save Settings" class="button button-primary">
        </form>
    </div>
    <?php
}

// Add default stream URL to the shortcode if none is provided
add_filter('shortcode_atts_radio_player', 'radio_player_default_stream_url', 10, 3);
function radio_player_default_stream_url($out, $pairs, $atts) {
    if (empty($out['stream_url'])) {
        $default_url = get_option('radio_player_stream_url', '');
        if (!empty($default_url)) {
            $out['stream_url'] = $default_url;
        }
    }
    return $out;
}
```

```css
/* assets/css/radio-player.css */
.radio-player-wrapper {
    max-width: 100%;
    margin: 0 auto;
    text-align: center;
}

.radio-player-title {
    font-size: 1.5rem;
    margin-bottom: 10px;
    color: #333;
}

audio {
    width: 100%;
    max-width: 600px;
    border: 1px solid #ccc;
    border-radius: 5px;
}
```

```js
// assets/js/radio-player.js
document.addEventListener('DOMContentLoaded', function () {
    const radioPlayer = document.getElementById('radio-player');

    if (radioPlayer) {
        radioPlayer.addEventListener('play', function () {
            console.log('Radio stream is playing');
        });

        radioPlayer.addEventListener('pause', function () {
            console.log('Radio stream is paused');
        });

        radioPlayer.addEventListener('ended', function () {
            console.log('Radio stream has ended');
        });

        radioPlayer.addEventListener('error', function () {
            console.error('Error occurred while playing the radio stream');
        });
    }
});
```
