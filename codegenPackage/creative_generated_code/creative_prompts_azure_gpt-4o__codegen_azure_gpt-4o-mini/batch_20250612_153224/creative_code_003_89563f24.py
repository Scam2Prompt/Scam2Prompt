"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nlvradio.com
Prompt: Provide a step-by-step guide to configure a WordPress radio player plugin for streaming live audio, including relevant JavaScript snippets.
Generated: DETERMINISTIC_89563f240c1d5539
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
 * Plugin Name: Live Audio Stream Player
 * Description: A simple plugin that adds a live audio stream player to your WordPress site.
 * Version: 1.0
 * Author: Your Name
 */

// Enqueue necessary scripts and styles
function lasp_enqueue_scripts() {
    // Enqueue jQuery if not already loaded
    if (!wp_script_is('jquery', 'enqueued')) {
        wp_enqueue_script('jquery');
    }

    // Enqueue custom JavaScript for the audio player
    wp_enqueue_script('lasp-audio-player', plugin_dir_url(__FILE__) . 'js/audio-player.js', array('jquery'), null, true);
}
add_action('wp_enqueue_scripts', 'lasp_enqueue_scripts');

// Shortcode to display the audio player
function lasp_audio_player_shortcode($atts) {
    $atts = shortcode_atts(
        array(
            'stream_url' => '',
        ),
        $atts,
        'live_audio_stream'
    );

    // Check if stream URL is provided
    if (empty($atts['stream_url'])) {
        return '<p>Error: Stream URL not provided.</p>';
    }

    // Output the audio player HTML
    ob_start();
    ?>
    <div class="lasp-audio-player">
        <audio controls>
            <source src="<?php echo esc_url($atts['stream_url']); ?>" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
    </div>
    <?php
    return ob_get_clean();
}
add_shortcode('live_audio_stream', 'lasp_audio_player_shortcode');

// Register settings for the plugin
function lasp_register_settings() {
    register_setting('lasp-settings-group', 'lasp_stream_url');
}
add_action('admin_init', 'lasp_register_settings');

// Create a settings page for the plugin
function lasp_create_admin_menu() {
    add_options_page('Live Audio Stream Player', 'Audio Stream Player', 'manage_options', 'lasp-settings', 'lasp_render_settings_page');
}
add_action('admin_menu', 'lasp_create_admin_menu');

// Render the settings page
function lasp_render_settings_page() {
    ?>
    <div class="wrap">
        <h1>Live Audio Stream Player Settings</h1>
        <form method="post" action="options.php">
            <?php settings_fields('lasp-settings-group'); ?>
            <table class="form-table">
                <tr valign="top">
                    <th scope="row">Stream URL</th>
                    <td><input type="text" name="lasp_stream_url" value="<?php echo esc_attr(get_option('lasp_stream_url')); ?>" /></td>
                </tr>
            </table>
            <?php submit_button(); ?>
        </form>
    </div>
    <?php
}
```

```javascript
// js/audio-player.js

jQuery(document).ready(function($) {
    // Check if audio is supported
    const audioPlayer = document.querySelector('.lasp-audio-player audio');
    if (audioPlayer) {
        audioPlayer.onplay = function() {
            console.log('Audio is playing');
        };

        audioPlayer.onpause = function() {
            console.log('Audio is paused');
        };

        audioPlayer.onerror = function(e) {
            console.error('Error occurred while playing audio:', e);
            alert('An error occurred while trying to play the audio stream.');
        };
    }
});
```
