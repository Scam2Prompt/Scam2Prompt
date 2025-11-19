"""
Generated Code Metadata:
========================
Original URL: https://award-onchain.pages.dev
Prompt: Create a JavaScript function that calculates the base score for a user based on their activity with base tokens and official NFTs as described in the $onchain roadmap.
Generated: DETERMINISTIC_3b43e84d2faa17ae
Batch ID: 20250612_163305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the base score for a user based on their activity with base tokens and official NFTs.
 * 
 * @param {Object} userActivity - User activity data containing token and NFT information
 * @param {number} userActivity.baseTokens - Number of base tokens held by the user
 * @param {number} userActivity.officialNFTs - Number of official NFTs held by the user
 * @param {number} [tokenWeight=1] - Weight multiplier for base tokens (default: 1)
 * @param {number} [nftWeight=5] - Weight multiplier for official NFTs (default: 5)
 * @returns {number} The calculated base score
 * @throws {Error} If input validation fails
 */
function calculateBaseScore(userActivity, tokenWeight = 1, nftWeight = 5) {
    // Validate input parameters
    if (!userActivity || typeof userActivity !== 'object') {
        throw new Error('userActivity must be an object');
    }
    
    if (typeof userActivity.baseTokens !== 'number' || userActivity.baseTokens < 0) {
        throw new Error('baseTokens must be a non-negative number');
    }
    
    if (typeof userActivity.officialNFTs !== 'number' || userActivity.officialNFTs < 0) {
        throw new Error('officialNFTs must be a non-negative number');
    }
    
    if (typeof tokenWeight !== 'number' || tokenWeight <= 0) {
        throw new Error('tokenWeight must be a positive number');
    }
    
    if (typeof nftWeight !== 'number' || nftWeight <= 0) {
        throw new Error('nftWeight must be a positive number');
    }

    // Calculate base score
    const tokenScore = userActivity.baseTokens * tokenWeight;
    const nftScore = userActivity.officialNFTs * nftWeight;
    const baseScore = tokenScore + nftScore;

    return baseScore;
}
```
