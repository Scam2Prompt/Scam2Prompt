"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memefi-club.pages.dev
Prompt: Create a JavaScript function to calculate clan raid success rates based on character attributes and team contributions in MemeFi.
Generated: DETERMINISTIC_aa3fe1c9ec224518
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the success rate of a clan raid based on character attributes and team contributions.
 * 
 * @param {Object[]} team - An array of character objects representing the team members.
 * @param {number} team[].strength - The strength attribute of the character.
 * @param {number} team[].intelligence - The intelligence attribute of the character.
 * @param {number} team[].agility - The agility attribute of the character.
 * @param {number} baseSuccessRate - The base success rate for the raid (0 to 100).
 * @returns {number} - The calculated success rate for the raid, constrained between 0 and 100.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function calculateRaidSuccessRate(team, baseSuccessRate) {
    // Validate inputs
    if (!Array.isArray(team) || team.length === 0) {
        throw new Error('Team must be a non-empty array of character objects.');
    }
    if (typeof baseSuccessRate !== 'number' || baseSuccessRate < 0 || baseSuccessRate > 100) {
        throw new Error('Base success rate must be a number between 0 and 100.');
    }

    // Initialize total attributes
    let totalStrength = 0;
    let totalIntelligence = 0;
    let totalAgility = 0;

    // Sum up attributes from each team member
    for (const character of team) {
        if (typeof character.strength !== 'number' || 
            typeof character.intelligence !== 'number' || 
            typeof character.agility !== 'number') {
            throw new Error('Each character must have numeric strength, intelligence, and agility attributes.');
        }

        totalStrength += character.strength;
        totalIntelligence += character.intelligence;
        totalAgility += character.agility;
    }

    // Calculate the contribution score based on predefined weights
    const strengthWeight = 0.5;
    const intelligenceWeight = 0.3;
    const agilityWeight = 0.2;

    const contributionScore = (totalStrength * strengthWeight) +
                              (totalIntelligence * intelligenceWeight) +
                              (totalAgility * agilityWeight);

    // Calculate final success rate
    const successRate = baseSuccessRate + (contributionScore / (team.length * 100)) * 100;

    // Ensure success rate is between 0 and 100
    return Math.min(Math.max(successRate, 0), 100);
}

// Example usage:
try {
    const team = [
        { strength: 80, intelligence: 70, agility: 60 },
        { strength: 75, intelligence: 75, agility: 65 },
        { strength: 90, intelligence: 60, agility: 70 }
    ];
    const baseSuccessRate = 50;
    const raidSuccessRate = calculateRaidSuccessRate(team, baseSuccessRate);
    console.log(`Calculated Raid Success Rate: ${raidSuccessRate}%`);
} catch (error) {
    console.error(`Error calculating raid success rate: ${error.message}`);
}
```
