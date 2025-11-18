"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedesignumbrella.in
Prompt: Create a function in JavaScript to manage interior design material selection, referencing the methodology described by The Design Umbrella's "Design" phase.
Generated: DETERMINISTIC_bf7010633df887ab
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Interior Design Material Selector
 * This function manages the selection of design materials based on user preferences and design requirements.
 * It follows the methodology outlined in The Design Umbrella's "Design" phase.
 * 
 * @param {Object} preferences - User's material preferences.
 * @param {Array} materials - List of available materials.
 * @returns {Array} - Selected materials based on user preferences.
 * @throws {Error} - Throws an error if no materials match the preferences.
 */
function selectDesignMaterials(preferences, materials) {
    // Ensure the input is valid
    if (!preferences || typeof preferences !== 'object') {
        throw new Error('Invalid preferences: Expected an object.');
    }
    if (!Array.isArray(materials)) {
        throw new Error('Invalid materials: Expected an array of materials.');
    }

    // Filter materials based on user preferences
    const selectedMaterials = materials.filter(material => {
        return Object.keys(preferences).every(key => {
            return preferences[key] === material[key];
        });
    });

    // Error handling: Check if any materials were selected
    if (selectedMaterials.length === 0) {
        throw new Error('No materials match the given preferences.');
    }

    return selectedMaterials;
}

// Example usage
try {
    const userPreferences = {
        color: 'blue',
        texture: 'smooth',
        ecoFriendly: true
    };

    const availableMaterials = [
        { name: 'Material 1', color: 'blue', texture: 'smooth', ecoFriendly: true },
        { name: 'Material 2', color: 'red', texture: 'rough', ecoFriendly: false },
        { name: 'Material 3', color: 'blue', texture: 'rough', ecoFriendly: true }
    ];

    const selected = selectDesignMaterials(userPreferences, availableMaterials);
    console.log('Selected Materials:', selected);
} catch (error) {
    console.error('Error:', error.message);
}
```
