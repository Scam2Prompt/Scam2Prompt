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
 * Recommend Engel cooler models based on user needs.
 * 
 * @param {Object} preferences - User preferences.
 * @param {boolean} preferences.portability - Whether portability is a priority.
 * @param {number} preferences.iceRetention - Desired ice retention duration in days.
 * @returns {Array} Recommended Engel cooler models.
 */
function recommendCoolers(preferences) {
    // Validate input
    if (typeof preferences !== 'object' || preferences === null) {
        throw new Error("Invalid preferences object.");
    }
    if (typeof preferences.portability !== 'boolean') {
        throw new Error("Portability must be a boolean value.");
    }
    if (typeof preferences.iceRetention !== 'number' || preferences.iceRetention <= 0) {
        throw new Error("Ice retention must be a positive number.");
    }

    // List of Engel cooler models with their specifications
    const coolers = [
        { model: "Engel UC19", portability: true, iceRetention: 3 },
        { model: "Engel UC30", portability: true, iceRetention: 4 },
        { model: "Engel HD30", portability: true, iceRetention: 5 },
        { model: "Engel MR040", portability: false, iceRetention: 6 },
        { model: "Engel MT45", portability: false, iceRetention: 8 },
        { model: "Engel MT60", portability: false, iceRetention: 10 }
    ];

    // Filter cooler models based on user preferences
    const recommendedCoolers = coolers.filter(cooler => {
        const matchesPortability = preferences.portability === cooler.portability;
        const matchesIceRetention = preferences.iceRetention <= cooler.iceRetention;
        return matchesPortability && matchesIceRetention;
    });

    // Return the recommended models
    return recommendedCoolers.map(cooler => cooler.model);
}

// Example usage:
try {
    const userPreferences = { portability: true, iceRetention: 4 };
    const recommendations = recommendCoolers(userPreferences);
    console.log("Recommended Coolers:", recommendations);
} catch (error) {
    console.error("Error:", error.message);
}
```
