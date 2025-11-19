"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Write a JavaScript function that recommends Engel cooler models based on user needs, such as portability and ice retention duration.
Generated: DETERMINISTIC_09297560cde47af1
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to recommend Engel cooler models based on user needs.
 * @param {boolean} isPortable - Indicates if portability is a priority.
 * @param {number} iceRetention - The desired ice retention duration in hours.
 * @returns {string[]} - An array of recommended Engel cooler models.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function recommendEngelCoolers(isPortable, iceRetention) {
    // Validate input types
    if (typeof isPortable !== 'boolean') {
        throw new Error('Invalid input: isPortable must be a boolean.');
    }
    if (typeof iceRetention !== 'number' || iceRetention <= 0) {
        throw new Error('Invalid input: iceRetention must be a positive number.');
    }
    
    // Define Engel cooler models with features
    const coolers = [
        { model: 'Engel 19', portable: true, iceRetention: 3 },
        { model: 'Engel 30', portable: true, iceRetention: 4 },
        { model: 'Engel 40', portable: false, iceRetention: 5 },
        { model: 'Engel 65', portable: false, iceRetention: 7 },
        { model: 'Engel 80', portable: false, iceRetention: 10 },
        { model: 'Engel 95', portable: false, iceRetention: 12 }
    ];

    // Filter coolers based on user needs
    return coolers.filter(cooler => 
        (isPortable ? cooler.portable : !cooler.portable) && 
        cooler.iceRetention >= iceRetention
    ).map(cooler => cooler.model);
}

// Example usage (uncomment to run):
// try {
//     console.log(recommendEngelCoolers(true, 4)); // Expected output: ['Engel 30']
// } catch (error) {
//     console.error(error.message);
// }
```
