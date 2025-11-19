"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Write code for a scroll progress indicator that works seamlessly in Webflow without jank.
Generated: DETERMINISTIC_7131b7049ec0c224
Batch ID: 20250612_161125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Scroll Progress Indicator for Webflow
 * Tracks and displays scroll progress as a percentage
 * Optimized for performance to avoid jank
 */

(function() {
  // Wait for Webflow to be ready
  window.addEventListener('load', function() {
    // Create progress element
    const progressIndicator = document.createElement('div');
    progressIndicator.style.position = 'fixed';
    progressIndicator.style.top = '0';
    progressIndicator.style.left = '0';
    progressIndicator.style.width = '0%';
    progressIndicator.style.height = '4px';
    progressIndicator.style.backgroundColor = '#000';
    progressIndicator.style.zIndex = '9999';
    progressIndicator.style.transition = 'width 0.1s ease-out';
    document.body.appendChild(progressIndicator);

    // Throttle scroll events for performance
    let ticking = false;
    let lastScrollY = 0;

    const updateProgress = () => {
      const scrollY = window.scrollY || window.pageYOffset;
      const windowHeight = window.innerHeight;
      const docHeight = document.documentElement.scrollHeight;
      const maxScroll = docHeight - windowHeight;
      const scrollPercent = (scrollY / maxScroll) * 100;

      progressIndicator.style.width = `${scrollPercent}%`;
      ticking = false;
    };

    const requestTick = () => {
      if (!ticking) {
        requestAnimationFrame(updateProgress);
        ticking = true;
      }
    };

    // Handle scroll events
    window.addEventListener('scroll', function() {
      const currentScrollY = window.scrollY || window.pageYOffset;
      
      // Only update if scroll position changed significantly
      if (Math.abs(currentScrollY - lastScrollY) > 5) {
        lastScrollY = currentScrollY;
        requestTick();
      }
    }, { passive: true });

    // Handle resize events
    window.addEventListener('resize', function() {
      requestTick();
    }, { passive: true });
  });
})();
```
