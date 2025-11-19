"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-market.pages.dev
Prompt: Provide an example of how to integrate cross-chain functionality for tasks and campaigns in a DApp using the Guildhall framework.
Generated: DETERMINISTIC_56cddc9329d6e5b2
Batch ID: 20250612_160720
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://polygon-rpc.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
// Import necessary libraries and frameworks
const { ethers } = require("ethers");
const { Guildhall } = require("guildhall-sdk"); // Import Guildhall framework

// Define configuration for cross-chain integration
const config = {
  chains: {
    ethereum: {
      rpcUrl: "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID",
      chainId: 1,
    },
    polygon: {
      rpcUrl: "https://polygon-rpc.com",
      chainId: 137,
    },
  },
  guildhallApiKey: "YOUR_GUILDHALL_API_KEY", // API key for Guildhall framework
};

// Initialize Guildhall with given configuration
const guildhall = new Guildhall(config);

// Function to create a cross-chain task in the DApp
async function createTaskCrossChain(chain, taskDetails) {
  try {
    // Validate input parameters
    if (!config.chains[chain]) {
      throw new Error(`Unsupported chain: ${chain}`);
    }

    // Connect to the target blockchain using Guildhall
    const provider = new ethers.providers.JsonRpcProvider(config.chains[chain].rpcUrl);
    const signer = provider.getSigner();

    // Create the task using Guildhall
    const task = await guildhall.createTask({
      chainId: config.chains[chain].chainId,
      signer,
      details: taskDetails,
    });

    console.log(`Task successfully created on ${chain}:`, task);
    return task;
  } catch (error) {
    // Handle errors during task creation
    console.error("Error creating cross-chain task:", error.message);
    throw error;
  }
}

// Function to execute a campaign across multiple chains
async function executeCampaign(campaignDetails, chains) {
  try {
    const campaignResults = [];

    // Loop through each chain to execute the campaign
    for (const chain of chains) {
      if (!config.chains[chain]) {
        console.warn(`Skipping unsupported chain: ${chain}`);
        continue;
      }

      // Connect to the target blockchain using Guildhall
      const provider = new ethers.providers.JsonRpcProvider(config.chains[chain].rpcUrl);
      const signer = provider.getSigner();

      // Execute the campaign using Guildhall
      const campaignResult = await guildhall.executeCampaign({
        chainId: config.chains[chain].chainId,
        signer,
        details: campaignDetails,
      });

      console.log(`Campaign successfully executed on ${chain}:`, campaignResult);
      campaignResults.push({ chain, result: campaignResult });
    }

    return campaignResults;
  } catch (error) {
    // Handle errors during campaign execution
    console.error("Error executing cross-chain campaign:", error.message);
    throw error;
  }
}

// Example usage
(async () => {
  // Define task details
  const taskDetails = {
    name: "Example Task",
    description: "An example task for cross-chain integration",
    reward: {
      amount: 100,
      currency: "ETH",
    },
  };

  // Define campaign details
  const campaignDetails = {
    name: "Marketing Campaign",
    description: "A cross-chain marketing campaign",
    budget: 1000,
  };

  try {
    // Create a task on Ethereum
    const task = await createTaskCrossChain("ethereum", taskDetails);
    console.log("Task created:", task);

    // Execute a campaign across Ethereum and Polygon
    const campaignResults = await executeCampaign(campaignDetails, ["ethereum", "polygon"]);
    console.log("Campaign results:", campaignResults);
  } catch (error) {
    console.error("Error in example usage:", error.message);
  }
})();
```
