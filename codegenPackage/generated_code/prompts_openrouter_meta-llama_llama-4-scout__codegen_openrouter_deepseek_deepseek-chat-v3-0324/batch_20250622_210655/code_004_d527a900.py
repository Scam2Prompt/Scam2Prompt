"""
Generated Code Metadata:
========================
Original URL: https://karenfixing.com
Prompt: "Create a JavaScript function to calculate the total surface area of a building facade that requires a dry facade system, given the dimensions of the building."
Generated: DETERMINISTIC_d527a9004ef5596b
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
 * Calculates the total surface area of a building facade for a dry facade system.
 * 
 * @param {Object} dimensions - An object containing the building dimensions.
 * @param {number} dimensions.height - The height of the building in meters.
 * @param {number} dimensions.width - The width of the building in meters.
 * @param {number} [dimensions.depth] - The depth of the building in meters (optional for rectangular buildings).
 * @param {number} [numFloors] - The number of floors (optional, defaults to 1).
 * @param {number} [windowArea] - The total area of windows/doors to subtract (optional).
 * @returns {number} The total surface area of the facade in square meters.
 * @throws {Error} If required parameters are missing or invalid.
 */
function calculateFacadeArea(dimensions, numFloors = 1, windowArea = 0) {
    // Validate input parameters
    if (!dimensions || typeof dimensions !== 'object') {
        throw new Error('Dimensions object is required');
    }
    
    const { height, width, depth } = dimensions;
    
    if (height == null || width == null) {
        throw new Error('Height and width are required');
    }
    
    if (typeof height !== 'number' || typeof width !== 'number' || 
        (depth != null && typeof depth !== 'number') ||
        typeof numFloors !== 'number' || typeof windowArea !== 'number') {
        throw new Error('All parameters must be numbers');
    }
    
    if (height <= 0 || width <= 0 || (depth != null && depth <= 0) || 
        numFloors <= 0 || windowArea < 0) {
        throw new Error('All values must be positive numbers');
    }
    
    // Calculate total height considering floors
    const totalHeight = height * numFloors;
    
    // Calculate facade area based on building shape
    let facadeArea;
    if (depth != null) {
        // Rectangular building: 2 sides (width) + 2 sides (depth)
        facadeArea = 2 * (width * totalHeight) + 2 * (depth * totalHeight);
    } else {
        // Simple wall (only width and height)
        facadeArea = width * totalHeight;
    }
    
    // Subtract window/door area if provided
    const totalArea = facadeArea - windowArea;
    
    // Ensure result is not negative
    return Math.max(0, totalArea);
}

// Example usage:
// const dimensions = { height: 3, width: 10, depth: 8 };
// const area = calculateFacadeArea(dimensions, 5, 20);
// console.log(`Total facade area: ${area} m²`);
```
