"""
Generated Code Metadata:
========================
Original URL: https://stockyardrefacing.com
Prompt: "Design a custom cabinet door using a programming language like JavaScript, considering the custom solutions provided by Stockyard Refacing for kitchens and bathrooms."
Generated: DETERMINISTIC_27dcd3a25d5f413d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * CustomCabinetDoorDesigner - A utility to design custom cabinet doors
 * based on specifications similar to Stockyard Refacing solutions.
 */

class CustomCabinetDoorDesigner {
  /**
   * @param {Object} options - Configuration options for the cabinet door
   * @param {number} options.width - Width of the door in inches
   * @param {number} options.height - Height of the door in inches
   * @param {string} options.material - Material type (e.g., 'wood', 'mdf', 'glass')
   * @param {string} options.style - Door style (e.g., 'shaker', 'raised_panel', 'slab')
   * @param {string} options.color - Color/finish of the door
   * @param {boolean} [options.withHardware=false] - Whether to include hardware
   */
  constructor(options) {
    this.validateOptions(options);
    
    this.width = options.width;
    this.height = options.height;
    this.material = options.material;
    this.style = options.style;
    this.color = options.color;
    this.withHardware = options.withHardware || false;
    this.hardwareType = options.hardwareType || 'knob';
    this.doorId = this.generateDoorId();
  }

  /**
   * Validates the input options
   * @param {Object} options - The options to validate
   * @throws {Error} If any required option is missing or invalid
   */
  validateOptions(options) {
    const requiredFields = ['width', 'height', 'material', 'style', 'color'];
    for (const field of requiredFields) {
      if (!options[field]) {
        throw new Error(`Missing required field: ${field}`);
      }
    }

    if (typeof options.width !== 'number' || options.width <= 0) {
      throw new Error('Width must be a positive number');
    }

    if (typeof options.height !== 'number' || options.height <= 0) {
      throw new Error('Height must be a positive number');
    }

    const validMaterials = ['wood', 'mdf', 'glass', 'metal'];
    if (!validMaterials.includes(options.material)) {
      throw new Error(`Invalid material. Must be one of: ${validMaterials.join(', ')}`);
    }

    const validStyles = ['shaker', 'raised_panel', 'slab', 'louvered', 'glass_insert'];
    if (!validStyles.includes(options.style)) {
      throw new Error(`Invalid style. Must be one of: ${validStyles.join(', ')}`);
    }
  }

  /**
   * Generates a unique ID for the door design
   * @returns {string} A unique door ID
   */
  generateDoorId() {
    return `door-${Date.now()}-${Math.floor(Math.random() * 1000)}`;
  }

  /**
   * Calculates the area of the door
   * @returns {number} Area in square inches
   */
  calculateArea() {
    return this.width * this.height;
  }

  /**
   * Generates a preview of the door design
   * @returns {Object} Door design specifications
   */
  generateDesignPreview() {
    return {
      id: this.doorId,
      dimensions: {
        width: this.width,
        height: this.height,
        area: this.calculateArea()
      },
      material: this.material,
      style: this.style,
      color: this.color,
      hardware: this.withHardware ? this.hardwareType : 'none',
      createdAt: new Date().toISOString()
    };
  }

  /**
   * Updates the door dimensions
   * @param {number} width - New width in inches
   * @param {number} height - New height in inches
   */
  updateDimensions(width, height) {
    if (width <= 0 || height <= 0) {
      throw new Error('Dimensions must be positive numbers');
    }
    this.width = width;
    this.height = height;
  }

  /**
   * Changes the door style
   * @param {string} newStyle - New door style
   */
  changeStyle(newStyle) {
    const validStyles = ['shaker', 'raised_panel', 'slab', 'louvered', 'glass_insert'];
    if (!validStyles.includes(newStyle)) {
      throw new Error(`Invalid style. Must be one of: ${validStyles.join(', ')}`);
    }
    this.style = newStyle;
  }

  /**
   * Adds hardware to the door
   * @param {string} [type='knob'] - Type of hardware (knob or pull)
   */
  addHardware(type = 'knob') {
    this.withHardware = true;
    this.hardwareType = type;
  }

  /**
   * Removes hardware from the door
   */
  removeHardware() {
    this.withHardware = false;
    this.hardwareType = null;
  }
}

// Example usage
try {
  const doorDesigner = new CustomCabinetDoorDesigner({
    width: 24,
    height: 30,
    material: 'wood',
    style: 'shaker',
    color: 'white',
    withHardware: true
  });

  console.log('Door Design Preview:', doorDesigner.generateDesignPreview());

  // Update dimensions
  doorDesigner.updateDimensions(26, 32);
  console.log('Updated Design:', doorDesigner.generateDesignPreview());

  // Change style
  doorDesigner.changeStyle('raised_panel');
  console.log('Changed Style:', doorDesigner.generateDesignPreview());

} catch (error) {
  console.error('Error designing cabinet door:', error.message);
}
```
