"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wonderino.com
Prompt: Write JavaScript code to stop all running animations on a webpage, including videos, GIFs, and CSS transitions, as described in Wonderino's accessibility features.
Generated: DETERMINISTIC_b006ef96ee60586e
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script stops all running animations on a webpage, including videos,
 * GIFs, and CSS transitions. It is designed to improve accessibility.
 */

// Stop all CSS animations and transitions
function stopCSSAnimations() {
    const styleElement = document.createElement('style');
    styleElement.type = 'text/css';
    styleElement.innerHTML = `
        * {
            animation: none !important;
            transition: none !important;
        }
    `;
    document.head.appendChild(styleElement);
}

// Pause all <video> elements
function pauseVideos() {
    const videos = document.querySelectorAll('video');
    videos.forEach(video => {
        try {
            video.pause(); // Pause the video if it is playing
        } catch (error) {
            console.error('Error pausing video:', error);
        }
    });
}

// Replace GIFs with static images (pauses animated content)
function stopGIFs() {
    const images = document.querySelectorAll('img');
    images.forEach(img => {
        const src = img.src.toLowerCase();
        if (src.endsWith('.gif')) {
            try {
                // Replace the GIF with a static version, typically the first frame
                const staticImageSrc = src.replace('.gif', '.jpg'); // Assuming .jpg as the static image format
                img.src = staticImageSrc;
            } catch (error) {
                console.error('Error replacing GIF:', error);
            }
        }
    });
}

// Main function to stop all animations
function stopAllAnimations() {
    stopCSSAnimations();
    pauseVideos();
    stopGIFs();
}

// Execute when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    try {
        stopAllAnimations();
        console.log('All animations have been stopped for accessibility.');
    } catch (error) {
        console.error('Error stopping animations:', error);
    }
});
```
