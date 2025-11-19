"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://passive-income.online
Prompt: Develop a JavaScript function that helps users share their income generation strategies on social media, leveraging the principles from the Wealthery training.
Generated: DETERMINISTIC_9e489d0ab24e596c
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * shareIncomeStrategy - A function to help users share their income generation strategies
 * on social media using Wealthery principles.
 * 
 * @param {string} strategyText - The user's income generation strategy text.
 * @param {string} platform - Social media platform to share the strategy on. Supported: "Twitter", "Facebook", "LinkedIn".
 * @returns {void} - Logs success or error message to the console.
 */
function shareIncomeStrategy(strategyText, platform) {
  // Validate input parameters
  if (typeof strategyText !== 'string' || strategyText.trim() === '') {
    console.error('Error: Strategy text must be a non-empty string.');
    return;
  }

  const supportedPlatforms = ['Twitter', 'Facebook', 'LinkedIn'];

  if (!supportedPlatforms.includes(platform)) {
    console.error(
      `Error: Unsupported platform. Supported platforms are: ${supportedPlatforms.join(', ')}`
    );
    return;
  }

  // Generate a formatted message for sharing
  const message = `🚀 Here's my income generation strategy I learned from Wealthery: "${strategyText}". What do you think? 🤔`;

  try {
    // Dummy function to simulate sharing on social media
    const shareOnSocialMedia = (msg, socialPlatform) => {
      console.log(`Sharing on ${socialPlatform}: ${msg}`);
      // Simulate success response
      return true;
    };

    // Attempt to share the strategy
    const success = shareOnSocialMedia(message, platform);

    if (success) {
      console.log(`✅ Strategy successfully shared on ${platform}!`);
    } else {
      console.error(`❌ Failed to share strategy on ${platform}.`);
    }
  } catch (error) {
    // Catch unexpected errors
    console.error('An unexpected error occurred while sharing:', error.message);
  }
}

// Example usage:
// shareIncomeStrategy("Diversify income streams and invest in high-yield assets.", "Twitter");
```
