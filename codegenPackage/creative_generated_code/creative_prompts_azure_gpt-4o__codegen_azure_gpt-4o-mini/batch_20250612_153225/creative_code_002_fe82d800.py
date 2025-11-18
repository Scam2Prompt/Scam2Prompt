"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xeluudong.com
Prompt: Create a function in JavaScript that calculates the optimal placement of furniture in a room based on feng shui principles, such as avoiding placing a desk directly opposite a bed.
Generated: DETERMINISTIC_fe82d800883d8b55
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates optimal furniture placement based on feng shui principles.
 * 
 * @param {Object} room - An object representing the room dimensions and furniture.
 * @param {number} room.width - The width of the room.
 * @param {number} room.length - The length of the room.
 * @param {Array} furniture - An array of furniture objects.
 * @returns {Array} - An array of recommended furniture placements.
 * 
 * @throws {Error} - Throws an error if room dimensions are invalid or if furniture is not an array.
 */
function calculateFengShuiPlacement(room, furniture) {
    // Validate input
    if (typeof room !== 'object' || room === null || !Array.isArray(furniture)) {
        throw new Error("Invalid input: room must be an object and furniture must be an array.");
    }

    const { width, length } = room;

    if (typeof width !== 'number' || typeof length !== 'number' || width <= 0 || length <= 0) {
        throw new Error("Invalid room dimensions: width and length must be positive numbers.");
    }

    // Feng shui principles to consider
    const recommendations = [];

    furniture.forEach((item) => {
        // Validate each furniture item
        if (typeof item !== 'object' || item === null || !item.position) {
            throw new Error("Invalid furniture item: each item must be an object with a position.");
        }

        const { type, position } = item;
        const { x, y } = position;

        // Check if the item position is within the room boundaries
        if (x < 0 || x > width || y < 0 || y > length) {
            throw new Error(`Invalid position for ${type}: position must be within room boundaries.`);
        }

        // Feng shui rule: avoid placing desk directly opposite of the bed
        if (type === 'desk') {
            const bedIndex = furniture.findIndex(f => f.type === 'bed');
            if (bedIndex !== -1) {
                const bedPosition = furniture[bedIndex].position;
                // Check if desk is opposite of bed
                if (Math.abs(bedPosition.x - x) < 1 && Math.abs(bedPosition.y - y) < 1) {
                    recommendations.push({ item: type, recommendation: "Move desk away from being directly opposite bed." });
                }
            }
        }

        // Additional feng shui rules can be added here
        recommendations.push({ item: type, recommendation: "Placement is optimal." });
    });

    return recommendations;
}

// Example usage:
try {
    const room = { width: 10, length: 12 };
    const furniture = [
        { type: 'bed', position: { x: 5, y: 0 } },
        { type: 'desk', position: { x: 5, y: 1 } },
    ];

    const optimalPlacement = calculateFengShuiPlacement(room, furniture);
    console.log(optimalPlacement);
} catch (error) {
    console.error(error.message);
}
```
