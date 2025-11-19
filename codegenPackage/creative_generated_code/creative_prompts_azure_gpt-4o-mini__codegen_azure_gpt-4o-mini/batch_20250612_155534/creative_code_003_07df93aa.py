"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reward-beamtoken.net
Prompt: Develop a JavaScript function that implements IKEA's sleep essentials recommendations for a bedroom layout.
Generated: DETERMINISTIC_07df93aad0fe2dc9
Batch ID: 20250612_155534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * IKEA Sleep Essentials Bedroom Layout Recommendation Function
 * 
 * This function generates a recommended layout for a bedroom based on IKEA's sleep essentials.
 * It takes into account the room dimensions, preferred bed size, and any additional furniture.
 * 
 * @param {number} width - The width of the bedroom in meters.
 * @param {number} length - The length of the bedroom in meters.
 * @param {string} bedSize - The preferred bed size ('single', 'double', 'queen', 'king').
 * @param {Array<string>} furniture - An array of additional furniture items (e.g., ['nightstand', 'dresser']).
 * @returns {string} - A recommendation message for the bedroom layout.
 * @throws {Error} - Throws an error if the dimensions are not valid or if the bed size is unsupported.
 */
function recommendBedroomLayout(width, length, bedSize, furniture) {
    // Validate input dimensions
    if (typeof width !== 'number' || width <= 0) {
        throw new Error('Invalid width provided. It must be a positive number.');
    }
    if (typeof length !== 'number' || length <= 0) {
        throw new Error('Invalid length provided. It must be a positive number.');
    }
    
    // Supported bed sizes
    const supportedBedSizes = ['single', 'double', 'queen', 'king'];
    
    if (!supportedBedSizes.includes(bedSize)) {
        throw new Error(`Unsupported bed size: ${bedSize}. Supported sizes are: ${supportedBedSizes.join(', ')}.`);
    }

    // Basic layout recommendations based on bed size
    let bedDimensions = {
        'single': { width: 0.9, length: 1.9 },
        'double': { width: 1.4, length: 1.9 },
        'queen': { width: 1.6, length: 2.0 },
        'king': { width: 1.8, length: 2.0 }
    };

    const bedWidth = bedDimensions[bedSize].width;
    const bedLength = bedDimensions[bedSize].length;

    // Suggesting layout positioning
    let layout = `For a ${bedSize} bed (dimensions: ${bedWidth}m x ${bedLength}m):\n`;
    layout += `- Place the bed against the longest wall for optimal space usage.\n`;

    // Check additional furniture placement
    if (furniture && furniture.length > 0) {
        layout += `- Consider the following furniture:\n`;
        furniture.forEach(item => {
            layout += `  * ${item}\n`;
            switch (item.toLowerCase()) {
                case 'nightstand':
                    layout += `    - Place nightstands on either side of the bed if space allows.\n`;
                    break;
                case 'dresser':
                    layout += `    - Position dressers against a wall that doesn't block pathways.\n`;
                    break;
                default:
                    layout += `    - Ensure ${item} placement does not obstruct movement.\n`;
            }
        });
    } else {
        layout += `- No additional furniture specified.\n`;
    }

    layout += `- Ensure a minimum of 0.6m clearance around the bed for easy access.`;

    return layout;
}

// Example usage (commented out to avoid execution during import)
// try {
//     console.log(recommendBedroomLayout(4, 5, 'queen', ['nightstand', 'dresser']));
// } catch (error) {
//     console.error(error.message);
// }
```
