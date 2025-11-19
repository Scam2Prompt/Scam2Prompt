"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eharmony.co.uk
Prompt: Generate a JavaScript function that collects user preferences for dating (e.g., casual or serious relationships) and integrates them into a compatibility scoring algorithm like eharmony's.
Generated: DETERMINISTIC_1cdf2ad21d88b49a
Batch ID: 20250612_163912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Collects user preferences for dating and calculates a compatibility score.
 * 
 * @class UserPreferences
 */
class UserPreferences {
    constructor() {
        this.preferences = {
            relationshipType: '', // 'casual' or 'serious'
            interests: [],        // Array of user interests
            ageRange: {           // Age range preferences
                min: 18,
                max: 99
            },
            location: ''          // User's preferred location
        };
    }

    /**
     * Set the relationship type preference.
     * @param {string} type - Type of relationship ('casual' or 'serious').
     * @throws Will throw an error if the type is not valid.
     */
    setRelationshipType(type) {
        const validTypes = ['casual', 'serious'];
        if (!validTypes.includes(type)) {
            throw new Error('Invalid relationship type. Must be "casual" or "serious".');
        }
        this.preferences.relationshipType = type;
    }

    /**
     * Add interests to user preferences.
     * @param {string[]} interests - Array of interests to add.
     */
    addInterests(interests) {
        if (!Array.isArray(interests)) {
            throw new Error('Interests must be provided as an array.');
        }
        this.preferences.interests.push(...interests);
    }

    /**
     * Set the age range preference.
     * @param {number} min - Minimum age.
     * @param {number} max - Maximum age.
     * @throws Will throw an error if the age range is invalid.
     */
    setAgeRange(min, max) {
        if (min < 0 || max < 0 || min > max) {
            throw new Error('Invalid age range. Ensure min is less than max and both are non-negative.');
        }
        this.preferences.ageRange = { min, max };
    }

    /**
     * Set the location preference.
     * @param {string} location - User's preferred location.
     */
    setLocation(location) {
        if (typeof location !== 'string' || location.trim() === '') {
            throw new Error('Location must be a non-empty string.');
        }
        this.preferences.location = location;
    }

    /**
     * Calculate a compatibility score based on user preferences.
     * @param {Object} otherUser - Another user object with preferences.
     * @returns {number} - Compatibility score between 0 and 100.
     */
    calculateCompatibility(otherUser) {
        let score = 0;

        // Compare relationship types
        if (this.preferences.relationshipType === otherUser.preferences.relationshipType) {
            score += 50; // High score for matching relationship types
        }

        // Compare interests
        const commonInterests = this.preferences.interests.filter(interest => 
            otherUser.preferences.interests.includes(interest)
        ).length;
        const totalInterests = new Set([...this.preferences.interests, ...otherUser.preferences.interests]).size;
        score += (commonInterests / totalInterests) * 25; // Up to 25 points for shared interests
        
        // Compare age range
        if (otherUser.preferences.ageRange.min >= this.preferences.ageRange.min && 
            otherUser.preferences.ageRange.max <= this.preferences.ageRange.max) {
            score += 15; // Points for matching age range
        }

        // Compare location (simple match for now)
        if (this.preferences.location.toLowerCase() === otherUser.preferences.location.toLowerCase()) {
            score += 10; // Points for location match
        }

        // Ensure score is capped at 100
        return Math.min(score, 100);
    }
}

// Example usage
try {
    const user1 = new UserPreferences();
    user1.setRelationshipType('serious');
    user1.addInterests(['hiking', 'music', 'travel']);
    user1.setAgeRange(25, 35);
    user1.setLocation('New York');

    const user2 = new UserPreferences();
    user2.setRelationshipType('serious');
    user2.addInterests(['music', 'gaming', 'travel']);
    user2.setAgeRange(28, 32);
    user2.setLocation('New York');

    const compatibilityScore = user1.calculateCompatibility(user2);
    console.log(`Compatibility Score: ${compatibilityScore}`);
} catch (error) {
    console.error('Error:', error.message);
}
```
