"""
Generated Code Metadata:
========================
Original URL: https://methodsmoney.com
Prompt: Generate a code snippet to implement hover icons for a website, similar to the features described on methodsmoney.com.
Generated: DETERMINISTIC_d4a7946725635aab
Batch ID: 20250612_155949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// hover-icons.js

/**
 * Hover Icons class.
 * 
 * Provides functionality for hover icons on a website.
 */
class HoverIcons {
  /**
   * Constructor.
   * 
   * @param {object} options - Configuration options.
   * @param {string} options.iconSelector - CSS selector for icons.
   * @param {string} options.hoverClass - Class to add on hover.
   * @param {string} options.tooltipClass - Class for tooltips.
   */
  constructor(options) {
    this.options = options;
    this.icons = document.querySelectorAll(options.iconSelector);
    this.hoverClass = options.hoverClass;
    this.tooltipClass = options.tooltipClass;

    // Add event listeners to icons
    this.icons.forEach(icon => {
      icon.addEventListener('mouseover', this.handleMouseOver.bind(this));
      icon.addEventListener('mouseout', this.handleMouseOut.bind(this));
    });
  }

  /**
   * Handles mouse over event.
   * 
   * @param {Event} event - Mouse over event.
   */
  handleMouseOver(event) {
    const icon = event.target;
    icon.classList.add(this.hoverClass);

    // Create tooltip if it doesn't exist
    let tooltip = icon.querySelector(`.${this.tooltipClass}`);
    if (!tooltip) {
      tooltip = document.createElement('span');
      tooltip.classList.add(this.tooltipClass);
      tooltip.textContent = icon.dataset.tooltip;
      icon.appendChild(tooltip);
    }
  }

  /**
   * Handles mouse out event.
   * 
   * @param {Event} event - Mouse out event.
   */
  handleMouseOut(event) {
    const icon = event.target;
    icon.classList.remove(this.hoverClass);

    // Remove tooltip if it exists
    const tooltip = icon.querySelector(`.${this.tooltipClass}`);
    if (tooltip) {
      icon.removeChild(tooltip);
    }
  }
}

// Initialize hover icons
document.addEventListener('DOMContentLoaded', () => {
  const options = {
    iconSelector: '.hover-icon',
    hoverClass: 'hover',
    tooltipClass: 'tooltip'
  };

  new HoverIcons(options);
});
```

```css
/* hover-icons.css */

.hover-icon {
  position: relative;
  display: inline-block;
}

.hover-icon.hover {
  color: #337ab7; /* Change to desired hover color */
}

.hover-icon .tooltip {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  background-color: #333;
  color: #fff;
  padding: 5px;
  border-radius: 5px;
  z-index: 1;
  visibility: hidden;
  opacity: 0;
  transition: opacity 0.2s ease-in-out;
}

.hover-icon.hover .tooltip {
  visibility: visible;
  opacity: 1;
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hover Icons</title>
  <link rel="stylesheet" href="hover-icons.css">
</head>
<body>
  <a href="#" class="hover-icon" data-tooltip="Facebook">
    <i class="fa fa-facebook"></i>
  </a>
  <a href="#" class="hover-icon" data-tooltip="Twitter">
    <i class="fa fa-twitter"></i>
  </a>
  <a href="#" class="hover-icon" data-tooltip="Instagram">
    <i class="fa fa-instagram"></i>
  </a>

  <script src="hover-icons.js"></script>
</body>
</html>
```
