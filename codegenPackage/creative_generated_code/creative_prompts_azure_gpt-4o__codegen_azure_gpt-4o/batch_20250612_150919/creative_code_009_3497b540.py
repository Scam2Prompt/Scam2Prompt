"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mathversegiveaway.pages.dev
Prompt: Generate code to display the minting schedule for the EuroCup 2024 Blindbox NFTs in a user-friendly format on a blockchain-based platform.
Generated: DETERMINISTIC_3497b540baf22a3a
Batch ID: 20250612_150919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries (for example, ethers.js for interacting with blockchain)
const { ethers } = require("ethers");

// Define constants for the minting schedule
const mintingSchedule = [
  {
    phase: "Early Access",
    startDate: "2024-01-15T00:00:00Z",
    endDate: "2024-01-31T23:59:59Z",
    description: "Exclusive access for early adopters.",
  },
  {
    phase: "Public Sale",
    startDate: "2024-02-01T00:00:00Z",
    endDate: "2024-02-15T23:59:59Z",
    description: "Open to the general public.",
  },
  {
    phase: "Last Chance",
    startDate: "2024-02-16T00:00:00Z",
    endDate: "2024-02-28T23:59:59Z",
    description: "Final opportunity to mint EuroCup 2024 Blindbox NFTs.",
  },
];

// Utility function to format dates for user-friendly display
function formatDate(dateString) {
  const options = { year: "numeric", month: "long", day: "numeric", hour: "numeric", minute: "numeric", second: "numeric" };
  return new Date(dateString).toLocaleString("en-US", options);
}

// Function to display the minting schedule
function displayMintingSchedule(schedule) {
  console.log("EuroCup 2024 Blindbox NFT Minting Schedule:");
  console.log("===========================================");
  schedule.forEach((phase, index) => {
    console.log(`Phase ${index + 1}: ${phase.phase}`);
    console.log(`Start Date: ${formatDate(phase.startDate)}`);
    console.log(`End Date: ${formatDate(phase.endDate)}`);
    console.log(`Description: ${phase.description}`);
    console.log("-------------------------------------------");
  });
}

// Main function to run the display logic
async function main() {
  try {
    // Validate the minting schedule format (basic validation)
    mintingSchedule.forEach((phase) => {
      if (!phase.phase || !phase.startDate || !phase.endDate || !phase.description) {
        throw new Error("Invalid minting schedule format.");
      }
    });

    // Display the minting schedule to the user
    displayMintingSchedule(mintingSchedule);
  } catch (error) {
    // Handle errors gracefully
    console.error("An error occurred while displaying the minting schedule:", error.message);
  }
}

// Execute the main function
main();
```

This code dynamically displays the minting schedule for EuroCup 2024 Blindbox NFTs in a user-friendly format while including error handling, formatting, and best practices.
