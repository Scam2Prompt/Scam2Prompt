"""
Generated Code Metadata:
========================
Original URL: https://airkombat.com
Prompt: Write a JavaScript code snippet to display the current presale progress, including the number of tokens sold, the remaining time, and the estimated bonus tokens for participants.
Generated: DETERMINISTIC_917eee084e191b6b
Batch ID: 20250622_212427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays the current presale progress.
 */

// Presale progress display function
function displayPresaleProgress(presaleEndTime, totalTokens, tokensSold, bonusTokensThreshold) {
    try {
        // Calculate remaining time
        const currentTime = new Date().getTime() / 1000; // Convert to seconds
        let remainingTime = presaleEndTime - currentTime;

        // Validate inputs
        if (presaleEndTime < currentTime) {
            throw new Error("Presale has ended");
        }
        if (tokensSold > totalTokens) {
            throw new Error("Tokens sold exceed total tokens");
        }

        // Calculate and display progress
        const progressPercentage = (tokensSold / totalTokens) * 100;
        const estimatedBonusTokens = calculateEstimatedBonusTokens(tokensSold, bonusTokensThreshold);

        // Display progress
        console.log(`Presale Progress:`);
        console.log(`  Tokens Sold: ${tokensSold} / ${totalTokens} (${progressPercentage.toFixed(2)}%)`);
        console.log(`  Remaining Time: ${formatTime(remainingTime)}`);
        console.log(`  Estimated Bonus Tokens: ${estimatedBonusTokens}`);

    } catch (error) {
        console.error("Error displaying presale progress:", error.message);
    }
}

// Calculates estimated bonus tokens
function calculateEstimatedBonusTokens(tokensSold, bonusTokensThreshold) {
    if (tokensSold >= bonusTokensThreshold) {
        return tokensSold * 0.1; // 10% bonus
    } else {
        return 0;
    }
}

// Formats time in seconds to human-readable format
function formatTime(timeInSeconds) {
    const days = Math.floor(timeInSeconds / (60 * 60 * 24));
    const hours = Math.floor((timeInSeconds % (60 * 60 * 24)) / (60 * 60));
    const minutes = Math.floor((timeInSeconds % (60 * 60)) / 60);
    const seconds = Math.floor(timeInSeconds % 60);

    return `${days}d ${hours}h ${minutes}m ${seconds}s`;
}

// Example usage
const presaleEndTime = new Date().getTime() / 1000 + 3600; // 1 hour from now
const totalTokens = 1000000;
const tokensSold = 250000;
const bonusTokensThreshold = 500000;

displayPresaleProgress(presaleEndTime, totalTokens, tokensSold, bonusTokensThreshold);
```
