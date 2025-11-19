"""
Generated Code Metadata:
========================
Original URL: https://scienceartthinking.de
Prompt: Develop a JavaScript function that visualizes the relationship between gravity and art, drawing from the themes in "Schwerkraft und Kunst."
Generated: DETERMINISTIC_0d91e60ea431df21
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Visualizes the relationship between gravity and art, inspired by "Schwerkraft und Kunst".
 * This function creates a canvas animation where particles are influenced by gravity,
 * creating an artistic representation of gravitational forces.
 * 
 * @param {string} canvasId - The ID of the canvas element to render the animation.
 * @param {number} particleCount - Number of particles to simulate (default: 100).
 * @param {Object} options - Configuration options for the animation.
 * @param {number} options.gravity - Strength of gravity (default: 0.1).
 * @param {number} options.friction - Friction coefficient (default: 0.99).
 * @param {string} options.particleColor - Color of particles (default: 'rgba(200, 200, 255, 0.8)').
 */
function visualizeGravityAndArt(canvasId, particleCount = 100, options = {}) {
    // Merge default options with user-provided options
    const config = {
        gravity: 0.1,
        friction: 0.99,
        particleColor: 'rgba(200, 200, 255, 0.8)',
        ...options
    };

    // Get canvas and context
    const canvas = document.getElementById(canvasId);
    if (!canvas) {
        console.error(`Canvas with ID '${canvasId}' not found.`);
        return;
    }

    const ctx = canvas.getContext('2d');
    if (!ctx) {
        console.error('Could not get 2D rendering context.');
        return;
    }

    // Set canvas dimensions
    function resizeCanvas() {
        canvas.width = canvas.clientWidth;
        canvas.height = canvas.clientHeight;
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    // Particle class
    class Particle {
        constructor() {
            this.reset();
            this.y = Math.random() * canvas.height;
        }

        reset() {
            this.x = Math.random() * canvas.width;
            this.y = -20;
            this.size = Math.random() * 5 + 1;
            this.speedX = Math.random() * 3 - 1.5;
            this.speedY = Math.random() * 3;
        }

        update() {
            this.speedY += config.gravity;
            this.x += this.speedX;
            this.y += this.speedY;
            this.speedX *= config.friction;
            this.speedY *= config.friction;

            // Reset particle if it goes off screen
            if (this.y > canvas.height + 20 || 
                this.x < -20 || 
                this.x > canvas.width + 20) {
                this.reset();
            }
        }

        draw() {
            ctx.fillStyle = config.particleColor;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    // Create particles
    const particles = Array.from({ length: particleCount }, () => new Particle());

    // Animation loop
    function animate() {
        // Clear canvas with semi-transparent background for trail effect
        ctx.fillStyle = 'rgba(10, 10, 20, 0.1)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Update and draw particles
        particles.forEach(particle => {
            particle.update();
            particle.draw();
        });

        requestAnimationFrame(animate);
    }

    // Start animation
    animate();

    // Return API for controlling the animation if needed
    return {
        updateConfig: (newOptions) => {
            Object.assign(config, newOptions);
        },
        resizeCanvas
    };
}
```
