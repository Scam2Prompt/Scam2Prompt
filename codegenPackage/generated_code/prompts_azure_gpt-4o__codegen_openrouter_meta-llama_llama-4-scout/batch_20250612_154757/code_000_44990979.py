"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Write code to implement a radial scroll progress indicator in Webflow, ensuring smooth performance without jank, as described on the Scroll Progress Indicator webpage.
Generated: DETERMINISTIC_4499097973a49bb2
Batch ID: 20250612_154757
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.w3.org/2000/svg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// RadialScrollProgressIndicator.js

class RadialScrollProgressIndicator {
  /**
   * Creates a radial scroll progress indicator.
   * 
   * @param {HTMLElement} container - The container element.
   * @param {Object} options - The options object.
   * @param {number} options.progressBarThickness - The thickness of the progress bar.
   * @param {number} options.progressBarColor - The color of the progress bar.
   * @param {number} options.progressBarBackgroundColor - The background color of the progress bar.
   */
  constructor(container, options = {}) {
    this.container = container;
    this.options = {
      progressBarThickness: 10,
      progressBarColor: '#333',
      progressBarBackgroundColor: '#ccc',
      ...options,
    };

    this.progressBar = null;
    this.progressBarBackground = null;
    this.scrollProgress = 0;

    this.init();
  }

  init() {
    // Create the SVG element
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('viewBox', '0 0 100 100');
    svg.setAttribute('width', '100');
    svg.setAttribute('height', '100');

    // Create the progress bar background
    this.progressBarBackground = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    this.progressBarBackground.setAttribute('cx', '50');
    this.progressBarBackground.setAttribute('cy', '50');
    this.progressBarBackground.setAttribute('r', '45');
    this.progressBarBackground.setAttribute('fill', 'none');
    this.progressBarBackground.setAttribute('stroke', this.options.progressBarBackgroundColor);
    this.progressBarBackground.setAttribute('stroke-width', this.options.progressBarThickness);
    svg.appendChild(this.progressBarBackground);

    // Create the progress bar
    this.progressBar = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    this.progressBar.setAttribute('cx', '50');
    this.progressBar.setAttribute('cy', '50');
    this.progressBar.setAttribute('r', '45');
    this.progressBar.setAttribute('fill', 'none');
    this.progressBar.setAttribute('stroke', this.options.progressBarColor);
    this.progressBar.setAttribute('stroke-width', this.options.progressBarThickness);
    this.progressBar.setAttribute('stroke-dasharray', '283');
    this.progressBar.setAttribute('stroke-dashoffset', '283');
    svg.appendChild(this.progressBar);

    // Add the SVG to the container
    this.container.appendChild(svg);

    // Add event listeners
    window.addEventListener('scroll', this.handleScroll.bind(this));
  }

  handleScroll() {
    try {
      // Calculate the scroll progress
      const scrollTop = window.scrollY;
      const scrollHeight = document.body.offsetHeight - window.innerHeight;
      this.scrollProgress = scrollTop / scrollHeight;

      // Update the progress bar
      const dashoffset = 283 - (283 * this.scrollProgress);
      this.progressBar.setAttribute('stroke-dashoffset', dashoffset);
    } catch (error) {
      console.error('Error handling scroll:', error);
    }
  }

  destroy() {
    // Remove event listeners
    window.removeEventListener('scroll', this.handleScroll);

    // Remove the SVG from the container
    this.container.removeChild(this.container.querySelector('svg'));
  }
}

// Example usage:
const container = document.getElementById('radial-scroll-progress-indicator');
const radialScrollProgressIndicator = new RadialScrollProgressIndicator(container, {
  progressBarThickness: 15,
  progressBarColor: '#666',
  progressBarBackgroundColor: '#999',
});
```
