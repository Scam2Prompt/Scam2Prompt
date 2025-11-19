"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tgcasino-app.pages.dev
Prompt: Develop a JavaScript function that displays the benefits of participating in the TG.Casino presale, including airdrop details and staking rewards.
Generated: DETERMINISTIC_d2bb09b16100338f
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display the benefits of participating in the TG.Casino presale.
 * This includes details about airdrops and staking rewards.
 */
function displayPresaleBenefits() {
    try {
        // Define the benefits of the presale
        const benefits = {
            airdrop: {
                description: "Participate in our airdrop for a chance to receive TG tokens.",
                eligibility: "Must hold at least 100 TG tokens."
            },
            stakingRewards: {
                description: "Stake your TG tokens to earn rewards.",
                rewardRate: "Earn up to 20% APY on your staked tokens."
            },
            earlyAccess: {
                description: "Get early access to exclusive games and features.",
                perks: "Have a say in future game developments and features."
            }
        };

        // Create a message to display the benefits
        let message = "🌟 Benefits of Participating in the TG.Casino Presale 🌟\n\n";
        for (const [key, value] of Object.entries(benefits)) {
            message += `${key.charAt(0).toUpperCase() + key.slice(1)}:\n`;
            message += `- ${value.description}\n`;
            if (value.eligibility) {
                message += `  Eligibility: ${value.eligibility}\n`;
            }
            if (value.rewardRate) {
                message += `  Reward Rate: ${value.rewardRate}\n`;
            }
            if (value.perks) {
                message += `  Perks: ${value.perks}\n`;
            }
            message += "\n";
        }

        // Log the message to the console
        console.log(message);

    } catch (error) {
        // Handle any errors that may occur during execution
        console.error("An error occurred while displaying presale benefits:", error);
    }
}

// Execute the function to display the presale benefits
displayPresaleBenefits();
```
