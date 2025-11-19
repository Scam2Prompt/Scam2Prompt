"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Generate SVG code for a radial scroll progress indicator that updates dynamically based on the scroll position, as outlined on the Scroll Progress Indicator website.
Generated: DETERMINISTIC_3b5df2f798955c84
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
   * @param {number} options.size - The size of the indicator.
   * @param {number} options.strokeWidth - The stroke width of the indicator.
   * @param {string} options.color - The color of the indicator.
   */
  constructor(container, options) {
    this.container = container;
    this.options = Object.assign({
      size: 100,
      strokeWidth: 10,
      color: '#333',
    }, options);

    this.svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    this.svg.setAttribute('width', this.options.size);
    this.svg.setAttribute('height', this.options.size);

    this.circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    this.circle.setAttribute('cx', this.options.size / 2);
    this.circle.setAttribute('cy', this.options.size / 2);
    this.circle.setAttribute('r', (this.options.size / 2) - this.options.strokeWidth / 2);
    this.circle.setAttribute('fill', 'none');
    this.circle.setAttribute('stroke', this.options.color);
    this.circle.setAttribute('stroke-width', this.options.strokeWidth);
    this.circle.setAttribute('stroke-linecap', 'round');

    this.progressCircle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    this.progressCircle.setAttribute('cx', this.options.size / 2);
    this.progressCircle.setAttribute('cy', this.options.size / 2);
    this.progressCircle.setAttribute('r', (this.options.size / 2) - this.options.strokeWidth / 2);
    this.progressCircle.setAttribute('fill', 'none');
    this.progressCircle.setAttribute('stroke', this.options.color);
    this.progressCircle.setAttribute('stroke-width', this.options.strokeWidth);
    this.progressCircle.setAttribute('stroke-linecap', 'round');
    this.progressCircle.setAttribute('stroke-dasharray', this.getCircumference());
    this.progressCircle.setAttribute('stroke-dashoffset', this.getCircumference());

    this.svg.appendChild(this.circle);
    this.svg.appendChild(this.progressCircle);

    this.container.appendChild(this.svg);

    this.updateProgress = this.updateProgress.bind(this);

    window.addEventListener('scroll', this.updateProgress);
  }

  /**
   * Updates the progress of the indicator based on the scroll position.
   */
  updateProgress() {
    const scrollPosition = window.scrollY;
    const documentHeight = document.body.offsetHeight;
    const windowHeight = window.innerHeight;
    const progress = scrollPosition / (documentHeight - windowHeight);

    this.progressCircle.setAttribute('stroke-dashoffset', this.getCircumference() * (1 - progress));
  }

  /**
   * Gets the circumference of the circle.
   * 
   * @returns {number} The circumference of the circle.
   */
  getCircumference() {
    const radius = (this.options.size / 2) - this.options.strokeWidth / 2;
    return 2 * Math.PI * radius;
  }

  /**
   * Destroys the indicator and removes event listeners.
   */
  destroy() {
    window.removeEventListener('scroll', this.updateProgress);
    this.container.removeChild(this.svg);
  }
}

// Example usage
const container = document.getElementById('indicator-container');
const indicator = new RadialScrollProgressIndicator(container, {
  size: 200,
  strokeWidth: 20,
  color: '#666',
});

// Clean up on page unload
window.onunload = function() {
  indicator.destroy();
};
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Radial Scroll Progress Indicator</title>
  <style>
    /* Add some basic styling to demonstrate the indicator */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }
    #indicator-container {
      position: fixed;
      top: 20px;
      right: 20px;
    }
  </style>
</head>
<body>
  <div id="indicator-container"></div>
  <script src="RadialScrollProgressIndicator.js"></script>
</body>
</html>
```
