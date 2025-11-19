"""
Generated Code Metadata:
========================
Original URL: https://dolphiniran.com
Prompt: Develop a JavaScript function that dynamically updates the display settings of a backlit mirror, inspired by the "آینه بک لایت" products from Dolphin Iran.
Generated: DETERMINISTIC_b71a47f848dba22d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * BacklitMirrorController - Controls the display settings of a backlit mirror.
 * Inspired by Dolphin Iran's "آینه بک لایت" products.
 */
class BacklitMirrorController {
  /**
   * @constructor
   * @param {HTMLElement} mirrorElement - The mirror DOM element to control
   * @param {Object} options - Configuration options
   * @param {number} options.defaultBrightness - Initial brightness (0-100)
   * @param {string} options.defaultColor - Initial color in hex format
   * @param {number} options.transitionSpeed - Transition speed in milliseconds
   */
  constructor(mirrorElement, options = {}) {
    if (!mirrorElement) {
      throw new Error('Mirror element is required');
    }

    this.mirrorElement = mirrorElement;
    this.settings = {
      brightness: options.defaultBrightness || 50,
      color: options.defaultColor || '#ffffff',
      transitionSpeed: options.transitionSpeed || 300,
      isOn: false
    };

    this._initializeMirror();
  }

  /**
   * Initialize mirror with default settings
   * @private
   */
  _initializeMirror() {
    this.mirrorElement.style.transition = `all ${this.settings.transitionSpeed}ms ease-in-out`;
    this._updateMirrorDisplay();
  }

  /**
   * Update the mirror's visual display based on current settings
   * @private
   */
  _updateMirrorDisplay() {
    if (this.settings.isOn) {
      this.mirrorElement.style.backgroundColor = this.settings.color;
      this.mirrorElement.style.opacity = this.settings.brightness / 100;
    } else {
      this.mirrorElement.style.backgroundColor = 'transparent';
      this.mirrorElement.style.opacity = 1;
    }
  }

  /**
   * Toggle mirror power state
   */
  togglePower() {
    this.settings.isOn = !this.settings.isOn;
    this._updateMirrorDisplay();
    return this.settings.isOn;
  }

  /**
   * Set mirror brightness
   * @param {number} level - Brightness level (0-100)
   */
  setBrightness(level) {
    if (typeof level !== 'number' || level < 0 || level > 100) {
      throw new Error('Brightness must be a number between 0 and 100');
    }
    this.settings.brightness = level;
    if (this.settings.isOn) {
      this._updateMirrorDisplay();
    }
  }

  /**
   * Set mirror color
   * @param {string} color - Color in hex format (#RRGGBB)
   */
  setColor(color) {
    if (!/^#([0-9A-F]{3}){1,2}$/i.test(color)) {
      throw new Error('Invalid color format. Use hex format (#RRGGBB)');
    }
    this.settings.color = color;
    if (this.settings.isOn) {
      this._updateMirrorDisplay();
    }
  }

  /**
   * Set transition speed
   * @param {number} speed - Transition speed in milliseconds
   */
  setTransitionSpeed(speed) {
    if (typeof speed !== 'number' || speed < 0) {
      throw new Error('Speed must be a positive number');
    }
    this.settings.transitionSpeed = speed;
    this.mirrorElement.style.transition = `all ${speed}ms ease-in-out`;
  }

  /**
   * Get current mirror settings
   * @returns {Object} Current settings
   */
  getSettings() {
    return {...this.settings};
  }

  /**
   * Apply multiple settings at once
   * @param {Object} settings - Settings to apply
   */
  applySettings(settings) {
    if (settings.brightness !== undefined) {
      this.setBrightness(settings.brightness);
    }
    if (settings.color !== undefined) {
      this.setColor(settings.color);
    }
    if (settings.transitionSpeed !== undefined) {
      this.setTransitionSpeed(settings.transitionSpeed);
    }
    if (settings.isOn !== undefined) {
      this.settings.isOn = settings.isOn;
      this._updateMirrorDisplay();
    }
  }
}

// Example usage:
// const mirror = document.getElementById('backlit-mirror');
// const controller = new BacklitMirrorController(mirror, {
//   defaultBrightness: 70,
//   defaultColor: '#ffcc00',
//   transitionSpeed: 500
// });
// controller.togglePower();
// controller.setBrightness(80);
// controller.setColor('#00ffcc');
```
