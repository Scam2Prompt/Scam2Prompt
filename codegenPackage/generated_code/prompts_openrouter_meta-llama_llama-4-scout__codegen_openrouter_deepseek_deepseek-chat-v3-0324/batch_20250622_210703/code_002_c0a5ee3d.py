"""
Generated Code Metadata:
========================
Original URL: https://yury.lt
Prompt: Generate a code example in JavaScript to create a simple hair color calculator that suggests suitable hair colors based on a client's skin tone and natural hair color.
Generated: DETERMINISTIC_c0a5ee3d83620d4d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Hair Color Calculator
 * 
 * This module provides functionality to suggest suitable hair colors
 * based on a client's skin tone and natural hair color.
 */

// Skin tone categories
const SKIN_TONE = {
    FAIR: 'fair',
    LIGHT: 'light',
    MEDIUM: 'medium',
    OLIVE: 'olive',
    DARK: 'dark',
    DEEP: 'deep'
};

// Natural hair color categories
const HAIR_COLOR = {
    BLACK: 'black',
    BROWN: 'brown',
    BLONDE: 'blonde',
    RED: 'red',
    GRAY: 'gray'
};

// Hair color suggestions mapped by skin tone and natural hair color
const COLOR_SUGGESTIONS = {
    [SKIN_TONE.FAIR]: {
        [HAIR_COLOR.BLACK]: ['Platinum Blonde', 'Ash Brown', 'Pastel Pink'],
        [HAIR_COLOR.BROWN]: ['Golden Blonde', 'Caramel', 'Honey'],
        [HAIR_COLOR.BLONDE]: ['Champagne', 'Beige Blonde', 'Icy Blonde'],
        [HAIR_COLOR.RED]: ['Strawberry Blonde', 'Copper', 'Auburn'],
        [HAIR_COLOR.GRAY]: ['Silver', 'Platinum', 'Ash Blonde']
    },
    [SKIN_TONE.LIGHT]: {
        [HAIR_COLOR.BLACK]: ['Dark Chocolate', 'Espresso', 'Cool Black'],
        [HAIR_COLOR.BROWN]: ['Honey Brown', 'Golden Brown', 'Chestnut'],
        [HAIR_COLOR.BLONDE]: ['Golden Blonde', 'Buttercream', 'Sandy Blonde'],
        [HAIR_COLOR.RED]: ['Copper', 'Ginger', 'Mahogany'],
        [HAIR_COLOR.GRAY]: ['Pearl Blonde', 'Silver Gray', 'Ash Brown']
    },
    [SKIN_TONE.MEDIUM]: {
        [HAIR_COLOR.BLACK]: ['Blue Black', 'Dark Brown', 'Mocha'],
        [HAIR_COLOR.BROWN]: ['Caramel', 'Cinnamon', 'Bronze'],
        [HAIR_COLOR.BLONDE]: ['Honey Blonde', 'Warm Beige', 'Golden'],
        [HAIR_COLOR.RED]: ['Burgundy', 'Cherry Cola', 'Spiced Red'],
        [HAIR_COLOR.GRAY]: ['Salt & Pepper', 'Dark Ash', 'Taupe']
    },
    [SKIN_TONE.OLIVE]: {
        [HAIR_COLOR.BLACK]: ['Jet Black', 'Dark Espresso', 'Cool Brown'],
        [HAIR_COLOR.BROWN]: ['Warm Brown', 'Chestnut', 'Amber'],
        [HAIR_COLOR.BLONDE]: ['Golden Blonde', 'Honey', 'Warm Beige'],
        [HAIR_COLOR.RED]: ['Deep Auburn', 'Copper Red', 'Brick'],
        [HAIR_COLOR.GRAY]: ['Dark Gray', 'Charcoal', 'Smoky']
    },
    [SKIN_TONE.DARK]: {
        [HAIR_COLOR.BLACK]: ['Blue Black', 'Dark Brown', 'Espresso'],
        [HAIR_COLOR.BROWN]: ['Chocolate', 'Chestnut', 'Mahogany'],
        [HAIR_COLOR.BLONDE]: ['Golden Brown', 'Caramel', 'Bronde'],
        [HAIR_COLOR.RED]: ['Burgundy', 'Deep Red', 'Wine'],
        [HAIR_COLOR.GRAY]: ['Silver', 'Platinum', 'Graphite']
    },
    [SKIN_TONE.DEEP]: {
        [HAIR_COLOR.BLACK]: ['Jet Black', 'Blue Black', 'Cool Black'],
        [HAIR_COLOR.BROWN]: ['Dark Chocolate', 'Espresso', 'Mahogany'],
        [HAIR_COLOR.BLONDE]: ['Golden Brown', 'Honey', 'Caramel'],
        [HAIR_COLOR.RED]: ['Deep Burgundy', 'Cherry', 'Ruby'],
        [HAIR_COLOR.GRAY]: ['Silver', 'Platinum', 'Graphite']
    }
};

/**
 * Validates input parameters
 * @param {string} skinTone - Client's skin tone
 * @param {string} naturalHairColor - Client's natural hair color
 * @throws {Error} If parameters are invalid
 */
function validateInput(skinTone, naturalHairColor) {
    if (!Object.values(SKIN_TONE).includes(skinTone)) {
        throw new Error(`Invalid skin tone. Must be one of: ${Object.values(SKIN_TONE).join(', ')}`);
    }
    
    if (!Object.values(HAIR_COLOR).includes(naturalHairColor)) {
        throw new Error(`Invalid hair color. Must be one of: ${Object.values(HAIR_COLOR).join(', ')}`);
    }
}

/**
 * Gets hair color suggestions based on skin tone and natural hair color
 * @param {string} skinTone - Client's skin tone
 * @param {string} naturalHairColor - Client's natural hair color
 * @returns {string[]} Array of suggested hair colors
 * @throws {Error} If parameters are invalid
 */
function getHairColorSuggestions(skinTone, naturalHairColor) {
    try {
        validateInput(skinTone, naturalHairColor);
        return COLOR_SUGGESTIONS[skinTone][naturalHairColor] || [];
    } catch (error) {
        console.error('Error getting hair color suggestions:', error.message);
        throw error;
    }
}

// Export the functionality for external use
module.exports = {
    SKIN_TONE,
    HAIR_COLOR,
    getHairColorSuggestions
};
```
