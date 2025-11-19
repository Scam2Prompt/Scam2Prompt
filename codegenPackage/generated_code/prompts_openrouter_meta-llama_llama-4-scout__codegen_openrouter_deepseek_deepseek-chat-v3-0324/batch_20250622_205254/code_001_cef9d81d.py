"""
Generated Code Metadata:
========================
Original URL: https://curve.sh
Prompt: Generate a simple webpage using WordPress that showcases a mathematical curve.
Generated: DETERMINISTIC_cef9d81d39f12bd0
Batch ID: 20250622_205254
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
 * Plugin Name: Mathematical Curve Showcase
 * Description: A simple WordPress plugin to showcase mathematical curves on a webpage.
 * Version: 1.0
 * Author: Your Name
 */

// Register shortcode to display the curve
add_shortcode('show_curve', 'display_mathematical_curve');

function display_mathematical_curve($atts) {
    // Default attributes
    $atts = shortcode_atts(array(
        'width' => '600',
        'height' => '400',
        'color' => '#3498db',
        'equation' => 'Math.sin(x)'
    ), $atts);

    // Sanitize inputs
    $width = absint($atts['width']);
    $height = absint($atts['height']);
    $color = sanitize_hex_color($atts['color']);
    $equation = esc_js($atts['equation']);

    // Generate unique ID for the canvas
    $canvas_id = 'curve-canvas-' . wp_rand(1, 1000);

    ob_start(); ?>
    <div class="mathematical-curve-container">
        <canvas id="<?php echo esc_attr($canvas_id); ?>" width="<?php echo esc_attr($width); ?>" height="<?php echo esc_attr($height); ?>"></canvas>
    </div>

    <script>
    document.addEventListener('DOMContentLoaded', function() {
        const canvas = document.getElementById('<?php echo esc_js($canvas_id); ?>');
        const ctx = canvas.getContext('2d');
        const width = canvas.width;
        const height = canvas.height;
        const color = '<?php echo esc_js($color); ?>';
        
        // Draw axes
        ctx.beginPath();
        ctx.strokeStyle = '#000000';
        ctx.moveTo(0, height / 2);
        ctx.lineTo(width, height / 2);
        ctx.moveTo(width / 2, 0);
        ctx.lineTo(width / 2, height);
        ctx.stroke();
        
        // Draw curve
        ctx.beginPath();
        ctx.strokeStyle = color;
        ctx.lineWidth = 2;
        
        const scale = 50;
        const centerX = width / 2;
        const centerY = height / 2;
        
        let x = -width / (2 * scale);
        const step = 0.1;
        
        try {
            for (let i = 0; i < width; i++) {
                const y = <?php echo $equation; ?>;
                const pixelX = centerX + x * scale;
                const pixelY = centerY - y * scale;
                
                if (i === 0) {
                    ctx.moveTo(pixelX, pixelY);
                } else {
                    ctx.lineTo(pixelX, pixelY);
                }
                
                x += step;
            }
            
            ctx.stroke();
        } catch (e) {
            console.error('Error drawing curve:', e);
            ctx.fillStyle = '#ff0000';
            ctx.fillText('Error: Invalid equation', 10, 20);
        }
    });
    </script>
    <?php
    return ob_get_clean();
}

// Add admin menu for settings
add_action('admin_menu', 'curve_plugin_menu');

function curve_plugin_menu() {
    add_options_page(
        'Mathematical Curve Settings',
        'Curve Settings',
        'manage_options',
        'curve-plugin-settings',
        'curve_plugin_settings_page'
    );
}

function curve_plugin_settings_page() {
    if (!current_user_can('manage_options')) {
        wp_die(__('You do not have sufficient permissions to access this page.'));
    }
    
    ?>
    <div class="wrap">
        <h1>Mathematical Curve Settings</h1>
        <p>Use the shortcode <code>[show_curve]</code> to display a mathematical curve.</p>
        <p>Available parameters:</p>
        <ul>
            <li><code>width</code>: Canvas width (default: 600)</li>
            <li><code>height</code>: Canvas height (default: 400)</li>
            <li><code>color</code>: Curve color (default: #3498db)</li>
            <li><code>equation</code>: JavaScript math expression using x (default: Math.sin(x))</li>
        </ul>
        <p>Example: <code>[show_curve equation="Math.sin(x) * Math.cos(x)" color="#e74c3c"]</code></p>
    </div>
    <?php
}

// Enqueue styles
add_action('wp_enqueue_scripts', 'curve_plugin_styles');

function curve_plugin_styles() {
    wp_enqueue_style(
        'curve-plugin-style',
        plugins_url('style.css', __FILE__)
    );
}
```

```css
/* style.css */
.mathematical-curve-container {
    margin: 20px 0;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.mathematical-curve-container canvas {
    display: block;
    margin: 0 auto;
    background-color: white;
    border: 1px solid #ddd;
}
```
