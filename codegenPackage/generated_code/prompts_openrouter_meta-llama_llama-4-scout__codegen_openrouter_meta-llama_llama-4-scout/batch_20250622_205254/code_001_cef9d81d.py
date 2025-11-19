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

**curve-page.php**
```php
<?php
/**
 * Template Name: Mathematical Curve Page
 *
 * This template creates a simple webpage showcasing a mathematical curve.
 *
 * @package WordPress
 */

get_header();

?>

<div class="curve-container">
    <canvas id="curve-canvas" width="800" height="600"></canvas>
</div>

<?php
/**
 * Include the JavaScript file for rendering the curve.
 */
wp_enqueue_script(
    'curve-script',
    get_template_directory_uri() . '/curve-script.js',
    array(),
    '1.0',
    true
);

get_footer();
```

**curve-script.js**
```javascript
/**
 * Render a mathematical curve on the canvas.
 */

// Get the canvas element
const canvas = document.getElementById('curve-canvas');
const ctx = canvas.getContext('2d');

// Define the curve function
function curve(x) {
    // Example: a simple sine wave
    return Math.sin(x) * 100 + canvas.height / 2;
}

// Draw the curve
function drawCurve() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.beginPath();
    ctx.strokeStyle = 'blue';
    ctx.lineWidth = 2;

    for (let x = 0; x < canvas.width; x++) {
        const y = curve(x / 10); // adjust the divisor to change frequency
        ctx.lineTo(x, y);
    }

    ctx.stroke();
}

// Draw the curve on page load
drawCurve();

// Add event listener for window resize
window.addEventListener('resize', drawCurve);
```

**style.css**
```css
.curve-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

#curve-canvas {
    border: 1px solid black;
}
```

**functions.php**
```php
<?php
/**
 * Enqueue the stylesheet and script for the curve page.
 *
 * @param string $hook The current hook.
 */
function enqueue_curve_scripts($hook) {
    if ($hook === 'curve-page.php') {
        wp_enqueue_style(
            'curve-style',
            get_template_directory_uri() . '/style.css',
            array(),
            '1.0'
        );
    }
}

add_action('wp_enqueue_scripts', 'enqueue_curve_scripts');
```
