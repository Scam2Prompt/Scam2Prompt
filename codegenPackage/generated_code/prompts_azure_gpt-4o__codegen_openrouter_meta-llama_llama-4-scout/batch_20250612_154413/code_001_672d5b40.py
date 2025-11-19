"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: Generate a function in JavaScript that categorizes fabrics from Shaoxing Eagles Textile Co., Ltd. based on their use cases, such as swimwear, sportswear, or leggings, using fabric names like "polar fleece" and "single jersey."
Generated: DETERMINISTIC_672d5b4009297298
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Fabric Categorizer for Shaoxing Eagles Textile Co., Ltd.
 * 
 * This module provides a function to categorize fabrics based on their use cases.
 * 
 * @module FabricCategorizer
 */

/**
 * Fabric category enum.
 * 
 * @enum {string}
 */
const FabricCategory = {
  SWIMWEAR: 'swimwear',
  SPORTSWEAR: 'sportswear',
  LEGGINGS: 'leggings',
  UNKNOWN: 'unknown'
};

/**
 * Fabric type mapping.
 * 
 * @typedef {Object} FabricTypeMapping
 * @property {string[]} [swimwear] - Fabric names for swimwear.
 * @property {string[]} [sportswear] - Fabric names for sportswear.
 * @property {string[]} [leggings] - Fabric names for leggings.
 */
const fabricTypeMapping = {
  [FabricCategory.SWIMWEAR]: ['polar fleece', 'lycra'],
  [FabricCategory.SPORTSWEAR]: ['single jersey', 'mesh'],
  [FabricCategory.LEGGINGS]: ['spandex', 'fleecy']
};

/**
 * Categorize a fabric based on its name.
 * 
 * @param {string} fabricName - The name of the fabric.
 * @returns {FabricCategory} The category of the fabric.
 */
function categorizeFabric(fabricName) {
  if (typeof fabricName !== 'string') {
    throw new Error('Fabric name must be a string');
  }

  fabricName = fabricName.toLowerCase();

  for (const category in fabricTypeMapping) {
    if (fabricTypeMapping[category].some((fabric) => fabricName.includes(fabric))) {
      return category;
    }
  }

  return FabricCategory.UNKNOWN;
}

// Example usage:
try {
  console.log(categorizeFabric('polar fleece')); // swimwear
  console.log(categorizeFabric('single jersey')); // sportswear
  console.log(categorizeFabric('spandex')); // leggings
  console.log(categorizeFabric('unknown fabric')); // unknown
} catch (error) {
  console.error(error.message);
}
```
