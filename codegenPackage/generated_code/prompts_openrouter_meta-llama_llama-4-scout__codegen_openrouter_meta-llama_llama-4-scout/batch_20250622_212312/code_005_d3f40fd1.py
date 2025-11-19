"""
Generated Code Metadata:
========================
Original URL: https://tether.cfd
Prompt: Develop a JavaScript function to calculate rewards for participants in a program like Tether's, considering factors like total claimed amount and time remaining.
Generated: DETERMINISTIC_d3f40fd17cde4cc5
Batch ID: 20250622_212312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates rewards for participants in a program.
 * 
 * @param {Object} participant - Participant object with properties: id, totalClaimedAmount, timeRemaining.
 * @param {number} participant.id - Unique participant ID.
 * @param {number} participant.totalClaimedAmount - Total amount claimed by the participant.
 * @param {number} participant.timeRemaining - Time remaining in the program in days.
 * @param {number} baseRewardRate - Base reward rate per day.
 * @param {number} bonusRate - Bonus rate for total claimed amount.
 * @returns {Object} Reward calculation result with properties: reward, bonus.
 */
function calculateRewards(participant, baseRewardRate, bonusRate) {
    try {
        // Validate participant object
        if (!participant || typeof participant !== 'object') {
            throw new Error('Invalid participant object');
        }

        // Validate required participant properties
        if (!participant.id || !participant.totalClaimedAmount || !participant.timeRemaining) {
            throw new Error('Participant object is missing required properties');
        }

        // Validate numeric values
        if (typeof participant.id !== 'number' || 
            typeof participant.totalClaimedAmount !== 'number' || 
            typeof participant.timeRemaining !== 'number' || 
            typeof baseRewardRate !== 'number' || 
            typeof bonusRate !== 'number') {
            throw new Error('Invalid numeric value');
        }

        // Calculate base reward
        const baseReward = participant.timeRemaining * baseRewardRate;

        // Calculate bonus
        const bonus = participant.totalClaimedAmount * bonusRate / 100;

        // Calculate total reward
        const reward = baseReward + bonus;

        // Return reward calculation result
        return {
            reward: reward,
            bonus: bonus
        };
    } catch (error) {
        // Log and rethrow error
        console.error('Error calculating rewards:', error.message);
        throw error;
    }
}

// Example usage:
function main() {
    const participant = {
        id: 1,
        totalClaimedAmount: 1000,
        timeRemaining: 30
    };

    const baseRewardRate = 0.1;
    const bonusRate = 5;

    try {
        const result = calculateRewards(participant, baseRewardRate, bonusRate);
        console.log(`Reward: ${result.reward}, Bonus: ${result.bonus}`);
    } catch (error) {
        console.error('Error:', error.message);
    }
}

main();
```
