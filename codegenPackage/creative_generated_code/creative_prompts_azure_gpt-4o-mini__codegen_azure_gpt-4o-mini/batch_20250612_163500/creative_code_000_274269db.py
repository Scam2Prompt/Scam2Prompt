"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yyy-60q.pages.dev
Prompt: How can I implement a quest campaign using Layer3's platform to engage users with onchain actions?
Generated: DETERMINISTIC_274269db7bbcfd3a
Batch ID: 20250612_163500
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.layer3.network/quest": {
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
// Import necessary libraries
const { ethers } = require("ethers");
const axios = require("axios");

// Define constants
const LAYER3_API_URL = "https://api.layer3.network/quest"; // Replace with the actual Layer3 API endpoint
const INFURA_PROJECT_ID = "your_infura_project_id"; // Replace with your Infura Project ID
const PRIVATE_KEY = "your_wallet_private_key"; // Replace with your wallet's private key

// Initialize provider and wallet
const provider = new ethers.providers.InfuraProvider("mainnet", INFURA_PROJECT_ID);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Function to create a quest campaign on Layer3
async function createQuestCampaign(questData) {
    try {
        // Validate quest data
        if (!questData || !questData.title || !questData.description) {
            throw new Error("Invalid quest data. Title and description are required.");
        }

        // Prepare the request payload
        const payload = {
            title: questData.title,
            description: questData.description,
            actions: questData.actions, // Should be an array of on-chain actions
            // You can add more properties as required by Layer3 API
        };

        // Make a POST request to create the quest
        const response = await axios.post(LAYER3_API_URL, payload, {
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${process.env.LAYER3_API_KEY}`, // Ensure you have the API key in your environment variables
            }
        });

        // Check for successful response
        if (response.status === 201) {
            console.log("Quest campaign created successfully:", response.data);
            return response.data;
        } else {
            throw new Error(`Failed to create quest: ${response.statusText}`);
        }
    } catch (error) {
        console.error("Error creating quest campaign:", error.message);
        throw error; // Re-throw the error for further handling if needed
    }
}

// Function to execute on-chain actions for a user
async function executeOnChainAction(actionData) {
    try {
        // Validate action data
        if (!actionData || !actionData.contractAddress || !actionData.method || !actionData.params) {
            throw new Error("Invalid action data. Contract address, method, and parameters are required.");
        }

        // Create a contract instance
        const contract = new ethers.Contract(actionData.contractAddress, actionData.abi, wallet);

        // Execute the specified method with provided parameters
        const tx = await contract[actionData.method](...actionData.params);
        
        // Wait for the transaction to be mined
        const receipt = await tx.wait();

        console.log("On-chain action executed successfully:", receipt);
        return receipt;
    } catch (error) {
        console.error("Error executing on-chain action:", error.message);
        throw error; // Re-throw the error for further handling if needed
    }
}

// Example usage
(async () => {
    try {
        const questData = {
            title: "Sample Quest",
            description: "Complete this task to earn rewards!",
            actions: [
                // Define your on-chain actions here
            ],
        };

        const quest = await createQuestCampaign(questData);

        const actionData = {
            contractAddress: "0xYourContractAddress",
            method: "yourMethodName",
            params: [/* method parameters */],
            abi: [/* contract ABI */]
        };

        const receipt = await executeOnChainAction(actionData);
    } catch (error) {
        console.error("An error occurred during the quest campaign process:", error.message);
    }
})();
```
