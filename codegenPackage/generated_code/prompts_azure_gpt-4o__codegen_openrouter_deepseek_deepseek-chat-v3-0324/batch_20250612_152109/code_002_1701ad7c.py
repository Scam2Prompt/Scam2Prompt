"""
Generated Code Metadata:
========================
Original URL: https://udizine.com
Prompt: Generate JavaScript code to dynamically adjust the display configurations of UDIZINE's SlatStrip system based on user input for shelf depth and hanging rail requirements.
Generated: DETERMINISTIC_1701ad7cdd009dcd
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * UDIZINE SlatStrip Configuration Adjuster
 * Dynamically adjusts display configurations based on shelf depth and hanging rail requirements.
 */

class SlatStripConfigurator {
  /**
   * Initialize the configurator with default values
   * @param {Object} options - Configuration options
   * @param {number} options.defaultShelfDepth - Default shelf depth in mm
   * @param {boolean} options.defaultHangingRail - Default hanging rail requirement
   */
  constructor(options = {}) {
    this.defaults = {
      shelfDepth: options.defaultShelfDepth || 300,
      hasHangingRail: options.defaultHangingRail || false
    };
    this.currentConfig = { ...this.defaults };
    this.validDepths = [200, 250, 300, 350, 400, 450, 500];
    this.components = {
      slatStrip: { length: 1000, quantity: 1 },
      brackets: { quantity: 2 },
      hangingRail: { length: 1000, quantity: 0 }
    };
  }

  /**
   * Validate and set shelf depth
   * @param {number} depth - Shelf depth in mm
   * @throws {Error} If depth is invalid
   */
  setShelfDepth(depth) {
    if (!this.validDepths.includes(depth)) {
      throw new Error(`Invalid shelf depth. Valid depths are: ${this.validDepths.join(', ')} mm`);
    }
    this.currentConfig.shelfDepth = depth;
    this._updateBracketQuantity();
  }

  /**
   * Set hanging rail requirement
   * @param {boolean} required - Whether hanging rail is needed
   */
  setHangingRail(required) {
    this.currentConfig.hasHangingRail = required;
    this._updateHangingRailQuantity();
  }

  /**
   * Update bracket quantity based on shelf depth
   * @private
   */
  _updateBracketQuantity() {
    const { shelfDepth } = this.currentConfig;
    this.components.brackets.quantity = shelfDepth <= 300 ? 2 : 3;
  }

  /**
   * Update hanging rail quantity based on requirement
   * @private
   */
  _updateHangingRailQuantity() {
    this.components.hangingRail.quantity = this.currentConfig.hasHangingRail ? 1 : 0;
  }

  /**
   * Get current configuration
   * @returns {Object} Current configuration
   */
  getConfiguration() {
    return {
      ...this.currentConfig,
      components: { ...this.components }
    };
  }

  /**
   * Reset to default configuration
   */
  reset() {
    this.currentConfig = { ...this.defaults };
    this._updateBracketQuantity();
    this._updateHangingRailQuantity();
  }
}

// Example usage:
try {
  const configurator = new SlatStripConfigurator({
    defaultShelfDepth: 350,
    defaultHangingRail: true
  });

  // Update configuration based on user input
  configurator.setShelfDepth(400);
  configurator.setHangingRail(false);

  // Get current configuration
  const currentConfig = configurator.getConfiguration();
  console.log('Current Configuration:', currentConfig);

} catch (error) {
  console.error('Configuration Error:', error.message);
}
```
