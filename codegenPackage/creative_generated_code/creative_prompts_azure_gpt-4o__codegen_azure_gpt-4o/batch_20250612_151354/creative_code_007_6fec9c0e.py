"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bearsontheblock.com
Prompt: Write a JavaScript program to display the details of "Bears On The Block" islands, including marketplace items and community stats.
Generated: DETERMINISTIC_6fec9c0ecb1f2838
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript program to display details of "Bears On The Block" islands,
// including marketplace items and community stats.
// This program uses mock data and simulates the behavior for demonstration purposes.

/**
 * Mock data for islands, marketplace items, and community stats.
 */
const islands = [
  {
    id: 1,
    name: "Honeycomb Haven",
    description: "A lush island where bears cultivate honey.",
    marketplaceItems: [
      { itemName: "Honey Jar", price: 10 },
      { itemName: "Beehive", price: 25 },
    ],
    communityStats: {
      totalBears: 150,
      activeUsers: 75,
    },
  },
  {
    id: 2,
    name: "Bearclaw Bay",
    description: "An adventurous island for fishing and exploration.",
    marketplaceItems: [
      { itemName: "Fishing Rod", price: 15 },
      { itemName: "Treasure Map", price: 50 },
    ],
    communityStats: {
      totalBears: 200,
      activeUsers: 120,
    },
  },
];

/**
 * Function to display island details.
 * @param {Array} islands - Array of island objects.
 */
function displayIslandDetails(islands) {
  try {
    if (!Array.isArray(islands)) {
      throw new Error("Invalid data format: islands must be an array.");
    }

    islands.forEach((island) => {
      console.log(`Island Name: ${island.name}`);
      console.log(`Description: ${island.description}`);
      console.log("\nMarketplace Items:");
      island.marketplaceItems.forEach((item) => {
        console.log(`- ${item.itemName}: $${item.price}`);
      });
      console.log("\nCommunity Stats:");
      console.log(`Total Bears: ${island.communityStats.totalBears}`);
      console.log(`Active Users: ${island.communityStats.activeUsers}`);
      console.log("--------------------------------------------------");
    });
  } catch (error) {
    console.error("Error displaying island details:", error.message);
  }
}

/**
 * Main function to execute the program logic.
 */
function main() {
  console.log("Welcome to 'Bears On The Block' Islands!");
  console.log("Displaying island details...\n");
  displayIslandDetails(islands);
}

// Run the program.
main();
```
