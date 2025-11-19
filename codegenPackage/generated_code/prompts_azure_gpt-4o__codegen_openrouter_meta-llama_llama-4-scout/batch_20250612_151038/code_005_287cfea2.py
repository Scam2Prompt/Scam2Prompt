"""
Generated Code Metadata:
========================
Original URL: https://pacmonn.pages.dev
Prompt: Implement a JavaScript function to track and calculate $PAC earnings for creators based on their tweets about Pacmoon, following the earning model described on the website.
Generated: DETERMINISTIC_287cfea2aef9d9a8
Batch ID: 20250612_151038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates $PAC earnings for creators based on their tweets about Pacmoon.
 * 
 * The earning model is as follows:
 * - For tweets with 0-100 engagements (likes, retweets, replies), the creator earns $0.01 per engagement.
 * - For tweets with 101-1000 engagements, the creator earns $0.005 per engagement.
 * - For tweets with 1001+ engagements, the creator earns $0.001 per engagement.
 * 
 * @param {Object} tweet - The tweet object containing engagement data.
 * @param {number} tweet.engagements - The total number of engagements (likes, retweets, replies) on the tweet.
 * @return {number} The calculated $PAC earnings for the creator.
 */
function calculatePacEarnings(tweet) {
    // Check if the tweet object has the required engagement data
    if (!tweet || typeof tweet.engagements !== 'number') {
        throw new Error('Invalid tweet data');
    }

    let earningsPerEngagement;
    if (tweet.engagements <= 100) {
        // $0.01 per engagement for 0-100 engagements
        earningsPerEngagement = 0.01;
    } else if (tweet.engagements <= 1000) {
        // $0.005 per engagement for 101-1000 engagements
        earningsPerEngagement = 0.005;
    } else {
        // $0.001 per engagement for 1001+ engagements
        earningsPerEngagement = 0.001;
    }

    // Calculate the total earnings
    const totalEarnings = tweet.engagements * earningsPerEngagement;

    return totalEarnings;
}

/**
 * Tracks and calculates $PAC earnings for creators based on their tweets about Pacmoon.
 * 
 * @param {Array<Object>} tweets - An array of tweet objects containing engagement data.
 * @return {Object} An object containing the total $PAC earnings and a breakdown of earnings per tweet.
 */
function trackPacEarnings(tweets) {
    // Check if the input is an array of tweet objects
    if (!Array.isArray(tweets) || !tweets.every(tweet => typeof tweet === 'object')) {
        throw new Error('Invalid input data');
    }

    let totalEarnings = 0;
    const earningsBreakdown = [];

    // Iterate over each tweet and calculate earnings
    tweets.forEach((tweet, index) => {
        try {
            const earnings = calculatePacEarnings(tweet);
            totalEarnings += earnings;

            // Store the earnings breakdown per tweet
            earningsBreakdown.push({
                tweetIndex: index,
                engagements: tweet.engagements,
                earnings: earnings,
            });
        } catch (error) {
            // Handle any errors that occur during earnings calculation
            // eslint-disable-next-line no-console
            console.error(`Error calculating earnings for tweet ${index}:`, error);
        }
    });

    return {
        totalEarnings: totalEarnings,
        earningsBreakdown: earningsBreakdown,
    };
}

// Example usage:
const tweets = [
    { engagements: 50 },
    { engagements: 200 },
    { engagements: 1500 },
];

const pacEarnings = trackPacEarnings(tweets);
// eslint-disable-next-line no-console
console.log(pacEarnings);
```
