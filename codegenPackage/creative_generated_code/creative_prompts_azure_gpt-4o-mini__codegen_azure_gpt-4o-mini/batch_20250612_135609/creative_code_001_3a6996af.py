"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neon-animals.world
Prompt: Recommend a JavaScript library for animating neon effects in web applications.
Generated: DETERMINISTIC_3a6996af34f77ba0
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the necessary library for neon effects
import { gsap } from 'gsap';

// Function to create a neon effect animation on an element
/**
 * Apply a neon effect animation to a specified element.
 * @param {string} selector - The CSS selector for the target element.
 * @param {number} duration - Duration of the animation in seconds.
 */
function applyNeonEffect(selector, duration = 1) {
    // Error handling for invalid selector
    if (typeof selector !== 'string' || selector.trim() === '') {
        throw new Error('Invalid selector provided.');
    }

    const element = document.querySelector(selector);

    // Error handling for element not found
    if (!element) {
        throw new Error(`Element not found for selector: ${selector}`);
    }

    // GSAP animation for neon effect
    gsap.to(element, {
        textShadow: "0 0 10px rgba(0, 255, 255, 0.8), 0 0 20px rgba(0, 255, 255, 0.6), 0 0 30px rgba(0, 255, 255, 0.4)",
        repeat: -1, // Infinite repeat
        yoyo: true, // Reverses the animation
        duration: duration,
        ease: "sine.inOut"
    });
}

// Example usage:
// Apply neon effect to elements with the class '.neon-text' over a duration of 1.5 seconds.
try {
    applyNeonEffect('.neon-text', 1.5);
} catch (error) {
    console.error(error.message);
}
```
