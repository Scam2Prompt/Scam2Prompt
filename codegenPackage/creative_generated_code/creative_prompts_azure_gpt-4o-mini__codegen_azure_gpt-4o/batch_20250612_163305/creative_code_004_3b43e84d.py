"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://award-onchain.pages.dev
Prompt: Create a JavaScript function that calculates the base score for a user based on their activity with base tokens and official NFTs as described in the $onchain roadmap.
Generated: DETERMINISTIC_3b43e84d2faa17ae
Batch ID: 20250612_163305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the base score for a user based on activity with base tokens and official NFTs.
 * 
 * @param {Object} activity - User activity details.
 * @param {number} activity.baseTokens - Number of base tokens the user has.
 * @param {number} activity.officialNFTs - Number of official NFTs the user owns.
 * @returns {number} - The calculated base score for the user.
 * 
 * @throws {Error} - Throws error if invalid input is provided.
 */
function calculateBaseScore(activity) {
    // Validate input
    if (!activity || typeof activity !== 'object') {
        throw new Error("Invalid activity object provided.");
    }
    if (typeof activity.baseTokens !== 'number' || activity.baseTokens < 0) {
        throw new Error("Invalid number of base tokens.");
    }
    if (typeof activity.officialNFTs !== 'number' || activity.officialNFTs < 0) {
        throw new Error("Invalid number of official NFTs.");
    }

    // Constants for scoring
    const BASE_TOKEN_MULTIPLIER = 10; // Score per base token
    const OFFICIAL_NFT_MULTIPLIER = 50; // Score per official NFT

    // Calculate base score
    const baseScore = (activity.baseTokens * BASE_TOKEN_MULTIPLIER) +
                      (activity.officialNFTs * OFFICIAL_NFT_MULTIPLIER);

    // Return the final score
    return baseScore;
}

// Example usage
try {
    const userActivity = {
        baseTokens: 100,
        officialNFTs: 5
    };

    const score = calculateBaseScore(userActivity);
    console.log("User Base Score:", score); // Output: User Base Score: 1250
} catch (error) {
    console.error("Error:", error.message);
}
```
