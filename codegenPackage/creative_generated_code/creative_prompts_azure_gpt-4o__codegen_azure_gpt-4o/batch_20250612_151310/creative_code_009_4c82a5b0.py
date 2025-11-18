"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-edd.pages.dev
Prompt: Develop a JavaScript application that uses the DOGE20 tokenomics data to display the distribution of presale, marketing, treasury, staking rewards, and liquidity allocation.
Generated: DETERMINISTIC_4c82a5b0968f0386
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript application to display DOGE20 tokenomics distribution

// Distribution percentages for DOGE20 tokenomics
const tokenomicsDistribution = {
  presale: 30,       // Presale allocation percentage
  marketing: 20,     // Marketing allocation percentage
  treasury: 15,      // Treasury allocation percentage
  stakingRewards: 20,// Staking rewards allocation percentage
  liquidity: 15      // Liquidity allocation percentage
};

// Function to validate tokenomics percentages
function validateDistribution(distribution) {
  const totalPercentage = Object.values(distribution).reduce((sum, value) => sum + value, 0);
  if (totalPercentage !== 100) {
    throw new Error(`Invalid distribution: Total percentage must equal 100, found ${totalPercentage}`);
  }
}

// Function to display tokenomics distribution in a readable format
function displayTokenomics(distribution) {
  try {
    // Validate distribution before displaying
    validateDistribution(distribution);

    console.log("DOGE20 Tokenomics Distribution:");
    Object.entries(distribution).forEach(([category, percentage]) => {
      console.log(`${capitalize(category)}: ${percentage}%`);
    });
  } catch (error) {
    console.error("Error displaying tokenomics:", error.message);
  }
}

// Utility function to capitalize the first letter of a string
function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

// Main function to execute the application
function main() {
  console.log("Starting DOGE20 Tokenomics Application...");
  
  // Display tokenomics distribution
  displayTokenomics(tokenomicsDistribution);
}

// Execute the script
main();
```
