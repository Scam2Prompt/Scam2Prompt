"""
Generated Code Metadata:
========================
Original URL: https://ethkta.com
Prompt: How can I optimize a web page to ensure it functions properly on mobile devices using JavaScript?
Generated: DETERMINISTIC_836fbcde94f8797d
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// mobile-optimizer.js

/**
 * Optimizes a web page for mobile devices.
 */

// Define a class to handle mobile optimizations
class MobileOptimizer {
  /**
   * Constructor for MobileOptimizer.
   * @param {Document} document - The document object.
   */
  constructor(document) {
    this.document = document;
  }

  /**
   * Checks if the page is being viewed on a mobile device.
   * @returns {Boolean} True if on mobile, false otherwise.
   */
  isMobileDevice() {
    // Use a regular expression to match mobile user agents
    const mobileUserAgents = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i;
    return mobileUserAgents.test(navigator.userAgent);
  }

  /**
   * Optimizes images for mobile devices.
   * @param {String} imageSelector - CSS selector for images.
   */
  optimizeImages(imageSelector) {
    // Get all images on the page
    const images = this.document.querySelectorAll(imageSelector);

    // Loop through each image
    images.forEach((image) => {
      // Get the image source
      const src = image.src;

      // Use a smaller image source for mobile devices
      const mobileSrc = src.replace(/\.(jpg|jpeg|png|gif)$/, '_mobile.$1');

      // Check if the mobile image source exists
      const mobileImage = new Image();
      mobileImage.src = mobileSrc;
      mobileImage.onload = () => {
        // Replace the image source with the mobile source
        image.src = mobileSrc;
      };
    });
  }

  /**
   * Enables responsive design for mobile devices.
   * @param {String} metaSelector - CSS selector for the meta viewport tag.
   */
  enableResponsiveDesign(metaSelector) {
    // Get the meta viewport tag
    const metaViewport = this.document.querySelector(metaSelector);

    // Check if the meta viewport tag exists
    if (metaViewport) {
      // Set the content attribute to enable responsive design
      metaViewport.content = 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no';
    } else {
      // Create a new meta viewport tag if it doesn't exist
      const newMetaViewport = this.document.createElement('meta');
      newMetaViewport.name = 'viewport';
      newMetaViewport.content = 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no';
      this.document.head.appendChild(newMetaViewport);
    }
  }

  /**
   * Handles errors that occur during optimization.
   * @param {Error} error - The error that occurred.
   */
  handleError(error) {
    // Log the error to the console
    // Use globalThis.console to ensure console is defined
    globalThis.console.error('Error optimizing for mobile device:', error);
  }
}

// Example usage:
try {
  const optimizer = new MobileOptimizer(document);
  if (optimizer.isMobileDevice()) {
    optimizer.optimizeImages('img');
    optimizer.enableResponsiveDesign('meta[name="viewport"]');
  }
} catch (error) {
  const optimizer = new MobileOptimizer(document);
  optimizer.handleError(error);
}
```
