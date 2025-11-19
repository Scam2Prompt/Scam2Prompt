"""
Generated Code Metadata:
========================
Original URL: https://usgddm.com
Prompt: What are the best practices for using JavaScript to enhance mobile user experience on a website?
Generated: DETERMINISTIC_aca086f738123455
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a JavaScript code snippet that implements best practices for enhancing mobile user experience on a website:

```javascript
/**
 * Mobile UX Enhancement Utilities
 * A collection of functions to improve mobile user experience
 */

class MobileUX {
  constructor() {
    this.touchStartX = 0;
    this.touchEndX = 0;
    this.lastTapTime = 0;
    this.viewportMeta = document.querySelector('meta[name="viewport"]');
    this.init();
  }

  /**
   * Initialize mobile UX enhancements
   */
  init() {
    this.setupViewport();
    this.addTouchClass();
    this.preventZoom();
    this.enableFastClick();
    this.handleSwipeGestures();
    this.disablePullToRefresh();
    this.optimizeScrolling();
  }

  /**
   * Ensure proper viewport settings for mobile devices
   */
  setupViewport() {
    if (!this.viewportMeta) {
      this.viewportMeta = document.createElement('meta');
      this.viewportMeta.name = 'viewport';
      document.head.appendChild(this.viewportMeta);
    }
    this.viewportMeta.content = 'width=device-width, initial-scale=1, maximum-scale=1, shrink-to-fit=no';
  }

  /**
   * Add 'touch' class to body for touch-specific styling
   */
  addTouchClass() {
    if ('ontouchstart' in window || navigator.maxTouchPoints) {
      document.body.classList.add('touch');
    } else {
      document.body.classList.add('no-touch');
    }
  }

  /**
   * Prevent accidental zooming on mobile devices
   */
  preventZoom() {
    let lastTouchEnd = 0;
    document.addEventListener('touchend', (event) => {
      const now = Date.now();
      if (now - lastTouchEnd <= 300) {
        event.preventDefault();
      }
      lastTouchEnd = now;
    }, false);
  }

  /**
   * Reduce click delay on touch devices
   */
  enableFastClick() {
    document.addEventListener('DOMContentLoaded', () => {
      const elements = document.querySelectorAll('[data-fast-click]');
      elements.forEach(element => {
        element.addEventListener('touchend', (e) => {
          e.preventDefault();
          e.target.click();
        });
      });
    });
  }

  /**
   * Handle swipe gestures for navigation
   */
  handleSwipeGestures() {
    document.addEventListener('touchstart', (e) => {
      this.touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    document.addEventListener('touchend', (e) => {
      this.touchEndX = e.changedTouches[0].screenX;
      this.handleSwipe();
    }, { passive: true });
  }

  /**
   * Process swipe gesture and trigger appropriate action
   */
  handleSwipe() {
    const threshold = 100;
    const difference = this.touchStartX - this.touchEndX;

    if (Math.abs(difference) > threshold) {
      if (difference > 0) {
        // Swipe left
        this.dispatchSwipeEvent('swipeLeft');
      } else {
        // Swipe right
        this.dispatchSwipeEvent('swipeRight');
      }
    }
  }

  /**
   * Dispatch custom swipe event
   * @param {string} eventName - Name of the swipe event
   */
  dispatchSwipeEvent(eventName) {
    const event = new Event(eventName);
    document.dispatchEvent(event);
  }

  /**
   * Disable pull-to-refresh behavior on mobile
   */
  disablePullToRefresh() {
    document.body.style.overscrollBehaviorY = 'contain';
  }

  /**
   * Optimize scrolling performance
   */
  optimizeScrolling() {
    document.body.style.webkitOverflowScrolling = 'touch';
    document.documentElement.style.scrollBehavior = 'smooth';
  }

  /**
   * Handle double tap for zooming
   */
  handleDoubleTap() {
    document.addEventListener('touchend', (e) => {
      const currentTime = new Date().getTime();
      const tapLength = currentTime - this.lastTapTime;
      
      if (tapLength < 300 && tapLength > 0) {
        // Double tap detected
        this.dispatchDoubleTapEvent(e.target);
        e.preventDefault();
      }
      this.lastTapTime = currentTime;
    });
  }

  /**
   * Dispatch custom double tap event
   * @param {HTMLElement} target - The element that was double tapped
   */
  dispatchDoubleTapEvent(target) {
    const event = new CustomEvent('doubletap', {
      detail: { target },
      bubbles: true,
      cancelable: true
    });
    target.dispatchEvent(event);
  }
}

// Initialize MobileUX when DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  const mobileUX = new MobileUX();
});

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
  module.exports = MobileUX;
}
```

This code includes comprehensive mobile UX enhancements while following JavaScript best practices. The implementation is encapsulated in a class, uses event delegation, and provides proper touch event handling.
