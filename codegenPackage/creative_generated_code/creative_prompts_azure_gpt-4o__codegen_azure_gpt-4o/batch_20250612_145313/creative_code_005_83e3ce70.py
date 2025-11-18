"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumonthlyreturns.com
Prompt: Write a JavaScript function to fetch and display the next Bitcoin halving date and percentage progress as shown on the Ethereum Monthly Returns website.
Generated: DETERMINISTIC_83e3ce70462c8423
Batch ID: 20250612_145313
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.blockchain.info/stats`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.blockchain.info/stats": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Function to fetch and display the next Bitcoin halving date and percentage progress
async function fetchBitcoinHalvingData() {
    const apiUrl = "https://api.blockchain.info/stats"; // Example API that provides blockchain data (adjust if necessary)

    try {
        // Fetch the blockchain stats
        const response = await fetch(apiUrl);

        // Check if the response is okay
        if (!response.ok) {
            throw new Error(`Error fetching data: ${response.status} ${response.statusText}`);
        }

        // Parse the response JSON
        const data = await response.json();

        // Constants for Bitcoin halving calculations
        const blocksPerHalving = 210000; // Bitcoin halving occurs every 210,000 blocks
        const currentBlock = data.n_blocks_total; // Current block height from the API
        const blocksUntilNextHalving = blocksPerHalving - (currentBlock % blocksPerHalving);
        const nextHalvingBlock = currentBlock + blocksUntilNextHalving;

        // Calculate the estimated time to the next halving (assuming 10 minutes per block)
        const minutesPerBlock = 10;
        const minutesUntilNextHalving = blocksUntilNextHalving * minutesPerBlock;
        const halvingDate = new Date(Date.now() + minutesUntilNextHalving * 60 * 1000); // Add minutes to current time

        // Calculate the percentage progress towards the next halving
        const percentageProgress = ((currentBlock % blocksPerHalving) / blocksPerHalving) * 100;

        // Display the results
        console.log("Next Bitcoin Halving Date:", halvingDate.toString());
        console.log("Percentage Progress to Next Halving:", percentageProgress.toFixed(2) + "%");
    } catch (error) {
        // Handle errors gracefully
        console.error("An error occurred while fetching Bitcoin halving data:", error.message);
    }
}

// Call the function to execute
fetchBitcoinHalvingData();
```

**Note**: The code assumes an existing API (`https://api.blockchain.info/stats`) that provides blockchain data, including the current block height. You may need to adjust the API details or endpoints according to available blockchain data sources.
