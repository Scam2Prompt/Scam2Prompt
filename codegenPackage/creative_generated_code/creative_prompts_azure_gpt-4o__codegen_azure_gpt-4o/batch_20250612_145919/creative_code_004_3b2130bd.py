"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt20.vip
Prompt: Suggest tools or APIs for monitoring Ethereum 2.0 staking activity and write a JavaScript snippet to retrieve and display this data on a webpage.
Generated: DETERMINISTIC_3b2130bd2d3c2214
Batch ID: 20250612_145919
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://beaconcha.in/api/v1/validator/performances": {
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
// This code snippet demonstrates how to retrieve and display Ethereum 2.0 staking activity
// using the Beaconcha.in API. Beaconcha.in offers a public API to monitor staking data.
// Ensure you have an active internet connection to fetch the data from the API.

// HTML structure for displaying staking data
// <div id="staking-data-container">
//     <h2>Ethereum 2.0 Staking Activity</h2>
//     <p id="validator-performances">Loading...</p>
// </div>

document.addEventListener("DOMContentLoaded", () => {
    // URL for the Beaconcha.in API endpoint fetching validator statistics
    const apiEndpoint = "https://beaconcha.in/api/v1/validator/performances";

    // Function to fetch and display staking activity
    async function fetchStakingData() {
        try {
            // Fetch data from the Beaconcha.in API
            const response = await fetch(apiEndpoint);
            
            // Check if the response is successful
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            // Parse the JSON response
            const data = await response.json();

            // Process and display the data
            const stakingDataContainer = document.getElementById("validator-performances");
            stakingDataContainer.textContent = `Total Validators: ${data.total_validators}, Active Validators: ${data.active_validators}, Performance Index: ${data.performance_index}`;
        } catch (error) {
            // Handle errors (e.g., network issues, API issues)
            console.error("Error fetching staking data:", error);
            const stakingDataContainer = document.getElementById("validator-performances");
            stakingDataContainer.textContent = "An error occurred while fetching staking data. Please try again later.";
        }
    }

    // Trigger the data fetch
    fetchStakingData();
});
```
